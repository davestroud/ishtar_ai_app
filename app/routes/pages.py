from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

from app.config import settings
from app.content.blog_articles import get_rag_copilots_article_content

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# Add config to all template contexts
def get_template_context(request: Request, **kwargs):
    """Get template context with config"""
    context = {"request": request, "config": settings, **kwargs}
    return context


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", get_template_context(request))


@router.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    """Services page"""
    return templates.TemplateResponse("services.html", get_template_context(request))


@router.get("/finance", response_class=HTMLResponse)
async def finance(request: Request):
    """Finance focus page"""
    return templates.TemplateResponse("finance.html", get_template_context(request))


@router.get("/media-ads", response_class=HTMLResponse)
async def media_ads(request: Request):
    """Media/Advertising focus page"""
    return templates.TemplateResponse("media_ads.html", get_template_context(request))


@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact page"""
    return templates.TemplateResponse("contact.html", get_template_context(request))


@router.get("/privacy", response_class=HTMLResponse)
async def privacy(request: Request):
    """Privacy Policy page"""
    return templates.TemplateResponse("privacy.html", get_template_context(request))


@router.get("/terms", response_class=HTMLResponse)
async def terms(request: Request):
    """Terms of Service page"""
    return templates.TemplateResponse("terms.html", get_template_context(request))


def get_blog_posts():
    """Get list of blog posts for RSS and blog listing"""
    return [
        {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "slug": "future-of-rag-copilots-financial-services",
            "author": "Ishtar AI Team",
        },
        {
            "title": "AI Governance: Building Trust in Enterprise AI Systems",
            "excerpt": "Best practices for implementing governance frameworks that ensure AI systems are secure, compliant, and reliable.",
            "date": "2024-01-10",
            "slug": "ai-governance-trust-enterprise",
            "author": "Ishtar AI Team",
        },
        {
            "title": "Synthetic Media Compliance: What Media Companies Need to Know",
            "excerpt": "Navigating the regulatory landscape for AI-generated content and ensuring brand safety in the age of synthetic media.",
            "date": "2024-01-05",
            "slug": "synthetic-media-compliance-guide",
            "author": "Ishtar AI Team",
        },
    ]


@router.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    """Blog page"""
    posts = get_blog_posts()
    return templates.TemplateResponse(
        "blog.html", get_template_context(request, posts=posts)
    )


@router.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    """Individual blog post page"""
    # Article content mapping
    articles = {
        "future-of-rag-copilots-financial-services": {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "slug": "future-of-rag-copilots-financial-services",
            "content": get_rag_copilots_article_content(),
        },
        "future-of-rag-copilots-finance": {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "slug": "future-of-rag-copilots-finance",
            "content": get_rag_copilots_article_content(),
        },
    }

    # Get article or return placeholder
    post = articles.get(
        slug,
        {
            "title": "Blog Post",
            "content": "<p>This is a placeholder blog post. Content coming soon.</p>",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "excerpt": "Blog post excerpt.",
            "slug": slug,
        },
    )

    # Ensure slug is set for all posts
    if "slug" not in post:
        post["slug"] = slug

    return templates.TemplateResponse(
        "blog_post.html", get_template_context(request, post=post)
    )


@router.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    """FAQ page"""
    faqs = [
        {
            "question": "What industries do you serve?",
            "answer": "We specialize in finance and media/advertising organizations, helping them implement enterprise-grade AI solutions.",
        },
        {
            "question": "How long does a typical implementation take?",
            "answer": "Implementation timelines vary based on project scope, but most engagements range from 8-16 weeks for production-ready solutions.",
        },
        {
            "question": "Do you provide ongoing support?",
            "answer": "Yes, we offer comprehensive support packages including maintenance, updates, and optimization services.",
        },
        {
            "question": "What security standards do you follow?",
            "answer": "We implement industry-standard security practices including encryption, audit trails, and compliance with SOC 2, GDPR, and other relevant frameworks.",
        },
        {
            "question": "Can you integrate with our existing systems?",
            "answer": "Absolutely. Our solutions are designed to integrate seamlessly with existing enterprise infrastructure and workflows.",
        },
        {
            "question": "What is your pricing model?",
            "answer": "Pricing varies based on project scope and requirements. Contact us for a customized quote tailored to your needs.",
        },
    ]
    return templates.TemplateResponse(
        "faq.html", get_template_context(request, faqs=faqs)
    )


@router.get("/pricing", response_class=HTMLResponse)
async def pricing(request: Request):
    """Pricing page"""
    return templates.TemplateResponse("pricing.html", get_template_context(request))


@router.post("/newsletter", response_class=HTMLResponse)
async def subscribe_newsletter(request: Request, email: str = Form(...)):
    """Handle newsletter subscription"""
    # Note: Newsletter integration can be added here (Mailchimp, SendGrid, etc.)
    # For now, just return success
    return templates.TemplateResponse(
        "newsletter_success.html",
        get_template_context(request, email=email),
    )


@router.get("/case-studies", response_class=HTMLResponse)
async def case_studies(request: Request, industry: Optional[str] = None):
    """Case studies listing page"""
    from app.content.case_studies import get_case_studies

    all_case_studies = get_case_studies()

    # Filter by industry if specified
    if industry and industry != "All":
        filtered_case_studies = [
            c for c in all_case_studies if c.get("industry") == industry
        ]
    else:
        filtered_case_studies = all_case_studies

    return templates.TemplateResponse(
        "case_studies.html",
        get_template_context(
            request,
            case_studies=filtered_case_studies,
            selected_industry=industry or "All",
        ),
    )


@router.get("/case-studies/{slug}", response_class=HTMLResponse)
async def case_study_detail(request: Request, slug: str):
    """Individual case study page"""
    from app.content.case_studies import get_case_study_by_slug

    case_study = get_case_study_by_slug(slug)

    if not case_study:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Case study not found")

    return templates.TemplateResponse(
        "case_study.html", get_template_context(request, case_study=case_study)
    )


@router.get("/demo", response_class=HTMLResponse)
async def demo(request: Request):
    """Request demo page"""
    return templates.TemplateResponse("demo.html", get_template_context(request))


@router.post("/demo", response_class=HTMLResponse)
async def submit_demo_request(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    company: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    use_case: str = Form(...),
    company_size: Optional[str] = Form(None),
    industry: Optional[str] = Form(None),
    challenges: Optional[str] = Form(None),
    timeline: Optional[str] = Form(None),
    budget_range: Optional[str] = Form(None),
    website: Optional[str] = Form(None),  # Honeypot
):
    """Handle demo request form submission"""
    # Honeypot spam protection
    if website:
        return templates.TemplateResponse(
            "demo.html",
            get_template_context(
                request,
                success=True,
                message="Thank you for your request! We'll contact you soon.",
            ),
        )

    # Send email if configured
    from app.utils.email import send_contact_form_email

    message = f"""
Demo Request Details:
- Use Case: {use_case}
- Company Size: {company_size or 'Not specified'}
- Industry: {industry or 'Not specified'}
- Challenges: {challenges or 'Not specified'}
- Timeline: {timeline or 'Not specified'}
- Budget Range: {budget_range or 'Not specified'}
"""

    email_sent = await send_contact_form_email(
        name=name, email=email, phone=phone, company=company, message=message
    )

    return templates.TemplateResponse(
        "demo.html",
        get_template_context(
            request,
            success=True,
            message="Thank you for your demo request! We'll contact you within 24 hours to schedule a consultation.",
        ),
    )


@router.get("/resources", response_class=HTMLResponse)
async def resources(request: Request, category: Optional[str] = None):
    """Resources/Downloads page"""
    from app.content.resources import get_resources, get_resource_categories

    all_resources = get_resources()
    categories = get_resource_categories()

    # Filter by category if specified
    if category and category != "All":
        filtered_resources = [r for r in all_resources if r.get("category") == category]
    else:
        filtered_resources = all_resources

    return templates.TemplateResponse(
        "resources.html",
        get_template_context(
            request,
            resources=filtered_resources,
            categories=categories,
            selected_category=category or "All",
        ),
    )


@router.post("/resources/download", response_class=HTMLResponse)
async def download_resource(
    request: Request,
    resource_path: str = Form(...),
    email: Optional[str] = Form(None),
    name: Optional[str] = Form(None),
):
    """Handle resource downloads with optional email capture"""
    from fastapi.responses import FileResponse
    import os

    # Track download analytics
    if hasattr(request.app.state, "gtag"):
        # Analytics tracking would go here
        pass

    # If email provided, send thank you email (optional)
    if email:
        # Could send email here using utils.email
        pass

    # Return file if it exists
    file_path = f"app/static{resource_path}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Resource not found")


@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: Optional[str] = None, type: Optional[str] = None):
    """Search page"""
    from app.utils.search import search as search_content

    results = []
    doc_types = None

    # Parse type filter
    if type:
        doc_types = (
            [type]
            if type in ["blog", "page", "faq", "resource", "case_study"]
            else None
        )

    if q and q.strip():
        results = search_content(q.strip(), doc_types=doc_types, limit=50)

    # Track search analytics
    if q and results:
        if hasattr(request.app.state, "gtag"):
            # Analytics tracking would go here if needed
            pass

    return templates.TemplateResponse(
        "search.html",
        get_template_context(
            request, query=q, results=results, result_count=len(results)
        ),
    )


@router.post("/contact", response_class=HTMLResponse)
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: Optional[str] = Form(None),
    company: Optional[str] = Form(None),
    message: str = Form(...),
    website: Optional[str] = Form(None),  # Honeypot field for spam protection
):
    """Handle contact form submission"""
    # Honeypot spam protection
    if website:
        # Bot detected, return success anyway to not reveal the honeypot
        return templates.TemplateResponse(
            "contact.html",
            get_template_context(
                request,
                success=True,
                message="Thank you for your message! We'll get back to you soon.",
            ),
        )

    # Send email if configured
    from app.utils.email import send_contact_form_email

    email_sent = await send_contact_form_email(
        name=name, email=email, phone=phone, company=company, message=message
    )

    if email_sent:
        success_message = "Thank you for your message! We'll get back to you soon."
    else:
        # Still show success to user even if email fails (log error server-side)
        success_message = "Thank you for your message! We'll get back to you soon."

    return templates.TemplateResponse(
        "contact.html",
        get_template_context(request, success=True, message=success_message),
    )

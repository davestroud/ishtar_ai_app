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
    """Regulated Enterprise Solutions page"""
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


@router.get("/security", response_class=HTMLResponse)
async def security(request: Request):
    """Security & Compliance page"""
    return templates.TemplateResponse("security.html", get_template_context(request))


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page"""
    return templates.TemplateResponse("about.html", get_template_context(request))


@router.get("/trust-center", response_class=HTMLResponse)
async def trust_center(request: Request):
    """Trust Center page"""
    return templates.TemplateResponse(
        "trust_center.html", get_template_context(request)
    )


@router.get("/products/{slug}", response_class=HTMLResponse)
async def product_detail(request: Request, slug: str):
    """Product detail page"""
    from app.content.products import get_product_by_slug
    from fastapi import HTTPException

    product = get_product_by_slug(slug)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return templates.TemplateResponse(
        "product.html", get_template_context(request, product=product)
    )


@router.get("/implementation", response_class=HTMLResponse)
async def implementation(request: Request):
    """Implementation Method page"""
    return templates.TemplateResponse(
        "implementation.html", get_template_context(request)
    )


@router.get("/responsible-ai", response_class=HTMLResponse)
async def responsible_ai(request: Request):
    """Responsible AI page"""
    return templates.TemplateResponse(
        "responsible_ai.html", get_template_context(request)
    )


def get_blog_posts():
    """Get list of blog posts for RSS and blog listing"""
    return [
        {
            "title": "The Future of RAG Copilots in Regulated Enterprises",
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
            "title": "The Future of RAG Copilots in Regulated Enterprises",
            "excerpt": "How Retrieval-Augmented Generation is reshaping compliance and research into evidence-native workflows",
            "date": "2024-01-15",
            "author": "Ishtar AI Team",
            "slug": "future-of-rag-copilots-financial-services",
            "content": get_rag_copilots_article_content(),
        },
        "future-of-rag-copilots-finance": {
            "title": "The Future of RAG Copilots in Regulated Enterprises",
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
    faqs = {
        "general": [
            {
                "question": "What industries do you serve?",
                "answer": "We specialize in regulated enterprises and media/advertising organizations, helping them implement enterprise-grade AI solutions.",
            },
            {
                "question": "How long does a typical implementation take?",
                "answer": "Implementation timelines vary based on project scope, but most engagements range from 6-9 weeks for production-ready solutions. See our <a href='/pricing'>pricing page</a> for specific timelines.",
            },
            {
                "question": "Do you provide ongoing support?",
                "answer": "Yes, we offer comprehensive support packages including maintenance, updates, and optimization services. Our Platform Partner program provides ongoing improvement, monitoring, incident response, and expansion into additional use cases.",
            },
            {
                "question": "What is your pricing model?",
                "answer": "We offer fixed-scope engagements with clear success metrics. Pricing ranges from $50k-$200k depending on the offering. See our <a href='/pricing'>pricing page</a> for detailed information.",
            },
        ],
        "authentication": [
            {
                "question": "Do you support SSO (Single Sign-On)?",
                "answer": "Yes, we support both SAML 2.0 and OIDC (OpenID Connect) for SSO integration. We work with major identity providers including Okta, Azure AD, Google Workspace, and Auth0.",
            },
            {
                "question": "Do you support SCIM provisioning?",
                "answer": "Yes, we support SCIM 2.0 for automated user provisioning and deprovisioning, enabling seamless integration with your identity management systems.",
            },
            {
                "question": "Do you support multi-factor authentication (MFA)?",
                "answer": "Yes, MFA is supported and can be enforced through your SSO provider or natively within our platform.",
            },
        ],
        "deployment": [
            {
                "question": "Can you deploy in our VPC?",
                "answer": "Yes, we support VPC deployments with dedicated infrastructure in your cloud environment. This provides full network isolation and allows you to manage encryption keys.",
            },
            {
                "question": "Do you support on-premise deployments?",
                "answer": "Yes, we support on-premise deployments using containerized infrastructure (Docker, Kubernetes). We can deploy in air-gapped environments with regular security updates and patches.",
            },
            {
                "question": "What are your data residency requirements?",
                "answer": "We can deploy in multiple regions (US, EU, Asia-Pacific) and support customer-specified data residency requirements. For VPC and on-premise deployments, data never leaves your infrastructure.",
            },
        ],
        "data_privacy": [
            {
                "question": "What is your data retention policy?",
                "answer": "Active data is retained for the duration of the engagement. Backup data is retained for 30 days after contract termination. Audit logs are retained for 7 years (or per customer requirement). Processing data is deleted immediately after completion.",
            },
            {
                "question": "What is your data deletion process?",
                "answer": "Upon contract termination or customer request, all customer data is deleted within 30 days with certified deletion confirmation. Data export is available in standard formats (JSON, CSV) before deletion.",
            },
            {
                "question": "Do you train on customer data?",
                "answer": "No, we do not train models on customer data. Customer data is used only for inference and is not used to improve our models or shared with other customers.",
            },
            {
                "question": "Where is data processed?",
                "answer": "Data processing occurs in the region specified by the customer. For SaaS deployments, we support US, EU, and Asia-Pacific regions. For VPC and on-premise deployments, all processing occurs within your infrastructure.",
            },
        ],
        "security": [
            {
                "question": "How do you prevent prompt injection?",
                "answer": "We implement multiple layers of protection: input sanitization, prompt validation, output filtering, and monitoring for suspicious patterns. Our RAG systems use citation-based responses that can be verified against source documents.",
            },
            {
                "question": "How do you prevent data exfiltration in RAG systems?",
                "answer": "We implement permission-aware retrieval that respects source-level entitlements, query filtering to prevent unauthorized access, and audit logging of all queries. Data is isolated per tenant with no cross-tenant access.",
            },
            {
                "question": "What logs are stored and for how long?",
                "answer": "We log all authentication, authorization, data access, and configuration changes. Logs are stored in tamper-proof storage with 7-year retention (configurable per customer). Real-time log streaming and search capabilities are available.",
            },
            {
                "question": "What is your security incident process?",
                "answer": "We have a defined incident response process with initial response within 4 hours for critical issues. Customers are immediately notified of any security incident affecting their data, with regular status updates and a post-incident report within 30 days. Contact security@ishtar-ai.com for security concerns.",
            },
        ],
        "ip": [
            {
                "question": "Who owns the intellectual property (prompts, pipelines, code, fine-tunes)?",
                "answer": "Customer-specific customizations, prompts, and fine-tuned models are owned by the customer. Our platform code and general frameworks remain our IP, but all customer-specific work product is owned by the customer.",
            },
            {
                "question": "What are your license terms?",
                "answer": "We provide perpetual licenses for custom-built solutions. Our Platform Partner program includes ongoing updates and improvements. See our Terms of Service for detailed licensing information.",
            },
        ],
        "support": [
            {
                "question": "What is your support SLA?",
                "answer": "For Platform Partner customers, we provide 24/7 support with 4-hour response time for critical issues. Standard support includes business hours coverage with 8-hour response time for high-priority issues.",
            },
            {
                "question": "What does your incident response process look like?",
                "answer": "We follow a structured incident response process: immediate triage, customer notification, regular status updates, root cause analysis, remediation, and post-incident reporting. Critical incidents receive 4-hour initial response with 24-hour resolution target.",
            },
            {
                "question": "What tools and systems do you integrate with?",
                "answer": "We integrate with major enterprise systems including SharePoint, Confluence, Slack, Microsoft Teams, Active Directory, Okta, Azure AD, and various databases and APIs. Custom integrations can be built as part of engagements.",
            },
        ],
    }
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

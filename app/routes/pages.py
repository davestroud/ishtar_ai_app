from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

from app.config import settings

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


@router.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    """Blog page"""
    # Placeholder blog posts
    posts = [
        {
            "title": "The Future of RAG Copilots in Financial Services",
            "excerpt": "Exploring how Retrieval-Augmented Generation is transforming compliance and research workflows in finance.",
            "date": "2024-01-15",
            "slug": "future-of-rag-copilots-finance",
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
    return templates.TemplateResponse(
        "blog.html", get_template_context(request, posts=posts)
    )


@router.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    """Individual blog post page"""
    # Placeholder post content
    post = {
        "title": "The Future of RAG Copilots in Financial Services",
        "content": "<p>This is a placeholder blog post. Content coming soon.</p>",
        "date": "2024-01-15",
        "author": "Ishtar AI Team",
    }
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


@router.post("/newsletter", response_class=HTMLResponse)
async def subscribe_newsletter(request: Request, email: str = Form(...)):
    """Handle newsletter subscription"""
    # TODO: Integrate with email service (Mailchimp, SendGrid, etc.)
    # For now, just return success
    return templates.TemplateResponse(
        "newsletter_success.html",
        get_template_context(request, email=email),
    )


@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: Optional[str] = None):
    """Search page"""
    results = []
    if q:
        # Placeholder search - in production, implement actual search
        # For now, return empty results
        results = []
    return templates.TemplateResponse(
        "search.html", get_template_context(request, query=q, results=results)
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

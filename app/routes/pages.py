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
    return templates.TemplateResponse("services.html", {"request": request})


@router.get("/finance", response_class=HTMLResponse)
async def finance(request: Request):
    """Finance focus page"""
    return templates.TemplateResponse("finance.html", {"request": request})


@router.get("/media-ads", response_class=HTMLResponse)
async def media_ads(request: Request):
    """Media/Advertising focus page"""
    return templates.TemplateResponse("media_ads.html", {"request": request})


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

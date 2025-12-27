from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", {"request": request})

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
    return templates.TemplateResponse("contact.html", {"request": request})

@router.post("/contact", response_class=HTMLResponse)
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: Optional[str] = Form(None),
    company: Optional[str] = Form(None),
    message: str = Form(...)
):
    """Handle contact form submission"""
    # TODO: Add email sending or API integration here
    # For now, just return success message
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "success": True,
            "message": "Thank you for your message! We'll get back to you soon."
        }
    )


"""Pydantic models for request validation"""
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import bleach


class ContactFormSchema(BaseModel):
    """Contact form validation schema"""

    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    company: Optional[str] = Field(None, max_length=100)
    message: str = Field(..., min_length=10, max_length=5000)
    website: Optional[str] = None  # Honeypot field

    @field_validator("name", "company")
    @classmethod
    def sanitize_text(cls, v: Optional[str]) -> Optional[str]:
        """Sanitize text fields to prevent XSS"""
        if v:
            return bleach.clean(v.strip(), tags=[], strip=True)
        return v

    @field_validator("message")
    @classmethod
    def sanitize_message(cls, v: str) -> str:
        """Sanitize message field, allowing basic formatting"""
        if v:
            # Allow basic text formatting but strip all HTML tags
            return bleach.clean(v.strip(), tags=[], strip=True)
        return v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        """Basic phone validation"""
        if v:
            # Remove common phone formatting characters
            cleaned = "".join(c for c in v if c.isdigit() or c in "+-() ")
            return cleaned.strip()
        return v


class DemoFormSchema(BaseModel):
    """Demo request form validation schema"""

    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    company: Optional[str] = Field(None, max_length=100)
    phone: Optional[str] = Field(None, max_length=20)
    use_case: str = Field(..., min_length=10, max_length=1000)
    company_size: Optional[str] = Field(None, max_length=50)
    industry: Optional[str] = Field(None, max_length=100)
    challenges: Optional[str] = Field(None, max_length=2000)
    timeline: Optional[str] = Field(None, max_length=100)
    budget_range: Optional[str] = Field(None, max_length=100)
    website: Optional[str] = None  # Honeypot field

    @field_validator("name", "company", "industry", "company_size", "timeline", "budget_range")
    @classmethod
    def sanitize_text(cls, v: Optional[str]) -> Optional[str]:
        """Sanitize text fields to prevent XSS"""
        if v:
            return bleach.clean(v.strip(), tags=[], strip=True)
        return v

    @field_validator("use_case", "challenges")
    @classmethod
    def sanitize_long_text(cls, v: Optional[str]) -> Optional[str]:
        """Sanitize longer text fields"""
        if v:
            return bleach.clean(v.strip(), tags=[], strip=True)
        return v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        """Basic phone validation"""
        if v:
            cleaned = "".join(c for c in v if c.isdigit() or c in "+-() ")
            return cleaned.strip()
        return v


class NewsletterFormSchema(BaseModel):
    """Newsletter subscription form validation schema"""

    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email_domain(cls, v: EmailStr) -> EmailStr:
        """Additional email validation"""
        # Could add domain blacklist checking here if needed
        return v

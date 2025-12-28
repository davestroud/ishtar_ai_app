from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Email Configuration
    email_enabled: bool = False
    email_provider: str = "smtp"  # "smtp" or "sendgrid"

    # SMTP Configuration
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    smtp_use_tls: bool = True

    # SendGrid Configuration
    sendgrid_api_key: Optional[str] = None

    # Email Recipients
    contact_email_to: str = "contact@ishtar-ai.com"
    contact_email_from: str = "noreply@ishtar-ai.com"
    contact_email_from_name: str = "Ishtar AI Website"

    # Security
    enable_csrf: bool = True
    csrf_secret_key: Optional[str] = None

    # Analytics
    google_analytics_id: Optional[str] = "G-KRTEM16GDJ"
    plausible_domain: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

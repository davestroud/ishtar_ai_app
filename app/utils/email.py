import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
import os

from app.config import settings


async def send_email_smtp(
    to_email: str, subject: str, body_html: str, body_text: Optional[str] = None
) -> bool:
    """Send email using SMTP"""
    if not settings.email_enabled or not settings.smtp_host:
        return False

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = (
            f"{settings.contact_email_from_name} <{settings.contact_email_from}>"
        )
        msg["To"] = to_email

        if body_text:
            msg.attach(MIMEText(body_text, "plain"))
        msg.attach(MIMEText(body_html, "html"))

        with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as server:
            if settings.smtp_use_tls:
                server.starttls()
            if settings.smtp_user and settings.smtp_password:
                server.login(settings.smtp_user, settings.smtp_password)
            server.send_message(msg)

        return True
    except Exception as e:
        print(f"Error sending email via SMTP: {e}")
        return False


async def send_email_sendgrid(
    to_email: str, subject: str, body_html: str, body_text: Optional[str] = None
) -> bool:
    """Send email using SendGrid API"""
    if not settings.email_enabled or not settings.sendgrid_api_key:
        return False

    try:
        import sendgrid
        from sendgrid.helpers.mail import Mail, Email, To, Content

        sg = sendgrid.SendGridAPIClient(api_key=settings.sendgrid_api_key)

        from_email = Email(
            settings.contact_email_from, settings.contact_email_from_name
        )
        to_email_obj = To(to_email)

        content_html = Content("text/html", body_html)
        if body_text:
            content_text = Content("text/plain", body_text)
            mail = Mail(from_email, to_email_obj, subject, content_text)
            mail.add_content(content_html)
        else:
            mail = Mail(from_email, to_email_obj, subject, content_html)

        response = sg.send(mail)
        return response.status_code in [200, 201, 202]
    except ImportError:
        print("SendGrid library not installed. Install with: poetry add sendgrid")
        return False
    except Exception as e:
        print(f"Error sending email via SendGrid: {e}")
        return False


async def send_contact_form_email(
    name: str, email: str, phone: Optional[str], company: Optional[str], message: str
) -> bool:
    """Send contact form submission email"""
    subject = f"New Contact Form Submission from {name}"

    body_html = f"""
    <html>
    <body>
        <h2>New Contact Form Submission</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        {f'<p><strong>Phone:</strong> {phone}</p>' if phone else ''}
        {f'<p><strong>Company:</strong> {company}</p>' if company else ''}
        <p><strong>Message:</strong></p>
        <p>{message.replace(chr(10), '<br>')}</p>
    </body>
    </html>
    """

    body_text = f"""
New Contact Form Submission

Name: {name}
Email: {email}
{f'Phone: {phone}' if phone else ''}
{f'Company: {company}' if company else ''}

Message:
{message}
    """

    if settings.email_provider == "sendgrid":
        return await send_email_sendgrid(
            settings.contact_email_to, subject, body_html, body_text
        )
    else:
        return await send_email_smtp(
            settings.contact_email_to, subject, body_html, body_text
        )

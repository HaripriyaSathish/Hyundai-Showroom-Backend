import requests
from django.conf import settings


def send_lead_notification_email(lead):
    """
    Sends a notification email via Resend's HTTP API whenever a new lead
    comes in from either the Hero 'Get Free Quote' form or the Contact
    'Send an Enquiry' form.

    Uses Resend (not Django's SMTP EmailBackend) because Render's free tier
    blocks outbound SMTP ports — same fix applied to EduStruc's forgot
    password flow and the Vetri Tech enquiry/enroll forms.

    Returns True on success, False otherwise (never raises — a failed
    notification email should not fail the lead submission itself).
    """
    if not settings.RESEND_API_KEY or not settings.LEAD_NOTIFICATION_EMAIL:
        return False

    source_label = 'Contact Page Enquiry' if lead.source == 'contact' else 'Hero Quote Request'

    optional_rows = ''
    if lead.preferred_contact_time:
        optional_rows += f"<p><strong>Preferred Contact Time:</strong> {lead.preferred_contact_time}</p>"
    if lead.message:
        optional_rows += f"<p><strong>Message:</strong> {lead.message}</p>"

    html_body = f"""
    <h2>New {source_label}</h2>
    <p><strong>Name:</strong> {lead.name}</p>
    <p><strong>Mobile:</strong> {lead.mobile}</p>
    <p><strong>City:</strong> {lead.city}</p>
    <p><strong>Interested Model:</strong> {lead.interested_model}</p>
    {optional_rows}
    <p><strong>Submitted:</strong> {lead.created_at}</p>
    """

    try:
        response = requests.post(
            'https://api.resend.com/emails',
            headers={
                'Authorization': f'Bearer {settings.RESEND_API_KEY}',
                'Content-Type': 'application/json',
            },
            json={
                'from': settings.RESEND_FROM_EMAIL,
                'to': [settings.LEAD_NOTIFICATION_EMAIL],
                'subject': f'New Lead ({source_label}): {lead.name} interested in {lead.interested_model}',
                'html': html_body,
            },
            timeout=10,
        )
        return response.status_code in (200, 201)
    except requests.RequestException:
        return False
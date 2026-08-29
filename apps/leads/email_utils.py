import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_lead_notification_email(lead):
    """
    Sends a notification email via Resend's HTTP API whenever a new lead
    comes in — from the Hero quote form, the Contact enquiry form, or the
    Book Test Drive popup.
    """
    if not settings.RESEND_API_KEY or not settings.LEAD_NOTIFICATION_EMAIL:
        return False

    source_labels = {
        'contact': 'Contact Page Enquiry',
        'test_drive': 'Book Test Drive Popup',
    }
    source_label = source_labels.get(lead.source, 'Hero Quote Request')

    # If this enquiry came from clicking "Claim Offer" on a specific offer
    # card, call it out distinctly in the subject line and body so the
    # sales team immediately knows which promotion the customer wants.
    if lead.offer_interested:
        subject = (
            f'New Offer Enquiry ({lead.offer_interested}): '
            f'{lead.name} interested in {lead.interested_model}'
        )
        offer_banner = (
            f'<p style="background:#FEF2F2;border:1px solid #FCA5A5;'
            f'border-radius:8px;padding:10px 14px;color:#B91C1C;'
            f'font-weight:600;">'
            f'Enquiring about offer: {lead.offer_interested}'
            f'</p>'
        )
    else:
        subject = f'New Lead ({source_label}): {lead.name} interested in {lead.interested_model}'
        offer_banner = ''

    optional_rows = ''
    if lead.city:
        optional_rows += f"<p><strong>City:</strong> {lead.city}</p>"
    if lead.email:
        optional_rows += f"<p><strong>Email:</strong> {lead.email}</p>"
    if lead.preferred_contact_time:
        optional_rows += f"<p><strong>Preferred Contact Time:</strong> {lead.preferred_contact_time}</p>"
    if lead.message:
        optional_rows += f"<p><strong>Message:</strong> {lead.message}</p>"

    html_body = f"""
    <h2>New {source_label}</h2>
    {offer_banner}
    <p><strong>Name:</strong> {lead.name}</p>
    <p><strong>Mobile:</strong> {lead.mobile}</p>
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
                'subject': subject,
                'html': html_body,
            },
            timeout=10,
        )
        if response.status_code not in (200, 201):
            logger.error(
                "Resend email failed for lead %s: status=%s body=%s",
                lead.id, response.status_code, response.text,
            )
            return False
        return True
    except requests.RequestException as exc:
        logger.error("Resend email request error for lead %s: %s", lead.id, exc)
        return False
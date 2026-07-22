from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer
from .email_utils import send_lead_notification_email


class LeadCreateView(generics.CreateAPIView):
    """
    POST /api/leads/  — used by the Hero 'Get Free Quote' form.
    Saves the lead, then fires a Resend notification email.
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def perform_create(self, serializer):
        lead = serializer.save()
        lead.email_sent = send_lead_notification_email(lead)
        lead.save(update_fields=['email_sent'])

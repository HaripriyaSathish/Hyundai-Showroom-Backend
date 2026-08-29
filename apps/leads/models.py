from django.db import models


class Lead(models.Model):
    CONTACT_TIME_CHOICES = [
        ('Morning (9 AM – 12 PM)', 'Morning (9 AM – 12 PM)'),
        ('Afternoon (12 PM – 4 PM)', 'Afternoon (12 PM – 4 PM)'),
        ('Evening (4 PM – 8 PM)', 'Evening (4 PM – 8 PM)'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('test_drive_booked', 'Test Drive Booked'),
        ('converted', 'Converted'),
        ('closed', 'Closed'),
    ]

    SOURCE_CHOICES = [
        ('hero', 'Hero — Get Free Quote'),
        ('contact', 'Contact — Send an Enquiry'),
        ('test_drive', 'Book Test Drive Popup'),
    ]

    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(
        blank=True, default='',
        help_text="Optional — collected via the Book Test Drive popup.",
    )
    interested_model = models.CharField(max_length=100)
    preferred_contact_time = models.CharField(
        max_length=50, choices=CONTACT_TIME_CHOICES, blank=True,
        help_text="Only used by the Hero quote form. Left blank for other sources.",
    )
    message = models.TextField(
        blank=True,
        help_text="Optional message — only used by the Contact 'Send an Enquiry' form.",
    )
    # NEW — set when the enquiry originated from clicking "Claim Offer" on
    # a specific offer card. Blank for enquiries not tied to any offer.
    offer_interested = models.CharField(
        max_length=120,
        blank=True,
        default='',
        help_text="Name of the offer the customer clicked 'Claim Offer' on, if any (e.g. 'Cash Discount').",
    )
    source = models.CharField(
        max_length=20, choices=SOURCE_CHOICES, default='hero',
        help_text="Which form on the site this lead came from.",
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)

    email_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.interested_model} ({self.mobile})"
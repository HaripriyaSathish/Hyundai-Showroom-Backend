from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class HeroContent(models.Model):
    """
    Singleton-style model — only one row is meant to exist. Holds every
    piece of text in the Hero section that should be editable from the
    admin panel instead of hardcoded in Hero.jsx.
    """

    badge_text = models.CharField(
        max_length=150,
        default="Authorized Hyundai Dealer · Best Price Guaranteed",
    )

    heading_line1 = models.CharField(max_length=100, default="Drive home your dream")
    heading_highlight = models.CharField(
        max_length=50,
        default="Hyundai",
        help_text="This word is shown with the blue-to-cyan gradient style.",
    )
    heading_line2 = models.CharField(max_length=50, default="today")

    paragraph = models.TextField(
        default=(
            "Explore the latest Hyundai models with exclusive offers, easy "
            "finance options, exchange benefits and instant test drive "
            "booking at Hyundai Susee Showroom."
        )
    )

    cta_book_label = models.CharField(max_length=50, default="Book Test Drive")
    cta_offer_label = models.CharField(max_length=50, default="Get Best Offer")
    cta_whatsapp_label = models.CharField(max_length=50, default="WhatsApp Now")

    feature_1_label = models.CharField(max_length=50, default="Authorized")
    feature_2_label = models.CharField(max_length=50, default="Easy Finance")
    feature_3_label = models.CharField(max_length=50, default="Exchange Bonus")

    form_title = models.CharField(max_length=100, default="Get Instant Best Price")
    form_subtitle = models.CharField(
        max_length=200,
        default="Fill in the details — our advisor will call within 15 minutes.",
    )
    form_badge_text = models.CharField(max_length=50, default="LIMITED TIME OFFER")
    form_footnote = models.CharField(
        max_length=100, default="Your information is 100% safe & secure"
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero Section Content"
        verbose_name_plural = "Hero Section Content"

    def __str__(self):
        return "Hero Section Content"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class WhyChooseSection(models.Model):
    """
    Singleton — the header text above the "Why Choose Hyundai Susee"
    feature-card grid. The cards themselves are a separate model
    (WhyChooseCard) so you can add/remove/reorder them freely.
    """

    eyebrow_text = models.CharField(max_length=60, default="Why Choose Hyundai Susee")
    heading_line1 = models.CharField(max_length=100, default="India's most trusted Hyundai")
    heading_highlight = models.CharField(
        max_length=50,
        default="dealer",
        help_text="This word is shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default=(
            "Everything you need for a seamless car buying experience — "
            "from authorized service to unbeatable offers."
        ),
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Why Choose Section — Header"
        verbose_name_plural = "Why Choose Section — Header"

    def __str__(self):
        return "Why Choose Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class WhyChooseCard(models.Model):
    """
    One feature card in the "Why Choose Hyundai Susee" grid
    (e.g. "Authorized Hyundai Dealer"). Fully admin-managed — add,
    edit, remove, or reorder as many as you want; the frontend renders
    them in a responsive grid (1 col mobile / 2 cols tablet / 4 cols
    desktop) automatically.
    """

    ICON_CHOICES = [
        ("check-circle", "Check Circle (verified/authorized)"),
        ("shield-check", "Shield Check (genuine/protection)"),
        ("wallet", "Wallet (finance/money)"),
        ("repeat", "Repeat (exchange)"),
        ("percent", "Percent (discount)"),
        ("truck", "Truck (delivery)"),
        ("users", "Users (people/advisors)"),
        ("calendar", "Calendar (booking)"),
        ("phone", "Phone (contact)"),
        ("message-circle", "Message Circle (chat/support)"),
    ]

    icon = models.CharField(max_length=30, choices=ICON_CHOICES, default="check-circle")
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers appear first."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Why Choose Card"
        verbose_name_plural = "Why Choose Cards"

    def __str__(self):
        return self.title


class OffersSection(models.Model):
    """
    Singleton — header text above the offers grid
    ("EXCLUSIVE OFFERS" / "Unbeatable Hyundai offers this month").
    """

    eyebrow_text = models.CharField(max_length=60, default="Exclusive Offers")
    heading_line1 = models.CharField(max_length=100, default="Unbeatable Hyundai offers")
    heading_highlight = models.CharField(
        max_length=50,
        default="this month",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default=(
            "Save more with our current benefits, festival specials and "
            "corporate deals — limited stock available."
        ),
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Offers Section — Header"
        verbose_name_plural = "Offers Section — Header"

    def __str__(self):
        return "Offers Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class OfferCard(models.Model):
    """
    One offer card (e.g. "Cash Discount", "Exchange Bonus"). Fully
    admin-managed — add, edit, remove, or reorder any number of offers.
    Icon badge uses a red gradient (distinct from the navy/cyan used
    elsewhere) to visually signal "deal/promotion".
    """

    ICON_CHOICES = [
        ("wallet", "Wallet (cash discount)"),
        ("repeat", "Repeat (exchange bonus)"),
        ("percent", "Percent (EMI/discount)"),
        ("users", "Users (corporate offers)"),
        ("sparkles", "Sparkles (festival offers)"),
        ("gift", "Gift (free accessories)"),
        ("shield-check", "Shield Check"),
        ("check-circle", "Check Circle"),
    ]

    icon = models.CharField(max_length=30, choices=ICON_CHOICES, default="wallet")
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    cta_label = models.CharField(max_length=40, default="Claim Offer")
    cta_link = models.CharField(max_length=200, default="#contact")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Offer Card"
        verbose_name_plural = "Offer Cards"

    def __str__(self):
        return self.title


class FinanceSection(models.Model):
    """
    Singleton — header text above the Finance & Insurance section, plus
    the text on the dark "Our Finance Partners" card.
    """

    eyebrow_text = models.CharField(max_length=60, default="Finance & Insurance")
    heading_line1 = models.CharField(max_length=100, default="Easy finance, simple")
    heading_highlight = models.CharField(
        max_length=50, default="ownership",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default="Partnered with India's leading banks and NBFCs to make owning your Hyundai easier than ever.",
    )
    partners_heading = models.CharField(max_length=80, default="Our Finance Partners")
    partners_subtitle = models.CharField(
        max_length=200,
        default="Get instant loan quotations from India's top banks & NBFCs.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Finance Section — Header"
        verbose_name_plural = "Finance Section — Header"

    def __str__(self):
        return "Finance Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FinanceFeatureCard(models.Model):
    """
    One small feature card on the left side (e.g. "Low EMI",
    "Instant Loan Approval"). Fully admin-managed.
    """

    ICON_CHOICES = [
        ("percent", "Percent (Low EMI)"),
        ("check-circle", "Check Circle (Instant Approval)"),
        ("wallet", "Wallet (100% Finance)"),
        ("shield-check", "Shield Check (Insurance)"),
    ]

    icon = models.CharField(max_length=30, choices=ICON_CHOICES, default="percent")
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Finance Feature Card"
        verbose_name_plural = "Finance Feature Cards"

    def __str__(self):
        return self.title


class FinancePartner(models.Model):
    """One bank/NBFC pill shown on the dark 'Our Finance Partners' card."""

    name = models.CharField(max_length=60, help_text="e.g. 'HDFC Bank'")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Finance Partner"
        verbose_name_plural = "Finance Partners"

    def __str__(self):
        return self.name


class TestDriveCTA(models.Model):
    """
    Singleton — the "Book Your Free Test Drive Today" banner between
    the Finance and Testimonials sections.
    """

    badge_text = models.CharField(max_length=60, default="Free & Doorstep")
    heading = models.CharField(max_length=120, default="Book Your Free Test Drive Today")
    paragraph = models.CharField(
        max_length=250,
        default="Experience the Hyundai you love — right at your doorstep. Pick your model, choose your time, and we'll bring the car to you.",
    )
    cta_book_label = models.CharField(max_length=50, default="Book Test Drive")
    cta_whatsapp_label = models.CharField(max_length=50, default="WhatsApp Now")
    whatsapp_number = models.CharField(
        max_length=20, default="910000000000",
        help_text="Digits only, with country code, no + or spaces — e.g. 919876543210",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Test Drive CTA Banner"
        verbose_name_plural = "Test Drive CTA Banner"

    def __str__(self):
        return "Test Drive CTA Banner"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class TestimonialsSection(models.Model):
    """Singleton — header text above the customer testimonials grid."""

    eyebrow_text = models.CharField(max_length=60, default="Customer Stories")
    heading_line1 = models.CharField(max_length=100, default="Loved by thousands of")
    heading_highlight = models.CharField(
        max_length=50, default="Hyundai owners",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default="Real experiences from happy customers who trusted Hyundai Susee for their car buying journey.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testimonials Section — Header"
        verbose_name_plural = "Testimonials Section — Header"

    def __str__(self):
        return "Testimonials Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Testimonial(models.Model):
    """
    One customer review card. Fully admin-managed — add, edit, remove,
    or reorder any number of reviews. Avatar shows the customer's
    initials (computed automatically) rather than an uploaded photo,
    matching the design.
    """

    customer_name = models.CharField(max_length=80)
    purchased_model = models.CharField(max_length=80, help_text="e.g. 'Hyundai Creta'")
    review_text = models.TextField(max_length=400)
    rating = models.PositiveSmallIntegerField(
        default=5,
        help_text="1 to 5 stars.",
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.customer_name} — {self.purchased_model}"


class GallerySection(models.Model):
    """Singleton — header text above the showroom gallery grid."""

    eyebrow_text = models.CharField(max_length=60, default="Showroom Gallery")
    heading_line1 = models.CharField(max_length=100, default="Step inside Hyundai")
    heading_highlight = models.CharField(
        max_length=50, default="Susee",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default="A glimpse of our showroom, delivery moments and the premium Hyundai experience.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery Section — Header"
        verbose_name_plural = "Gallery Section — Header"

    def __str__(self):
        return "Gallery Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class GalleryImage(models.Model):
    """
    One photo in the showroom gallery (e.g. "Showroom Exterior",
    "Vehicle Display"). Fully admin-managed — add, edit, remove, or
    reorder any number of images.
    """

    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=80, help_text="e.g. 'Showroom Exterior'")
    image_alt = models.CharField(
        max_length=150,
        blank=True,
        help_text="SEO alt text for this image, e.g. 'Hyundai Susee Showroom Exterior'. Falls back to the caption if left blank.",
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.caption


class TrustedStatsSection(models.Model):
    """
    Singleton — the "Trusted by millions across India" banner with
    animated count-up statistics.
    """

    badge_text = models.CharField(max_length=60, default="Why Hyundai")
    heading = models.CharField(max_length=120, default="Trusted by millions across India")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Trusted Stats Banner — Header"
        verbose_name_plural = "Trusted Stats Banner — Header"

    def __str__(self):
        return "Trusted Stats Banner Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class TrustedStat(models.Model):
    """
    One animated count-up statistic (e.g. "1M+ Happy Hyundai
    Customers"). count_to is the number the counter animates up to;
    suffix is appended after the number once counting finishes
    (e.g. "M+", "+", "★"). Fully admin-managed.
    """

    count_to = models.PositiveIntegerField(help_text="The number to count up to, e.g. 1, 25, 5, 100.")
    suffix = models.CharField(max_length=10, default="+", help_text="e.g. '+', 'M+', '★'")
    label = models.CharField(max_length=80, help_text="e.g. 'Happy Hyundai Customers'")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Trusted Stat"
        verbose_name_plural = "Trusted Stats"

    def __str__(self):
        return f"{self.count_to}{self.suffix} — {self.label}"
    
class FAQSection(models.Model):
    """
    Singleton — header text above the FAQ accordion
    ("FAQ" / "Frequently asked questions").
    """

    eyebrow_text = models.CharField(max_length=60, default="FAQ")
    heading_line1 = models.CharField(max_length=100, default="Frequently asked")
    heading_highlight = models.CharField(
        max_length=50,
        default="questions",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default="Everything you need to know before you buy your next Hyundai.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ Section — Header"
        verbose_name_plural = "FAQ Section — Header"

    def __str__(self):
        return "FAQ Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FAQItem(models.Model):
    """
    One question/answer pair in the FAQ accordion. Fully admin-managed —
    add, edit, remove, or reorder any number of FAQs. Only one item is
    open at a time on the frontend (accordion behavior), matching the
    Lovable design.
    """

    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=600)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "FAQ Item"
        verbose_name_plural = "FAQ Items"

    def __str__(self):
        return self.question   

class ContactSection(models.Model):
    """
    Singleton — the "Get in touch with Hyundai Susee" section: header
    text, showroom info cards (address, phone, email, working hours),
    and the coordinates used for the embedded map.
    """

    eyebrow_text = models.CharField(max_length=60, default="Visit Us")
    heading_line1 = models.CharField(max_length=100, default="Get in touch with")
    heading_highlight = models.CharField(
        max_length=50,
        default="Hyundai Susee",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default=(
            "Drop by our showroom, call us, or send an enquiry — we're "
            "here to help you drive home your dream Hyundai."
        ),
    )

    address_line1 = models.CharField(max_length=150, default="Susee Auto Complex, Main Road")
    address_line2 = models.CharField(max_length=150, default="Madurai, Tamil Nadu 625001")

    phone_1 = models.CharField(max_length=20, default="+91 98765 43210")
    phone_2 = models.CharField(max_length=20, blank=True, default="+91 98765 43211")

    email = models.EmailField(default="sales@hyundaisusee.com")

    working_hours_weekday = models.CharField(
        max_length=80, default="Mon – Sat: 9:00 AM – 8:00 PM"
    )
    working_hours_weekend = models.CharField(
        max_length=80, default="Sun: 10:00 AM – 5:00 PM"
    )

    map_latitude = models.FloatField(default=9.9252, help_text="Used for the embedded map.")
    map_longitude = models.FloatField(default=78.1198, help_text="Used for the embedded map.")
    map_place_label = models.CharField(
        max_length=100, default="Madurai",
        help_text="Label shown on the map card (e.g. city or showroom name).",
    )

    map_title = models.CharField(
        max_length=100, default="Find Our Hyundai Showroom",
        help_text="Heading shown above the embedded map.",
    )
    map_description = models.CharField(
        max_length=250, blank=True,
        default="Serving customers from Theni, Periyakulam, Bodinayakanur, Cumbum, Chinnamanur, Andipatti, and nearby areas.",
        help_text="Short text shown below the map heading.",
    )

    form_heading = models.CharField(max_length=100, default="Send an Enquiry")
    form_subtitle = models.CharField(
        max_length=200, default="Get personalized quotes, offers and finance options."
    )
    form_submit_label = models.CharField(max_length=50, default="Submit Enquiry")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Section"
        verbose_name_plural = "Contact Section"

    def __str__(self):
        return "Contact Section"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj   

class FooterSection(models.Model):
    """
    Singleton — footer branding text and copyright line. Social links,
    quick links, and models are handled separately (SocialLink model,
    static anchors, and the existing car inventory respectively).
    """

    description = models.CharField(
        max_length=250,
        default=(
            "Authorized Hyundai dealer offering the complete Hyundai "
            "range with best price, easy finance and premium service."
        ),
    )
    copyright_text = models.CharField(
        max_length=150, default="© 2026 Hyundai Susee Showroom. All rights reserved."
    )

    # Kept for backward compatibility / manual override — leave as "#" if
    # you're using the uploaded documents below instead.
    privacy_policy_url = models.CharField(max_length=200, default="#")
    terms_url = models.CharField(max_length=200, default="#")

    # NEW — upload the actual Privacy Policy / Terms & Conditions
    # document (PDF or Word) here. When a file is uploaded, the
    # frontend opens it directly in a new tab instead of using the
    # URL fields above.
    privacy_policy_file = models.FileField(
        upload_to="legal_docs/",
        storage=RawMediaCloudinaryStorage(),
        blank=True,
        null=True,
        help_text="Upload the Privacy Policy as a PDF or Word document.",
    )
    terms_conditions_file = models.FileField(
        upload_to="legal_docs/",
        storage=RawMediaCloudinaryStorage(),
        blank=True,
        null=True,
        help_text="Upload the Terms & Conditions as a PDF or Word document.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Section"

    def __str__(self):
        return "Footer Section"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SocialLink(models.Model):
    """
    One social media icon shown in the footer. Fully admin-managed —
    add, edit, remove, or reorder any platforms.
    """

    PLATFORM_CHOICES = [
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
        ("twitter", "Twitter / X"),
        ("linkedin", "LinkedIn"),
        ("whatsapp", "WhatsApp"),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=250)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.get_platform_display()      
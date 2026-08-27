from django.db import models


class FeaturedModel(models.Model):
    """Full-width banner directly under the Hero section."""

    badge_label = models.CharField(max_length=30, default="FEATURED")
    heading = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to="featured_models/")
    image_alt = models.CharField(
        max_length=150,
        blank=True,
        default="Hyundai Showroom",
        help_text="SEO alt text describing the banner image (e.g. 'Hyundai Showroom in Theni').",
    )
    cta_label = models.CharField(max_length=50, default="View Details", blank=True)
    cta_link = models.CharField(max_length=200, default="#models", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Featured Model Banner"
        verbose_name_plural = "Featured Model Banner"

    def __str__(self):
        return self.heading


class CarModelsSection(models.Model):
    """
    Singleton — header text above the car-models carousel
    ("FEATURED HYUNDAI MODELS" / "Explore the latest Hyundai lineup").
    """

    eyebrow_text = models.CharField(max_length=60, default="Featured Hyundai Models")
    heading_line1 = models.CharField(max_length=100, default="Explore the")
    heading_highlight = models.CharField(
        max_length=50,
        default="latest Hyundai lineup",
        help_text="Shown with the navy-to-cyan gradient style.",
    )
    subtitle = models.CharField(
        max_length=250,
        default="From city hatchbacks to premium SUVs and electric vehicles — find your perfect Hyundai.",
    )
    footnote = models.CharField(
        max_length=200,
        default="*Ex-showroom prices. On-road pricing varies by city & variant.",
        blank=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Car Models Section — Header"
        verbose_name_plural = "Car Models Section — Header"

    def __str__(self):
        return "Car Models Section Header"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class CarModel(models.Model):

    name = models.CharField(max_length=80, help_text="e.g. 'Hyundai Creta'")
    category_label = models.CharField(
        max_length=40, help_text="e.g. 'Premium SUV', 'Compact SUV'"
    )
    image = models.ImageField(upload_to="car_models/")
    image_alt = models.CharField(
        max_length=120,
        blank=True,
        help_text="SEO alt text for the car image, e.g. 'Hyundai Creta SUV'.",
    )
    detail_image = models.ImageField(
        upload_to="car_models_detail/",
        blank=True,
        null=True,
        help_text=(
            "Optional wide lifestyle/scenic photo shown as the background in the "
            "car's detail popup (e.g. car parked against a scenic backdrop). "
            "Falls back to the regular gradient card image if left blank."
        ),
    )
    detail_image_alt = models.CharField(
        max_length=150,
        blank=True,
        help_text=(
            "SEO alt text for the detail popup's lifestyle photo, e.g. "
            "'Hyundai Alcazar parked outside a grand estate'. Falls back to "
            "the regular image alt text if left blank."
        ),
    )

    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="In Lakhs, e.g. 11.00"
    )

    mileage_label = models.CharField(max_length=30, help_text="e.g. '17.7 kmpl' or '631 km range'")
    transmission_label = models.CharField(max_length=30, default="Auto/Manual")
    fuel_type_label = models.CharField(max_length=30, help_text="e.g. 'Petrol/Diesel', 'Electric'")

    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first (left side).")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"

    def __str__(self):
        return self.name
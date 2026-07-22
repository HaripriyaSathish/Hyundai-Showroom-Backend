from django.contrib import admin
from django.utils.html import format_html
from .models import (
    HeroContent, WhyChooseSection, WhyChooseCard,
    OffersSection, OfferCard,
    FinanceSection, FinanceFeatureCard, FinancePartner,
    TestDriveCTA,
    TestimonialsSection, Testimonial,
    GallerySection, GalleryImage,
    TrustedStatsSection, TrustedStat,
)
from .models import FAQSection, FAQItem
from .models import ContactSection
from .models import FooterSection, SocialLink


@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Badge", {"fields": ("badge_text",)}),
        ("Heading", {"fields": ("heading_line1", "heading_highlight", "heading_line2")}),
        ("Paragraph", {"fields": ("paragraph",)}),
        ("Buttons", {"fields": ("cta_book_label", "cta_offer_label", "cta_whatsapp_label")}),
        (
            "Feature badges",
            {"fields": ("feature_1_label", "feature_2_label", "feature_3_label")},
        ),
        (
            "Quote form card",
            {
                "fields": (
                    "form_badge_text",
                    "form_title",
                    "form_subtitle",
                    "form_footnote",
                )
            },
        ),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not HeroContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(WhyChooseSection)
class WhyChooseSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not WhyChooseSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(WhyChooseCard)
class WhyChooseCardAdmin(admin.ModelAdmin):
    # Manage all feature cards here (separate from the section header,
    # since cards aren't tied to it by a foreign key — there's only one
    # section anyway). Add, edit, remove, or reorder freely.
    list_display = ("title", "order", "icon", "is_active")
    list_display_links = ("title",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "icon")
    search_fields = ("title", "description")
    ordering = ("order",)


@admin.register(OffersSection)
class OffersSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not OffersSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(OfferCard)
class OfferCardAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "icon", "is_active")
    list_display_links = ("title",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "icon")
    search_fields = ("title", "description")
    ordering = ("order",)


@admin.register(FinanceSection)
class FinanceSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
        ("Finance Partners card", {"fields": ("partners_heading", "partners_subtitle")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not FinanceSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FinanceFeatureCard)
class FinanceFeatureCardAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "icon", "is_active")
    list_display_links = ("title",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "icon")
    ordering = ("order",)


@admin.register(FinancePartner)
class FinancePartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(TestDriveCTA)
class TestDriveCTAAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Text", {"fields": ("badge_text", "heading", "paragraph")}),
        ("Buttons", {"fields": ("cta_book_label", "cta_whatsapp_label", "whatsapp_number")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not TestDriveCTA.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not TestimonialsSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "purchased_model", "rating", "order", "is_active")
    list_display_links = ("customer_name",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "rating")
    search_fields = ("customer_name", "purchased_model")
    ordering = ("order",)


@admin.register(GallerySection)
class GallerySectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not GallerySection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "order", "is_active", "image_preview")
    list_display_links = ("caption",)
    list_editable = ("order", "is_active")
    ordering = ("order",)
    readonly_fields = ("image_preview_large", "created_at")
    fieldsets = (
        ("Basics", {"fields": ("caption", "image_alt", "order", "is_active")}),
        ("Image", {"fields": ("image", "image_preview_large")}),
        ("Meta", {"fields": ("created_at",)}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:6px;" />', obj.image.url)
        return "—"
    image_preview.short_description = "Preview"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:220px;border-radius:12px;" />', obj.image.url)
        return "No image uploaded yet"
    image_preview_large.short_description = "Current image"


@admin.register(TrustedStatsSection)
class TrustedStatsSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("badge_text", "heading")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not TrustedStatsSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TrustedStat)
class TrustedStatAdmin(admin.ModelAdmin):
    list_display = ("label", "count_to", "suffix", "order", "is_active")
    list_display_links = ("label",)
    list_editable = ("order", "is_active")
    ordering = ("order",)


@admin.register(FAQSection)
class FAQSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not FAQSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active")
    list_display_links = ("question",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("question", "answer")
    ordering = ("order",)    

@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle")}),
        ("Address", {"fields": ("address_line1", "address_line2")}),
        ("Contact details", {"fields": ("phone_1", "phone_2", "email")}),
        ("Working hours", {"fields": ("working_hours_weekday", "working_hours_weekend")}),
        ("Map", {"fields": ("map_latitude", "map_longitude", "map_place_label", "map_title", "map_description")}),
        ("Enquiry form text", {"fields": ("form_heading", "form_subtitle", "form_submit_label")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not ContactSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False    
    
@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Text", {"fields": ("description", "copyright_text")}),
        ("Legal links", {"fields": ("privacy_policy_url", "terms_url")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not FooterSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "order", "is_active")
    list_display_links = ("platform",)
    list_editable = ("order", "is_active")
    list_filter = ("platform", "is_active")
    ordering = ("order",)    
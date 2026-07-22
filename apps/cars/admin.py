from django.contrib import admin
from django.utils.html import format_html
from .models import FeaturedModel, CarModelsSection, CarModel


@admin.register(FeaturedModel)
class FeaturedModelAdmin(admin.ModelAdmin):
    list_display = ("heading", "badge_label", "is_active", "image_preview", "updated_at")
    list_filter = ("is_active",)
    readonly_fields = ("image_preview_large", "created_at", "updated_at")
    fieldsets = (
        ("Badge & Text", {"fields": ("badge_label", "heading", "subtitle")}),
        ("Image", {"fields": ("image", "image_alt", "image_preview_large")}),
        ("Button (optional)", {"fields": ("cta_label", "cta_link")}),
        ("Status", {"fields": ("is_active", "created_at", "updated_at")}),
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


@admin.register(CarModelsSection)
class CarModelsSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header text", {"fields": ("eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "footnote")}),
    )
    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not CarModelsSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "category_label", "price", "is_active", "image_preview")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "category_label")
    search_fields = ("name", "category_label")
    ordering = ("order",)
    readonly_fields = ("image_preview_large", "created_at")
    fieldsets = (
        ("Basics", {"fields": ("name", "category_label", "order", "is_active")}),
        ("Image", {"fields": ("image", "image_alt", "image_preview_large")}),
        ("Pricing", {"fields": ("price",)}),
        ("Specs", {"fields": ("mileage_label", "transmission_label", "fuel_type_label")}),
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
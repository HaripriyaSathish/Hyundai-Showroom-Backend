from rest_framework import serializers
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


class HeroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroContent
        fields = [
            "badge_text", "heading_line1", "heading_highlight", "heading_line2",
            "paragraph", "cta_book_label", "cta_offer_label", "cta_whatsapp_label",
            "feature_1_label", "feature_2_label", "feature_3_label",
            "form_title", "form_subtitle", "form_badge_text", "form_footnote",
        ]


class WhyChooseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseCard
        fields = ["icon", "title", "description"]


class WhyChooseSectionSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    class Meta:
        model = WhyChooseSection
        fields = ["eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "cards"]

    def get_cards(self, obj):
        active_cards = WhyChooseCard.objects.filter(is_active=True)
        return WhyChooseCardSerializer(active_cards, many=True).data


class OfferCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferCard
        fields = ["icon", "title", "description", "cta_label", "cta_link"]


class OffersSectionSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    class Meta:
        model = OffersSection
        fields = ["eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "cards"]

    def get_cards(self, obj):
        active_cards = OfferCard.objects.filter(is_active=True)
        return OfferCardSerializer(active_cards, many=True).data


class FinanceFeatureCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceFeatureCard
        fields = ["icon", "title", "description"]


class FinancePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancePartner
        fields = ["name"]


class FinanceSectionSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()
    partners = serializers.SerializerMethodField()

    class Meta:
        model = FinanceSection
        fields = [
            "eyebrow_text", "heading_line1", "heading_highlight", "subtitle",
            "partners_heading", "partners_subtitle", "cards", "partners",
        ]

    def get_cards(self, obj):
        active = FinanceFeatureCard.objects.filter(is_active=True)
        return FinanceFeatureCardSerializer(active, many=True).data

    def get_partners(self, obj):
        active = FinancePartner.objects.filter(is_active=True)
        return FinancePartnerSerializer(active, many=True).data


class TestDriveCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDriveCTA
        fields = [
            "badge_text", "heading", "paragraph",
            "cta_book_label", "cta_whatsapp_label", "whatsapp_number",
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["customer_name", "purchased_model", "review_text", "rating"]


class TestimonialsSectionSerializer(serializers.ModelSerializer):
    testimonials = serializers.SerializerMethodField()

    class Meta:
        model = TestimonialsSection
        fields = ["eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "testimonials"]

    def get_testimonials(self, obj):
        active = Testimonial.objects.filter(is_active=True)
        return TestimonialSerializer(active, many=True).data


class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ["image", "caption", "image_alt"]

    def get_image(self, obj):
        if obj.image:
            try:
                return obj.image.url
            except ValueError:
                return None
        return None


class GallerySectionSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = GallerySection
        fields = ["eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "images"]

    def get_images(self, obj):
        active = GalleryImage.objects.filter(is_active=True)
        return GalleryImageSerializer(active, many=True).data


class TrustedStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustedStat
        fields = ["count_to", "suffix", "label"]


class TrustedStatsSectionSerializer(serializers.ModelSerializer):
    stats = serializers.SerializerMethodField()

    class Meta:
        model = TrustedStatsSection
        fields = ["badge_text", "heading", "stats"]

    def get_stats(self, obj):
        active = TrustedStat.objects.filter(is_active=True)
        return TrustedStatSerializer(active, many=True).data
    


class FAQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = ["question", "answer"]


class FAQSectionSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = FAQSection
        fields = ["eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "items"]

    def get_items(self, obj):
        active = FAQItem.objects.filter(is_active=True)
        return FAQItemSerializer(active, many=True).data    
    

class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = [
            "eyebrow_text", "heading_line1", "heading_highlight", "subtitle",
            "address_line1", "address_line2",
            "phone_1", "phone_2", "email",
            "working_hours_weekday", "working_hours_weekend",
            "map_latitude", "map_longitude", "map_place_label",
            "map_title", "map_description",
            "form_heading", "form_subtitle", "form_submit_label",
        ]

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ["platform", "url"]


class FooterSectionSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField()
    privacy_policy_file_url = serializers.SerializerMethodField()
    terms_conditions_file_url = serializers.SerializerMethodField()

    class Meta:
        model = FooterSection
        fields = [
            "description", "copyright_text",
            "privacy_policy_url", "terms_url", "social_links",
            "privacy_policy_file_url", "terms_conditions_file_url",
        ]

    def get_social_links(self, obj):
        active = SocialLink.objects.filter(is_active=True)
        return SocialLinkSerializer(active, many=True).data

    def get_privacy_policy_file_url(self, obj):
        if obj.privacy_policy_file:
            try:
                request = self.context.get("request")
                url = obj.privacy_policy_file.url
                return request.build_absolute_uri(url) if request else url
            except ValueError:
                return None
        return None

    def get_terms_conditions_file_url(self, obj):
        if obj.terms_conditions_file:
            try:
                request = self.context.get("request")
                url = obj.terms_conditions_file.url
                return request.build_absolute_uri(url) if request else url
            except ValueError:
                return None
        return None      

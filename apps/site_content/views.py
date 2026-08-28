from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    HeroContent, WhyChooseSection, OffersSection, FinanceSection,
    TestDriveCTA, TestimonialsSection, GallerySection, TrustedStatsSection,
)
from .serializers import (
    HeroContentSerializer, WhyChooseSectionSerializer,
    OffersSectionSerializer, FinanceSectionSerializer,
    TestDriveCTASerializer, TestimonialsSectionSerializer,
    GallerySectionSerializer, TrustedStatsSectionSerializer,
)
from .models import FAQSection  # add to existing import
from .serializers import FAQSectionSerializer 

from .models import ContactSection  # add to existing import
from .serializers import ContactSectionSerializer
from .models import FooterSection  # add to existing import
from .serializers import FooterSectionSerializer


class HeroContentView(APIView):
    """GET /api/site-content/hero/"""

    def get(self, request):
        content = HeroContent.get_solo()
        return Response(HeroContentSerializer(content).data)


class WhyChooseView(APIView):
    """GET /api/site-content/why-choose/"""

    def get(self, request):
        section = WhyChooseSection.get_solo()
        return Response(WhyChooseSectionSerializer(section).data)


class OffersView(APIView):
    """GET /api/site-content/offers/"""

    def get(self, request):
        section = OffersSection.get_solo()
        return Response(OffersSectionSerializer(section).data)


class FinanceView(APIView):
    """GET /api/site-content/finance/"""

    def get(self, request):
        section = FinanceSection.get_solo()
        return Response(FinanceSectionSerializer(section).data)


class TestDriveCTAView(APIView):
    """GET /api/site-content/test-drive-cta/"""

    def get(self, request):
        content = TestDriveCTA.get_solo()
        return Response(TestDriveCTASerializer(content).data)


class TestimonialsView(APIView):
    """GET /api/site-content/testimonials/"""

    def get(self, request):
        section = TestimonialsSection.get_solo()
        return Response(TestimonialsSectionSerializer(section).data)


class GalleryView(APIView):
    """GET /api/site-content/gallery/"""

    def get(self, request):
        section = GallerySection.get_solo()
        return Response(GallerySectionSerializer(section).data)


class TrustedStatsView(APIView):
    """GET /api/site-content/trusted-stats/"""

    def get(self, request):
        section = TrustedStatsSection.get_solo()
        return Response(TrustedStatsSectionSerializer(section).data)
    
class FAQView(APIView):
    """GET /api/site-content/faq/"""

    def get(self, request):
        section = FAQSection.get_solo()
        return Response(FAQSectionSerializer(section).data)    
    
class ContactView(APIView):
    """GET /api/site-content/contact/"""

    def get(self, request):
        section = ContactSection.get_solo()
        return Response(ContactSectionSerializer(section).data)    
    
class FooterView(APIView):
    """GET /api/site-content/footer/"""

    def get(self, request):
        section = FooterSection.get_solo()
        return Response(FooterSectionSerializer(section, context={"request": request}).data)
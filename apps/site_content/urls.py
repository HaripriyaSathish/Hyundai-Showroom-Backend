from django.urls import path
from .views import (
    HeroContentView, WhyChooseView, OffersView, FinanceView,
    TestDriveCTAView, TestimonialsView, GalleryView, TrustedStatsView,
    FAQView, ContactView, FooterView,
)

urlpatterns = [
    path("hero/", HeroContentView.as_view(), name="hero-content"),
    path("why-choose/", WhyChooseView.as_view(), name="why-choose"),
    path("offers/", OffersView.as_view(), name="offers"),
    path("finance/", FinanceView.as_view(), name="finance"),
    path("test-drive-cta/", TestDriveCTAView.as_view(), name="test-drive-cta"),
    path("testimonials/", TestimonialsView.as_view(), name="testimonials"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("trusted-stats/", TrustedStatsView.as_view(), name="trusted-stats"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("footer/", FooterView.as_view(), name="footer"),
]
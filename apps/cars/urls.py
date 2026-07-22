from django.urls import path
from .views import FeaturedModelView, CarModelsView

urlpatterns = [
    path("featured/", FeaturedModelView.as_view(), name="featured-model"),
    path("models/", CarModelsView.as_view(), name="car-models"),
]
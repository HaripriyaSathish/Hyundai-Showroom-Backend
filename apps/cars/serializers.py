from rest_framework import serializers
from .models import FeaturedModel, CarModelsSection, CarModel


class FeaturedModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedModel
        fields = ["badge_label", "heading", "subtitle", "image", "image_alt", "cta_label", "cta_link"]

    def get_image(self, obj):
        if obj.image:
            try:
                return obj.image.url
            except ValueError:
                return None
        return None


class CarModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    detail_image = serializers.SerializerMethodField()

    class Meta:
        model = CarModel
        fields = [
            "name", "category_label", "image", "image_alt",
            "detail_image", "detail_image_alt", "price",
            "mileage_label", "transmission_label", "fuel_type_label",
        ]

    def get_image(self, obj):
        if obj.image:
            try:
                return obj.image.url
            except ValueError:
                return None
        return None

    def get_detail_image(self, obj):
        if obj.detail_image:
            try:
                return obj.detail_image.url
            except ValueError:
                return None
        return None


class CarModelsSectionSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = CarModelsSection
        fields = ["eyebrow_text", "heading_line1", "heading_highlight", "subtitle", "footnote", "cars"]

    def get_cars(self, obj):
        active_cars = CarModel.objects.filter(is_active=True)
        return CarModelSerializer(active_cars, many=True).data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FeaturedModel, CarModelsSection
from .serializers import FeaturedModelSerializer, CarModelsSectionSerializer


class FeaturedModelView(APIView):
    """GET /api/cars/featured/"""

    def get(self, request):
        featured = FeaturedModel.objects.filter(is_active=True).first()
        if not featured:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(FeaturedModelSerializer(featured).data)


class CarModelsView(APIView):
    """
    GET /api/cars/models/
    Returns the section header plus every active car, ordered.
    """

    def get(self, request):
        section = CarModelsSection.get_solo()
        return Response(CarModelsSectionSerializer(section).data)
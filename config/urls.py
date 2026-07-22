from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/leads/', include('apps.leads.urls')),
    path('api/cars/', include('apps.cars.urls')),
    path('api/site-content/', include('apps.site_content.urls')),
]

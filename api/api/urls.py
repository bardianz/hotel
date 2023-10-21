from django.urls import path, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from hotel.models import Hotel
from hotel.serializers import HotelSerializer
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

router = routers.DefaultRouter()
router.register(r'all', HotelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('', include('hotel.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
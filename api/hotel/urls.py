from django.urls import path, include
from hotel import views
from .views import HotelListView, HotelCreateView
from rest_framework import routers, viewsets
from hotel.models import Hotel
from hotel.serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

router = routers.DefaultRouter()
router.register(r'all', HotelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("hotels/", HotelListView.as_view(), name='hotel-list'),
    path("hotels/create/", HotelCreateView.as_view(), name='hotel-create'),
    path("hotels/inject/", views.inject_data),
]
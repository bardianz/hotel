from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", admin.site.urls),
    path('api/', include('hotel.urls')),
]
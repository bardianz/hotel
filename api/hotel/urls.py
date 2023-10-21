from django.urls import path
from hotel import views

urlpatterns = [
    path('hotels/', views.hotels_list),
    path('hotel/<int:pk>/', views.hotel_detail),
]
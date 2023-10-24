from django.contrib import admin
# from .models import Hotel,Picture,Amenitie
from .models import Hotel


class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "picture_url"]

admin.site.register(Hotel, HotelAdmin)


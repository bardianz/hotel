from django.contrib import admin
from .models import Hotel,Picture

# admin.site.register(Picture)

class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "picture_url"]

admin.site.register(Hotel, HotelAdmin)
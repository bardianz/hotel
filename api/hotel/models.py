from django.db import models

# Create your models here.


class Picture(models.Model):
    url = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"{self.url}"

class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    is_active = models.BooleanField(default=True)
    rate = models.FloatField()
    property_type = models.CharField(max_length=100, blank=True, default='')
    host_name = models.CharField(max_length=100, blank=True, default='')
    room_type = models.CharField(max_length=100, blank=True, default='')
    accommodates = models.CharField(max_length=100, blank=True, default='')
    guests_included = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    space = models.CharField(max_length=100, blank=True, default='')
    summary= models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    smart_location = models.CharField(max_length=100, blank=True, default='')
    picture_url = models.ForeignKey(Picture,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
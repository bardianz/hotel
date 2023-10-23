from django.db import models

# Create your models here.


class Picture(models.Model):
    url = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"{self.url}"

class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True, default='',null=True)
    is_active = models.BooleanField(default=True,null=True)
    rate = models.FloatField(null=True)
    property_type = models.CharField(max_length=100, blank=True, default='',null=True)
    host_name = models.CharField(max_length=100, blank=True, default='',null=True)
    room_type = models.CharField(max_length=100, blank=True, default='',null=True)
    accommodates = models.CharField(max_length=100, blank=True, default='',null=True)
    guests_included = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    space = models.CharField(max_length=100, blank=True, default='',null=True)
    summary= models.CharField(max_length=100, blank=True, default='',null=True)
    price = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    number_of_reviews = models.IntegerField(null=True,blank=True)
    smart_location = models.CharField(max_length=100, blank=True, default='',null=True)
    picture_url = models.ForeignKey(Picture,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name
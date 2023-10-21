# from rest_framework import serializers
# from hotel.models import Post


# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = (
#             "id",
#             "name",
#             "is_active",
#             "rate",
#             "property_type",
#             "host_name",
#             "room_type",
#             "accommodates",
#             "guests_included",
#             "bedrooms",
#             "beds",
#             "bathrooms",
#             "space",
#             "summary",
#             "latitude",
#             "smart_location",
#             "price",
#             "longitude",
#         )


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class Picture_Url(serializers.Serializer):
    url = serializers.CharField(max_length=200, default='')

class HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(max_length=100, default='')
    is_active = serializers.BooleanField(default=True)
    rate = serializers.FloatField()
    property_type = serializers.CharField(max_length=100, default='')
    host_name = serializers.CharField(max_length=100, default='')
    room_type = serializers.CharField(max_length=100, default='')
    accommodates = serializers.CharField(max_length=100, default='')
    guests_included = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    beds = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    space = serializers.CharField(max_length=100, default='')
    summary= serializers.CharField(max_length=100, default='')
    price = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    smart_location = serializers.CharField(max_length=100, default='')
    picture_url = Picture_Url()

from rest_framework import serializers
from .models import Hotel

class PictureSerializer(serializers.Serializer):
    url = serializers.CharField()

class HotelSerializer(serializers.ModelSerializer):
    picture_url = PictureSerializer()  # اضافه کردن مشخصه "picture"

    class Meta:
        model = Hotel
        fields = '__all__'

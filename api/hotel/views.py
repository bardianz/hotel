
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer
from extensions.data_injector import filter_data


class HotelListView(APIView):
    def get(self, request):
        queryset = Hotel.objects.all()
        serializer = HotelSerializer(queryset, many=True)
        return Response(serializer.data)

class HotelCreateView(APIView):
    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetailView(APIView):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            serializer = HotelSerializer(hotel)
            return Response(serializer.data)
        except Hotel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class HotelUpdateView(APIView):
    def put(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            serializer = HotelSerializer(hotel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Hotel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class HotelDeleteView(APIView):
    def delete(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            hotel.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Hotel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



def inject_data(request):
    data = filter_data()
    if request.method == 'GET':
        for iiem in data:
            url = iiem['picture_url']
            url = url['url']
            hotel_data = Hotel(
            id=iiem['id'],
            name=iiem['name'],
            rate=iiem['rate'],
            property_type=iiem['property_type'],
            host_name=iiem['host_name'],
            room_type=iiem['room_type'],
            accommodates=iiem['accommodates'],
            guests_included=iiem['guests_included'],
            bedrooms=iiem['bedrooms'],
            beds=iiem['beds'],
            bathrooms=iiem['bathrooms'],
            space=iiem['space'],
            summary=iiem['summary'],
            price=iiem['price'],
            longitude=iiem['longitude'],
            latitude=iiem['latitude'],
            amenities=iiem['amenities'],
            smart_location=iiem['smart_location'],
            picture_url={'url': url} )
            hotel_data.save()
        return HttpResponse("Data added successfully")

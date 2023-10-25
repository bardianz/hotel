
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer
from extensions.data_injector import filter_data
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


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


"""
this HotelDetailView class should rewrite again because does not work!
"""

# class HotelDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             hotel = Hotel.objects.filter(pk=pk)
#             print(hotel)
#             serializer = HotelSerializer(hotel)
#             return Response(serializer.data)
#         except Hotel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
@csrf_exempt
def hotel_detail(request, pk):

    try:
        hotel = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = HotelSerializer(hotel)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HotelSerializer(hotel, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        hotel.delete()
        return HttpResponse(status=204)

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

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from hotel.models import Hotel
from hotel.serializers import HotelSerializer

@csrf_exempt
def hotels_list(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def hotel_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
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



import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_all(loc):

    f = open(loc)
    data = json.load(f)

    all = []
    for i in data['hotels'] : all.append(i)

    f.close()
    return all


def filter_data():
    save_items = [
        "id",
        # "title",
        "name",
        # "is_active",
        "rate",
        "property_type",
        "host_name",
        "room_type",
        "accommodates",
        "guests_included",
        "bedrooms",
        "beds",
        "bathrooms",
        "space",
        "summary",
        "price",
        "longitude",
        "latitude",
        "smart_location",
        "picture_url",
    ]

    loc = str(BASE_DIR) + '/db.json'
    all = get_all(loc)
    # print(all[0])
    new_list = []
    for i in all:
        new_dict = {}
        for j in save_items:
            new_dict[j] = i[j]
        
        new_list.append(new_dict)
            
    print(new_list[0])
    return new_list



def inject_data(request):
    data = filter_data()
    if request.method == 'GET':
        for i in data:
            h = Hotel(
            id=i['id'],
            # title=i['title'],
            name=i['name'],
            # is_active=i['is_active'],
            rate=i['rate'],
            property_type=i['property_type'],
            host_name=i['host_name'],
            room_type=i['room_type'],
            accommodates=i['accommodates'],
            guests_included=i['guests_included'],
            bedrooms=i['bedrooms'],
            beds=i['beds'],
            bathrooms=i['bathrooms'],
            space=i['space'],
            summary=i['summary'],
            price=i['price'],
            longitude=i['longitude'],
            latitude=i['latitude'],
            smart_location=i['smart_location'],
            # picture_url=i['picture_url'],
                    )
            h.save()
        return HttpResponse()


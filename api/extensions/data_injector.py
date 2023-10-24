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
        "name",
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
        "amenities",
    ]
    loc = str(BASE_DIR) + '/db.json'
    all = get_all(loc)
    new_list = []
    for i in all:
        new_dict = {}
        for j in save_items:
            new_dict[j] = i[j]
        new_list.append(new_dict) 
    return new_list


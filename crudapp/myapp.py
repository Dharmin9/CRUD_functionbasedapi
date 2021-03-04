import requests
import json

URL = "http://127.0.0.1:8000/myapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}

    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}
    r = requests.get(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)


# get_data()


def post_data():
    data = {
        "e_no": "171203",
        "name": "anjali",
        "city": "ahmedabad",
        "branch": "computer",
    }
    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}
    r = requests.post(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {
        "id": "4",
        "e_no": "17129056",
        "name": "domesticss",
        # 'branch': 'Itss',
        "city": "bomby",
    }
    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}
    r = requests.put(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {"id": "4"}

    json_data = json.dumps(data)
    headers = {"content-type": "application/json"}
    r = requests.delete(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)


# delete_data()

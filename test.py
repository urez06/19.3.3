import requests
import json


def get_pets_by_status(status: str = "available"):
    headers = {'accept': 'application/json'}
    res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers=headers)
    try:
        res.json()
        print(res.status_code)
        print(res.text)
        print(res.json())
        print(type(res.json()))
    except json.decoder.JSONDecodeError:
        res.text


def post_pet(pet_id: int = 9223372036854774000):
    headers = {'Content-Type': 'application/json'}
    data_for_post = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Peselevich",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    res = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data_for_post)
    try:
        res.json()
        print(res.status_code)
        print(res.text)
        print(res.json())
        print(type(res.json()))
    except json.decoder.JSONDecodeError:
        res.text


def put_pet(pet_id: int = 9223372036854774000):
    headers = {'Content-Type': 'application/json'}
    data_for_put = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Peselevich",
        "photoUrls": [
            "https://oir.mobi/uploads/posts/2021-04/1619125911_46-oir_mobi-p-sobaka-ulibaka-zhivotnie-krasivo-foto-48.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "sold"
    }
    res = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, json=data_for_put)
    try:
        res.json()
        print(res.status_code)
        print(res.text)
        print(res.json())
        print(type(res.json()))
    except json.decoder.JSONDecodeError:
        res.text


def delete_pet(pet_id: int = 9223372036854774000):
    headers = {'accept': 'application/json', 'api_key': 'special-key'}
    res = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}", headers=headers)
    try:
        res.json()
        print(res.status_code)
        print(res.text)
        print(res.json())
        print(type(res.json()))
    except json.decoder.JSONDecodeError:
        res.text

get_pets_by_status()
post_pet()
put_pet()
delete_pet()
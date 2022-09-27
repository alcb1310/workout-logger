import requests
from environment import *

headers = {
    "x-app-id": nutrition_api_appid,
    'x-app-key': nutrition_api_key
}

body = {
    "query": input("Tell me which exercises you did: "),
    "gender": nutrition_gener,
    "weight_kg": nutrition_weight,
    "height_cm": nutrition_height_cm,
    "age": nutrition_age
}

response = requests.post(
    url=f"{nutrition_api_end_point}/exercise", json=body, headers=headers)
response.raise_for_status()

exercises = [{"name": data['name'], "duration": data['duration_min'], "calories": data['nf_calories']} for data in response.json()['exercises']]
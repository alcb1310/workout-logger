import requests
from datetime import datetime
from environment import *

headers = {
    "x-app-id": nutrition_api_appid,
    'x-app-key': nutrition_api_key
}

body = {
    "query": "swam 2km freestyle walked 2km ran 3km",
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 168,
    "age": 47
}

right_now = datetime.now()

response = requests.post(
    url=f"{nutrition_api_end_point}/exercise", json=body, headers=headers)
response.raise_for_status()

excercise = [{"name": data['name'], "duration": data['duration_min'], "calories": data['nf_calories']} for data in response.json()['exercises']]
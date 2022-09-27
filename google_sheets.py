import requests
from environment import *

headers = {
    "Authorization": f"Bearer {sheety_api_bearer_token}"
}

response = requests.get(url=sheety_api_endpoint, headers=headers)
response.raise_for_status()


def save_data(data):
    response = requests.post(url=sheety_api_endpoint, json=data, headers=headers)
    response.raise_for_status()
    
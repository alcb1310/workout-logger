import requests
from environment import *

headers = {
    "Authorization": f"Bearer {sheety_api_bearer_token}"
}

# response = requests.get(url=sheety_api_endpoint, headers=headers)
# response.raise_for_status()


def save_data(data):
    """
    Recieves the data in a dictionary with this format:
    {
        "workout": {
            "date": current date,
            "time": current_time,
            "exercise": the name of the exercise,
            "duration": duration of the exercise,
            "calories": calories burned
        }
    }
    """
    response = requests.post(url=sheety_api_endpoint, json=data, headers=headers)
    response.raise_for_status()
    
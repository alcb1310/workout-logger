from excercise import exercises
from datetime import datetime
from google_sheets import save_data

right_now = datetime.now()

for exercise in exercises:
    data = {
        "workout": {
            "date": right_now.strftime("%Y-%m-%d"),
            "time": right_now.strftime("%H:%M"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration'],
            "calories": exercise['calories']
        }
    }
    save_data(data)

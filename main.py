import requests
from datetime import datetime
import os

WEIGHT_KG = 81
HEIGHT_CM = 176
AGE = 31
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
TOKEN = os.environ["TOKEN"]

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e0018555e89e3af42ab4ff77ea396bd4/myWorkouts/workouts"


exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=exercise_parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # No Authentication
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )

    # Bearer Token Authentication
    # bearer_headers = {
    #     "Authorization": f"Bearer {TOKEN}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )




import requests
import datetime as dt
import json


api_id = "ef0655b5"
api_key ="08233854a813796a7225556490a8104e"
workout_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

# url = "https://developer.nutritionix.com"

ask = input("Tell me which exercises you did: ")

header= {

        "x-api-id" : api_id,
        "x-app-key" : api_key      
}

parameters = {
    "query": ask,
    "gender": "male",
    "weight_kg": 98,
    "height_cm": 174,
    "age": 27
}

response = requests.post(workout_url, json=parameters, headers=header)
result = response.json()
print(result)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
time_now = dt.datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "sayfa1": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
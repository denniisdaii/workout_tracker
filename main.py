from dotenv import load_dotenv
import os
import requests
from datetime import datetime
load_dotenv()

params = {
    "query":input("what exercise"),
    "gender":os.getenv("GENDER"),
    "weight_kg":os.getenv("WEIGHT"),
    "height_cm":os.getenv("HEIGHT"),
    "age":os.getenv("AGE")
}
headers = {
    "x-app-id":os.getenv("APP_ID"),
    "x-app-key":os.getenv("API_KEY"),
}

base_url="https://trackapi.nutritionix.com"
exercise_endpoint = "/v2/natural/exercise"
response = requests.post(url=f"{base_url}{exercise_endpoint}", json=params, headers=headers)
response.raise_for_status()
results = response.json()

exercise = results["exercises"][0]["name"].title()
duration = results["exercises"][0]["duration_min"]
calories = results["exercises"][0]["nf_calories"]

now = datetime.now()
params2 = {
    "workout":{
    "date":now.strftime("%d/%m/%Y"),
    "time":now.strftime("%H:%M:%S"),
    "exercise":exercise,
    "duration":duration,
    "calories":calories
    }
}

auth = {
    "Authorization":f"Bearer {os.getenv("AUTH_TOKEN")}"
}

reponse = requests.post(url=f"https://api.sheety.co/{os.getenv("SHEET_ENDPOINT")}/myWorkouts/workouts", json=params2, headers=auth)
reponse.raise_for_status()

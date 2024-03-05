import requests
import os
from datetime import datetime

EXERCISE_APP_ID = os.environ['EXERCISE_APP_ID']
EXERCISE_API_KEY = os.environ['EXERCISE_API_KEY']
AUTHORISATION_KEY = os.environ['AUTHORISATION_KEY']
EXERCISE_ENDPOINT = os.environ['EXERCISE_ENDPOINT']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
WEIGHT_KG = 90
HEIGHT_CM = 184
AGE = 19
query = input("Tell me which exercises you did: ")
DATE = datetime.now()
FORMATTED_DATE = DATE.strftime("%Y/%m/%d")
TIME = datetime.time(DATE)
FORMATTED_TIME = TIME.strftime("%H:%M:%S")

EXERCISE_PARAMS = {
    'query': query,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY
}

response = requests.post(EXERCISE_ENDPOINT, json=EXERCISE_PARAMS, headers=headers)
data = response.json()['exercises']

sheety_headers = {
    'Authorization': f'Basic {AUTHORISATION_KEY}',
    'Content-Type': 'application/json'
}

for i in range(len(data)):
    exercise = {
        'sheet1': {
            'date': FORMATTED_DATE,
            'time': FORMATTED_TIME,
            'exercise': data[i]['name'],
            'duration': data[i]['duration_min'],
            'calories': data[i]['nf_calories']
        }
    }
    add_row = requests.post(SHEETY_ENDPOINT, json=exercise, headers=sheety_headers)
    print(add_row.text)

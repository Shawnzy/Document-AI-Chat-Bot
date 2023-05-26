import requests

API_URL = "http://localhost:3000/api/v1/prediction/034fcb24-decf-4339-8b9f-610f22ba9b81"


def query(payload):
    response = requests.post(API_URL, json=payload)
    print(response.json())
    return response.json()


output = query(
    {
        "question": "Hey, how are you?",
    }
)

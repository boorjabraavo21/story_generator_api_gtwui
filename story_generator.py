import requests
import json

url = "http://127.0.0.1:5000/v1/completions"
headers = {"Content-Type": "application/json"}

while True:
    user_message = input("Buenas, ¿qué quieres saber?> ")
    body = {"prompt": user_message, "max_tokens": 200, "temperature":0.8,
            "top_p": 0.9, "seed": 15}
    response = requests.post(url, headers=headers, json=body)
    message_response = json.loads(response.content.decode("utf-8"))
    assistant_message = message_response["choices"][0]["text"]
    print(assistant_message)
    print("\n")
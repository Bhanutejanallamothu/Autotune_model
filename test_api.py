import requests

API_URL = "https://router.huggingface.co/models/bhanuteja110/Autotune"
headers = {
    "Authorization": "Bearer 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"
}

data = {
    "inputs": "test"
}

response = requests.post(API_URL, headers=headers, json=data)
print(response.status_code)
print(response.json())

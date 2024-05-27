import requests

url = "http://localhost:8000/predict/"

data ={
    "area": "zimbabwe",
    "item": "sorghum",
    "avg_rain": 100,
    "pesticides": 2,
    "temperature": 30
}

response = requests.post(url, json=data)

print(response.json())
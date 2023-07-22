import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

print(response.json())
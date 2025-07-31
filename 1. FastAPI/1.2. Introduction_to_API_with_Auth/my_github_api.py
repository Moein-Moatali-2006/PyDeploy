import requests
import json

response = requests.get("https://api.github.com/users/Moein-Moatali-2006")

print(response.status_code)
print(json.loads(response.text))

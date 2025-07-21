import requests

url = "https://api.example.com/data"
token = ""

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())

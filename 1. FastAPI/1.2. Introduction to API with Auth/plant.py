import os
import argparse
import requests
import json
import dotenv


dotenv = dotenv.load_dotenv()

parser = argparse.ArgumentParser(description="Get Flower name and show flower image")
parser.add_argument("--plant_path", help="plant path")
args = parser.parse_args()
print(args.plant_path)
print("-------------------------------------------------------------")

try:
    API_KEY = os.getenv("PlantNet_API_KEY")
    PROJECT = "all"
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    image_path_1 = args.plant_path
    image_data_1 = open(image_path_1, 'rb')

    data = { 'organs': ['flower'] }

    files = [
    ('images', (image_path_1, image_data_1))]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    print(response.status_code)
    print(json_result)
except:
    print("API ERROR")
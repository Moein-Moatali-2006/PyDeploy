import os
import dotenv
import json
import asyncio
import requests


dotenv.load_dotenv()

async def rhyme_finder(word: str= None):
    try:
        API_KEY = os.getenv("API_KEY_RHYME_FINDER")
        url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
        response = requests.request("GET", url)
        result = json.loads(response.text)
        for i in result["data_items"]:
            print(i)
    except Exception as e:
        print("Error", e)

async def get_states():
    try:
        url = "https://iran-locations-api.ir/api/v1/fa/states"
        response = requests.request("GET", url)
        result = json.loads(response.text)
        for i in result:
            print(i)
    except Exception as e:
        print("Error", e)

async def get_cities(state_id: int= None):
    try:
        url = f"https://iran-locations-api.ir/api/v1/fa/states?id={state_id}"
        response = requests.request("GET", url)
        result = json.loads(response.text)

        print("name:", result["name"])
        print("latitude:", result["latitude"])
        print("longitude:", result["longitude"])
    except Exception as e:
        print("Error", e)

async def main():
    # values are test. write your own values
    await asyncio.gather(rhyme_finder("جان"),
                        get_states(),
                        get_cities(1))

asyncio.run(main())




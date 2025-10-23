import os
import dotenv
import json
import asyncio
import requests


dotenv.load_dotenv()

async def rhyme_finder(word: str=None):
    try:
        API_KEY = os.getenv("API_KEY_RHYME_FINDER")
        url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
        response = requests.request("GET", url)
        result = json.loads(response.text)
        for i in result["data_items"]:
            print(i)
    except:
        print("Error")


# asyncio.run(rhyme_finder("جان"))




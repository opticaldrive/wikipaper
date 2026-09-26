# Python 3
import json

import certifi
import ssl

ssl_ctx = ssl.create_default_context(
    cafile=certifi.where()
)  # apparently removing this still breaks things uh


# Get today's date in YYYY-MM-DD format.
import datetime

today = datetime.datetime.now()
date = today.strftime("%Y/%m/%d")

# Choose your language, and get today's featured content.
# import requests
import aiohttp
import asyncio

import json

language = "en"  # English Wikipedia
headers = {"User-Agent": "YOUR_APP_OR_USER_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)"}

url = "https://api.wikimedia.org/feed/v1/wikipedia/" + language + "/featured/" + date
# response = aiohttp.get(url, headers=headers)
# data = response.json()


async def get_featured_content():
    connector = aiohttp.TCPConnector(ssl=ssl_ctx)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            print(json.dumps(data, indent=2))
            if "onthisday" in data:
                print("--- ON THIS DAY ---")
                for event in data["onthisday"]:
                    print(f"• {event['text']}")

            # To parse the "Did You Know" section specifically:
            if "tfa" in data:  # Today's Featured Article
                print(f"\n--- FEATURED ARTICLE: {data['tfa']['title']} ---")
                print(data["tfa"]["extract"])
            return data


asyncio.run(get_featured_content())

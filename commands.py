import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = f'https://discord.com/api/v10/applications/{os.environ["DISCORD_CLIENT_ID"]}/commands'

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "a",
    "type": 1,
    "description": "",
    "options": [
        {
            "name": "text",
            "description": "",
            "type": 3,
            "required": True
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": f'Bot {os.environ["DISCORD_CLIENT_SECRET"]}'
}

r = requests.post(url, headers=headers, json=json)
import requests
import os
from dotenv import load_dotenv
load_dotenv()


url = f"https://discord.com/api/v10/applications/{os.environ['DISCORD_CLIENT_ID']}/guilds/{os.environ['TESTING_GUILD']}/commands"

# This is an example USER command, with a type of 2
json = {
    "name": "a",
    "type": 2
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": f"Bot {os.environ['DISCORD_CLIENT_SECRET']}"
}

r = requests.post(url, headers=headers, json=json)
import requests
import os
from dotenv import load_dotenv
load_dotenv()

for x in []:
    res = requests.delete(
        "https://discord.com/api/v10/applications/" + os.environ["DISCORD_CLIENT_ID"] + "/commands/" + x,
        headers={
            "Authorization": "Bot " + os.environ["DISCORD_CLIENT_SECRET"]
        },
    )
    print(res.status_code)

commands = [
    {
        "name": "a",
        "type": 3
    },
    {
        "name": "p",
        "type": 5
    }
]
for x in commands:
    r = requests.post(
        "https://discord.com/api/v10/applications/" + os.environ["DISCORD_CLIENT_ID"] + "/commands",
        headers={
            "Authorization": "Bot " + os.environ["DISCORD_CLIENT_SECRET"]
        },
        json=x
    )
    print(r.status_code)
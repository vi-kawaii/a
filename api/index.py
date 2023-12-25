import sys
from flask import Flask
from flask_discord_interactions import DiscordInteractions
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]

@discord.command()
def ping(ctx, pong: str = "pong"):
    f"Respond with a friendly 'pong'!"
    return f"{pong} with signature verification!"

discord.set_route("/interactions")
discord.update_commands()

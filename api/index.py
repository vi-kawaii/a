import sys
from chatterbot import ChatBot
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

app.config["DONT_REGISTER_WITH_DISCORD"] = True

bot = ChatBot("a")

@discord.command()
def a(ctx, text: str):
    return bot.get_response(text)

discord.set_route("/interactions")
discord.update_commands(guild_id=os.environ["TESTING_GUILD"])

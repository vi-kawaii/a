import sys
from flask import Flask
from flask_discord_interactions import DiscordInteractions
from dotenv import load_dotenv
from textblob import TextBlob
import os

load_dotenv()

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]

app.config["DONT_REGISTER_WITH_DISCORD"] = True

@discord.command()
def a(ctx, text: str):
    # Создаем объект TextBlob для анализа текста
    blob = TextBlob(text)

    # Получаем оценку настроения
    sentiment_score = blob.sentiment.polarity

    # Определяем настроение на основе оценки
    if sentiment_score > 0:
        mood = "positive"
    elif sentiment_score < 0:
        mood = "negative"
    else:
        mood = "neutral"

    return f"You wrote: {text}\nSentiment Analysis: {mood}"

discord.set_route("/interactions")
discord.update_commands()

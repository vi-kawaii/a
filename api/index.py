import sys
from flask import Flask
from flask_discord_interactions import DiscordInteractions
from dotenv import load_dotenv
from textblob import TextBlob
from langdetect import detect
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
    # Определяем язык текста
    language = detect(text)

    # Если язык не английский, переводим текст на английский
    if language != 'en':
        blob = TextBlob(text)
        text = str(blob.translate(to='en'))

    # Создаем объект TextBlob для анализа текста
    blob = TextBlob(text)

    # Получаем оценку настроения
    sentiment_score = blob.sentiment.polarity

    # Определяем настроение на основе оценки
    if sentiment_score > 0:
        mood = "позитивное"
    elif sentiment_score < 0:
        mood = "негативное"
    else:
        mood = "нейтральное"

    return f"Вы написали: {text}\nАнализ настроения: {mood}"

discord.set_route("/interactions")
discord.update_commands()

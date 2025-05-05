import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import os

KICK_USERNAME = os.getenv("KICK_USERNAME")
KICK_URL = f"https://kick.com/{KICK_USERNAME}"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

def is_live():
    try:
        response = requests.get(KICK_URL)
        return 'isLive' in response.text
    except:
        return False

def notify_group():
    message = f"{KICK_USERNAME} yayına başladı! 🎮\nŞimdi izle: {KICK_URL}"
    bot.send_message(chat_id=CHAT_ID, text=message)

already_live = False

while True:
    live_now = is_live()
    if live_now and not already_live:
        notify_group()
        already_live = True
    elif not live_now:
        already_live = False
    time.sleep(60)
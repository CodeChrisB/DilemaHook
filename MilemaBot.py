import random
from DiscordWebhook import *
from register import Quotes, Character
from ChracterCustomizer import customizeWebhook
import sys
import os


# Discord webhook URL 
os.system('cls')
with open(".env", "r", encoding="utf-8") as f:
    WEBHOOK_URL = f.read().strip()



quotes = Quotes()
# Register character quote files (filename is Characters/{enum.value}.txt)
quotes.register(Character.Breadbot)
#quotes.register(Character.Morgana)
# Get a random quote
character, quote = quotes.getRandomQuote()

discord = DiscordWebhook(webhook_url=WEBHOOK_URL)
customizeWebhook(discord, character)
discord.send(quote)

from DiscordWebhook import DiscordWebhook
from register import Character
from ChracterCustomizer import customizeWebhook
import os

os.system('cls')
with open(".env", "r", encoding="utf-8") as f:
    WEBHOOK_URL = f.read().strip()

def select_character():
    print("=" * 40)
    print("   MilemaBot - Character Talk Utility")
    print("=" * 40)
    print("Select a character to talk as:\n")
    for idx, char in enumerate(Character):
        print(f"  [{idx + 1}] {char.value}")
    print()
    while True:
        try:
            choice = int(input("Enter the number of your character: "))
            if 1 <= choice <= len(Character):
                return list(Character)[choice - 1]
        except ValueError:
            pass
        print("Invalid selection. Please enter a valid number.\n")

character = select_character()
print("\nType your message below. Press Enter to send.")
print("-" * 40)
message = input(f"> {character.value}: ")
print("-" * 40)

webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
customizeWebhook(webhook, character)
webhook.send(message)
print(f"\nMessage sent as {character.value}!\n")


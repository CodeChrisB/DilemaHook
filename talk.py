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

def select_message_type():
    print("\nSelect the type of message to send:")
    print("  [1] Single Message")
    print("  [2] Image with Text")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2]:
                return choice
        except ValueError:
            pass
        print("Invalid selection. Please enter 1 or 2.\n")

character = select_character()
message_type = select_message_type()

print("\nType your message below. Press Enter to send.")
print("-" * 40)

if message_type == 1:
    message = input(f"> {character.value}: ")
    print("-" * 40)
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)
    webhook.send(message)
    print(f"\nMessage sent as {character.value}!\n")
elif message_type == 2:
    image_url = input("Enter the image URL: ")
    message = input(f"> {character.value} (text to send with image): ")
    print("-" * 40)
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)
    webhook.send(message)
    webhook.send(image_url)
    print(f"\nText and image sent as {character.value}!\n")


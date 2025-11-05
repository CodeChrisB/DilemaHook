from DiscordWebhook import DiscordWebhook
from register import Character
from ChracterCustomizer import customizeWebhook
import os
import time

# Clear screen
os.system('cls')

# Read CSV-style .env
entries = []
with open(".env", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line or ";" not in line:
            continue
        name, url = line.split(";", 1)
        entries.append((name.strip(), url.strip()))

# Show choices to user
for i, (name, _) in enumerate(entries, 1):
    print(f"[{i}] {name}")

# Ask for selection
choice = 0
while choice < 1 or choice > len(entries):
    try:
        choice = int(input("Select an entry: "))
    except ValueError:
        pass

WEBHOOK_URL = entries[choice-1][1]
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
    print("  [2] Multi Message")
    print("  [3] Image with Text")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2, 3]:
                return choice
        except ValueError:
            pass
        print("Invalid selection. Please enter 1, 2, or 3.\n")

character = select_character()
message_type = select_message_type()

print("-" * 40)

# --- Single Message ---
if message_type == 1:
    print("\nType your message below. Press Enter to send.")
    message = input(f"> {character.value}: ")
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)
    webhook.send(message)
    print(f"\nMessage sent as {character.value}!\n")

# --- Multi Message ---
elif message_type == 2:
    print("\nEnter multiple lines. Press Enter on an empty line to finish.\n")
    lines = []
    while True:
        line = input(f"> {character.value}: ")
        if line.strip() == "":
            break
        lines.append(line)

    if not lines:
        print("No messages entered.\n")
    else:
        webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
        customizeWebhook(webhook, character)
        for line in lines:
            webhook.send(line)
            time.sleep(0.5)  # small delay between messages
        print(f"\n{len(lines)} messages sent as {character.value}!\n")

# --- Image with Text ---
elif message_type == 3:
    image_url = input("Enter the image URL: ")
    message = input(f"> {character.value} (text to send with image): ")
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)
    webhook.send(message)
    webhook.send(image_url)
    print(f"\nText and image sent as {character.value}!\n")

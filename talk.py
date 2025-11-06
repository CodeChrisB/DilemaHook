import os
import time
from typing import List, Dict, Any
import requests
import json
from DiscordWebhook import DiscordWebhook
from register import Character
from ChracterCustomizer import customizeWebhook

# --------------------------
# Clear screen
# --------------------------
os.system('cls')

# --------------------------
# Webhook selection
# --------------------------
def set_webhook_url():
    entries = []
    with open(".env", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ";" not in line:
                continue
            name, url = line.split(";", 1)
            entries.append((name.strip(), url.strip()))

    print("\nSelect a channel/webhook:")
    for i, (name, _) in enumerate(entries, 1):
        print(f"[{i}] {name}")

    choice = 0
    while choice < 1 or choice > len(entries):
        try:
            choice = int(input("Enter the number of your channel: "))
        except ValueError:
            pass
    return entries[choice - 1][1]

# --------------------------
# Character selection
# --------------------------
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

# --------------------------
# Message type selection
# --------------------------
def select_message_type():
    print("\nSelect the type of message to send:")
    print("  [1] Single Message")
    print("  [2] Multi Message")
    print("  [3] Image with URL")
    print("  [4] Local Files (Image/GIF/MP4)")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2, 3, 4]:
                return choice
        except ValueError:
            pass
        print("Invalid selection.\n")

# --------------------------
# Local file browser
# --------------------------
def emoji_for_file(path):
    ext = path.lower().split('.')[-1]
    if ext in ["png", "jpg", "jpeg", "gif", "webp"]:
        return "🖼️"
    elif ext in ["mp4", "mov", "webm"]:
        return "🎞️"
    else:
        return "📄"

def browse_data_folder(base_path="data"):
    current_path = base_path
    while True:
        entries = sorted(os.listdir(current_path))
        menu = []
        for i, entry in enumerate(entries, 1):
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                menu.append((entry, full_path, "folder"))
            else:
                menu.append((entry, full_path, "file"))

        print("\nAvailable entries:\n")
        for i, (name, _, typ) in enumerate(menu, 1):
            if typ == "folder":
                print(f"[{i}] 📁 {name}")
            else:
                print(f"[{i}] {emoji_for_file(name)} {name}")

        choice = input("\nEnter the number to select (or 'b' to go back): ")
        if choice.lower() == "b":
            if os.path.abspath(current_path) == os.path.abspath(base_path):
                print("Already at root folder.")
            else:
                current_path = os.path.dirname(current_path)
            continue

        try:
            choice = int(choice)
            if 1 <= choice <= len(menu):
                name, full_path, typ = menu[choice - 1]
                if typ == "folder":
                    current_path = full_path
                else:
                    return full_path
        except ValueError:
            pass
        print("Invalid selection.")

# --------------------------
# Main script
# --------------------------
character = select_character()
message_type = select_message_type()
WEBHOOK_URL = set_webhook_url()

print("-" * 40)

# --- Single Message ---
if message_type == 1:
    message = input(f"> {character.value}: ")
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)
    webhook.send(content=message)
    print(f"\nMessage sent as {character.value}!\n")

# --- Multi Message ---
elif message_type == 2:
    print("\nEnter multiple lines. Press Enter on an empty line to finish.\n")
    lines = []
    while True:
        line = input(f"> {character.value}: ")
        if not line.strip():
            break
        lines.append(line)

    if lines:
        webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
        customizeWebhook(webhook, character)
        for line in lines:
            webhook.send(content=line)
            time.sleep(0.5)
        print(f"\n{len(lines)} messages sent as {character.value}!\n")
    else:
        print("No messages entered.\n")

# --- Image with URL ---
elif message_type == 3:
    image_url = input("Enter the image URL: ")
    message = input(f"> {character.value} (text to send with image): ")
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)
    if message.strip():
        webhook.send(content=message)
    webhook.send(content=None, files=None, embeds=None)
    webhook.send(content=None, embeds=None)
    webhook.send(content=None)

# --- Send Local File ---
elif message_type == 4:
    selected = browse_data_folder("data")
    message = input(f"> {character.value} (optional text): ")
    webhook = DiscordWebhook(webhook_url=WEBHOOK_URL)
    customizeWebhook(webhook, character)

    if message.strip():
        webhook.send(content=message, files=[selected])
    else:
        webhook.send(files=[selected])

    print(f"\nFile '{os.path.basename(selected)}' sent as {character.value}!\n")

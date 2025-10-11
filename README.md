# MilemaBot

MilemaBot is a simple Discord webhook utility that allows you to send character-themed messages to a Discord channel. Each character has its own set of quotes and a customizable avatar and username. The bot can be used interactively or to send random quotes from a character.

## Features

- Send messages as different characters to Discord via webhooks.
- Each character has a unique avatar and username.
- Easily add new characters and quotes.
- Supports sending custom messages or random quotes.

## Project Structure

- `MilemaBot.py` - Main script to send a random quote as a character.
- `talk.py` - Interactive utility to send a custom message as a selected character.
- `ChracterCustomizer.py` - Handles character avatar and username customization.
- `register.py` - Manages character registration and quote loading.
- `DiscordWebhook.py` - Handles Discord webhook communication.
- `CharacterLines/` - Folder containing text files with quotes for each character (e.g., `Breadbot.txt`, `Morgana.txt`).
- `.env` - Contains your Discord webhook URL (see below).
- `talk.bat` - Batch file to run `talk.py` on Windows.

## Setup

1. **Clone the repository and install dependencies**  
   This project requires Python 3 and the `requests` library.  
   Install dependencies with:
   ```sh
   pip install requests
   ```

2. **Configure the `.env` file**  
   The `.env` file should contain your Discord webhook URL on a single line.  
   Example:
   ```
   https://discord.com/api/webhooks/your_webhook_id/your_webhook_token
   ```

3. **Add character quote files**  
   Place your character quote files (e.g., `Breadbot.txt`, `Morgana.txt`) in a folder named `CharacterLines` in the same directory as the scripts. Each file should contain one quote per line.

## Usage

- **Send a random quote:**  
  Run:
  ```sh
  python MilemaBot.py
  ```
  This will send a random quote from a registered character to your Discord channel.

- **Send a custom message as a character:**  
  Run:
  ```sh
  python talk.py
  ```
  Follow the prompts to select a character and enter your message.

## Customization

- To add new characters, update the `Character` enum in `register.py` and add their avatar info in `ChracterCustomizer.py`.
- Add a corresponding quote file in the `CharacterLines` folder.

## .env File

The `.env` file is required and must contain your Discord webhook URL.  
**Example:**
```
https://discord.com/api/webhooks/1234567890/abcdefghijklmnopqrstuvwxyz
```
Do not share your webhook URL publicly.

---

**Note:**  
This project is for fun and demonstration purposes. Use responsibly and do not spam Discord servers.

import random
from enum import Enum
import os

class Character(Enum):
    Breadbot = "Breadbot"
    Morgana = "Morgana"
    # Add more characters as needed

class Quotes:
    def __init__(self):
        self.quotes = {}

    def register(self, character: Character):
        # Build the filename from the enum value
        filename = os.path.join("CharacterLines", f"{character.value}.txt")
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Quote file not found: {filename}")
        # Read quotes from the file
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        # Add to internal quotes dictionary
        if character not in self.quotes:
            self.quotes[character] = []
        self.quotes[character].extend(lines)

    def getRandomQuote(self):
        # Flatten all quotes and pick one at random, returning quote and character
        all_quotes = [
            (character, quote)
            for character, quotes in self.quotes.items()
            for quote in quotes
        ]
        if not all_quotes:
            return None
        character, quote = random.choice(all_quotes)
        return character, quote
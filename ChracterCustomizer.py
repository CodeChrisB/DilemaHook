from register import Character

# Define avatar URLs and names for each character
CHARACTER_AVATARS = {
    Character.Breadbot: {
        "username": "Breadbot",
        "avatar_url": "https://media.discordapp.net/attachments/1417936473570676867/1426339328107479141/BreadbotAvatar.png?ex=68eadd83&is=68e98c03&hm=afcf15bfe9dbdaa41bc60f3bdd7ca725858be761c1d623afa42ff4bb92f44a6a&=&format=webp&quality=lossless"
    },
    Character.Morgana: {
        "username": "Morgana",
        "avatar_url": "https://example.com/morgana_avatar.png"
    },
    # Add more characters as needed
}

def customizeWebhook(webhook, character_enum):
    # Set the username and avatar_url for the webhook based on the character
    info = CHARACTER_AVATARS.get(character_enum)
    if info:
        webhook.set_username(info["username"])
        webhook.set_avatar_url(info["avatar_url"])
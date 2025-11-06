from register import Character

# Define avatar URLs and names for each character
CHARACTER_AVATARS = {
    Character.Breadbot: {
        "username": "Breadbot",
        "avatar_url": "https://media.discordapp.net/attachments/1417936473570676867/1426339328107479141/BreadbotAvatar.png?ex=68eadd83&is=68e98c03&hm=afcf15bfe9dbdaa41bc60f3bdd7ca725858be761c1d623afa42ff4bb92f44a6a&=&format=webp&quality=lossless"
    },
    Character.Morgana: {
        "username": "Morgana",
        "avatar_url": "https://media.discordapp.net/attachments/1331163030364360828/1433182714252759173/Morgana.png?ex=6903c2ea&is=6902716a&hm=8c333ba6fb9fb726aded3aa277ca7016e0d4445a5ed0963b945681bbebaf36da&=&format=webp&quality=lossless"
    },
    Character.DrChair: {
        "username": "Dr. Chair",
        "avatar_url": "https://media.discordapp.net/attachments/1331163030364360828/1435602348620644413/image.png?ex=690c9060&is=690b3ee0&hm=242c37a44701ae28734e2dff5c3a1b6b3944b30a2d811793ba60bddf1d7bc39d&=&format=webp&quality=lossless"
    },
    Character.Zara:{
        "username": "Zara",
        "avatar_url": "https://media.discordapp.net/attachments/1331163030364360828/1435686436689940541/image.png?ex=690cdeb0&is=690b8d30&hm=0a868c243eaa41c51a8edf29c418c52802ded3880aa8b0ca3cff34c03ee361aa&=&format=webp&quality=lossless"
    }
    # Add more characters as needed
}

def customizeWebhook(webhook, character_enum):
    # Set the username and avatar_url for the webhook based on the character
    info = CHARACTER_AVATARS.get(character_enum)
    if info:
        webhook.set_username(info["username"])
        webhook.set_avatar_url(info["avatar_url"])
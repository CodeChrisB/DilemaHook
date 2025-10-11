import requests
from typing import List, Dict, Any

class DiscordWebhook:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self._username: str = None
        self._avatar_url: str = None
        self._allowed_mentions: Dict[str, Any] = None

    # --------------------------
    # Fluent configuration
    # --------------------------
    def set_username(self, username: str):
        self._username = username
        return self

    def set_avatar_url(self, avatar_url: str):
        self._avatar_url = avatar_url
        return self

    def set_allowed_mentions(self, allowed_mentions: Dict[str, Any]):
        self._allowed_mentions = allowed_mentions
        return self

    # --------------------------
    # Sending messages
    # --------------------------
    def send(self, content: str = None, embeds: List[Dict[str, Any]] = None,
             tts: bool = False, files: List[str] = None,
             username: str = None, avatar_url: str = None,
             allowed_mentions: Dict[str, Any] = None,
             components: List[Dict[str, Any]] = None):

        payload = {}
        if content:
            payload["content"] = content
        if embeds:
            payload["embeds"] = embeds
        if tts:
            payload["tts"] = True
        payload["username"] = username or self._username
        payload["avatar_url"] = avatar_url or self._avatar_url
        payload["allowed_mentions"] = allowed_mentions or self._allowed_mentions
        if components:
            payload["components"] = components

        if files:
            multipart_files = [("file", open(f, "rb")) for f in files]
            response = requests.post(self.webhook_url, data={"payload_json": str(payload)}, files=multipart_files)
            for _, f in multipart_files:
                f.close()
        else:
            response = requests.post(self.webhook_url, json=payload)
        return response

    # --------------------------
    # Embed Builder
    # --------------------------
    class EmbedBuilder:
        def __init__(self):
            self.embed: Dict[str, Any] = {}
            self._buttons: List[Dict[str, Any]] = []

        # Fluent embed setters
        def setTitle(self, title: str):
            self.embed["title"] = title
            return self

        def setDescription(self, description: str):
            self.embed["description"] = description
            return self

        def setColor(self, color: int):
            self.embed["color"] = color
            return self

        def setThumbnail(self, url: str):
            self.embed["thumbnail"] = {"url": url}
            return self

        def setImage(self, url: str):
            self.embed["image"] = {"url": url}
            return self

        def setFooter(self, text: str, icon_url: str = None):
            footer = {"text": text}
            if icon_url:
                footer["icon_url"] = icon_url
            self.embed["footer"] = footer
            return self

        def setAuthor(self, name: str, url: str = None, icon_url: str = None):
            author = {"name": name}
            if url:
                author["url"] = url
            if icon_url:
                author["icon_url"] = icon_url
            self.embed["author"] = author
            return self

        def addField(self, name: str, value: str, inline: bool = False):
            if "fields" not in self.embed:
                self.embed["fields"] = []
            self.embed["fields"].append({"name": name, "value": value, "inline": inline})
            return self

        # --------------------------
        # Button support
        # --------------------------
        def addButton(self, label: str, url: str):
            if len(self._buttons) >= 5:
                raise ValueError("A single ActionRow can have max 5 buttons. You can add multiple rows manually if needed.")
            self._buttons.append({
                "type": 2,   # Button
                "style": 5,  # Link button
                "label": label,
                "url": url
            })
            return self

        # Build embed dict
        def build(self) -> Dict[str, Any]:
            return self.embed

        # Build components array (top-level for webhook)
        def buildComponents(self) -> List[Dict[str, Any]]:
            if not self._buttons:
                return None
            return [{"type": 1, "components": self._buttons}]

    # --------------------------
    # Embed helpers
    # --------------------------
    def createEmbed(self) -> 'DiscordWebhook.EmbedBuilder':
        return self.EmbedBuilder()

    def sendEmbed(self, embed: 'DiscordWebhook.EmbedBuilder', content: str = None):
        return self.send(
            content=content,
            embeds=[embed.build()],
            components=embed.buildComponents()
        )

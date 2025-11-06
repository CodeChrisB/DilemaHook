import requests
import json
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

        # --- handle file uploads ---
        if files:
            multipart_files = []
            try:
                for path in files:
                    multipart_files.append(("file", (path.split("/")[-1], open(path, "rb"))))
                response = requests.post(
                    self.webhook_url,
                    data={"payload_json": json.dumps(payload)},
                    files=multipart_files
                )
            finally:
                for _, f in multipart_files:
                    f[1].close()
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

        def addButton(self, label: str, url: str):
            if len(self._buttons) >= 5:
                raise ValueError("A single ActionRow can have max 5 buttons.")
            self._buttons.append({
                "type": 2,
                "style": 5,
                "label": label,
                "url": url
            })
            return self

        def build(self) -> Dict[str, Any]:
            return self.embed

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

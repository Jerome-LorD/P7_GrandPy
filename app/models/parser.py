import re
import json

from config import Config
from app.models.utils import hello


class Parser:
    """Parser class."""

    def __init__(self):
        """Init."""

        self.selected_words = []
        self.quotePattern = r"l'|d'|j'|qu'|m'|n'|qu'|t'"

    def stopWords(self):
        """Load a french word list from file."""
        with open(Config.JSON_DIR / "fr.json", encoding="utf-8") as f:
            return json.load(f)

    def isolate_keywords(self, sanitized_text):
        self.quotePattern = r"l'|d'|m'|n'|qu'|s'|t'|\,"
        onlyWords = re.sub(self.quotePattern, "", sanitized_text)
        return onlyWords

    def sanitize_text(self, text):
        """emove str in stop_word list."""
        self.selected_words = []

        for word in text.split():
            if word in self.stopWords():
                pass
            else:
                self.selected_words.append(word)
        return " ".join(self.selected_words)

    def isolated_target(self, text):
        """apture and isolate the targeted place."""
        targeted = []
        for word in text.split():
            if word[0].isupper():
                targeted.append(word)
        return " ".join(word for word in targeted if word not in hello.keys())

    def greetings(self, text):
        """Return the same greetings as those sent."""
        self.hello = hello
        for word in text.split():
            if word in self.hello.keys():
                return self.hello[word]

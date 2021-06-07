import re
import json

from config import Config
from app.models.utils import hello


class Parser:
    """Parser class."""

    def __init__(self):
        """Init."""

        self.selected_words = []
        self.quotePattern = r"l'|d'|m'|n'|qu'|s'|t'|\,|\?|\.|\!"

    def stop_words(self):
        """Load a french word list from file."""
        with open(Config.JSON_DIR / "fr.json", encoding="utf-8") as f:
            return json.load(f)

    def remove_defined_articles(self, text):
        """Remove french defined articles with apostrophe."""
        cleaned_text = re.sub(self.quotePattern, "", text)
        return cleaned_text.strip()

    def replace_malicious_text(self, text):
        """Relace malicious text."""
        refusedChars = r"[\<\>]{1,}|[$|*|£|¤|#|~|&|`|^|\"]{2,}|(.)\1{4,}|\
        \W*(alert)\W*|\W*(script)\W*"
        goodText = "montmartre"
        return goodText if re.search(refusedChars, text) else text

    def sanitize_text(self, text):
        """Remove str in stop_word list."""
        lowerTxt = text.lower()
        return " ".join(
            [word for word in lowerTxt.split() if word not in self.stop_words()]
        )

    def isolate_target(self, text):
        for word in text.split():
            if word in hello.keys():
                target = text.replace(word, "")
                return target.strip()
        return text

    def greetings(self, text):
        """Return the same greetings as those sent."""
        greets = [hello[word] for word in text.split() if word in hello.keys()]
        return "".join(greets) if len(greets) > 0 else "Des infos :"

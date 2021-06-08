import re
import json

from config import Config
from app.models.utils import hello


class Parser:
    """Parser class."""

    def __init__(self):
        """Init."""

        self.selected_words = []
        self.quote_pattern = r"l'|d'|m'|n'|qu'|s'|t'|\,|\?|\.|\!"

    def stop_words(self):
        """Load a french word list from file."""
        with open(Config.JSON_DIR / "fr.json", encoding="utf-8") as f:
            return json.load(f)

    def remove_defined_articles(self, text: str) -> str:
        """Remove french defined articles with apostrophe."""
        cleaned_text = re.sub(self.quote_pattern, "", text)
        return cleaned_text.strip()

    def replace_unwanted_chars(self, text: str) -> str:
        """Replace unwanted chars."""
        not_chars = r"[\<\>]{1,}|[$|*|£|¤|#|~|&|`|^|\"]{1,}|(.)\1{4,}|\d{1,}|\W*(alert)\W*|\W*(script)\W*"
        replacement_text = "montmartre"
        return replacement_text if re.search(not_chars, text) else text

    def sanitize_text(self, text: str) -> str:
        """Remove str in stop_word list."""
        low_txt = text.lower()
        return " ".join(
            [word for word in low_txt.split() if word not in self.stop_words()]
        )

    def isolate_target(self, text: str) -> str:
        """Isolate targeted words."""
        for word in text.split():
            if word in hello.keys():
                target = text.replace(word, "")
                print(target.strip())
                return target.strip()
        print(text)
        return text

    def greetings(self, text: str) -> str:
        """Return the same greetings as those sent."""
        greets = [hello[word] for word in text.split() if word in hello.keys()]
        return "".join(greets) if len(greets) > 0 else "Des infos :"

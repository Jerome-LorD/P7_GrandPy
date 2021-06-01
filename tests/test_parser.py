import re
import json

from config import Config
from app.models.utils import hello


class TestParser:
    """
    Test if Text Parser return sanitized string.
    """

    def stopWords(self):
        """Load a french word list from file."""
        with open(Config.JSON_DIR / "fr.json", encoding="utf-8") as f:
            return json.load(f)

    def isolate_keywords(self, sanitized_text):
        self.quotePattern = r"l'|d'|m'|n'|qu'|s'|t'|\,"
        onlyWords = re.sub(self.quotePattern, "", sanitized_text)
        return onlyWords

    def sanitize_text(self, text):
        """
        Remove str in stop_word list
        """
        self.selected_words = []

        for word in text.split():
            if word in self.stopWords():
                pass
            else:
                self.selected_words.append(word)
        return " ".join(self.selected_words)

    def isolated_target(self, text):
        """
        Capture and isolate the targeted place.
        """
        targeted = []
        for word in text.split():
            if word[0].isupper():
                targeted.append(word)
        return " ".join(word for word in targeted if word not in hello.keys())

    def greetings(self, text):
        """
        Return the same greetings as those sent.
        """
        self.hello = hello
        for word in text.split():
            if word in self.hello.keys():
                return self.hello[word]


question1 = "Salut GrandPy, quelle est l'adresse de la Tour Eiffel s'il te plait ?"


def test_sanitize_text():
    """
    Return sanitized string without the words in the stopWords list.
    """
    isolated_kw = TestParser().isolate_keywords(question1)
    result = TestParser().sanitize_text(isolated_kw)
    print(result)
    assert result == "Salut adresse Tour Eiffel plait ?"


def test_isolate_keywords():
    """
    Remove prefixed french quotes to keep only words.
    """
    isolated_text = TestParser().isolate_keywords(question1)
    result = TestParser().sanitize_text(isolated_text)
    print(result)
    assert result == "Salut adresse Tour Eiffel plait ?"


def test_isolated_target():
    isolated_kw = TestParser().isolate_keywords(question1)
    sanitized_txt = TestParser().sanitize_text(isolated_kw)
    result = TestParser().isolated_target(sanitized_txt)
    print(result)
    assert result == "Tour Eiffel"


def test_is_hello_in_sentence():
    """
    Use the same greetings in return.
    """
    isolated_kw = TestParser().isolate_keywords(question1)
    sanitized_txt = TestParser().sanitize_text(isolated_kw)
    result = TestParser().greetings(sanitized_txt)
    print(result)
    assert result == "Salut toi, j'ai l'adresse que tu cherches : "

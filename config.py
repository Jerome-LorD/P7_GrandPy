"""Config Module."""
import os

from pathlib import Path
from dotenv import load_dotenv, find_dotenv  # type: ignore

load_dotenv(find_dotenv())


class Config:
    """Config class."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "no way"
    GOOGLE_KEY = os.getenv("APIKEY")
    PLACES_KEY = os.getenv("PLACEAPIKEY")
    GOOGLE_SIGN = os.getenv("SIGNATURE")

    BASE_DIR = Path(".")
    APP_DIR = BASE_DIR / "app"
    JSON_DIR = BASE_DIR / APP_DIR / "json"

    MSG_NO_TEXT_FOUND = (
        "Désolé, je peux te montrer la carte mais je n'aurais pas plus d'info :/"
    )
    MSG_DONT_UNSERSTAND = "Je n'ai pas compris ! Quel lieu veux-tu découvrir ?"
    MSG_NO_GREETINGS = "Des infos : "

    TITLE_HTML = "GrandPy, le papy-robot"

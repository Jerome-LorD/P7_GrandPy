import os

from pathlib import Path
from dotenv import load_dotenv, find_dotenv  # type: ignore

load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "no way"
    GOOGLE_KEY = os.getenv("APIKEY")
    GOOGLE_SIGN = os.getenv("SIGNATURE")

    BASE_DIR = Path(".")
    APP_DIR = BASE_DIR / "app"
    JSON_DIR = BASE_DIR / APP_DIR / "json"

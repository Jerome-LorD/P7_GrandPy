#!/usr/bin/env python
"""Google API module."""
import requests

from config import Config


class GoogleAPI:
    """Class Google API."""

    def __init__(self):
        """Init."""
        self.url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        self.payload = {"key": Config.PLACES_API_KEY, "language": "fr"}

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

    def extract_data(self, keywords: str) -> dict:
        """Extract data."""
        try:
            self.payload["query"] = keywords
            req = requests.get(self.url, headers=self.headers, params=self.payload)
            data = req.json()
            if data["status"] == "OK":
                return {
                    "location": data["results"][0]["geometry"]["location"],
                    "address": data["results"][0]["formatted_address"],
                    "name": data["results"][0]["name"],
                }

        except requests.exceptions.RequestException as e:
            raise e

        except KeyError:
            return "Je n'ai pas compris."

"""Module Wiki api."""
import requests

from config import Config


class WikiAPI:
    """Wikipedia API."""

    def __init__(self):
        """Init."""
        self.url = "https://fr.wikipedia.org/w/api.php?"

        self.payload = {
            "action": "query",
            "format": "json",
            "prop": "coordinates|extracts",
            "generator": "geosearch",
            "utf8": 1,
            "exsentences": "5",
            "exlimit": "1",
            "explaintext": 1,
            "exsectionformat": "plain",
        }

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

    def extract_data(self, coords: dict) -> str:
        """Extract data from dict and return str."""
        try:
            if isinstance(coords, dict):
                lat = coords["location"]["lat"]
                lng = coords["location"]["lng"]

                self.payload["ggscoord"] = f"{lat}|{lng}"

                req = requests.get(self.url, headers=self.headers, params=self.payload)
                self.data = req.json()

                pageid = next(iter(self.data["query"]["pages"]))
                return self.data["query"]["pages"][pageid]["extract"]
            else:

                return Config.MSG_NO_TEXT_FOUND

        except requests.exceptions.RequestException as e:
            raise e

        except KeyError as e:
            print(e)

        except ValueError:
            return Config.MSG_NO_TEXT_FOUND

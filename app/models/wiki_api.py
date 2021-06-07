import requests

from config import Config


class WikiAPI:
    """Tests wiki."""

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
        }

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

    def extractData(self, coords) -> str:
        """Extract data."""
        try:
            lat = coords["location"]["lat"]
            lng = coords["location"]["lng"]
            self.payload["ggscoord"] = f"{lat}|{lng}"

            req = requests.get(self.url, headers=self.headers, params=self.payload)
            self.data = req.json()

            if len(self.data) > 1:
                pageid = next(iter(self.data["query"]["pages"]))
                self.extract = self.data["query"]["pages"][pageid]["extract"]
                return self.extract
            return Config.MSG_NO_TEXT_FOUND

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

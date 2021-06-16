#!/usr/bin/env python
"""Tests for GoogleAPI: extractData and requests.get."""
import requests

from app.models.google_api import GoogleAPI

googleApi = GoogleAPI()


class GoogleFakeResponse:
    """Google API fake response of requests get."""

    def json(self):
        """Fake json."""
        return {
            "results": [
                {
                    "formatted_address": "Some address",
                    "geometry": {
                        "location": {"lat": 12.345, "lng": 51.321},
                    },
                    "name": "Some name",
                }
            ],
            "status": "OK",
        }


def test_extract_data(monkeypatch):
    """Test extract_data monkeypatched."""

    def mock_requests_get(*args, **kwargs):
        """Mock request get returns Google fake response."""
        return GoogleFakeResponse()

    monkeypatch.setattr(requests, "get", mock_requests_get)

    result = googleApi.extract_data("cité du vatican")
    assert result == {
        "location": {"lat": 12.345, "lng": 51.321},
        "address": "Some address",
        "name": "Some name",
    }


class GoogleWrongFakeResponse:
    """Google places API wrong fake response class."""

    def json(self):
        """Fake json."""
        return {"html_attributions": [], "results": [], "status": "ZERO_RESULTS"}


def test_extract_data_wrong_key(monkeypatch):
    """Test the return from a wrong key."""

    def mock_requests_get(*args, **kwargs):
        """Mock request get returns Google wrong fake response."""
        return GoogleWrongFakeResponse()

    monkeypatch.setattr(requests, "get", mock_requests_get)

    result = googleApi.extract_data(
        {"location": {"lat": 36.1069258, "lng": -112.1129484}}
    )
    assert result is None


def test_integration_extract_data():
    """Integration real test -> extract_data."""
    result = googleApi.extract_data("chutes niagara")
    assert result == {
        "location": {"lat": 43.0828162, "lng": -79.07416289999999},
        "address": "Niagara Falls, NY 14303, États-Unis",
        "name": "Niagara Falls",
    }

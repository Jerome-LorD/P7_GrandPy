#!/usr/bin/env python
"""Tests wiki API."""
import requests

from app.models.wiki_api import WikiAPI
from config import Config

wiki = WikiAPI()


class WikiFakeResponse:
    """Wiki API fake response of requests get."""

    def json(self):
        """Fake json."""
        return {"query": {"pages": {"12345": {"extract": "mock_response"}}}}


class WikiWrongFakeResponse:
    """Wiki API wrong fake response class."""

    def json(self):
        """Fake json."""
        return {"batchcomplete": ""}


def test_extract_data(monkeypatch):
    """Test extract_data monkeypatched."""

    def mock_requests_get(*args, **kwargs):
        """Mock request get returns Wiki fake response."""
        return WikiFakeResponse()

    monkeypatch.setattr(requests, "get", mock_requests_get)

    result = wiki.extract_data({"location": {"lat": 43.07945, "lng": -79.07472}})
    assert result == "mock_response"


def test_extract_data_wrong_key(monkeypatch):
    """Test the return from a wrong key."""

    def mock_requests_get(*args, **kwargs):
        """Mock request get returns Wiki wrong fake response."""
        return WikiWrongFakeResponse()

    monkeypatch.setattr(requests, "get", mock_requests_get)

    result = wiki.extract_data({"location": {"lat": 12.3456, "lng": -3.456789}})
    assert result == Config.MSG_NO_TEXT_FOUND


def test_integration_extract_data():
    """Integration test of extract data."""
    result = wiki.extract_data({"location": {"lat": 43.07945, "lng": -79.07472}})
    assert result.startswith("Les chutes du Niagara")

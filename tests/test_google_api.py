#!/usr/bin/env python
"""Tests for GoogleAPI: extractData and requests.get."""

from app.models.google_api import GoogleAPI

googleApi = GoogleAPI()


class FakeResponse:
    def json():
        return {"mock_key": "mock_response"}


def mock_extract_data():
    return {"mock_key": "mock_response"}


def mock_requests_get(url, *args, **kwargs):
    return FakeResponse()


def test_mock_extractData(monkeypatch):
    monkeypatch.setattr(
        "app.models.google_api.GoogleAPI.extract_data", mock_extract_data
    )
    result = mock_extract_data()
    assert result == {"mock_key": "mock_response"}


def test_mock_request_get(monkeypatch):
    monkeypatch.setattr("requests.get", mock_requests_get)
    mock_requests_get("http://fakewebsite.com")
    result = FakeResponse.json()
    assert result == {"mock_key": "mock_response"}


def test_extractData():
    result = googleApi.extract_data("chutes niagara")
    assert result == {
        "location": {"lat": 43.0828162, "lng": -79.07416289999999},
        "address": "Niagara Falls, NY 14303, United States",
        "name": "Niagara Falls",
    }

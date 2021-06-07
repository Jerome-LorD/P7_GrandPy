"""Tests for GoogleAPI: extractData and requests.get."""

from app.models.google_api import GoogleAPI

googleApi = GoogleAPI("chutes niagara")


class FakeResponse:
    def json():
        return {"mock_key": "mock_response"}


def mock_extractData():
    return {"mock_key": "mock_response"}


def mock_requests_get(url, *args, **kwargs):
    return FakeResponse()


def test_mock_extractData(monkeypatch):
    monkeypatch.setattr("app.models.google_api.GoogleAPI.extractData", mock_extractData)
    result = mock_extractData()
    assert result == {"mock_key": "mock_response"}


def test_mock_request_get(monkeypatch):
    monkeypatch.setattr("requests.get", mock_requests_get)
    mock_requests_get("http://fakewebsite.com")
    result = FakeResponse.json()
    assert result == {"mock_key": "mock_response"}


def test_extractData():
    result = googleApi.extractData()
    assert result == {
        "location": {"lat": 43.0828162, "lng": -79.07416289999999},
        "address": "Niagara Falls, NY 14303, United States",
    }

#!/usr/bin/env python
"""Tests wiki API."""


class MockResponse:
    def json(self):
        return {"mock_key": "mock_response"}


def mock_extract_data(coords):
    return {"mock_key": "mock_response"}


def test_mock_extract_data(monkeypatch):
    monkeypatch.setattr("app.models.wiki_api.WikiAPI.extract_data", mock_extract_data)
    result = mock_extract_data("73.45|2.65")
    assert result == {"mock_key": "mock_response"}

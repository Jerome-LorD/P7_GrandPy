#!/usr/bin/env python
"""Tests wiki API."""

from app.models.wiki_api import WikiAPI


wiki = WikiAPI()


class MockResponse:
    def json(self):
        return {"mock_key": "mock_response"}


def mock_extract_data(coords):
    return {"mock_key": "mock_response"}


def test_mock_extract_data(monkeypatch):
    monkeypatch.setattr("app.models.wiki_api.WikiAPI.extract_data", mock_extract_data)
    result = mock_extract_data("73.45|2.65")
    assert result == {"mock_key": "mock_response"}


def test_extractData():
    result = WikiAPI().extract_data({"location": {"lat": 43.07945, "lng": -79.07472}})
    assert (
        result
        == "Les chutes du Niagara ou chutes Niagara (toponyme officiel au Canada,), en anglais Niagara Falls, sont un ensemble de trois chutes d’eau situées sur la rivière Niagara qui relie le lac Érié au lac Ontario, dans l’est de l’Amérique du Nord, à la frontière entre le Canada et les États-Unis :\n\nles « chutes du Fer-à-Cheval » (Horseshoe Falls) ou « chutes canadiennes » ;\nles « chutes américaines » (American Falls) ;\nles « chutes du Voile de la Mariée » (Bridal Veil Falls).Bien qu’elles ne soient pas particulièrement hautes (57 m), les chutes du Niagara sont très larges. Avec un débit de plus de 2 800 m3/s, elles sont les chutes les plus puissantes d’Amérique du Nord et parmi les plus connues à travers le monde.\nRenommées pour leur beauté, les chutes du Niagara sont aussi une source immense d’énergie hydroélectrique et leur préservation est un défi écologique. Cette merveille naturelle, haut-lieu du tourisme depuis plus d’un siècle, est partagée par les villes jumelles de Niagara Falls (New York) aux États-Unis et Niagara Falls (Ontario) au Canada.\n\n\nFormation\n\nLes chutes du Niagara, ainsi que la rivière Niagara et les Grands Lacs nord-américains, sont apparues lors de la déglaciation qui a suivi la période glaciaire du Wisconsin, il y a environ 30 000 à 50 000 ans."
    )

#!/usr/bin/env python
"""Tests API requests."""
import requests

from app.models.wiki_api import WikiAPI


# wiki = WikiAPI("43.07945|-79.07472")
# print(wiki.extractData())
# def get(url, **kwargs):
#     return MockResponse()


# class MockResponse:
#     def json(self):
#         return {"extracts": {"text retour"}}


# def test_request_get():
#     requests.get = get

#     result = WikiAPI("43.07945|-79.07472").extractData()
#     assert result == "text retour"


# def test_extractData():
#     result = WikiAPI("43.07945|-79.07472").extractData()
#     assert (
#         result
#         == "Les chutes du Niagara ou chutes Niagara (toponyme officiel au Canada,), en anglais Niagara Falls, sont un ensemble de trois chutes d’eau situées sur la rivière Niagara qui relie le lac Érié au lac Ontario, dans l’est de l’Amérique du Nord, à la frontière entre le Canada et les États-Unis :\n\nles « chutes du Fer-à-Cheval » (Horseshoe Falls) ou « chutes canadiennes » ;\nles « chutes américaines » (American Falls) ;\nles « chutes du Voile de la Mariée » (Bridal Veil Falls).Bien qu’elles ne soient pas particulièrement hautes (57 m), les chutes du Niagara sont très larges."
#     )

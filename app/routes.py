#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask import request
from flask import render_template
from . import app

from .forms import ResearchForm

from .models.parser import Parser
from .models.google_api import GoogleAPI
from .models.wiki_api import WikiAPI


@app.route("/")
@app.route("/index")
def research():

    return render_template(
        "index.html",
        title="GrandPy, le papy-robot",
        apikey=app.config["GOOGLE_KEY"],
        apisign=app.config["GOOGLE_SIGN"],
    )


@app.route("/ajax", methods=["POST"])
def ajax():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        parser = Parser()
        question = parser.replace_malicious_text(data["question"])
        isolated_kw = parser.remove_defined_articles(question)
        sanitized_txt = parser.sanitize_text(isolated_kw)
        quest = parser.isolate_target(sanitized_txt)
        greetings = parser.greetings(sanitized_txt)

        place = GoogleAPI()
        coordinates = place.extract_data(quest)
        print(coordinates)
        wiki = WikiAPI()
        histo = wiki.extract_data(coordinates)

        return jsonify(answer=histo, coords=coordinates, greetings=greetings)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="GrandPy, le papy-robot"), 404


if __name__ == "__main__":
    app.run(debug=True)

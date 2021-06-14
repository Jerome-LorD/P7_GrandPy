#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Routes module."""


from config import Config
from flask import jsonify
from flask import request
from flask import render_template
from . import app

from .models.parser import Parser
from .models.google_api import GoogleAPI
from .models.wiki_api import WikiAPI


@app.route("/")
@app.route("/index")
def index():
    """Index home page."""
    return render_template(
        "index.html",
        title=Config.TITLE_HTML,
        apikey=app.config["GOOGLE_KEY"],
        apisign=app.config["GOOGLE_SIGN"],
    )


@app.route("/ajax", methods=["POST"])
def ajax():
    """Ajax post method."""
    if request.method == "POST":
        data = request.get_json()
        parser = Parser()
        question = parser.replace_unwanted_chars(data["question"])
        isolated_kw = parser.remove_defined_articles(question)
        sanitized_txt = parser.sanitize_text(isolated_kw)
        quest = parser.isolate_target(sanitized_txt)
        greetings = parser.greetings(sanitized_txt)
        sanitized_quest = parser.replace_insult_to_stars(question)

        place = GoogleAPI()
        coordinates = place.extract_data(quest)

        if isinstance(coordinates, dict):
            wiki = WikiAPI()
            histo = wiki.extract_data(coordinates)

            return jsonify(
                sanitized_quest=sanitized_quest,
                answer=histo,
                coords=coordinates,
                greetings=greetings,
            )
        else:
            return jsonify(
                sanitized_quest=sanitized_quest,
                quest_err=Config.MSG_DONT_UNSERSTAND,
            )


@app.errorhandler(404)
def page_not_found(error):
    """Error 404 page."""
    return render_template("404.html", title=Config.TITLE_HTML), 404


if __name__ == "__main__":
    app.run(debug=True)

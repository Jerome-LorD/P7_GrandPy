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
        apikey=app.config["JS_API_KEY"],
    )


@app.route("/ajax", methods=["POST"])
def ajax():
    """Ajax post method."""
    data = request.get_json()
    parser = Parser()
    datas = parser.execute_parsing(data["question"])

    place = GoogleAPI()
    coordinates = place.extract_data(datas["quest"])

    if coordinates:
        wiki = WikiAPI()
        histo = wiki.extract_data(coordinates)

        return jsonify(
            sanitized_quest=datas["sanitized_quest"],
            answer=histo,
            coords=coordinates,
            greetings=datas["greetings"],
        )
    return jsonify(
        sanitized_quest=datas["sanitized_quest"],
        quest_err=Config.MSG_DONT_UNSERSTAND,
    )


@app.errorhandler(404)
def page_not_found(error):
    """Error 404 page."""
    return render_template("404.html", title=Config.TITLE_HTML), 404

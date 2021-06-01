# -*- coding: utf-8 -*-

import os
import re


from flask import jsonify
from flask import request
from flask import render_template
from . import app

from .forms import ResearchForm

from .models.parser import Parser


@app.route("/")
@app.route("/index", methods=["POST", "GET"])
def research():

    refusedChars = (
        r"[\<\>]{1,}|[$|*|£|¤|#|~|&|`|^|\"|\']{2,}|\W*(alert)\W*|\W*(script)\W*"
    )
    form = ResearchForm()

    if request.method == "POST":

        question = request.values.get("search", default=0, type=str)
        filtered_quest = re.search(refusedChars, question)
        if filtered_quest:
            questionF = "Bonjour GrandPy, quel jour sommes-nous ?"
        else:
            isolated_kw = Parser().isolate_keywords(question)
            sanitized_txt = Parser().sanitize_text(isolated_kw)
            questionF = Parser().isolated_target(sanitized_txt)

        form.search.data = ""
        return render_template(
            "index.html",
            title="GrandPy, le papy-robot",
            form=form,
            apikey=app.config["GOOGLE_KEY"],
            apiSign=app.config["GOOGLE_SIGN"],
            quest=questionF,
        )
    else:
        return render_template(
            "index.html",
            title="GrandPy, le papy-robot",
            form=form,
            apikey=app.config["GOOGLE_KEY"],
            apiSign=app.config["GOOGLE_SIGN"],
        )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="GrandPy, le papy-robot"), 404


if __name__ == "__main__":
    app.run(debug=True)

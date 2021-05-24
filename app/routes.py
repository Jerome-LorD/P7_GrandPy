from flask import render_template
from app import app
from app.forms import ResearchForm


@app.route("/")
@app.route("/index")
def research():
    form = ResearchForm()
    return render_template("index.html", title="GrandPy, le papy-robot", form=form)

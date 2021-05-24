from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class ResearchForm(FlaskForm):
    txt_area = TextAreaField(
        "TextArea", render_kw={"placeholder": "posez-moi votre question"}
    )
    submit = SubmitField("Rechercher")

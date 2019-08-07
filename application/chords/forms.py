from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ChordForm(FlaskForm):
    key = StringField("Key")
    name = StringField("Name")
    notes = StringField("Notes")

    class Meta:
        csrf = False

from flask_wtf import FlaskForm
from wtforms import StringField, validators


class SongForm(FlaskForm):

    name = StringField("Name", [validators.InputRequired()])
    artist = StringField("Artist", [validators.InputRequired()])

    class Meta:
        csrf = False

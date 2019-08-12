from flask_wtf import FlaskForm
from wtforms import StringField, validators


class SongForm(FlaskForm):

    name = StringField("Name", validators=[validators.required()])
    artist = StringField("Artist", validators=[validators.required()])

    class Meta:
        csrf = False


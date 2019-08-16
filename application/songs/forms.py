from flask_wtf import FlaskForm
from wtforms import StringField, validators


class SongForm(FlaskForm):

    name = StringField("Name", validators=[validators.InputRequired()])
    artist = StringField("Artist", validators=[validators.InputRequired()])

    class Meta:
        csrf = False

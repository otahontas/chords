from flask_wtf import FlaskForm
from wtforms import SelectMultipleField,StringField, validators
from application.chords.models import Chord


class SongForm(FlaskForm):

    name = StringField("Name", [validators.InputRequired()])
    artist = StringField("Artist", [validators.InputRequired()])

    class Meta:
        csrf = False


class SongEditForm(FlaskForm):
    """Form for editing songs, catches selection from Songs table. 
    Use basic query instead of QuerySelectField so we can format options 
    before showing them."""
    chords_in_database = Chord.query.with_entities(Chord.id, Chord.key, 
                                                   Chord.name)
    chords_in_database = [(x.id, "{} {}".format(x.key.title(), x.name))
                          for x in chords_in_database]

    new_name = StringField("Name", [validators.InputRequired()])
    new_artist = StringField("Artist", [validators.InputRequired()])
    chords = SelectMultipleField("Chords", choices=chords_in_database,
                                 coerce=int)

    class Meta:
        csrf = False

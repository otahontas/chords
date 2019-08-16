from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, ValidationError, validators
from application.notes.models import Note


def my_length_check(form, field):
    if len(field.data) != 2:
        raise ValidationError('Please select two notes')


class ChordForm(FlaskForm):
    """Form for new chord creation, catches selection from Notes table"""
    notes_in_database = Note.query.with_entities(Note.name)
    notes_in_database = [(x.name, x.name.title()) for x in notes_in_database]
    names = [('major', 'Major'), ('minor', 'Minor')]

    key = SelectField("Key", choices=notes_in_database)
    name = SelectField("Name", choices=names)
    notes = SelectMultipleField("Notes", choices=notes_in_database,
                                coerce=str, validators=[my_length_check])

    class Meta:
        csrf = False

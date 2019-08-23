from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, ValidationError
from application.notes.models import Note


def check_notes_length(form, field):
    """Validator for notes field"""
    if len(field.data) != 2:
        raise ValidationError('Please select two notes')


class ChordForm(FlaskForm):
    """Form for new chord creation, catches selection from Notes table. 
    Use basic query instead of QuerySelectField so we can format options 
    before showing them."""
    notes_in_database = Note.query.with_entities(Note.id, Note.name)
    notes_for_fields = [(x.id, x.name.title()) for x in notes_in_database]
    names = [('major', 'Major'), ('minor', 'Minor')]

    key = SelectField("Key", coerce=int, choices=notes_for_fields)
    name = SelectField("Name", choices=names)
    notes = SelectMultipleField("Notes", choices=notes_for_fields,
                                coerce=int, validators=[check_notes_length])

    class Meta:
        csrf = False

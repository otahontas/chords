from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators


class ChordForm(FlaskForm):
    # use notes from noteslist
    all_notes = []
    with open("application/notes/notesfordatabase.txt") as f:
        for line in f:
            all_notes.append((line, line))
    names = [('major', 'Major'), ('minor', 'Minor')]

    key = SelectField("Key", choices=all_notes)
    name = SelectField("Name", choices=names)
    notes = StringField("Notes", [validators.InputRequired(message="Field cannot be empty!")])

    class Meta:
        csrf = False

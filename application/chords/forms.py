from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, StringField, validators


class ChordForm(FlaskForm):
    # TODO: käytä tähän samaa moduulia kuin muualla näiden nuottien syöttämiseksi
    all_notes = []
    with open("application/notes/notesfordatabase.txt") as f:
        for line in f:
            all_notes.append((line, line.title()))
    names = [('major', 'Major'), ('minor', 'Minor')]

    key = SelectField("Key", choices=all_notes)
    name = SelectField("Name", choices=names)
    notes = SelectMultipleField("Notes", choices=all_notes)

    class Meta:
        csrf = False

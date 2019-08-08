from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.chords.models import Chord
from application.notes.models import Note
from application.chordnote.models import ChordNote
from application.chords.forms import ChordForm
from application.auth.models import User


@app.route("/chords", methods=["GET"])
def chords_index():
    users_in_database = User.query.with_entities(User.id, User.name)
    users_in_database = {x.id: x.name for x in users_in_database}

    return render_template("chords/list.html",
            chords=Chord.query.all(), users=users_in_database)


@app.route("/chords/<chord_id>/", methods=["GET"])
def chord_show_notes(chord_id):
    chord_to_show_id = Chord.query.get(chord_id).id
    notes_to_show = (db.session.query(Note)
        .join(ChordNote)
        .join(Chord)
        .filter(Note.id == ChordNote.note_id)
        .filter(Chord.id == ChordNote.chord_id)
        .filter(Chord.id == chord_id)
        .order_by(ChordNote.rank)
        .all())
    for note in notes_to_show:
        print(note.name)

    return render_template("chords/list.html",
            chords=Chord.query.all(),
            selected_chord_id = chord_to_show_id,
            selected_chord_notes = notes_to_show)


@app.route("/chords/new/")
@login_required
def chords_form():
    return render_template("chords/new.html", form=ChordForm())


@app.route("/chords/", methods=["POST"])
@login_required
def chords_create():
    # get form and check forward back to form if input is not validated
    # TODO: add validation
    form = ChordForm(request.form)

    # Add chord to database so we can get it's id
    new_chord = Chord(form.key.data, form.name.data)
    new_chord.account_id = current_user.id
    db.session().add(new_chord)
    db.session().commit()

    # get notes from database and turn returned list into dictionary
    # TODO: Pitäiskö tää siirtää omaan moduuliin, jotta hyödynnettävissä myös muualla?
    notes_in_database = Note.query.with_entities(Note.id, Note.name)
    notes_in_database = {x.name: x.id for x in notes_in_database}
    notes_from_user = request.form.get("notes").replace(" ", "").split(",")

    # link notes user has given to chord
    for i, note in enumerate(notes_from_user):
        new_note = ChordNote(i)
        new_note.chord_id = new_chord.id
        new_note.note_id = notes_in_database[note]
        db.session().add(new_note)
    db.session().commit()

    return redirect(url_for("chords_index"))

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.chords.models import Chord
from application.linktables.models import ChordNote
from application.notes.models import Note
from application.chords.forms import ChordForm

@app.route("/chords", methods=["GET"])
def chords_index():
    """View controller for showing all chords"""

    users_in_database = User.query.with_entities(User.id, User.username)
    users_in_database = {x.id: x.username for x in users_in_database}

    return render_template("chords/list.html",
            chords=Chord.query.all(), users=users_in_database)


@app.route("/chords/<chord_id>/", methods=["GET"])
def chord_show_notes(chord_id):
    """View controller for showing notes for individual chord"""
    chord_to_show_id = Chord.query.get(chord_id).id
    # TODO: refactor this so we don't have to get user list every time notes 
    # are shown for one chord, it'll eventually become slow
    users_in_database = User.query.with_entities(User.id, User.username)
    users_in_database = {x.id: x.username for x in users_in_database}
    notes_to_show = (db.session.query(Note)
        .join(ChordNote)
        .join(Chord)
        .filter(Note.id == ChordNote.note_id)
        .filter(Chord.id == ChordNote.chord_id)
        .filter(Chord.id == chord_id)
        .order_by(ChordNote.rank)
        .all())

    return render_template("chords/list.html",
            chords=Chord.query.all(),
            users=users_in_database,
            selected_chord_id = chord_to_show_id,
            selected_chord_notes = notes_to_show)


@app.route("/chords/new/")
@login_required
def chords_form():
    """View controller for adding new chord -functionality"""
    return render_template("chords/new.html", form=ChordForm())


@app.route("/chords/", methods=["POST"])
@login_required
def chords_create():
    """Method gets user input from form, adds new chord to db, catches its id
    and links chord to notes (base + others) user has given"""
    form = ChordForm(request.form)

    new_chord = Chord(form.key.data, form.name.data)
    new_chord.account_id = current_user.id
    db.session().add(new_chord)
    db.session().commit()

    # TODO: Refactor, this should be moved to different module so we can reuse it later
    notes_in_database = Note.query.with_entities(Note.id, Note.name)
    notes_in_database = {x.name: x.id for x in notes_in_database}
    notes_from_user = [new_chord.key].extend(form.notes.data)
    notes_from_user = [x.rstrip() for x in notes_from_user]

    for i, note in enumerate(notes_from_user):
        new_note = ChordNote(i)
        new_note.chord_id = new_chord.id
        new_note.note_id = notes_in_database[note]
        db.session().add(new_note)
    db.session().commit()

    return redirect(url_for("chords_index"))

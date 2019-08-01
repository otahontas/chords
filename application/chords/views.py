from application import app, db
from flask import redirect, render_template, request, url_for
from application.chords.models import Chord
from application.notes.models import Note
from application.chordnote.models import ChordNote

@app.route("/chords/", methods=["GET"])
def chords_index():
    return render_template("chords/list.html", chords=Chord.query.all())


@app.route("/chords/new/")
def chords_form():
    return render_template("chords/new.html")


@app.route("/chords/", methods=["POST"])
def chords_create():
    # Add chord to database so we can get it's id
    c = Chord(request.form.get("key"), request.form.get("name"))
    db.session().add(c)
    db.session().commit()

    # get notes from database and turn returned list into dictionary
    notes_in_database = Note.query.with_entities(Note.id, Note.name)
    notes_in_database = {x.name: x.id for x in notes_in_database}
    notes_from_user = request.form.get("notes").replace(" ","").split(",")

    # link notes user has given to chord
    for i,note in enumerate(notes_from_user):
        cn = ChordNote(i)
        cn.chord_id = c.id
        cn.note_id = notes_in_database[note]
        db.session().add(cn)
    db.session().commit()

    return redirect(url_for("chords_index"))

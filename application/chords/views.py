from application import app, db
from flask import redirect, render_template, request, url_for
from application.chords.models import Chord


@app.route("/chords/", methods=["GET"])
def chords_index():
    return render_template("chords/list.html", chords=Chord.query.all())


@app.route("/chords/new/")
def chords_form():
    return render_template("chords/new.html")


@app.route("/chords/<chord_id>/", methods=["POST"])
def chords_set_as_favourite(chord_id):
    c = Chord.query.get(chord_id)

    c.favourite = True
    db.session().commit()

    return redirect(url_for("chords_index"))


@app.route("/chords/", methods=["POST"])
def chords_create():
    c = Chord(request.form.get("name"))

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("chords_index"))

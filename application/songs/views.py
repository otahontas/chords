from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.songs.models import Song
from application.songs.forms import SongForm


@app.route("/songs", methods=["GET"])
def songs_index():
    """View controller for showing all songs"""
    users_in_database = User.query.with_entities(User.id, User.username)
    users_in_database = {x.id: x.username for x in users_in_database}
    return render_template("songs/list.html",
                           songs=Song.query.all(),
                           users=users_in_database)


@app.route("/songs/new")
@login_required
def songs_form():
    """View controller for adding new song"""
    return render_template("songs/new.html", form=SongForm())


@app.route("/songs", methods=["POST"])
@login_required
def songs_create():
    """Method gets user input from form and adds new song to db"""
    form = SongForm(request.form)

    if not form.validate():
        return render_template("songs/new.html", form=form)

    song_already_added = Song.query.filter_by(name=form.name.data,
                                              artist=form.artist.data).first()

    if song_already_added:
        form.name.errors.append("Song is already in database")
        return render_template("songs/new.html", form=form)

    new_song = Song(form.name.data, form.artist.data)
    new_song.account_id = current_user.id
    db.session().add(new_song)
    db.session().commit()

    return redirect(url_for("songs_index"))

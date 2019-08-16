from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.songs.models import Song
from application.songs.forms import SongForm


@app.route("/songs", methods=["GET"])
def songs_index():
    """View controller for showing all songs"""
    users_in_database = User.query.with_entities(User.id, User.name)
    users_in_database = {x.id: x.name for x in users_in_database}

    return render_template("songs/list.html",
            chords=Song.query.all(), users=users_in_database)

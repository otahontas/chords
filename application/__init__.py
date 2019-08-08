from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("    DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chords.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.chords import models
from application.chords import views

from application.notes import models
from application.notes.models import Note

try:
    db.create_all()
except:
    pass

# If there's no items in local notes database, initialize database
if not os.environ.get("HEROKU") and not Note.query.all():
    with open("application/notes/notesfordatabase.txt") as f:
        for line in f:
            n = Note(line.rstrip())
            db.session().add(n)
        db.session().commit()
        if Note.query.count() == 21:
            print("SUCCESS: Notes-table successfully initialized")
        else:
            print("ERROR: There was an error when initializing notes-table")

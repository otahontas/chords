# Flask
from flask import Flask
app = Flask(__name__)


# Database
from flask_sqlalchemy import SQLAlchemy
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chords.db"
    app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


# Load app features from different modules
from application import views

from application.chords import models
from application.chords import views

from application.auth import models
from application.auth import views


# Login functionality
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Create tables if needed

try:
    db.create_all()
    # TODO: siirrä omaan moduuliinsa?
    # Initialize notes table if not available
    from application.notes import models
    from application.notes.models import Note
    if not Note.query.all():
        with open("application/notes/notesfordatabase.txt") as f:
            for line in f:
                n = Note(line.rstrip())
                db.session().add(n)
            db.session().commit()
            if Note.query.count() == 21:
                print("SUCCESS: Notes-table successfully initialized")
            else:
                print("ERROR: There was an error when initializing notes-table")
except:
    pass

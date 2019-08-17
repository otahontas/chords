from application import db
from application.models import Base, Dates

class Song(Base, Dates):

    name = db.Column(db.String(144), nullable=False)
    artist = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    song_chords = db.relationship("SongChord", backref='song', lazy=True)
    favourite_songs = db.relationship("UserFavouriteSong", backref='song', lazy=True)

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

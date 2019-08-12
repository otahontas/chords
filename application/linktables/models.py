from application import db
from application.models import Base


class ChordNote(Base):

    chord_id = db.Column(db.Integer, db.ForeignKey('chord.id'), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def __init__(self,rank):
        self.rank = rank

class SongChord(Base):

    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('chord.id'), nullable=False)

    def __init__(self):
        pass

class UserFavouriteSong(Base):

    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self):
        pass

from application import db
from application.models import Base


class SongChord(Base):

    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('chord.id'), nullable=False)

    def __init__(self):
        pass

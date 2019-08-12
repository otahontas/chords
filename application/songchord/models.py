from application import db

class SongChord(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('chord.id'), nullable=False)

    def __init__(self):
        pass

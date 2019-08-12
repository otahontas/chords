from application import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    chord_notes = db.relationship("ChordNote", backref='note', lazy=True)

    def __init__(self,name):
        self.name = name

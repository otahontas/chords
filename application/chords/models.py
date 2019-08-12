from application import db
from application.models import Base


class Chord(Base):

    key = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    chord_notes = db.relationship("ChordNote", backref='chord', lazy=True)

    def __init__(self, key, name):
        self.key = key
        self.name = name

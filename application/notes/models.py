from application import db
from application.models import Base

class Note(Base):

    name = db.Column(db.String(144), nullable=False)

    chord_notes = db.relationship("ChordNote", backref='note', lazy=True)

    def __init__(self,name):
        self.name = name

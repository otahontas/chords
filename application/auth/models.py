from application import db
from application.models import Base


class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    chords = db.relationship("Chord", backref='account', lazy=True)
    songs = db.relationship("Song", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.roles = 1

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

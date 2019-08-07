from application import db


class Chord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate = db.func.current_timestamp())

    key = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, key, name):
        self.key = key
        self.name = name

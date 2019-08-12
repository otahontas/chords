from application import db


class Role(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100), nullable=False)

    users = db.relationship("User", backref='role', lazy=True)

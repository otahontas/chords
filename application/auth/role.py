from application import db
from application.models import Base


class Role(Base):
    name = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100), nullable=False)

    users = db.relationship("User", backref='role')

from .database import db, fs_mixin


class Book(db.Model, fs_mixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    writer = db.Column(db.String(255))
    ...



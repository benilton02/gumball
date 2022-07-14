from flask_serialize import FlaskSerialize
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
fs_mixin = FlaskSerialize(db)

def configure(app):
    db.init_app(app)
    app.db = db
    with app.app_context():
        db.create_all()
    ...
from flask import Flask
from flask_migrate import Migrate
from .views import configure as config_bp
from .database import configure as config_db

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///setup.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config_db(app)

    Migrate(app, app.db)

    config_bp(app)

    return app
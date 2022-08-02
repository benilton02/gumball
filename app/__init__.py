from flask import Flask
from flask_migrate import Migrate
from app.views import configure as config_bp
from app.config_database import config_db


def create_app(sqlite):
    app = Flask(__name__)    
    app.config['SQLALCHEMY_DATABASE_URI'] = sqlite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config_db(app)
    config_bp(app)
    
    
    Migrate(app, app.db)
    return app

from flask import Blueprint, jsonify, request
from app.models import Character
from app.config_database import db
import json

bp_app = Blueprint('endpoint', __name__)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/', methods=['POST'])
def save():
    payload = request.data
    payload = json.loads(payload.decode('utf-8'))
    name = payload.get('name')
    
        
    try: 
        character = Character(name=name)
        db.session.add(character)
        db.session.commit()
        
        data = {
            "id": character.id,
            "name": character.name,
        }
        status=201
    
    except:
        data = dict()
        status = 400
    
    finally:
        return jsonify(data), status
    
    ...


@bp_app.route('/update', methods=['POST'])
def update():
    ...


@bp_app.route('/create', methods=['POST'])
def create():
    ...


@bp_app.route('/delete', methods=['POST'])
def delete():
    ...

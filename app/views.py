from flask import Blueprint, jsonify, request
from app.models import Character
from app.config_database import db
import json

bp_app = Blueprint('gumball', __name__)

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
    

@bp_app.route('/', methods=['GET'])
def select():
     
    try:
        queryset = Character.query.all()
    
        data = [
            {
                "id": query.id,
                "name": query.name,
            }

            for query in queryset
        ]

        if data:
            status = 200
        
        else:
            status = 202
            data = {"message": "No content"}

    except:
        data = {"message": "Error!"}
        status = 400
    
    finally:
        return jsonify(data), status


@bp_app.route('/<int:id>', methods=['GET'])
def select_one(id):
    try:
        character = Character.query.get(id)

        data = {
            "id": character.id,
            "name": character.name,
        }

        status = 200
    
    except:
        data = dict()
        status = 400
    
    finally:
        return jsonify(data), status

    
@bp_app.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    
    try:
        character = Character.query.filter_by(id=id).first()
        db.session.delete(character)
        db.session.commit()
        
        data = {
            "message": "Success to deleting item",
        }
        status = 200

    except:
        data = {
            "message": "Error to deleting item",
        }
        status = 400

    finally:
        return jsonify(data), status

    ...

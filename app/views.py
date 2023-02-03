from flask import Blueprint, jsonify, request
from app.models import Author, Book, AuthorBook
from app.config_database import db
import json

bp_app = Blueprint('gumball', __name__)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/', methods=['POST'])
def save():
    payload = request.data
    payload = json.loads(payload.decode('utf-8'))
    
    author_id = payload['author']['id']
    author_name = payload['author']['name']
    
    book_id = payload['book']['id']
    book_name = payload['book']['name']
        
    try:
        author = Author(
            id = author_id,
            name=author_name
        )
        db.session.add(author)
        db.session.commit()

        book = Book(
            id = book_id,
            name=book_name
        )
        db.session.add(book)
        db.session.commit()

        author_book = AuthorBook(
            book_id=author.id,
            author_id=book.id
        )
        db.session.add(author_book)
        db.session.commit()
        
        data = {
            "author": {
                "id": author.id,
                "name": author.name,
            },
            
            "book": {
                "id": book.id,
                "name": book.name,
                },
            
            "author_book":{
                "author_id": author_book.author_id,
                "book_id": author_book.book_id   
            }

        }
        
        status=201
        
    except:
        data = dict()
        status = 400
    
    finally:
        return jsonify(data), status
  

@bp_app.route('/authors', methods=['GET'])
def get_all_authors():
     
    try:
        queryset = Author.query.all()
    
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
    
    
@bp_app.route('/books', methods=['GET'])
def get_all_books():
     
    try:
        queryset = Book.query.all()
    
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


@bp_app.route('/authors/<int:id>', methods=['GET'])
def get_author_by_id(id):
    try:
        author = Author.query.get(id)
        data = {
            "id": author.id,
            "name": author.name,
        }

        status = 200
    
    except:
        data = dict()
        status = 400
    
    finally:
        return jsonify(data), status


@bp_app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    try:
        book = Book.query.get(id)
        data = {
            "id": book.id,
            "name": book.name,
        }

        status = 200
    
    except:
        data = dict()
        status = 400
    
    finally:
        return jsonify(data), status
    
    
@bp_app.route('/authors/one', methods=['GET'])
def get_authors_by_name():
    try:
        name = request.args.get('name', '')
        queryset = Author.query.filter_by(name=name).all()
        
        data = [
            {
                "id": author.id,
                "name": author.name,
            }
            for author in queryset        
        ]

        status = 200
    
    except:
        data = dict()
        status = 400
    
    finally:
        return jsonify(data), status
    

@bp_app.route('/books/one', methods=['GET'])
def get_books_by_name():
    try:
        name = request.args.get('name', '')
        queryset = Book.query.filter_by(name=name).all()
        
        data = [
            {
                "id": book.id,
                "name": book.name,
            }
            for book in queryset        
        ]

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

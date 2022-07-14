from flask import Blueprint, jsonify
from .model import Book

bp_app = Blueprint('endpoint', __name__)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/get', methods=['GET'])
def get():
    queryset = Book.query.all()
    data = jsonify(queryset)
    return data, 200
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

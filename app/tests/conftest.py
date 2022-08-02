import pytest
from app import create_app


@pytest.fixture()
def app():
    sqlite = 'sqlite:///test.db'
    
    app = create_app(sqlite)
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"
    })
    
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

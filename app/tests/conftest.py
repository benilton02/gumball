import pytest
from app import create_app


@pytest.fixture(scope='module')
def app():
    sqlite = 'sqlite:///test.db'
    
    app = create_app(sqlite)
    app.config.update({
        "TESTING": True
    })
    
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

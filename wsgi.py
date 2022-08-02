from app import create_app

sqlite = 'sqlite:///setup.db'

app = application = create_app(sqlite)

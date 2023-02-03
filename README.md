# gumball 

#### Dependencies

- [Python 3.10^](https://www.python.org/)
- [Poetry](https://python-poetry.org/) 


#### How to run on production mode?
Create a virtual env with poetry
```sh
poetry shell
```

Run app
```sh
gunicorn wsgi:app
```

### How to run on development mode?
Set FLASK variables
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

```
### To test 
```sh
export FLASK_APP='app:create_app("sqlite:///test.db")'
```

```sh
pytest/app
```

Run app

```sh
flask run
```

### Migration
Creates a new migration repository:
```sh 
flask db init
```

Autogenerate a new revision file:
```sh
flask db migrate 
```

### How to test app?
inside virtualenv
```sh
pytest -v
```

### How to coverage test?
inside virtualenv
```sh
pytest --cov
```
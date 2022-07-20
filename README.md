# gumball 

#### WSGI Gunicorn
production mode
```sh
gunicorn wsgi:app
```

### Set FLASK variables:
Development mode
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

### Run app:
Development mode

```sh
flask run
```

### Migration:
Creates a new migration repository:
```sh 
flask db init
```
Autogenerate a new revision file.
```sh
flask db migrate 
```
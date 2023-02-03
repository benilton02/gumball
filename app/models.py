from app.config_database import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    books = db.relationship("AuthorBook", back_populates="author")
    ...

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    authors = db.relationship("AuthorBook", back_populates="book")
    ...

class AuthorBook(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), primary_key=True)
    author = db.relationship("Author", back_populates="books")
    book = db.relationship("Book", back_populates="authors")


# db.create_all()
# db.drop_all()

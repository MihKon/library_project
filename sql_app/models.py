from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, Text

from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    type_of_user = Column(Boolean, nullable=False)


class Authors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String, nullable=False)
    patronymic = Column(String)
    date_of_birth = Column(Date)
    date_of_death = Column(Date)


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    link = Column(String)
    publication_year = Column(Integer)


class Shelves(Base):
    __tablename__ = "shelves"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    type_of_shelf = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


class BookShelves(Base):
    __tablename__ = "book_shelves"

    id = Column(Integer, primary_key=True)
    shelf_id = Column(Integer, ForeignKey("shelves.id"))
    book_id = Column(Integer, ForeignKey("books.id"))


class BooksAuthors(Base):
    __tablename__ = "book_authors"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    author_id = Column(Integer, ForeignKey("authors.id"))


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer, nullable=False)


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    access = Column(Boolean, nullable=False)

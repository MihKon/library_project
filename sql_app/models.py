from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, Text
from sqlalchemy.orm import relationship

from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    type_of_user = Column(String)

    review = relationship("Reviews", back_populates="user")
    transaction = relationship("Transactions", back_populates="user")


class Authors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    date_of_birth = Column(Date)
    date_of_death = Column(Date)

    book = relationship("Books", back_populates="author")


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    link = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    publication_year = Column(Date)

    author = relationship("Authors", back_populates="book")
    review = relationship("Reviews", back_populates="book")
    transaction = relationship("Transactions", back_populates="book")
    shelf_of_book = relationship("BookShelves", back_populates="book")


class Shelves(Base):
    __tablename__ = "shelves"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    type_of_shelf = Column(Boolean)

    shelf_of_book = relationship("BookShelves", back_populates="shelf")


class BookShelves(Base):
    __tablename__ = "bookShelves"

    id = Column(Integer, primary_key=True)
    shelf_id = Column(Integer, ForeignKey("shelves.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    shelf = relationship("Shelves", back_populates="shelf_of_book")
    book = relationship("Books", back_populates="shelf_of_book")


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer)

    user = relationship("Users", back_populates="review")
    book = relationship("Books", back_populates="review")


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    access = Column(Boolean)

    user = relationship("Users", back_populates="transaction")
    book = relationship("Books", back_populates="transaction")

from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    login: str
    password: str
    name: str
    surname: str
    email: str
    type: bool


class User(UserBase):

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    id: int
    surname: str
    name: str
    patronymic: str
    date_of_birth: date
    date_of_death: date


class Author(AuthorBase):

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    id: int
    title: str
    price: float
    link: str
    author_id: int
    publication_year: date


class Book(BookBase):

    class Config:
        orm_mode = True


class ShelfBase(BaseModel):
    id: int
    title: str
    description: str
    type: bool


class Shelf(ShelfBase):

    class Config:
        orm_mode = True


class BookShelvesBase(BaseModel):
    id: int
    shelf_id: int
    book_id: int


class BookShelves(BookShelvesBase):

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int
    text: str
    book_id: int
    user_id: int
    score: int


class Review(ReviewBase):

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    id: int
    book_id: int
    user_id: int
    access: bool


class Transaction(TransactionBase):

    class Config:
        orm_mode = True

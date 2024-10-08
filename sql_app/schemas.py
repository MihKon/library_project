from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    login: str
    password: str
    name: str
    surname: str
    email: str

class UserCreate(UserBase):
    pass


class User(UserBase):
    type_of_user: bool
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
    publication_year: int


class Book(BookBase):

    class Config:
        orm_mode = True


class ShelfBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    type_of_shelf: bool


class ShelfCreate(ShelfBase):
    pass


class Shelf(ShelfBase):
    user_id: int

    class Config:
        orm_mode = True


class ShelfWithBooks(Shelf):
    books: List[Book]


class BookShelvesBase(BaseModel):
    id: int


class BookShelfCreate(BookShelvesBase):
    pass


class BookShelves(BookShelvesBase):
    shelf_id: int
    book_id: int

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    id: int
    text: Optional[str] = None
    score: int


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    book_id: int
    user_id: int

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    id: int
    access: bool


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    book_id: int
    user_id: int

    class Config:
        orm_mode = True

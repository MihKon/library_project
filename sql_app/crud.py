from sqlalchemy.orm import Session
from sqlalchemy import or_

from . import models, schemas


# Получение всех книг из БД
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Books).offset(skip).limit(limit).all()


# Получение одной книги из БД по id
def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Books).filter(models.Books.id == book_id).first()


# Поиск книги по названию
def get_book_by_name(db: Session, book_name: str):
    return db.query(models.Books).filter(models.Books.title.ilike(f'%{book_name}%')).all()


# Работа с авторами
def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Authors).offset(skip).limit(limit).all()


def get_author_by_id(db: Session, author_id: int):
    return db.query(models.Authors).filter(models.Authors.id == author_id).first()


# Поиск автора по имени
def get_author_by_name(db: Session, author_name: str):
    return db.query(models.Authors).filter(or_(
        models.Authors.name.ilike(f'%{author_name}%'), 
        models.Authors.surname.ilike(f'%{author_name}%'),
        models.Authors.patronymic.ilike(f'%{author_name}%'))
    ).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


# Работа с полками
def create_shelf(db: Session, shelf: schemas.ShelfCreate, user_id: int):
    db_shelf = models.Shelves(title=shelf.title, description=shelf.description, type_of_shelf=shelf.type_of_shelf,
                              user_id=user_id)
    db.add(db_shelf)
    db.commit()
    db.refresh(db_shelf)
    return db_shelf


def update_shelf(db: Session, shelf: schemas.ShelfCreate):
    db.query(models.Shelves).filter(models.Shelves.id == shelf.id).\
        update({
            "title": shelf.title,
            "description": shelf.description,
            "type_of_shelf": shelf.type_of_shelf
        })
    db.commit()
    return db.query(models.Shelves).filter(models.Shelves.id == shelf.id).first()


def get_shelves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shelves).offset(skip).limit(limit).all()


def delete_shelf_by_id(db: Session, shelf_id: int):
    db_shelves = db.query(models.Shelves).filter(models.Shelves.id == shelf_id)
    db_shelf = db_shelves.first()
    db_shelves.delete()
    db.commit()
    return db_shelf


def get_shelf_by_id(db: Session, shelf_id: int):
    shelf = db.query(models.Shelves).filter(models.Shelves.id == shelf_id).first()
    books = get_books_from_shelf(db, shelf_id)
    new_shelf = schemas.ShelfWithBooks(id=shelf.id, title=shelf.title, description=shelf.description,
                                       type_of_shelf=shelf.type_of_shelf, user_id=shelf.user_id, books=books)
    return new_shelf


def get_books_from_shelf(db: Session, shelf_id: int):
    books_id = db.query(models.BookShelves).filter(models.BookShelves.shelf_id == shelf_id)
    books = []
    for b in books_id:
        book = db.query(models.Books).filter(models.Books.id == b.book_id).first()
        books.append(book)
    return books


def add_book_on_shelf(db: Session, shelf_id: int, book_id: int):
    db_shelf = models.BookShelves(shelf_id=shelf_id, book_id=book_id)
    db.add(db_shelf)
    db.commit()
    db.refresh(db_shelf)
    return db_shelf


# Работа с отзывами
def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reviews).offset(skip).limit(limit).all()


def create_review(db: Session, review: schemas.ReviewCreate, user_id: int, book_id: int):
    db_review = models.Reviews(text=review.text, score=review.score, book_id=book_id, user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_review_by_id(db: Session, review_id: int):
    return db.query(models.Reviews).filter(models.Reviews.id == review_id).first()


def delete_review_by_id(db: Session, review_id: int):
    db_reviews = db.query(models.Reviews).filter(models.Reviews.id == review_id)
    db_review = db_reviews.first()
    db_reviews.delete()
    db.commit()
    return db_review


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transactions).offset(skip).limit(limit).all()


def get_transaction_by_id(db: Session, transaction_id: int):
    return db.query(models.Transactions).filter(models.Transactions.id == transaction_id).first()

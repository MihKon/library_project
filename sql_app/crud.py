from sqlalchemy.orm import Session

from . import models, schemas


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Books).filter(models.Books.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Books).offset(skip).limit(limit).all()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Authors).offset(skip).limit(limit).all()


def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reviews).offset(skip).limit(limit).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

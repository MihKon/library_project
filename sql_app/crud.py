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
    return db.query(models.Shelves).filter(models.Shelves.id == shelf_id).first()


def get_books_from_shelf(db: Session, shelf_id: int):
    return db.query(models.BookShelves).filter(models.BookShelves.shelf_id == shelf_id)


def add_book_on_shelf(db: Session, book_shelf: schemas.BookShelfCreate):
    db_shelf = models.BookShelves(shelf_id=book_shelf.shelf_id, book_id=book_shelf.book_id)
    db.add(db_shelf)
    db.commit()
    db.refresh(db_shelf)
    return db_shelf


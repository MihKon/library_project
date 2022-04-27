from typing import List

from fastapi import FastAPI, Depends
from .database import SessionLocal, engine
from . import models, schemas, crud
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/books", response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.get("/api/v1/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book_by_id(db, book_id)


# Поиск книг (нужно доделывать)
@app.get("/api/v1/books/", response_model=schemas.Book)
async def search_book(
    b: Optional[List[str]] = Query(None)
):
    found_book = {"b": b}
    return found_book

@app.get("/api/v1/authors", response_model=List[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)


@app.get("/api/v1/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_author_by_id(db, author_id)


# Работа с отзывами
@app.get("/api/v1/reviews", response_model=List[schemas.Review])
def read_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)


@app.get("/api/v1/reviews/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    return crud.get_review_by_id(db, review_id)


@app.post("/api/v1/reviews", response_model=schemas.Review)
def add_review(review: schemas.ReviewCreate, user_id: int, book_id: int, db: Session = Depends(get_db)):
    return crud.create_review(db, review, user_id, book_id)


@app.delete("/api/v1/reviews/{review_id}", response_model=schemas.Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return crud.delete_review_by_id(db, review_id)


@app.get("/api/v1/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/api/v1/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    return user


# URL полок
@app.get("/api/v1/shelves", response_model=List[schemas.Shelf])
def read_shelves(db: Session = Depends(get_db)):
    return crud.get_shelves(db)


@app.get("/api/v1/shelves/{shelf_id}", response_model=schemas.ShelfWithBooks)
def read_shelf(shelf_id: int, db: Session = Depends(get_db)):
    return crud.get_shelf_by_id(db, shelf_id)


@app.post("/api/v1/shelves", response_model=schemas.Shelf)
def create_shelf(shelf: schemas.ShelfCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_shelf(db, shelf, user_id)


@app.delete("/api/v1/shelves/{shelf_id}", response_model=schemas.Shelf)
def delete_shelf(shelf_id: int, db: Session = Depends(get_db)):
    return crud.delete_shelf_by_id(db, shelf_id)


@app.put("/api/v1/shelves/{shelf_id}", response_model=schemas.Shelf)
def update_shelf(shelf: schemas.ShelfCreate, db: Session = Depends(get_db)):
    return crud.update_shelf(db, shelf)


@app.post("/api/v1/shelves/{shelf_id}", response_model=schemas.BookShelves)
def add_book_to_shelf(book_id: int, shelf_id: int, db: Session = Depends(get_db)):
    return crud.add_book_on_shelf(db, shelf_id, book_id)


# URL транзакций
@app.get("/api/v1/transactions", response_model=List[schemas.Transaction])
def read_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)


@app.get("/api/v1/transactions/{transaction_id}", response_model=schemas.Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return crud.get_transaction_by_id(db, transaction_id)

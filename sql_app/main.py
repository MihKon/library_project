from typing import Optional, List

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


@app.get("/api/v1/authors", response_model=List[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)


@app.get("/api/v1/reviews", response_model=List[schemas.Review])
def read_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)


@app.get("/api/v1/users", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


# URL полок
@app.get("/api/v1/shelves", response_model=List[schemas.Shelf])
def read_shelves(db: Session = Depends(get_db)):
    return crud.get_shelves(db)


@app.get("/api/v1/shelves/{shelf_id}", response_model=schemas.Shelf)
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


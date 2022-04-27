from typing import List, Optional

from fastapi import FastAPI, Depends, Query, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .database import SessionLocal, engine
from . import models, schemas, crud
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = crud.get_user_by_login(db, login=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.post("/token")
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.get_user_by_login(db, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    password = form_data.password
    if not password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.login, "token_type": "bearer"}


@app.post("/registration", response_model=schemas.User)
async def registration(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, user)



@app.get("/api/v1/users/profile")
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@app.get("/api/v1/books", response_model=List[schemas.Book])
async def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.get("/api/v1/books/{book_id}", response_model=schemas.Book)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book_by_id(db, book_id)


# Поиск книг
@app.get("/api/v1/books/", response_model=List[schemas.Book])
async def search_book(
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return crud.get_book_by_name(db, q)


@app.get("/api/v1/authors", response_model=List[schemas.Author])
async def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)


@app.get("/api/v1/authors/{author_id}", response_model=schemas.Author)
async def read_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_author_by_id(db, author_id)


@app.get("/api/v1/authors/", response_model=List[schemas.Author])
async def search_author(
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return crud.get_author_by_name(db, q)


# Работа с отзывами
@app.get("/api/v1/reviews", response_model=List[schemas.Review])
async def read_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)


@app.get("/api/v1/reviews/{review_id}", response_model=schemas.Review)
async def read_review(review_id: int, db: Session = Depends(get_db)):
    return crud.get_review_by_id(db, review_id)


@app.post("/api/v1/reviews", response_model=schemas.Review)
async def add_review(review: schemas.ReviewCreate, user_id: int, book_id: int, db: Session = Depends(get_db)):
    return crud.create_review(db, review, user_id, book_id)


@app.delete("/api/v1/reviews/{review_id}", response_model=schemas.Review)
async def delete_review(review_id: int, db: Session = Depends(get_db)):
    return crud.delete_review_by_id(db, review_id)


@app.get("/api/v1/users", response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/api/v1/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    return user


@app.get("/api/v1/users/", response_model=List[schemas.User])
async def search_user(
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return crud.get_user_by_name(db, q)


# URL полок
@app.get("/api/v1/shelves", response_model=List[schemas.Shelf])
async def read_shelves(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.get_shelves(db, current_user.id)


@app.get("/api/v1/shelves/{shelf_id}", response_model=schemas.ShelfWithBooks)
async def read_shelf(shelf_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.get_shelf_by_id(db, shelf_id)


@app.post("/api/v1/shelves", response_model=schemas.Shelf)
async def create_shelf(shelf: schemas.ShelfCreate, db: Session = Depends(get_db),
                        current_user: schemas.User = Depends(get_current_user)):
    return crud.create_shelf(db, shelf, current_user.id)


@app.delete("/api/v1/shelves/{shelf_id}", response_model=schemas.Shelf)
async def delete_shelf(shelf_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.delete_shelf_by_id(db, shelf_id)


@app.put("/api/v1/shelves/{shelf_id}", response_model=schemas.Shelf)
async def update_shelf(shelf: schemas.ShelfCreate, db: Session = Depends(get_db), 
                        current_user: schemas.User = Depends(get_current_user)):
    return crud.update_shelf(db, shelf)


@app.post("/api/v1/shelves/{shelf_id}", response_model=schemas.BookShelves)
async def add_book_to_shelf(book_id: int, shelf_id: int, db: Session = Depends(get_db), 
                            current_user: schemas.User = Depends(get_current_user)):
    return crud.add_book_on_shelf(db, shelf_id, book_id)


# URL транзакций
@app.get("/api/v1/transactions", response_model=List[schemas.Transaction])
async def read_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)


@app.get("/api/v1/transactions/{transaction_id}", response_model=schemas.Transaction)
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return crud.get_transaction_by_id(db, transaction_id)


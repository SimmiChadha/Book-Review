from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models,schemas
from typing import List, Optional
from tasks import send_confirmation_email

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency for db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint to create a new book
@app.post("/books/", response_model=schemas.Book)
def create_book(book:schemas.BookCreate, db:Session=Depends(get_db)):
    print(book.dict(), '*************')
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Endpoint to retrieve all books
@app.get("/books/", response_model=List[schemas.Book])
def read_books(db:Session = Depends(get_db)):
    return db.query(models.Book).all()

# Endpoint to update a book by id
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id:int, book:schemas.BookUpdate, db:Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key,val in book.dict().items():
        setattr(db_book, key, val)
    db.commit()
    db.refresh(db_book)
    return db_book

# Endpoint to delete a book by id
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id:int, db:Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book

# Endpoint to create a review for a book
@app.post("/books/{book_id}/reviews/", response_model=schemas.Review)
def create_review(book_id:int, review:schemas.ReviewCreate, background_tasks: BackgroundTasks, db:Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_review = models.Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    background_tasks.add_task(send_confirmation_email, db_review.id)
    return db_review

# Endpoint to retrieve all reviews for a book
@app.get("/books/{book_id}/reviews/", response_model=List[schemas.Review])
def get_reviews(book_id:int, db:Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book.reviews
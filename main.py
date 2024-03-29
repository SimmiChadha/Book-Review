from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import Book, Review

app = FastAPI()

books_db = []
review_db = []

@app.post("/books/", response_model=Book)
def add_book(book:Book):
    books_db.append(book)
    return book

@app.post("/books/{book_id}/reviews/", response_model=Review)
def submit_review(book_id:int, review:Review):
    if book_id < 0 or book_id >= len(books_db):
        raise HTTPException(status_code=404, detail="Book not found")
    review_db.append((book_id, review))
    return review

@app.get("/books/", response_model=List[Book])
def get_books(author: Optional[str]=None, year:Optional[int]=None):
    if author:
        filtered_books = [book for book in books_db if book.author == author]
    elif year:
        filtered_books = [book for book in books_db if book.publication_year == year]
    else:
        filtered_books = books_db
    return filtered_books

@app.get("/books/{book_id}/reviews/", response_model=List[Review])
def get_reviews(book_id:int):
    if book_id < 0 or book_id >= len(books_db):
        raise HTTPException(status_code=404, detail="Book not found")
    reviews = [review for idx, review in review_db if idx == book_id]
    return reviews
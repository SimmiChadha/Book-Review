# Book-Review

This project is a Restful API built with FastAPI for a book review system.
It allows users to add books, submit reviews for books, retrieve books, and view reviews for specific books.

Features
- Add a new book with title, author, and publication year.
- Submit a review for a book with text review and rating.
- Retrieve all books.
- Retrieve all reviews for a specific book.

Technologies Used
- FastAPI: Python web framework for building APIs quickly and efficiently.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for database operations.
- Pydantic: Data validation and serialization library used with FastAPI.
- SQLite: Lightweight database engine for data storage.

Run the FastAPI server:
uvicorn main:app --reload

API Endpoints
- POST /books/: Add a new book.
- POST /books/{book_id}/reviews/: Submit a review for a book.
- GET /books/: Retrieve all books.
- GET /books/{book_id}/reviews/: Retrieve all reviews for a specific book.
- PUT books/{book_id}: Update a book
- DELETE books/{book_id}: Delete a book

Background Tasks
A background task is implemented for sending a confirmation email (simulated) after a review is posted.

Database Integration
SQLite is used for database integration, and CRUD operations are implemented for books and reviews.
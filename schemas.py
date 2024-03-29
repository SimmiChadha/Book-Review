from pydantic import BaseModel
from typing import List, Optional

class BookBase(BaseModel):
    title:str
    author:str
    publication_year:int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id:int

    class config:
        from_attributes = True

class ReviewBase(BaseModel):
    text:str
    rating:int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id:int
    book_id:int

    class Config:
        from_attributes = True

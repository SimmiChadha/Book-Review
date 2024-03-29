from pydantic import BaseModel
from typing import List, Optional

class Book(BaseModel):
    title:str
    author:str
    publication_year:int

class Review(BaseModel):
    text:str
    rating:int
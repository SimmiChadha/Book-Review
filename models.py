from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publication_year = Column(Integer)

    # define relationship with Review using foreign key
    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    rating = Column(Integer)

    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book", back_populates="reviews")
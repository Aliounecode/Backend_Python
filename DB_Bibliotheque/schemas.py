from pydantic import BaseModel
from typing import List, Optional

# --- AUTEURS ---
class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        from_attributes = True

# --- LIVRES ---
class BookBase(BaseModel):
    title: str
    genre: str
    year: int
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        from_attributes = True
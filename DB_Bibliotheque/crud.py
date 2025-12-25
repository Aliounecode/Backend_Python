from sqlalchemy.orm import Session
import models, schemas

# ---Voici mon crud pour les livres---
def get_books(db: Session, author_id: int = None):
    query = db.query(models.BookDB)
    if author_id:
        query = query.filter(models.BookDB.author_id == author_id)
    return query.all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.BookDB).filter(models.BookDB.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.BookDB(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_data: schemas.BookCreate):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db_book.title = book_data.title
        db_book.genre = book_data.genre
        db_book.year = book_data.year
        db_book.author_id = book_data.author_id
        db.commit()
        db.refresh(db_book)
    return db_book



def delete_book(db: Session, book_id: int):
    # 1. On cherche le livre
    db_book = db.query(models.BookDB).filter(models.BookDB.id == book_id).first()
    # 2. S'il existe, on le supprime
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

# --- Voici mon crud pour les auteurs ---

def get_authors(db: Session):
    return db.query(models.AuthorDB).all()

def get_author_by_id(db: Session, author_id: int):
    return db.query(models.AuthorDB).filter(models.AuthorDB.id == author_id).first()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.AuthorDB(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def update_author(db: Session, author_id: int, author_data: schemas.AuthorCreate):
    db_author = get_author_by_id(db, author_id)
    if db_author:
        db_author.name = author_data.name
        db.commit()
        db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = get_author_by_id(db, author_id)
    if db_author:
    
        db.delete(db_author)
        db.commit()
    return db_author
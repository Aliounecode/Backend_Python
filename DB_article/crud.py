from sqlalchemy.orm import Session
import models, schemas

# --- Logique Articles ---

def get_articles(db: Session, category_id: int = None):
    query = db.query(models.ArticleDB)
    if category_id:
        query = query.filter(models.ArticleDB.category_id == category_id)
    return query.all()

def get_article_by_id(db: Session, article_id: int):
    return db.query(models.ArticleDB).filter(models.ArticleDB.id == article_id).first()

def create_article(db: Session, article: schemas.ArticleCreate):
    # On transforme le schema Pydantic en Modèle DB
    db_article = models.ArticleDB(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, article_id: int, article_data: schemas.ArticleCreate):
    db_article = get_article_by_id(db, article_id)
    if db_article:
        db_article.title = article_data.title
        db_article.content = article_data.content
        db_article.price = article_data.price
        db_article.category_id = article_data.category_id
        db_article.image_url = article_data.image_url
        db.commit()
        db.refresh(db_article)
    return db_article

# --- SUPPRESSION ---
def delete_article(db: Session, article_id: int):
    db_article = db.query(models.ArticleDB).filter(models.ArticleDB.id == article_id).first()
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article

# --- Logique Catégories ---

def get_categories(db: Session):
    return db.query(models.CategoryDB).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.CategoryDB).filter(models.CategoryDB.id == category_id).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_cat = models.CategoryDB(name=category.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


def update_category(db: Session, category_id: int, category_data: schemas.CategoryCreate):
    db_cat = get_category_by_id(db, category_id)
    if db_cat:
        db_cat.name = category_data.name
        db.commit()
        db.refresh(db_cat)
    return db_cat

def delete_category(db: Session, category_id: int):
    db_cat = get_category_by_id(db, category_id)
    if db_cat:
        db.delete(db_cat)
        db.commit()
    return db_cat
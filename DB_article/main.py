from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

# On importe nos 3 autres fichiers
import models, schemas, crud

# Création des tables au démarrage
models.init_db()

app = FastAPI()

# CORS (Pour Angular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dépendance pour avoir la DB
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROUTES ARTICLES ---

@app.get("/articles/", response_model=List[schemas.Article])
def read_articles(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    # On appelle la fonction dans crud.py
    return crud.get_articles(db, category_id)

@app.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db, article)

@app.put("/articles/{article_id}", response_model=schemas.Article)
def update_article(article_id: int, article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = crud.update_article(db, article_id, article)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return db_article

@app.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article introuvable")
    return {"message": "Supprimé avec succès"}

# --- ROUTES CATEGORIES ---

@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

# GET (Récupérer une seule catégorie)
@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_cat = crud.get_category_by_id(db, category_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    return db_cat

# PUT (Modifier le nom d'une catégorie)
@app.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_cat = crud.update_category(db, category_id, category)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    return db_cat

# DELETE (Supprimer une catégorie)
@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_cat = crud.delete_category(db, category_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    return {"message": "Catégorie supprimée avec succès"}
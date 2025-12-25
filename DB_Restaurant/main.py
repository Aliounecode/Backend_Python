from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, crud

models.init_db()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROUTES PLATS ---

@app.get("/dishes/", response_model=List[schemas.Dish])
def read_dishes(menu_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_dishes(db, menu_id)

@app.get("/dishes/{dish_id}", response_model=schemas.Dish)
def read_one_dish(dish_id: int, db: Session = Depends(get_db)):
    db_d = crud.get_dish_by_id(db, dish_id)
    if db_d is None:
        raise HTTPException(status_code=404, detail="Plat non trouvé")
    return db_d

@app.post("/dishes/", response_model=schemas.Dish)
def create_dish(dish: schemas.DishCreate, db: Session = Depends(get_db)):
    return crud.create_dish(db, dish)

@app.put("/dishes/{dish_id}", response_model=schemas.Dish)
def update_dish(dish_id: int, dish: schemas.DishCreate, db: Session = Depends(get_db)):
    db_d = crud.update_dish(db, dish_id, dish)
    if db_d is None:
        raise HTTPException(status_code=404, detail="Plat non trouvé")
    return db_d

@app.delete("/dishes/{dish_id}")
def delete_dish(dish_id: int, db: Session = Depends(get_db)):
    db_d = crud.delete_dish(db, dish_id)
    if db_d is None:
        raise HTTPException(status_code=404, detail="Plat non trouvé")
    return {"message": "Supprimé avec succès"}


# --- ROUTES MENUS ---

@app.get("/menus/", response_model=List[schemas.Menu])
def read_menus(db: Session = Depends(get_db)):
    return crud.get_menus(db)

@app.get("/menus/{menu_id}", response_model=schemas.Menu)
def read_one_menu(menu_id: int, db: Session = Depends(get_db)):
    db_m = crud.get_menu_by_id(db, menu_id)
    if db_m is None:
        raise HTTPException(status_code=404, detail="Menu non trouvé")
    return db_m

@app.post("/menus/", response_model=schemas.Menu)
def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu)

@app.put("/menus/{menu_id}", response_model=schemas.Menu)
def update_menu(menu_id: int, menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    db_m = crud.update_menu(db, menu_id, menu)
    if db_m is None:
        raise HTTPException(status_code=404, detail="Menu non trouvé")
    return db_m

@app.delete("/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    db_m = crud.delete_menu(db, menu_id)
    if db_m is None:
        raise HTTPException(status_code=404, detail="Menu non trouvé")
    return {"message": "Supprimé avec succès"}
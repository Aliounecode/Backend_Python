from sqlalchemy.orm import Session
import models, schemas

# ==========================================
# LOGIQUE PLATS (Enfant)
# ==========================================

def get_dishes(db: Session, menu_id: int = None):
    query = db.query(models.DishDB)
    if menu_id:
        query = query.filter(models.DishDB.menu_id == menu_id)
    return query.all()

def get_dish_by_id(db: Session, dish_id: int):
    return db.query(models.DishDB).filter(models.DishDB.id == dish_id).first()

def create_dish(db: Session, dish: schemas.DishCreate):
    db_dish = models.DishDB(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def update_dish(db: Session, dish_id: int, dish_data: schemas.DishCreate):
    db_dish = get_dish_by_id(db, dish_id)
    if db_dish:
        db_dish.name = dish_data.name
        db_dish.ingredients = dish_data.ingredients
        db_dish.price = dish_data.price
        db_dish.is_spicy = dish_data.is_spicy
        db_dish.image_url = dish_data.image_url
        db_dish.menu_id = dish_data.menu_id
        db.commit()
        db.refresh(db_dish)
    return db_dish

def delete_dish(db: Session, dish_id: int):
    db_dish = get_dish_by_id(db, dish_id)
    if db_dish:
        db.delete(db_dish)
        db.commit()
    return db_dish


# ==========================================
# LOGIQUE MENUS (Parent)
# ==========================================

def get_menus(db: Session):
    return db.query(models.MenuDB).all()

def get_menu_by_id(db: Session, menu_id: int):
    return db.query(models.MenuDB).filter(models.MenuDB.id == menu_id).first()

def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.MenuDB(name=menu.name, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def update_menu(db: Session, menu_id: int, menu_data: schemas.MenuCreate):
    db_menu = get_menu_by_id(db, menu_id)
    if db_menu:
        db_menu.name = menu_data.name
        db_menu.description = menu_data.description
        db.commit()
        db.refresh(db_menu)
    return db_menu

def delete_menu(db: Session, menu_id: int):
    db_menu = get_menu_by_id(db, menu_id)
    if db_menu:
        db.delete(db_menu)
        db.commit()
    return db_menu
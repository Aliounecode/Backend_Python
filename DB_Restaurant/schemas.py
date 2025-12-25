from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS MENUS ---
class MenuBase(BaseModel):
    name: str
    description: str

class MenuCreate(MenuBase):
    pass

class Menu(MenuBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS PLATS ---
class DishBase(BaseModel):
    name: str
    ingredients: str
    price: float
    is_spicy: bool = False
    image_url: str
    menu_id: int

class DishCreate(DishBase):
    pass

class Dish(DishBase):
    id: int
    class Config:
        from_attributes = True
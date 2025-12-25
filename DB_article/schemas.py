from pydantic import BaseModel
from typing import List, Optional

# --- Schemas Catégorie ---
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True

# --- Schemas Article ---
class ArticleBase(BaseModel):
    title: str
    content: str
    price: float
    image_url: Optional[str] = "https://via.placeholder.com/150"
    category_id: int

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    class Config:
        from_attributes = True
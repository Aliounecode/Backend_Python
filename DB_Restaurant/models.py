from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Création de la DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./restaurant.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLE PARENT : MENUS (Catégories) ---
class MenuDB(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True) # Ex: "Entrées", "Burgers"
    description = Column(String)                   # Ex: "Pour bien commencer"
    dishes = relationship("DishDB", back_populates="menu")

# --- TABLE ENFANT : PLATS ---
class DishDB(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String)          # Ex: "Tomate, Mozza, Basilic"
    price = Column(Float)                 # Prix
    is_spicy = Column(Boolean, default=False) # Est-ce épicé ?
    image_url = Column(String)            # Lien vers la photo
    menu_id = Column(Integer, ForeignKey("menus.id"))
    menu = relationship("MenuDB", back_populates="dishes")

def init_db():
    Base.metadata.create_all(bind=engine)
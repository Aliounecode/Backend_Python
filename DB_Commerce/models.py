from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Création de la DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./commerce.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLE PARENT : CLIENTS ---
class CustomerDB(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True) # Nom complet
    email = Column(String, unique=True)    # Email
    address = Column(String)               # Adresse de livraison
    orders = relationship("OrderDB", back_populates="customer")

# --- TABLE ENFANT : COMMANDES ---
class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    reference = Column(String, unique=True) # Ex: CMD-2024-001
    total_amount = Column(Float)            # Montant total
    status = Column(String)                 # Ex: En cours, Livrée, Annulée
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("CustomerDB", back_populates="orders")

def init_db():
    Base.metadata.create_all(bind=engine)
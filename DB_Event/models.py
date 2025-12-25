from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Création de la DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./events.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLE PARENT : ÉVÉNEMENTS ---
class EventDB(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True) # Nom de l'événement
    location = Column(String) # Lieu (ex: Paris, Salle 101)
    date = Column(String)     # Date (ex: 2024-12-25)
    participants = relationship("ParticipantDB", back_populates="event")

# --- TABLE ENFANT : PARTICIPANTS ---
class ParticipantDB(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    phone = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("EventDB", back_populates="participants")

def init_db():
    Base.metadata.create_all(bind=engine)
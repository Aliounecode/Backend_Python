from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Création de la DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./hopital.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- TABLE PARENT : MÉDECINS ---
class DoctorDB(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)      # Nom du médecin
    specialty = Column(String)             # Ex: Cardiologue, Pédiatre
    office_number = Column(String)         # Numéro de bureau/salle
    patients = relationship("PatientDB", back_populates="doctor")

# --- TABLE ENFANT : PATIENTS ---
class PatientDB(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    age = Column(Integer)
    symptoms = Column(String)              # Ex: Fièvre, Toux
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("DoctorDB", back_populates="patients")

def init_db():
    Base.metadata.create_all(bind=engine)
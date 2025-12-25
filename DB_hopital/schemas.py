from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS MÉDECINS ---
class DoctorBase(BaseModel):
    name: str
    specialty: str
    office_number: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS PATIENTS ---
class PatientBase(BaseModel):
    full_name: str
    age: int
    symptoms: str
    doctor_id: int

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    class Config:
        from_attributes = True
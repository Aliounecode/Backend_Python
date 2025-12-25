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

# --- ROUTES PATIENTS ---

@app.get("/patients/", response_model=List[schemas.Patient])
def read_patients(doctor_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_patients(db, doctor_id)

@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_one_patient(patient_id: int, db: Session = Depends(get_db)):
    db_p = crud.get_patient_by_id(db, patient_id)
    if db_p is None:
        raise HTTPException(status_code=404, detail="Patient non trouvé")
    return db_p

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.put("/patients/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_p = crud.update_patient(db, patient_id, patient)
    if db_p is None:
        raise HTTPException(status_code=404, detail="Patient non trouvé")
    return db_p

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_p = crud.delete_patient(db, patient_id)
    if db_p is None:
        raise HTTPException(status_code=404, detail="Patient non trouvé")
    return {"message": "Supprimé avec succès"}


# --- ROUTES MÉDECINS ---

@app.get("/doctors/", response_model=List[schemas.Doctor])
def read_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

@app.get("/doctors/{doctor_id}", response_model=schemas.Doctor)
def read_one_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_d = crud.get_doctor_by_id(db, doctor_id)
    if db_d is None:
        raise HTTPException(status_code=404, detail="Médecin non trouvé")
    return db_d

@app.post("/doctors/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)

@app.put("/doctors/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(doctor_id: int, doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    db_d = crud.update_doctor(db, doctor_id, doctor)
    if db_d is None:
        raise HTTPException(status_code=404, detail="Médecin non trouvé")
    return db_d

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_d = crud.delete_doctor(db, doctor_id)
    if db_d is None:
        raise HTTPException(status_code=404, detail="Médecin non trouvé")
    return {"message": "Supprimé avec succès"}
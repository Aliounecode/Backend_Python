from sqlalchemy.orm import Session
import models, schemas

# crud pour les patients

def get_patients(db: Session, doctor_id: int = None):
    query = db.query(models.PatientDB)
    if doctor_id:
        query = query.filter(models.PatientDB.doctor_id == doctor_id)
    return query.all()

def get_patient_by_id(db: Session, patient_id: int):
    return db.query(models.PatientDB).filter(models.PatientDB.id == patient_id).first()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.PatientDB(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: int, p_data: schemas.PatientCreate):
    db_patient = get_patient_by_id(db, patient_id)
    if db_patient:
        db_patient.full_name = p_data.full_name
        db_patient.age = p_data.age
        db_patient.symptoms = p_data.symptoms
        db_patient.doctor_id = p_data.doctor_id
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient_by_id(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient



# crud pour les medecins


def get_doctors(db: Session):
    return db.query(models.DoctorDB).all()

def get_doctor_by_id(db: Session, doctor_id: int):
    return db.query(models.DoctorDB).filter(models.DoctorDB.id == doctor_id).first()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doc = models.DoctorDB(name=doctor.name, specialty=doctor.specialty, office_number=doctor.office_number)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def update_doctor(db: Session, doctor_id: int, doc_data: schemas.DoctorCreate):
    db_doc = get_doctor_by_id(db, doctor_id)
    if db_doc:
        db_doc.name = doc_data.name
        db_doc.specialty = doc_data.specialty
        db_doc.office_number = doc_data.office_number
        db.commit()
        db.refresh(db_doc)
    return db_doc

def delete_doctor(db: Session, doctor_id: int):
    db_doc = get_doctor_by_id(db, doctor_id)
    if db_doc:
        db.delete(db_doc)
        db.commit()
    return db_doc
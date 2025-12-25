from sqlalchemy.orm import Session
import models, schemas

# --- ÉTUDIANTS ---
def get_students(db: Session, classroom_id: int = None):
    query = db.query(models.StudentDB)
    if classroom_id:
        query = query.filter(models.StudentDB.classroom_id == classroom_id)
    return query.all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.StudentDB).filter(models.StudentDB.id == student_id).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.StudentDB(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student_data: schemas.StudentCreate):
    db_student = get_student_by_id(db, student_id)
    if db_student:
        db_student.full_name = student_data.full_name
        db_student.email = student_data.email
        db_student.age = student_data.age
        db_student.classroom_id = student_data.classroom_id
        db.commit()
        db.refresh(db_student)
    return db_student

# --- SUPPRESSION ---
def delete_student(db: Session, student_id: int):
    db_student = db.query(models.StudentDB).filter(models.StudentDB.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# --- CLASSES ---
def get_classrooms(db: Session):
    return db.query(models.ClassroomDB).all()

#  Récupérer une classe par son ID
def get_classroom_by_id(db: Session, classroom_id: int):
    return db.query(models.ClassroomDB).filter(models.ClassroomDB.id == classroom_id).first()


def create_classroom(db: Session, classroom: schemas.ClassroomCreate):
    db_cls = models.ClassroomDB(name=classroom.name)
    db.add(db_cls)
    db.commit()
    db.refresh(db_cls)
    return db_cls

#  Modifier une classe (ex: Renommer "Licence 2" en "Licence 3")
def update_classroom(db: Session, classroom_id: int, classroom_data: schemas.ClassroomCreate):
    db_classroom = get_classroom_by_id(db, classroom_id)
    if db_classroom:
        db_classroom.name = classroom_data.name
        db.commit()
        db.refresh(db_classroom)
    return db_classroom

#  Supprimer une classe
def delete_classroom(db: Session, classroom_id: int):
    db_classroom = get_classroom_by_id(db, classroom_id)
    if db_classroom:
        db.delete(db_classroom)
        db.commit()
    return db_classroom
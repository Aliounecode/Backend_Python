from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, crud

models.init_db()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Accepte tout pour l'examen
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

# ROUTES ÉTUDIANTS
@app.get("/students/", response_model=List[schemas.Student])
def read_students(classroom_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_students(db, classroom_id)

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return {"message": "Supprimé avec succès"}

# ROUTES CLASSES
@app.get("/classrooms/", response_model=List[schemas.Classroom])
def read_classrooms(db: Session = Depends(get_db)):
    return crud.get_classrooms(db)

@app.post("/classrooms/", response_model=schemas.Classroom)
def create_classroom(classroom: schemas.ClassroomCreate, db: Session = Depends(get_db)):
    return crud.create_classroom(db, classroom)


# GET (Une seule classe)
@app.get("/classrooms/{classroom_id}", response_model=schemas.Classroom)
def read_classroom(classroom_id: int, db: Session = Depends(get_db)):
    db_classroom = crud.get_classroom_by_id(db, classroom_id)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    return db_classroom

# PUT (Modifier une classe)
@app.put("/classrooms/{classroom_id}", response_model=schemas.Classroom)
def update_classroom(classroom_id: int, classroom: schemas.ClassroomCreate, db: Session = Depends(get_db)):
    db_classroom = crud.update_classroom(db, classroom_id, classroom)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    return db_classroom

# DELETE (Supprimer une classe)
@app.delete("/classrooms/{classroom_id}")
def delete_classroom(classroom_id: int, db: Session = Depends(get_db)):
    db_classroom = crud.delete_classroom(db, classroom_id)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    return {"message": "Classe supprimée avec succès"}
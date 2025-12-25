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

# ROUTES EMPLOYÉS
@app.get("/employees/", response_model=List[schemas.Employee])
def read_employees(department_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_employees(db, department_id)

@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db, employee_id, employee)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_emp = crud.delete_employee(db, employee_id)
    if db_emp is None:
        raise HTTPException(status_code=404, detail="Employé introuvable")
    return {"message": "Supprimé avec succès"}

# ROUTES DEPARTEMENTS
@app.get("/departments/", response_model=List[schemas.Department])
def read_departments(db: Session = Depends(get_db)):
    return crud.get_departments(db)

@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, department)


# GET (Un seul département)
@app.get("/departments/{department_id}", response_model=schemas.Department)
def read_department(department_id: int, db: Session = Depends(get_db)):
    db_dep = crud.get_department_by_id(db, department_id)
    if db_dep is None:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    return db_dep

# PUT (Modifier un département)
@app.put("/departments/{department_id}", response_model=schemas.Department)
def update_department(department_id: int, department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_dep = crud.update_department(db, department_id, department)
    if db_dep is None:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    return db_dep

# DELETE (Supprimer un département)
@app.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    db_dep = crud.delete_department(db, department_id)
    if db_dep is None:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    return {"message": "Département supprimé avec succès"}
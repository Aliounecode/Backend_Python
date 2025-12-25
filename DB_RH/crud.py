from sqlalchemy.orm import Session
import models, schemas

# --- EMPLOYÉS ---
def get_employees(db: Session, department_id: int = None):
    query = db.query(models.EmployeeDB)
    if department_id:
        query = query.filter(models.EmployeeDB.department_id == department_id)
    return query.all()

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(models.EmployeeDB).filter(models.EmployeeDB.id == employee_id).first()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_emp = models.EmployeeDB(**employee.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def update_employee(db: Session, employee_id: int, emp_data: schemas.EmployeeCreate):
    db_emp = get_employee_by_id(db, employee_id)
    if db_emp:
        db_emp.name = emp_data.name
        db_emp.position = emp_data.position
        db_emp.salary = emp_data.salary
        db_emp.department_id = emp_data.department_id
        db.commit()
        db.refresh(db_emp)
    return db_emp

# --- SUPPRESSION ---
def delete_employee(db: Session, employee_id: int):
    db_emp = db.query(models.EmployeeDB).filter(models.EmployeeDB.id == employee_id).first()
    if db_emp:
        db.delete(db_emp)
        db.commit()
    return db_emp

# --- DEPARTEMENTS ---
def get_departments(db: Session):
    return db.query(models.DepartmentDB).all()

#  Récupérer un département par son ID
def get_department_by_id(db: Session, department_id: int):
    return db.query(models.DepartmentDB).filter(models.DepartmentDB.id == department_id).first()


def create_department(db: Session, department: schemas.DepartmentCreate):
    db_dep = models.DepartmentDB(name=department.name)
    db.add(db_dep)
    db.commit()
    db.refresh(db_dep)
    return db_dep

#  Modifier un département (ex: Renommer "Info" en "DSI")
def update_department(db: Session, department_id: int, department_data: schemas.DepartmentCreate):
    db_dep = get_department_by_id(db, department_id)
    if db_dep:
        db_dep.name = department_data.name
        db.commit()
        db.refresh(db_dep)
    return db_dep

#  Supprimer un département
def delete_department(db: Session, department_id: int):
    db_dep = get_department_by_id(db, department_id)
    if db_dep:
        db.delete(db_dep)
        db.commit()
    return db_dep
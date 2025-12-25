from sqlalchemy.orm import Session
import models, schemas

def get_tasks(db: Session, project_id: int = None):
    query = db.query(models.TaskDB)
    if project_id:
        query = query.filter(models.TaskDB.project_id == project_id)
    return query.all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.TaskDB(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_data: schemas.TaskCreate):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        db_task.title = task_data.title
        db_task.description = task_data.description
        db_task.is_done = task_data.is_done
        db_task.project_id = task_data.project_id
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

def get_projects(db: Session):
    return db.query(models.ProjectDB).all()

#  Récupérer un projet par son ID
def get_project_by_id(db: Session, project_id: int):
    return db.query(models.ProjectDB).filter(models.ProjectDB.id == project_id).first()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_proj = models.ProjectDB(name=project.name)
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj

#  Modifier un projet (ex: Renommer "Site Web" en "Application Web")
def update_project(db: Session, project_id: int, project_data: schemas.ProjectCreate):
    db_project = get_project_by_id(db, project_id)
    if db_project:
        db_project.name = project_data.name
        db.commit()
        db.refresh(db_project)
    return db_project

#  Supprimer un projet
def delete_project(db: Session, project_id: int):
    db_project = get_project_by_id(db, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project
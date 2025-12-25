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

# ROUTES TÂCHES
@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(project_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db, project_id)

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    return {"message": "Supprimé avec succès"}

# ROUTES PROJETS
@app.get("/projects/", response_model=List[schemas.Project])
def read_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)

@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

# --- NOUVELLES ROUTES PROJETS ---

# GET (Un seul projet)
@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    return db_project

# PUT (Modifier un projet)
@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id, project)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    return db_project

# DELETE (Supprimer un projet)
@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.delete_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    return {"message": "Projet supprimé avec succès"}
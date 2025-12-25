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

# --- ROUTES PARTICIPANTS ---

@app.get("/participants/", response_model=List[schemas.Participant])
def read_participants(event_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_participants(db, event_id)

@app.post("/participants/", response_model=schemas.Participant)
def create_participant(participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    return crud.create_participant(db, participant)

@app.put("/participants/{participant_id}", response_model=schemas.Participant)
def update_participant(participant_id: int, participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    db_part = crud.update_participant(db, participant_id, participant)
    if db_part is None:
        raise HTTPException(status_code=404, detail="Participant non trouvé")
    return db_part

@app.delete("/participants/{participant_id}")
def delete_participant(participant_id: int, db: Session = Depends(get_db)):
    db_part = crud.delete_participant(db, participant_id)
    if db_part is None:
        raise HTTPException(status_code=404, detail="Participant non trouvé")
    return {"message": "Supprimé avec succès"}


# --- ROUTES ÉVÉNEMENTS ---

@app.get("/events/", response_model=List[schemas.Event])
def read_events(db: Session = Depends(get_db)):
    return crud.get_events(db)

@app.get("/events/{event_id}", response_model=schemas.Event)
def read_one_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event_by_id(db, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    return db_event

@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db, event)

@app.put("/events/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = crud.update_event(db, event_id, event)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    return db_event

@app.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.delete_event(db, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Événement non trouvé")
    return {"message": "Supprimé avec succès"}
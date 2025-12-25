from sqlalchemy.orm import Session
import models, schemas

# ==========================================
# LOGIQUE PARTICIPANTS (Create, Read, Update, Delete)
# ==========================================

def get_participants(db: Session, event_id: int = None):
    query = db.query(models.ParticipantDB)
    if event_id:
        query = query.filter(models.ParticipantDB.event_id == event_id)
    return query.all()

def get_participant_by_id(db: Session, participant_id: int):
    return db.query(models.ParticipantDB).filter(models.ParticipantDB.id == participant_id).first()

def create_participant(db: Session, participant: schemas.ParticipantCreate):
    db_part = models.ParticipantDB(**participant.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def update_participant(db: Session, participant_id: int, part_data: schemas.ParticipantCreate):
    db_part = get_participant_by_id(db, participant_id)
    if db_part:
        db_part.name = part_data.name
        db_part.email = part_data.email
        db_part.phone = part_data.phone
        db_part.event_id = part_data.event_id
        db.commit()
        db.refresh(db_part)
    return db_part

def delete_participant(db: Session, participant_id: int):
    db_part = get_participant_by_id(db, participant_id)
    if db_part:
        db.delete(db_part)
        db.commit()
    return db_part


# ==========================================
# LOGIQUE ÉVÉNEMENTS (Create, Read, Update, Delete)
# ==========================================

def get_events(db: Session):
    return db.query(models.EventDB).all()

def get_event_by_id(db: Session, event_id: int):
    return db.query(models.EventDB).filter(models.EventDB.id == event_id).first()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.EventDB(title=event.title, location=event.location, date=event.date)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def update_event(db: Session, event_id: int, event_data: schemas.EventCreate):
    db_event = get_event_by_id(db, event_id)
    if db_event:
        db_event.title = event_data.title
        db_event.location = event_data.location
        db_event.date = event_data.date
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = get_event_by_id(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event
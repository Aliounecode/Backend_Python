from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS ÉVÉNEMENTS ---
class EventBase(BaseModel):
    title: str
    location: str
    date: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS PARTICIPANTS ---
class ParticipantBase(BaseModel):
    name: str
    email: str
    phone: str
    event_id: int

class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id: int
    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS CLASSES ---
class ClassroomBase(BaseModel):
    name: str

class ClassroomCreate(ClassroomBase):
    pass

class Classroom(ClassroomBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS ÉTUDIANTS ---
class StudentBase(BaseModel):
    full_name: str
    email: str
    age: int
    classroom_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        from_attributes = True
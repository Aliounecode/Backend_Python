from pydantic import BaseModel
from typing import List, Optional

class ProjectBase(BaseModel):
    name: str
class ProjectCreate(ProjectBase):
    pass
class Project(ProjectBase):
    id: int
    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    description: str
    is_done: bool = False # <--- IMPORTANT
    project_id: int
class TaskCreate(TaskBase):
    pass
class Task(TaskBase):
    id: int
    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS DEPARTEMENTS ---
class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS EMPLOYÉS ---
class EmployeeBase(BaseModel):
    name: str
    position: str
    salary: float
    department_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        from_attributes = True
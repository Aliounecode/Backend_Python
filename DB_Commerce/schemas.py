from pydantic import BaseModel
from typing import List, Optional

# --- SCHEMAS CLIENTS ---
class CustomerBase(BaseModel):
    full_name: str
    email: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    class Config:
        from_attributes = True

# --- SCHEMAS COMMANDES ---
class OrderBase(BaseModel):
    reference: str
    total_amount: float
    status: str
    customer_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    class Config:
        from_attributes = True
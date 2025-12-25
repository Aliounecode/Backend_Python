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

# --- ROUTES COMMANDES ---

@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(customer_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_orders(db, customer_id)

@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    db_ord = crud.get_order_by_id(db, order_id)
    if db_ord is None:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return db_ord

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_ord = crud.update_order(db, order_id, order)
    if db_ord is None:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return db_ord

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_ord = crud.delete_order(db, order_id)
    if db_ord is None:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return {"message": "Supprimé avec succès"}


# --- ROUTES CLIENTS ---

@app.get("/customers/", response_model=List[schemas.Customer])
def read_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)

@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_one_customer(customer_id: int, db: Session = Depends(get_db)):
    db_cust = crud.get_customer_by_id(db, customer_id)
    if db_cust is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_cust

@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_cust = crud.update_customer(db, customer_id, customer)
    if db_cust is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_cust

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_cust = crud.delete_customer(db, customer_id)
    if db_cust is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return {"message": "Supprimé avec succès"}
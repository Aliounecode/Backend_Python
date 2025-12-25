from sqlalchemy.orm import Session
import models, schemas

# ==========================================
# LOGIQUE COMMANDES (Enfant)
# ==========================================

def get_orders(db: Session, customer_id: int = None):
    query = db.query(models.OrderDB)
    if customer_id:
        query = query.filter(models.OrderDB.customer_id == customer_id)
    return query.all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(models.OrderDB).filter(models.OrderDB.id == order_id).first()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.OrderDB(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, ord_data: schemas.OrderCreate):
    db_order = get_order_by_id(db, order_id)
    if db_order:
        db_order.reference = ord_data.reference
        db_order.total_amount = ord_data.total_amount
        db_order.status = ord_data.status
        db_order.customer_id = ord_data.customer_id
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = get_order_by_id(db, order_id)
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order


# ==========================================
# LOGIQUE CLIENTS (Parent)
# ==========================================

def get_customers(db: Session):
    return db.query(models.CustomerDB).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(models.CustomerDB).filter(models.CustomerDB.id == customer_id).first()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_cust = models.CustomerDB(**customer.dict())
    db.add(db_cust)
    db.commit()
    db.refresh(db_cust)
    return db_cust

def update_customer(db: Session, customer_id: int, cust_data: schemas.CustomerCreate):
    db_cust = get_customer_by_id(db, customer_id)
    if db_cust:
        db_cust.full_name = cust_data.full_name
        db_cust.email = cust_data.email
        db_cust.address = cust_data.address
        db.commit()
        db.refresh(db_cust)
    return db_cust

def delete_customer(db: Session, customer_id: int):
    db_cust = get_customer_by_id(db, customer_id)
    if db_cust:
        db.delete(db_cust)
        db.commit()
    return db_cust
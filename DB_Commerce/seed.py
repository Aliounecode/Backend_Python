import random
from models import SessionLocal, CustomerDB, OrderDB, engine, Base

print("Nettoyage de la base Commerce...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 1. Création des Clients
clients_data = [
    ("Alioune Badara", "alioune@mail.sn", "Dakar, Plateau"),
    ("Fatima Sy", "fatima@mail.sn", "Saint-Louis, Nord"),
    ("Jean Michel", "jean@mail.fr", "Paris, France"),
    ("Aissatou Diallo", "aicha@mail.sn", "Thiès, Centre")
]

db_customers = []
for name, email, addr in clients_data:
    cust = CustomerDB(full_name=name, email=email, address=addr)
    db.add(cust)
    db_customers.append(cust)
db.commit()

# 2. Création des Commandes
status_list = ["En attente", "Payée", "Expédiée", "Livrée", "Annulée"]

print("Génération des commandes...")
for i in range(30):
    cust = random.choice(db_customers)
    
    # Génération d'une ref unique (CMD-1, CMD-2...)
    ref = f"CMD-{2024}-{i+1000}"
    
    order = OrderDB(
        reference=ref,
        total_amount=round(random.uniform(5000, 250000), 2), # Prix entre 5000 et 250000
        status=random.choice(status_list),
        customer_id=cust.id
    )
    db.add(order)

db.commit()
db.close()
print("✅ BASE COMMERCE REMPLIE AVEC SUCCÈS !")
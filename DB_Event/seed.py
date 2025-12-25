import random
from models import SessionLocal, EventDB, ParticipantDB, engine, Base

print("Nettoyage de la base...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 1. Création des Événements
events_data = [
    ("Conférence Tech 2024", "Paris, Salle A", "2024-06-15"),
    ("Festival de Musique", "Lyon, Plein Air", "2024-07-20"),
    ("Hackathon Python", "Dakar, Campus", "2024-05-10"),
    ("Gala de Charité", "Marseille, Hotel Luxe", "2024-12-01")
]

db_events = []
for title, loc, date in events_data:
    ev = EventDB(title=title, location=loc, date=date)
    db.add(ev)
    db_events.append(ev)
db.commit()

# 2. Création des Participants
prenoms = ["Alice", "Bob", "Charlie", "David", "Eva", "Fatou", "Moussa", "Sophie"]
noms = ["Diop", "Dupont", "Mbaye", "Martin", "Fall", "Sow"]

print("Génération des participants...")
for i in range(30):
    ev = random.choice(db_events)
    fname = random.choice(prenoms)
    lname = random.choice(noms)
    
    part = ParticipantDB(
        name=f"{fname} {lname}",
        email=f"{fname.lower()}.{lname.lower()}@email.com",
        phone=f"+221 77 {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}",
        event_id=ev.id
    )
    db.add(part)

db.commit()
db.close()
print("✅ BASE ÉVÉNEMENTIEL REMPLIE AVEC SUCCÈS !")
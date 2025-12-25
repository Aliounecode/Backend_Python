import random
from models import SessionLocal, DoctorDB, PatientDB, engine, Base

print("Nettoyage de la base Hôpital...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 1. Création des Médecins
doctors_data = [
    ("Dr. Diop", "Diagnostic", "A-101"),
    ("Dr. Mamour", "Neurochirurgie", "B-205"),
    ("Dr. Ndiaye", "Généraliste", "C-003"),
    ("Dr. Fall", "Femme Médecin", "D-404")
]

db_doctors = []
for name, spec, office in doctors_data:
    doc = DoctorDB(name=name, specialty=spec, office_number=office)
    db.add(doc)
    db_doctors.append(doc)
db.commit()

# 2. Création des Patients
prenoms = ["Abdou", "Papa", "Modou", "Marie", "Fatou", "Awa"]
noms = ["Malade", "Tousseux", "Bobo", "Fatigué", "Enrhumé"]
symptomes_liste = ["Grippe", "Fracture", "Migraine", "Stress", "Contrôle routine", "Allergie"]

print("Admission des patients...")
for i in range(25):
    doc = random.choice(db_doctors)
    
    p = PatientDB(
        full_name=f"{random.choice(prenoms)} {random.choice(noms)}",
        age=random.randint(5, 90),
        symptoms=random.choice(symptomes_liste),
        doctor_id=doc.id
    )
    db.add(p)

db.commit()
db.close()
print("✅ BASE HÔPITAL REMPLIE AVEC SUCCÈS !")
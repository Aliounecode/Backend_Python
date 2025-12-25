import random
from models import SessionLocal, DepartmentDB, EmployeeDB, engine, Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Départements
deps_names = ["Ressources Humaines", "Informatique", "Marketing", "Comptabilité"]
deps_db = []
for name in deps_names:
    d = DepartmentDB(name=name)
    db.add(d)
    deps_db.append(d)
db.commit()

# Employés
postes = ["Directeur", "Assistant", "Stagiaire", "Manager", "Consultant"]
noms = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois"]

for i in range(25):
    dep = random.choice(deps_db)
    emp = EmployeeDB(
        name=f"{random.choice(noms)} {i}",
        position=random.choice(postes),
        salary=round(random.uniform(1500.00, 5000.00), 2), # Salaire aléatoire
        department_id=dep.id
    )
    db.add(emp)

db.commit()
db.close()
print("✅ RH PRÊT !")
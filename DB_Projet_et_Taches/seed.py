import random
from models import SessionLocal, ProjectDB, TaskDB, engine, Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Projets
projets_list = ["Site E-commerce", "App Mobile Flutter", "API Backend", "Soutenance"]
db_projets = []
for p in projets_list:
    proj = ProjectDB(name=p)
    db.add(proj)
    db_projets.append(proj)
db.commit()

# Tâches
actions = ["Coder", "Débugger", "Tester", "Deployer", "Rédiger"]
objets = ["le login", "la database", "le CSS", "le rapport", "l'API"]

for i in range(25):
    proj = random.choice(db_projets)
    t = TaskDB(
        title=f"{random.choice(actions)} {random.choice(objets)}",
        description="Il faut faire ça rapidement avant la deadline.",
        is_done=random.choice([True, False]),
        project_id=proj.id
    )
    db.add(t)

db.commit()
db.close()
print("✅ PROJETS PRÊTS !")
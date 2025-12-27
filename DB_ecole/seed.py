import random
from models import SessionLocal, ClassroomDB, StudentDB, engine, Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 1. Classes
classes_names = ["Licence 3", "Master 1", "Master 2", "Doctorat"]
classes_db = []
for name in classes_names:
    c = ClassroomDB(name=name)
    db.add(c)
    classes_db.append(c)
db.commit()

# 2. Étudiants
first_names = ["Alioune", "Fatim", "Massamba", "Mor", "Mouhamed", "Mbene"]
last_names = ["Diop", "Diop", "Diagne", "Sokhna", "Thiam"]

for i in range(30):
    cl = random.choice(classes_db) # on recharge pour avoir les IDs
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    
    s = StudentDB(
        full_name=f"{fname} {lname}",
        email=f"{fname.lower()}.{lname.lower()}@univ.sn",
        age=random.randint(20, 30),
        classroom_id=cl.id
    )
    db.add(s)

db.commit()
db.close()
print("✅ ÉCOLE PRÊTE !")
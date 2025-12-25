import random
from models import SessionLocal, AuthorDB, BookDB, engine, Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Auteurs
auteurs_data = ["J.K. Rowling", "Stephen King", "Victor Hugo", "Agatha Christie", "J.R.R. Tolkien"]
auteurs_db = []
for name in auteurs_data:
    a = AuthorDB(name=name)
    db.add(a)
    auteurs_db.append(a)
db.commit()

# Livres
titres = ["Le Mystère", "La Nuit Sombre", "L'aventure Ultime", "Le Dernier Combat", "Voyage Interdit"]
genres = ["Roman", "Policier", "Fantasy", "Science-Fiction", "Drame"]

for i in range(25):
    aut = random.choice(auteurs_db)
    bk = BookDB(
        title=f"{random.choice(titres)} {i}",
        genre=random.choice(genres),
        year=random.randint(1950, 2024),
        author_id=aut.id
    )
    db.add(bk)

db.commit()
db.close()
print("✅ BIBLIOTHÈQUE PRÊTE !")
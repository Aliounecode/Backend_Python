import random
# ATTENTION : On importe depuis 'models' maintenant que tu as structuré ton projet
from models import SessionLocal, CategoryDB, ArticleDB, engine, Base

print("--- DÉBUT DU REMPLISSAGE ---")

# 1. On nettoie la base
print("1. Nettoyage de la base de données...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# --- DONNÉES DE TESTS (Hardcodées pour la cohérence) ---

# Listes d'images réelles (Unsplash) par thème
images_tech = [
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&q=80", # Circuit board
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500&q=80", # Matrix code
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=500&q=80", # Laptop code
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500&q=80", # Robot hand
    "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=500&q=80", # Laptop on desk
]

images_sport = [
    "https://images.unsplash.com/photo-1517649763962-0c623066013b?w=500&q=80", # Gym
    "https://images.unsplash.com/photo-1526676037777-05a232554f77?w=500&q=80", # Surfer
    "https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?w=500&q=80", # Running track
    "https://images.unsplash.com/photo-1562771379-e7170e5b918c?w=500&q=80", # Basketball
    "https://images.unsplash.com/photo-1574680096145-d05b47434a5a?w=500&q=80", # Weights
]

images_voyage = [
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500&q=80", # Beach tropical
    "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=500&q=80", # Mountains lake
    "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=500&q=80", # Paris Eiffel
    "https://images.unsplash.com/photo-1503220317375-aaad61436b1b?w=500&q=80", # Hiker
    "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=500&q=80", # Venice
]

# Titres associés
titres_tech = ["Processeur Quantique", "L'IA générative", "Nouveau Framework Web", "Cybersécurité 2024", "PC Gamer Ultime"]
titres_sport = ["Marathon de Paris", "Finale de la Ligue", "Comment débuter le Yoga", "Record du monde battu", "Nutrition sportive"]
titres_voyage = ["Week-end à Rome", "Les plages de Bali", "Randonnée dans les Alpes", "Safari au Kenya", "Découvrir le Japon"]

# 2. Création des Catégories et stockage des objets DB
print("2. Création des catégories...")
cat_tech = CategoryDB(name="Technologie")
cat_sport = CategoryDB(name="Sport")
cat_voyage = CategoryDB(name="Voyage")

db.add_all([cat_tech, cat_sport, cat_voyage])
db.commit()

# On prépare une liste de tuples (CategorieDB, liste_titres, liste_images)
categories_config = [
    (cat_tech, titres_tech, images_tech),
    (cat_sport, titres_sport, images_sport),
    (cat_voyage, titres_voyage, images_voyage),
]

# 3. Création des Articles en boucle
print("3. Génération des articles cohérents...")

counter = 1
# On boucle sur chaque catégorie configurée
for cat_db, titres, images in categories_config:
    # Pour chaque catégorie, on crée 5 articles
    for i in range(5):
        # Astuce : on utilise modulo (%) pour boucler sur les listes d'images et titres si elles sont courtes
        titre_choisi = titres[i % len(titres)]
        image_choisie = images[i % len(images)]
        
        article = ArticleDB(
            title=f"{titre_choisi}",
            content=f"Description détaillée pour l'article sur {titre_choisi}. " * 3,
            price=random.randint(49, 999),
            image_url=image_choisie, # ICI : l'image correspond au thème !
            category_id=cat_db.id
        )
        db.add(article)
        print(f" - Article {counter} créé ({cat_db.name}): {titre_choisi}")
        counter += 1

db.commit()
db.close()
print("--- ✅ SUCCÈS : Base remplie avec des données COHÉRENTES ! ---")
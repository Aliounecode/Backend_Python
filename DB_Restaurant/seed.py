import random
from models import SessionLocal, MenuDB, DishDB, engine, Base

print("Cuisine en cours...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 1. Création des Menus
menus_data = [
    ("Entrées", "Pour ouvrir l'appétit"),
    ("Burgers & Sandwichs", "Nos classiques américains"),
    ("Pizzas", "Au feu de bois"),
    ("Desserts", "La touche sucrée")
]

db_menus = []
for name, desc in menus_data:
    menu = MenuDB(name=name, description=desc)
    db.add(menu)
    db_menus.append(menu)
db.commit()

# 2. Création des Plats (Fake Data réaliste)
plats_entrees = ["Salade César", "Ailes de poulet", "Soupe à l'oignon"]
plats_burgers = ["Cheeseburger Royal", "Chicken Burger", "Veggie Burger"]
plats_pizzas = ["Margherita", "4 Fromages", "Reine"]
plats_desserts = ["Tiramisu", "Fondant Chocolat", "Glace Vanille"]

# Mapping pour les images (Unsplash)
images_food = [
    "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&q=80", # Burger
    "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=500&q=80", # Pizza
    "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=500&q=80", # Drink/Dessert
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500&q=80"  # Salade
]

print("Dressage des assiettes...")
for i in range(25):
    # On choisit un menu au hasard
    menu = random.choice(db_menus)
    
    # On choisit un nom selon le menu
    if "Entrées" in menu.name:
        nom = random.choice(plats_entrees)
    elif "Burgers" in menu.name:
        nom = random.choice(plats_burgers)
    elif "Pizzas" in menu.name:
        nom = random.choice(plats_pizzas)
    else:
        nom = random.choice(plats_desserts)

    dish = DishDB(
        name=f"{nom} Spécial #{i}",
        ingredients="Tomate, Salade, Oignon, Sauce maison",
        price=random.randint(10, 25) + 0.99, # Ex: 15.99
        is_spicy=random.choice([True, False]),
        image_url=random.choice(images_food),
        menu_id=menu.id
    )
    db.add(dish)

db.commit()
db.close()
print("✅ RESTAURANT PRÊT À SERVIR !")
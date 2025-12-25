# 🚀 Ultimate CRUD Starter Kit (FastAPI + Angular)

Ce projet est un modèle d'application **Fullstack** robuste et modulaire. Il démontre une architecture propre séparant la logique métier, les données et les routes, permettant de créer rapidement des applications de gestion (Blog, École, Hôpital, Bibliothèque, etc.).

## 🌟 Points Forts

- **Backend :** Python avec **FastAPI** (Rapide, Asynchrone).
- **Base de Données :** **SQLite** avec **SQLAlchemy** (ORM).
- **Frontend :** **Angular** (Dernière version) avec **Tailwind CSS** pour le design.
- **Architecture :** Separation of Concerns (Modèles, Schémas, CRUD, Routes).
- **Fonctionnalités :** Create, Read, Update, Delete (CRUD) complet.

---

## 📂 Architecture du Backend

Le code n'est pas jeté dans un seul fichier. Il suit une structure logique et maintenable :

```text
backend/
│
├── models.py    # 🗄️ TABLES : La structure de la Base de Données (SQLAlchemy)
├── schemas.py   # 🛡️ VALIDATION : Les contrats de données (Pydantic)
├── crud.py      # 🧠 LOGIQUE : Les fonctions pures (Create, Get, Update, Delete)
├── main.py      # 🚦 ROUTES : Les points d'entrée de l'API (Endpoints)
├── seed.py      # 🌱 DATA : Script pour remplir la base avec des fausses données
└── events.db    # (Généré automatiquement) Le fichier de base de données

```

---

## 🛠️ Prérequis

Assurez-vous d'avoir installé :

- [Python](https://www.python.org/) (3.8+)
- [Node.js](https://nodejs.org/) (pour Angular)
- [Angular CLI](https://angular.io/cli) (`npm install -g @angular/cli`)

---

## 🚀 Installation et Démarrage

### 1️⃣ Backend (API Python)

1. Ouvrez un terminal dans le dossier du backend.
2. (Optionnel) Créez un environnement virtuel :

```bash
python -m venv venv
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

```

1. Installez les dépendances :

```bash
pip install fastapi uvicorn sqlalchemy pydantic

```

1. Remplissez la base de données avec des données de test (Optionnel) :

```bash
python seed.py

```

1. Lancez le serveur :

```bash
python -m uvicorn main:app --reload

```

_L'API sera accessible sur : `http://localhost:8000_`*La documentation interactive (Swagger) :`http://localhost:8000/docs\*`

### 2️⃣ Frontend (Interface Angular)

1. Ouvrez un nouveau terminal dans le dossier du frontend.
2. Installez les dépendances :

```bash
npm install

```

1. Lancez l'application :

```bash
ng serve

```

1. Ouvrez votre navigateur sur : `http://localhost:4200`

---

## 📚 Fonctionnalités de l'API

L'application expose une API REST complète. Voici un exemple des endpoints disponibles (selon le kit utilisé) :

| Méthode  | Endpoint      | Description                  |
| -------- | ------------- | ---------------------------- |
| `GET`    | `/items/`     | Récupérer toute la liste     |
| `GET`    | `/items/{id}` | Récupérer un élément par ID  |
| `POST`   | `/items/`     | Créer un nouvel élément      |
| `PUT`    | `/items/{id}` | Modifier un élément existant |
| `DELETE` | `/items/{id}` | Supprimer un élément         |

_(Remplacez `/items/` par `/articles`, `/students`, `/patients` selon le contexte)._

---

## 🎨 Design (Frontend)

L'interface utilise **Tailwind CSS** (via CDN pour la légèreté).

- Pas d'installation complexe requise pour le CSS.
- Design responsive (Mobile / Desktop).
- Interface utilisateur claire avec modales et formulaires.

---

## 🔄 Adaptabilité

Ce projet a été conçu pour être **agnostique**. Il peut être transformé en quelques minutes pour gérer :

- 🏫 Une École (Classes / Étudiants)
- 🏥 Un Hôpital (Médecins / Patients)
- 🛒 Un Site E-commerce (Clients / Commandes)
- 📅 Une Gestion d'Événements (Events / Participants)

Il suffit de modifier les fichiers `models.py` et `schemas.py` pour adapter les données.

---

## 👤 Auteur

Projet réalisé dans le cadre d'un examen de Licence 3 / Projet personnel.
Alioune Badara Diop

---

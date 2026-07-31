# BiblioLivre

API Django REST Framework pour gérer des livres et des avis (avec notation et likes), authentification via JWT.

## Installation

```bash
cd biblioLivre
python -m venv .venv
source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Base de données

```bash
python manage.py migrate
```

Optionnel, pour accéder à l'admin Django (`/admin/`) :
```bash
python manage.py createsuperuser
```

## Lancer le serveur

```bash
python manage.py runserver
```

L'API est disponible sur `http://127.0.0.1:8000/`.

## Authentification (JWT)

- `POST /api/token/` avec `{"username": "...", "password": "..."}` → renvoie `access` + `refresh`
- `POST /api/token/refresh/` avec `{"refresh": "..."}` → renvoie un nouveau `access`

Utiliser le token dans les requêtes suivantes : header `Authorization: Bearer <access>`.

## Endpoints principaux

- `/api/livres/` — CRUD sur les livres
- `/api/avis/` — CRUD sur les avis
- `POST /api/avis/{id}/like/` — like/unlike un avis (toggle)

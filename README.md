# Devops Ecommerce Platform (Django)

Minimal Django ecommerce demo with basic product creation and browsing.

Quick start:

1. Create a virtualenv and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

3. Open http://127.0.0.1:8000/

## Docker

This project is now configured to run with a separate PostgreSQL database service.

Copy the example `.env` file and edit values before running.

```powershell
copy .env.example .env
```

Build and run the development container:

```powershell
docker compose up --build
```

For production-like deployment, use the production compose file:

```powershell
docker compose -f docker-compose.prod.yml up --build
```

The compose setup loads database and Django secrets from `.env`, and starts both the Django web app and a PostgreSQL database.

Then open:

```text
http://127.0.0.1:8000/
```

If you need to run the web container alone, the database settings use environment variables from `.env`.

The app still falls back to SQLite when `DATABASE_HOST` is not set.

To push to GitHub, create a repository and push following normal git workflow. If you want I can initialize git and push (you'll need to provide credentials or set up an SSH key).

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

To push to GitHub, create a repository and push following normal git workflow. If you want I can initialize git and push (you'll need to provide credentials or set up an SSH key).

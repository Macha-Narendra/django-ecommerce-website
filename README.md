# Devops Ecommerce Platform (Django)

Minimal Django ecommerce demo with basic product creation and browsing.

## Quick Setup

1. Create a virtualenv and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. **Generate a secure Django secret key:**

```powershell
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. Copy the example `.env` file and add your generated secret key:

```powershell
copy .env.example .env
# Edit .env and replace DJANGO_SECRET_KEY with the generated value
```

4. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

5. Open http://127.0.0.1:8000/

## Docker

This project is now configured to run with a separate PostgreSQL database service.

Copy the development or production example file and edit values before running.

For local development:

```powershell
copy .env.dev.example .env
```

For production-like deployment:

```powershell
copy .env.prod.example .env
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

## GitHub Actions

Two CI/CD workflows are configured:

### 1. Django CI (`.github/workflows/ci.yml`)
Runs on every push and pull request to `master`:
- Python setup
- Dependency install
- Django migrations
- System checks
- Tests
- Static file collection

No configuration needed — this runs automatically.

### 2. Docker Build & Push (`.github/workflows/docker-build-push.yml`)
Builds and pushes Docker image to AWS ECR on push to `main`.

**Setup required:**
1. Create an AWS IAM role for OIDC (or use an existing one).
2. In your GitHub repository, add these **Repository Variables** (not secrets):
   - `AWS_ROLE_ARN`: Your AWS IAM role ARN (e.g., `arn:aws:iam::123456789012:role/GitHubActionsRole`)
   - `AWS_REGION`: AWS region (e.g., `us-east-1`)
   - `ECR_REPOSITORY`: ECR repository name (e.g., `ecommerce-app`)

3. Ensure the IAM role has permissions for `ecr:*` on the target repository.

Once configured, pushing to `main` will:
- Build the Docker image
- Authenticate with AWS via OIDC
- Push to your ECR repository with tag = Git commit SHA

To push to GitHub, create a repository and push following normal git workflow. If you want I can initialize git and push (you'll need to provide credentials or set up an SSH key).

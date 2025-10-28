# AI DJ Backend (FastAPI + MariaDB)

Minimal, runnable scaffold for the AI DJ backend.

## Quickstart (Local)
```bash
# 1) Create and activate venv (optional)
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run dev server
uvicorn app.main:app --reload --port 8000
# Open http://localhost:8000/api/v1/healthz
```

## Docker Compose (DB/Redis/MinIO + Backend)
```bash
cp .env.example .env
docker compose up -d --build
# Open http://localhost:8000/api/v1/healthz
```

> NOTE: DB migrations (Alembic) are wired but initial models are simple.

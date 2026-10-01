# Backend — Product AI Assistant

FastAPI backend foundation (SQLAlchemy 2.x + PostgreSQL via `psycopg`).

## Setup (Windows PowerShell)

From repo root:

```powershell
py -3.13 -m venv backend/venv
backend\venv\Scripts\Activate.ps1
backend\venv\Scripts\python.exe -m pip install --upgrade pip
backend\venv\Scripts\pip.exe install -r backend\requirements.txt
```

## Run API

```powershell
cd backend
..\backend\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

Endpoints:

- `GET /` → `{"message": "Product AI Assistant API is running"}`
- `GET /health` → `{"status": "healthy"}`

## Tests

Tests do not require PostgreSQL.

```powershell
cd backend
..\venv\Scripts\pytest.exe -v
```

## Env

See `.env.example`:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5433/product_ai_assistant
```

Copy for local use (do not commit):

```powershell
Copy-Item backend\.env.example backend\.env
```

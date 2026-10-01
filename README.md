# Product AI Assistant

Initial backend foundation for the **Product AI Assistant** project.

## Project purpose

Starter foundation for a product-focused AI assistant backend.
This stage sets up only the base FastAPI service, SQLAlchemy 2.x database
foundation, environment configuration, and pytest verification — no chatbot,
LLM, RAG, embeddings, pgvector, document processing, auth/JWT, frontend,
Docker, or deployment yet. Those will be built later.

Current API:

- `GET /` → `{"message": "Product AI Assistant API is running"}`
- `GET /health` → `{"status": "healthy"}`

## Requirements

- Windows 10/11 with PowerShell 5.1+
- Git 2.x+
- Python **3.13.x** (project Python version)
- PostgreSQL connection string for runtime (tests do not require PostgreSQL)

Check versions:

```powershell
py -3.13 --version
py -3.13 -m pip --version
git --version
```

If Python 3.13 is missing, install it (winget example):

```powershell
winget install -e --id Python.Python.3.13 --silent --accept-package-agreements --accept-source-agreements
```

## Python version

This project uses **Python 3.13.x**.

The virtual environment must be created with Python 3.13:

```powershell
py -3.13 -m venv backend/venv
backend\venv\Scripts\python.exe --version
```

Expected: `Python 3.13.x`.

> Note: if `python --version` on your machine points to a different version
> (e.g. 3.14), always use `py -3.13` to create the venv and
> `backend\venv\Scripts\python.exe` afterwards.

## Virtual environment setup

From the repository root (`product-ai-assistant/`):

```powershell
py -3.13 -m venv backend/venv
```

Do NOT commit `backend/venv/`. It is ignored via root `.gitignore`
(`venv/`, `backend/venv/`, `.venv/`).

## Windows PowerShell activation

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
backend\venv\Scripts\Activate.ps1
python --version
# should show Python 3.13.x inside the venv
```

Deactivate:

```powershell
deactivate
```

Alternatively, without activating, call the venv Python directly:

```powershell
backend\venv\Scripts\python.exe --version
backend\venv\Scripts\pip.exe --version
```

## Dependency installation

Runtime:

- fastapi
- uvicorn[standard]
- sqlalchemy
- psycopg[binary]
- pydantic
- pydantic-settings
- python-dotenv

Testing:

- pytest
- httpx

Install (with venv activated, from `backend/` or root):

```powershell
backend\venv\Scripts\python.exe -m pip install --upgrade pip
backend\venv\Scripts\pip.exe install fastapi "uvicorn[standard]" sqlalchemy "psycopg[binary]" pydantic pydantic-settings python-dotenv pytest httpx
```

Or from pinned file:

```powershell
backend\venv\Scripts\pip.exe install -r backend\requirements.txt
```

Dependencies are recorded in `backend/requirements.txt` via `pip freeze`.
Do not add unnecessary packages.

## Running FastAPI

From `backend/` with venv activated:

```powershell
cd backend
..\backend\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```

Or without `cd`:

```powershell
backend\venv\Scripts\uvicorn.exe app.main:app --reload --port 8000 --app-dir backend
```

Verify:

- http://127.0.0.1:8000/ → `{"message": "Product AI Assistant API is running"}`
- http://127.0.0.1:8000/health → `{"status": "healthy"}`
- http://127.0.0.1:8000/docs (Swagger UI)

## Running tests

Tests do NOT require PostgreSQL. They use FastAPI `TestClient`.

From `backend/`:

```powershell
cd backend
..\venv\Scripts\Activate.ps1
pytest -v
```

Expected:

- `test_health` → `GET /health` returns HTTP 200 + `{"status": "healthy"}`
- `test_root` → `GET /` returns HTTP 200 + `{"message": "..."}`
- 2 passed

If running from repo root, set `PYTHONPATH`:

```powershell
$env:PYTHONPATH="backend"; backend\venv\Scripts\pytest.exe backend/tests -v
```

## Environment variables

Do NOT commit real credentials. Only `backend/.env.example` is tracked.

`backend/.env.example`:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5433/product_ai_assistant
```

Local setup:

```powershell
Copy-Item backend\.env.example backend\.env
# then edit backend\.env with your local values
```

`backend/.env` is ignored (`.env` in root `.gitignore`).

`backend/app/database.py`:

- SQLAlchemy 2.x (`DeclarativeBase`, `create_engine`, `sessionmaker`)
- Reads `DATABASE_URL` from environment (via `python-dotenv`)
- Exposes `Base`, `engine`, `SessionLocal`, `get_db`
- No hard-coded credentials
- No `Base.metadata.create_all()` yet
- Safe to import without `DATABASE_URL` set (engine is `None`, `get_db` raises `RuntimeError` if used)

## Project structure

```text
product-ai-assistant/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   └── __init__.py
│   │   ├── routers/
│   │   │   └── __init__.py
│   │   ├── services/
│   │   │   └── __init__.py
│   │   └── repositories/
│   │       └── __init__.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_health.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
├── docs/
│   └── .gitkeep
├── .gitignore
└── README.md
```

## Office PC ↔ laptop Git workflow

Both machines clone the same GitHub repo. Never commit `venv/` or `.env`.

On first machine (e.g. office PC):

```powershell
git status
git add .gitignore README.md backend docs
git commit -m "chore: initial backend foundation"
git push -u origin main
```

On second machine (e.g. laptop):

```powershell
git clone <repo-url>
cd product-ai-assistant
py -3.13 -m venv backend/venv
backend\venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
Copy-Item backend\.env.example backend\.env
pytest backend/tests -v  # or: cd backend; pytest -v
```

Daily sync:

```powershell
# before work
git pull

# after work (from repo root)
git status
git add -A
git commit -m "describe your change"
git push
```

If the other machine has changes:

```powershell
git pull --rebase
# resolve conflicts if any, then:
git push
```

Verify before pushing:

```powershell
backend\venv\Scripts\python.exe --version
backend\venv\Scripts\pytest.exe backend/tests -v
git status --short
git check-ignore -v backend/venv backend/.env
```

## Scope (not built yet)

- chatbot
- LLM
- RAG
- embeddings
- pgvector
- document processing
- authentication/JWT
- frontend
- Docker
- deployment

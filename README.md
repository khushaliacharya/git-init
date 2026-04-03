# git-init
# FocusFlow
A minimalist task + Pomodoro session tracker with session history and productivity stats.

## Stack
- **Backend:** Python 3.11+, Flask 3.x, SQLAlchemy 2.0, Pydantic v2, Flask-CORS, SQLite
- **Frontend:** React 18, Vite, Axios
- **Database:** SQLite (dev), PostgreSQL-ready via SQLAlchemy dialect swap

## Key Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Flask over FastAPI | Explicit routing, mature ecosystem, easier AI scaffolding for small REST APIs |
| SQLAlchemy 2.0 | Declarative models, 100% sync/async ready, seamless PostgreSQL migration |
| Pydantic for Validation | Strict request typing, clear error messages, reduces boilerplate |
| No Auth in v1 | Keeps scope focused on core CRUD + session tracking; JWT can be layered later |
| React + Vite | Fast HMR, modern build pipeline, minimal config |

## Setup & Run
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py  # Runs on http://localhost:5000

# Frontend
cd frontend
npm install
npm run dev  # Runs on http://localhost:5173

# Python/Flask
- Use Flask application factory pattern
- SQLAlchemy 2.0 syntax: `db.select()`, `session.execute()`, or declarative models with `db.Column`
- Validation: Pydantic v2, reject malformed payloads early
- Error handling: Return 400/404/500 with JSON error object

# React
- Vite + React 18, functional components
- State: `useState`/`useEffect` for API calls (upgrade to React Query later)
- Styling: Inline/Tailwind acceptable, keep it minimal
- API calls: Centralized in `src/api.js` with Axios instance

# Git/Commits
- Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Max 100 char line length in code

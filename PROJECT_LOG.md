# Project Log

## 2026-02-20
- Created initial plan for the de-identification web app.
- Added `.gitignore` and `README.md`.
- Created Python virtual environment at `.venv`.
- Added frontend (Vue + Vite) scaffold and UI shell.
- Added backend (Flask + pydicom) with `/api/deidentify` and `/api/health`.
- Added Dockerfiles, nginx config, and docker-compose for deployment.
- Added HTTPS dev setup with self-signed cert script and compose override.
- Switched backend Docker runtime to Gunicorn for production.
- Added `VITE_API_BASE` support for frontend API calls (Render static site).
- Adjusted frontend nginx config: default no `/api` proxy for Render; local compose uses `nginx.local.conf`.
- Frontend Docker build now accepts `VITE_API_BASE` at build time.
- Documented Render deployment behavior and build cache requirements.

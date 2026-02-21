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

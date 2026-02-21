# DICOM Anonymizer

Lightweight web app to de-identify medical images by blanking patient-identifying DICOM tags (personal info tags only, for now). No image data is stored in any database. Output filenames match input filenames.

## Stack (Planned)
- Backend: Flask
- Frontend: Vue

## Project Notes
- De-identification blanks patient-identifying tags (set empty).
- Supports both 2D and 3D DICOM series.
- Stateless and scalable.

## Setup (Planned)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Run (Local)
Backend:
```bash
pip install -r backend/requirements.txt
python backend/run.py
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## Docker (Deployment Ready)
Build and run with Docker Compose:
```bash
docker compose up --build
```

Frontend will be available at `http://localhost:8080` and backend at `http://localhost:5000`.

Render note: the backend and frontend `Dockerfile` files assume the build context is the repo root.
For Render, the frontend uses `frontend/nginx.conf` without an `/api` proxy. Set `VITE_API_BASE` to your backend URL.

## Production
The backend Docker image runs with `gunicorn` (WSGI) for production deployment.

## Render Frontend Config
If deploying the frontend as a Static Site on Render, set an environment variable:
```
VITE_API_BASE=https://your-backend.onrender.com
```
This is used by the frontend to call the backend API.
If deploying the frontend as a Docker Web Service, set the same variable as a build-time env var and redeploy (the Dockerfile uses `ARG VITE_API_BASE` for the build).

## HTTPS (Local Dev, No Domain)
Generate a self-signed cert and run the HTTPS compose override:
```bash
./scripts/generate-dev-cert.sh
docker compose -f docker-compose.yml -f docker-compose.https.yml up --build
```

Then open `https://localhost:8443`. Your browser will warn about the self-signed cert.

## Files
- `PLAN.md` high-level plan
- `DISCUSSION_SUMMARY.md` running summary of decisions
- `PROJECT_LOG.md` change log / activity log

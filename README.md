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

Render note: the backend `Dockerfile` assumes the build context is the repo root.

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

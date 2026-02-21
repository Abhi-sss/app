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

## Files
- `PLAN.md` high-level plan
- `DISCUSSION_SUMMARY.md` running summary of decisions
- `PROJECT_LOG.md` change log / activity log

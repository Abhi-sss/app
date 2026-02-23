# Handoff Notes (Resume Here)

## Project Name
DICOM Anonymizer

## Stack
- Backend: Flask + pydicom
- Frontend: Vue 3 + Vite
- Deployment: Docker + Render

## Key Requirements
- De-identify DICOM by blanking personal-info tags.
- Remove hospital/center tags (InstitutionName, InstitutionalDepartmentName, etc.).
- Remove specific date-time tags: StudyDate, SeriesDate, ContentDate, AcquisitionDateTime.
- Output filename matches input.
- No DB storage.

## Deployment Status
- Backend deployed on Render at: https://app-backend-w6ey.onrender.com
- Backend runs Gunicorn and listens on `$PORT` (Render uses 10000).
- Frontend deployed as **Render Web Service** (Docker). Build-time `VITE_API_BASE` is required.
- Frontend Nginx config for Render does **not** proxy `/api`.
- Local Docker uses `frontend/nginx.local.conf` to proxy `/api` to backend.

## Frontend Configuration
- Set `VITE_API_BASE=https://app-backend-w6ey.onrender.com` in Render frontend service.
- Must **Clear build cache & deploy** so Vite bakes the value into the build.

## Recent Fixes
- Added upload progress and file name list in UI (XHR upload progress).
- Improved download filename fallback when `Content-Disposition` is missing.

## Files to Know
- Backend: `backend/app/deid.py`, `backend/app/routes.py`, `backend/Dockerfile`
- Frontend: `frontend/src/App.vue`, `frontend/src/style.css`, `frontend/Dockerfile`
- Nginx configs: `frontend/nginx.conf` (Render), `frontend/nginx.local.conf` (local)
- Compose: `docker-compose.yml`, `docker-compose.https.yml`

## Open Items / Next Steps
- Verify frontend requests hit backend after build-cache clear.
- Add security hardening (HTTPS, size limits, log redaction) when ready.

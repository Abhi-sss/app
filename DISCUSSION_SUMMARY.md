# Discussion Summary

## Scope and Requirements
- Build a lightweight, scalable web app to de-identify medical images.
- Focus on DICOM tags for both 2D and 3D modalities.
- Do not store images in any database due to clinical compliance and privacy.
- Prefer Flask backend and Vue frontend.
- De-identification should blank patient-identifying (personal info) tags by setting them empty.
- Output filename should match input filename.
- Later phase: allow users to choose which DICOM tags to de-identify.
- Project name selected: DICOM Anonymizer.

## Current Status
- Plan created in `PLAN.md`.
- Virtual environment created at `.venv`.
- Frontend scaffold created in `frontend/` (Vue + Vite).
- Backend scaffold created in `backend/` (Flask + pydicom) with `/api/deidentify` and `/api/health`.
- De-identification now blanks patient personal info tags plus hospital/center related tags.
- Specific date-time tags requested removed: StudyDate, SeriesDate, ContentDate, AcquisitionDateTime.
- Security hardening discussion deferred for later.

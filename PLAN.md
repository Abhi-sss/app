# Plan: Medical Image De‑Identification Web App

## Goal
Build a lightweight, scalable web app to de‑identify medical images by removing/overwriting DICOM tags (and other metadata) for both 2D and 3D modalities, without storing images in any database. Prefer Flask backend and Vue frontend with a simple interactive UI.
De‑identification should blank (set empty) patient‑identifying tags, and the output file name should match the input file name.

## Assumptions
- Images are provided by users at request time (upload) and are not persisted server‑side.
- Temporary in‑memory processing is acceptable; if temporary disk is required, it will be ephemeral and deleted immediately after processing.
- Primary focus is DICOM; non‑DICOM images can be either rejected or handled with a minimal path.
- The app will run in a controlled environment (e.g., containerized) where storage and logs are governed by compliance policies.

## Non‑Goals (initial phase)
- Long‑term storage, PACS integration, or complex routing workflows.
- User authentication/authorization (can be added later).
- Full HIPAA compliance certification (architecture will be designed to support it).

## Architecture Overview
- Frontend: Vue SPA for upload, progress, and download.
- Backend: Flask API for upload/de‑identify/download.
- Processing: Use a DICOM library (e.g., `pydicom`) to strip or replace tags.
- Storage: No DB; use streaming responses or short‑lived in‑memory/ephemeral files only.
- Scaling: Stateless backend; compatible with horizontal scaling behind a load balancer.

## Milestones
1. Requirements and compliance checklist
2. API and UI design
3. Backend DICOM de‑identification pipeline
4. Frontend upload/download workflow
5. Operational hardening (logging, observability, security)

## Detailed Tasks

### 1) Requirements & Compliance
- Define required DICOM tags to remove by setting them empty (use a de‑identification profile as baseline).
- Decide whether pixel data should be preserved or anonymized (e.g., remove burned‑in annotations).
- Document data handling rules: no persistence, log redaction, request size limits.
- Ensure output file naming preserves the original filename.

### 2) API Design
- Endpoints:
  - `POST /api/deidentify` accepts DICOM file(s) and returns de‑identified file(s).
  - `GET /api/health` for readiness.
- Response options:
  - Immediate response with processed file.
  - Optional zip for multi‑file series.
- Define errors for unsupported modalities, invalid DICOM, or size limits.

### 3) Backend (Flask)
- Implement DICOM parsing and tag blanking for patient‑identifying fields.
- Support both single file and multi‑file series (3D volumes).
- Use streaming responses to avoid disk use when feasible.
- Ensure ephemeral temp files are securely deleted if used.
- Provide unit tests for tag removal and file integrity.

### 4) Frontend (Vue)
- Simple UI:
  - File/series upload
  - Progress indicator
  - Download button
  - Status/error messaging
- Validate file type/size client‑side before upload.
- Minimal styling, responsive layout.

### 5) Scalability & Security
- Stateless service, scale out with multiple replicas.
- Input size limits and rate limiting.
- Audit logs without PHI/PII.
- Secure headers and CORS policy.

### 6) Deployment
- Containerize with a small base image.
- Configure runtime environment variables for size limits and tag policies.
- Provide sample docker‑compose for local dev.

## Open Questions
- Which de‑identification profile to follow (e.g., DICOM PS3.15 Basic Profile), noting that for now we will stick to personal‑info tags only?
- Should the app handle burned‑in pixel text redaction?
- Max file/series size constraints?
- Will authentication be required?
- In later phases, should users be allowed to choose custom tag sets for de‑identification?

## Deliverables
- Flask backend with de‑identification pipeline
- Vue frontend for upload/download
- Documentation for usage and compliance considerations
- Tests for core de‑identification logic

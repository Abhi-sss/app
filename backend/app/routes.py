from io import BytesIO
import zipfile
from flask import Blueprint, jsonify, request, send_file

from .deid import deidentify_dicom_bytes

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/health")
def health():
    return jsonify({"status": "ok"})


@api.post("/deidentify")
def deidentify():
    if "files" not in request.files:
        return jsonify({"error": "No files uploaded"}), 400

    files = request.files.getlist("files")
    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    if len(files) == 1:
        file_obj = files[0]
        filename = file_obj.filename or "deidentified.dcm"
        output_bytes = deidentify_dicom_bytes(file_obj.read())
        return send_file(
            BytesIO(output_bytes),
            as_attachment=True,
            download_name=filename,
            mimetype="application/dicom",
        )

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_obj in files:
            filename = file_obj.filename or "deidentified.dcm"
            output_bytes = deidentify_dicom_bytes(file_obj.read())
            zf.writestr(filename, output_bytes)

    zip_buffer.seek(0)
    return send_file(
        zip_buffer,
        as_attachment=True,
        download_name="deidentified.zip",
        mimetype="application/zip",
    )

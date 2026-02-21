from io import BytesIO
import pydicom

# Personal-information tags only (initial phase). Future phases can extend this.
PERSONAL_INFO_TAGS = [
    "PatientName",
    "PatientID",
    "IssuerOfPatientID",
    "PatientBirthDate",
    "PatientBirthTime",
    "PatientSex",
    "PatientAge",
    "PatientSize",
    "PatientWeight",
    "PatientAddress",
    "PatientTelephoneNumbers",
    "PatientMotherBirthName",
    "OtherPatientIDs",
    "OtherPatientNames",
    "PatientComments",
    "ResponsiblePerson",
    "ResponsiblePersonRole",
    "ResponsibleOrganization",
    "PatientReligiousPreference",
    "PatientInsurancePlanCodeSequence",
    "MedicalRecordLocator",
    "Occupation",
    "AdditionalPatientHistory",
    # Facility / institution identifiers
    "InstitutionName",
    "InstitutionAddress",
    "InstitutionalDepartmentName",
    "StationName",
    "PerformingPhysicianName",
    "ReferringPhysicianName",
    "PhysiciansOfRecord",
    "OperatorsName",
    "PerformingPhysicianIdentificationSequence",
    "ReferringPhysicianIdentificationSequence",
    # Date-time fields requested to be removed
    "StudyDate",
    "SeriesDate",
    "ContentDate",
    "AcquisitionDateTime",
]


def deidentify_dicom_bytes(data: bytes) -> bytes:
    dataset = pydicom.dcmread(BytesIO(data), force=True)

    for keyword in PERSONAL_INFO_TAGS:
        if keyword in dataset:
            element = dataset.data_element(keyword)
            if element.VR == "SQ":
                element.value = []
            else:
                element.value = ""

    output = BytesIO()
    dataset.save_as(output, write_like_original=False)
    return output.getvalue()

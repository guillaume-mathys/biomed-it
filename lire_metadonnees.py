from pathlib import Path
import pydicom

dossier = Path.home() / "dicom-test"

for fichier in dossier.rglob("*.dcm"):
    ds = pydicom.dcmread(fichier, stop_before_pixels=True)
    print("Fichier :", fichier.name)
    print("  Patient :", ds.get("PatientID", "inconnu"))
    print("  Modalité :", ds.get("Modality", "inconnue"))
    print("  Date :", ds.get("StudyDate", "inconnue"))
    print("  Description :", ds.get("StudyDescription", "aucune"))
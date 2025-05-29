import os
import subprocess
from pathlib import Path
from google.cloud import storage

# Paramètres GCS (peuvent venir d’une variable d’environnement)
BUCKET_NAME = os.environ.get("BUCKET_NAME", "us-east1-paris-opendata-com-baec303d-bucket")

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

def convert_and_upload_notebooks(base_dir):
    base_path = Path(base_dir)

    for ipynb_path in base_path.rglob("*.ipynb"):
        relative_path = ipynb_path.relative_to(".")  # Garde le chemin complet relatif
        py_local_path = Path("data/scripts") / relative_path.with_suffix(".py")
        ipynb_bucket_path = Path("data/traitements") / relative_path
        py_bucket_path = Path("data/scripts") / relative_path.with_suffix(".py")

        # Créer les dossiers de destination localement
        py_local_path.parent.mkdir(parents=True, exist_ok=True)

        # Convertir le notebook
        subprocess.run([
            "jupyter", "nbconvert", "--to", "script",
            str(ipynb_path),
            "--output", py_local_path.stem,
            "--output-dir", str(py_local_path.parent)
        ], check=True)

        # Upload de l’original
        bucket.blob(str(ipynb_bucket_path)).upload_from_filename(ipynb_path)

        # Upload du script converti
        if not py_local_path.exists():
            raise FileNotFoundError(f"Fichier converti introuvable : {py_local_path}")
        bucket.blob(str(py_bucket_path)).upload_from_filename(py_local_path)

def upload_dags():
    for dag_file in Path("workflow").rglob("*.py"):
        bucket_path = f"dags/{dag_file.name}"
        bucket.blob(bucket_path).upload_from_filename(dag_file)

if __name__ == "__main__":
    # Appliquer la logique à tous les dossiers nécessaires
    for folder in ["Workspace"]:
        if Path(folder).exists():
            convert_and_upload_notebooks(folder)

    upload_dags()
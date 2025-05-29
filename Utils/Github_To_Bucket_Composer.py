import os
import subprocess
from pathlib import Path
from google.cloud import storage
import shutil

# Paramètres GCS (peuvent venir d’une variable d’environnement)
BUCKET_NAME = os.environ.get("BUCKET_NAME", "us-east1-paris-opendata-com-baec303d-bucket")

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

def rename_and_upload_notebooks(base_dir):
    base_path = Path(base_dir)

    for ipynb_path in base_path.rglob("*.ipynb"):
        relative_path = ipynb_path.relative_to(".")
        py_local_path = Path("data/scripts") / relative_path.with_suffix(".py")
        ipynb_bucket_path = Path("data/traitements") / relative_path
        py_bucket_path = Path("data/scripts") / relative_path.with_suffix(".py")

        # Créer les dossiers localement
        py_local_path.parent.mkdir(parents=True, exist_ok=True)

        # Copier/renommer simplement le fichier .ipynb en .py (pas de conversion réelle)
        shutil.copy(ipynb_path, py_local_path)

        # Upload de l’original .ipynb
        bucket.blob(str(ipynb_bucket_path)).upload_from_filename(ipynb_path)

        # Upload de la copie renommée .py
        bucket.blob(str(py_bucket_path)).upload_from_filename(py_local_path)

def upload_dags():
    for dag_file in Path("Workflow").rglob("*.py"):
        bucket_path = f"dags/{dag_file.name}"
        bucket.blob(bucket_path).upload_from_filename(dag_file)

if __name__ == "__main__":
    for folder in ["Workspace", "Notebooks", "AutresDossiers"]:
        if Path(folder).exists():
            rename_and_upload_notebooks(folder)

    upload_dags()
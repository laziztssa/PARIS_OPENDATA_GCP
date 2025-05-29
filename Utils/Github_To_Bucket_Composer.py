import os
import subprocess
from pathlib import Path
from google.cloud import storage

# Paramètres GCS (peuvent venir d’une variable d’environnement)
BUCKET_NAME = os.environ.get("BUCKET_NAME", "us-east1-paris-opendata-com-baec303d-bucket")

# Répertoires
BASE_DATA_DIR = "Workspace"
SCRIPTS_SUBDIR = "data/scripts"
TRAITS_SUBDIR = "data/traitements"
DAGS_SRC_DIR = "Workflow"
DAGS_DST_DIR = "dags"

def convert_ipynb_to_py_and_upload():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    # Recherche tous les notebooks dans data/**/
    for ipynb_path in Path(BASE_DATA_DIR).rglob("*.ipynb"):
        relative_path = ipynb_path.relative_to(BASE_DATA_DIR)
        py_path = Path(SCRIPTS_SUBDIR) / relative_path.with_suffix(".py")
        trait_path = Path(TRAITS_SUBDIR) / relative_path

        # Créer les dossiers localement
        py_path.parent.mkdir(parents=True, exist_ok=True)
        trait_path.parent.mkdir(parents=True, exist_ok=True)

        # Copier .ipynb → traitement local
        trait_path.write_bytes(ipynb_path.read_bytes())

        # Convertir .ipynb → .py
        subprocess.run([
            "jupyter", "nbconvert", "--to", "script",
            str(ipynb_path),
            "--output", str(py_path.with_suffix(""))  # output sans .py
        ], check=True)

        # Upload .ipynb vers GCS
        bucket.blob(f"{TRAITS_SUBDIR}/{relative_path.as_posix()}").upload_from_filename(ipynb_path)

        # Upload .py vers GCS
        bucket.blob(f"{SCRIPTS_SUBDIR}/{relative_path.with_suffix('.py').as_posix()}").upload_from_filename(py_path)

def upload_dags():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    for dag_file in Path(DAGS_SRC_DIR).rglob("*.py"):
        blob_path = f"{DAGS_DST_DIR}/{dag_file.name}"
        print(f"Uploading DAG: {dag_file} → {blob_path}")
        bucket.blob(blob_path).upload_from_filename(dag_file)

if __name__ == "__main__":
    convert_ipynb_to_py_and_upload()
    upload_dags()

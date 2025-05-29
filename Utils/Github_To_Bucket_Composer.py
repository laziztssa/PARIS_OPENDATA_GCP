import os
import subprocess
from pathlib import Path
from google.cloud import storage

# Paramètres GCS (peuvent venir d’une variable d’environnement)
BUCKET_NAME = os.environ.get("BUCKET_NAME", "us-east1-paris-opendata-com-baec303d-bucket")

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

def clean_notebook_script(file_path):
    """
    Supprime les lignes magiques Jupyter d’un fichier .py converti.
    """
    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "get_ipython()" in line or line.strip().startswith("%"):
                continue
            lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def convert_and_upload_notebooks(base_dir):
    base_path = Path(base_dir)

    for ipynb_path in base_path.rglob("*.ipynb"):
        relative_path = ipynb_path.relative_to(".")
        py_local_path = Path("data/scripts") / relative_path.with_suffix(".py")
        ipynb_bucket_path = Path("data/traitements") / relative_path
        py_bucket_path = Path("data/scripts") / relative_path.with_suffix(".py")

        py_local_path.parent.mkdir(parents=True, exist_ok=True)

        # Convertir le notebook
        subprocess.run([
            "jupyter", "nbconvert", "--to", "script",
            str(ipynb_path),
            "--output", py_local_path.stem,
            "--output-dir", str(py_local_path.parent)
        ], check=True)

        # Nettoyer le .py généré
        clean_notebook_script(py_local_path)

        # Upload de l’original (.ipynb)
        bucket.blob(str(ipynb_bucket_path)).upload_from_filename(ipynb_path)

        # Upload du .py nettoyé
        if not py_local_path.exists():
            raise FileNotFoundError(f"Fichier converti introuvable : {py_local_path}")
        bucket.blob(str(py_bucket_path)).upload_from_filename(py_local_path)

def upload_dags():
    for dag_file in Path("workflow").rglob("*.py"):
        bucket_path = f"dags/{dag_file.name}"
        bucket.blob(bucket_path).upload_from_filename(dag_file)

if __name__ == "__main__":
    for folder in ["Workspace", "Notebooks", "AutresDossiers"]:
        if Path(folder).exists():
            convert_and_upload_notebooks(folder)

    upload_dags()
# import all modules
import airflow
from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocSubmitJobOperator,
)

# define the variables
PROJECT_ID = "paris-opendata-gcp"
REGION = "us-east1"
CLUSTER_NAME = "paris-opendata-cluster"
COMPOSER_BUCKET = "us-east1-paris-opendata-com-baec303d-bucket" ## change this 


GCS_JOB_FILE_1 = f"gs://{COMPOSER_BUCKET}/data/Workspace/Velib/Bronze_Velib_Emplacement_Stations_CSV.ipynb"
JOB_1 = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "job": {"main_python_file_uri": GCS_JOB_FILE_1},
}


GCS_JOB_FILE_2 = f"gs://{COMPOSER_BUCKET}/data/Workspace/Velib/Silver_Velib_Emplacement_Stations.ipynb"
JOB_2 = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "job": {"main_python_file_uri": GCS_JOB_FILE_2},
}




GCS_JOB_FILE_3 = f"gs://{COMPOSER_BUCKET}/data/Workspace/Velib/Graphique_Emplacement_Station.ipynb"
JOB_3 = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "job": {"main_python_file_uri": GCS_JOB_FILE_3},
}




ARGS = {
    "owner": "Laziz TESSA",
    "start_date": None,
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": ["***@gmail.com"],
    "email_on_success": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# define the dag
with DAG(
    dag_id="Velib_Ingestion_dag",
    schedule_interval=None,
    description=" run Pyspark and Pandas jobs",
    default_args=ARGS,
    tags=["pyspark", "dataproc", "etl", "marvel"]
) as dag:
    
   

    task_1 = DataprocSubmitJobOperator(
        task_id="Bronze_Velib_Station", 
        job=JOB_1, 
        region=REGION, 
        project_id=PROJECT_ID
    )

    task_2 = DataprocSubmitJobOperator(
        task_id="Silver_Velib_Station", 
        job=JOB_2, 
        region=REGION, 
        project_id=PROJECT_ID
    )

    task_3 = DataprocSubmitJobOperator(
        task_id="Graphique_Velib", 
        job=JOB_3, 
        region=REGION, 
        project_id=PROJECT_ID
    )

    
# define the task dependencies
task_1 >> task_2 >> task_3
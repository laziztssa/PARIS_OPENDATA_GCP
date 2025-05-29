{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "87e3205f-07c3-4d5a-88e3-42ba460256c0",
   "metadata": {},
   "source": [
    "#### Importation des Bibliotheques"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9069293f-3a31-47b2-ad5a-e723c82b9700",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "from google.cloud import bigquery\n",
    "from pandas_gbq import to_gbq"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6adf6baa-1038-42e8-ae53-b8ffde42d0ae",
   "metadata": {},
   "source": [
    "#### Reccuepration des parametres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a0866b36-7526-4486-a59a-5bc4e630b44f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "os.chdir(\"/PARIS_OPENDATA_GCP/Workspace/Velib\")\n",
    "\n",
    "%run ../Commun/Params.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "33e94a5f-e9e6-41b8-bdb7-352556f6c1da",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'BQ_BRONZE_DATASET': 'paris-opendata-gcp.bronze', 'BQ_GLOD_DATASET': 'paris-opendata-gcp.gold', 'BQ_SILVER_DATASET': 'paris-opendata-gcp.silver', 'BUCKET_NAME': 'paris-opendata-gcp-data', 'REGION': 'region', 'TEMP_GCS_BUCKET': 'paris-opendata-gcp-data/temporary', 'URL_API_VELIB': 'https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilites-en-temps-reel&q=&rows=10000&facet=contract_name&facet=station_state&facet=banking&facet=bonus&facet=last_update'}\n"
     ]
    }
   ],
   "source": [
    "print(parametres)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "072cf483-75e4-4b8b-8dc5-74eec294352f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "BQ_BRONZE_DATASET =  parametres[\"BQ_BRONZE_DATASET\"]\n",
    "TEMP_GCS_BUCKET = parametres[\"TEMP_GCS_BUCKET\"]\n",
    "BUCKET_NAME = parametres[\"BUCKET_NAME\"]\n",
    "BQ_BRONZE_TABLE = f\"{BQ_BRONZE_DATASET}.velib_emplacement_stations\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "600880e8-be6f-4516-bb52-10a5a967b37d",
   "metadata": {},
   "source": [
    "##### Lecture du fichier csv Velib emplacement des stations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "14bbff23-e318-466a-b580-5c1c01942c72",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "station_velib_df = pd.read_csv(f\"gs://{BUCKET_NAME}/landing/opendata_velib/raw/velib-emplacement-des-stations.csv\", header=0, delimiter=\";\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1202451b-8bb4-40b6-96ee-15c2236c4cec",
   "metadata": {
    "tags": []
   },
   "source": [
    "#### Charegement de la table Bronze"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7dbcd0df-936f-4a2a-bc04-b77a2b5c052e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 1/1 [00:00<00:00, 4262.50it/s]\n"
     ]
    }
   ],
   "source": [
    "to_gbq(\n",
    "    dataframe=station_velib_df,\n",
    "    destination_table=f\"{BQ_BRONZE_TABLE}\",\n",
    "    if_exists=\"replace\"\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PySpark",
   "language": "python",
   "name": "pyspark"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

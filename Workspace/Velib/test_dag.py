import pandas as pd
import os
from google.cloud import bigquery
from pandas_gbq import to_gbq, read_gbq
import unidecode
from datetime import datetime

print("Starting data processing...")


BQ_BRONZE_DATASET =  "paris-opendata-gcp.bronze"
SILVER_BRONZE_DATASET =  "paris-opendata-gcp.silver"
TEMP_GCS_BUCKET = "paris-opendata-gcp-data/temporary"
BUCKET_NAME = "paris-opendata-gcp-data"
BQ_BRONZE_TABLE = f"{BQ_BRONZE_DATASET}.velib_emplacement_stations"
BQ_SILVER_TABLE = f"{SILVER_BRONZE_DATASET}.velib_emplacement_stations"

print("Parametres declarés :")



bronze_station_velib_df = pd.read_gbq(BQ_BRONZE_TABLE)
print("Data loaded from BigQuery Bronze table.")


bronze_station_velib_df[["Longitude", "Latitude"]] = bronze_station_velib_df["Coordonnées géographiques"].str.split(",", expand=True).astype(float)

print("Longitude and Latitude columns created.")



drop_geo_df = bronze_station_velib_df.drop("Coordonnées géographiques", axis =1)
df_final = drop_geo_df.copy()

print("Dropped 'Coordonnées géographiques' column.")


df_final.columns = [unidecode.unidecode(cols).replace(" ","_").lower() for cols in drop_geo_df.columns]
print("Column names normalized.")

#rajouts de timepstamps de chargement
df_final["ts_Chargement"] = datetime.now()
print("Timestamp of loading added.")


to_gbq(
    dataframe=df_final,
    destination_table=f"{BQ_SILVER_TABLE}",
    if_exists="replace"
)
print("Data written to BigQuery Silver table.")
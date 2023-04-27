import os
from prefect import task, flow

from tasks import convert_to_parquet, parquet_to_postgres


@task
def download_gp_dataset():
    dowload_path = "https://github.com/gauthamp10/Google-Playstore-Dataset.git"
    os.system(f"git clone {dowload_path}")

@task
def convert_csv_to_parquet():
    convert_to_parquet.convert_to_parquet() 

@task
def load_parquet_to_postgres():
    parquet_to_postgres.parquet_to_postgres()

@task
def run_dbt_transformations():
    os.system("dbt run --profiles-dir /dbt/profiles")

@task
def setup_metabase():
    # Set up your Metabase configuration here
    pass

@flow
def data_pipeline():
    download_gp_dataset()
    convert_csv_to_parquet()
    load_parquet_to_postgres()
    run_dbt_transformations()

if __name__ == "__main__":
    data_pipeline()
import os
import pandas as pd
import psycopg2
from prefect import task, Flow
from prefect.engine.results import LocalResult
from prefect.tasks.shell import ShellTask

from data.download_dataset import download_dataset

@task
def download_kaggle_data():
   download_dataset()

@task
def convert_csv_to_parquet():
    # Read the CSV dataset
    data = pd.read_csv("./data/dataset.csv")

    # Convert the CSV dataset to Parquet format
    data.to_parquet("./parquet/dataset.parquet")

@task
def load_parquet_to_postgres():
    # Read the Parquet dataset
    data = pd.read_parquet("./parquet/dataset.parquet")

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="postgres",
        dbname="mydb",
        user="myuser",
        password="mypassword",
    )

    # Insert the data into the PostgreSQL database
    data.to_sql("mytable", conn, if_exists="replace", index=False)

    # Close the connection
    conn.close()

@task
def run_dbt_transformations():
    shell_task = ShellTask()
    return shell_task.run("dbt run --profiles-dir /dbt/profiles")

@task
def setup_metabase():
    # Set up your Metabase configuration here
    pass

with Flow("kaggle-data-pipeline") as flow:
    download_task = download_kaggle_data()
    convert_task = convert_csv_to_parquet(upstream_tasks=[download_task])
    load_task = load_parquet_to_postgres(upstream_tasks=[convert_task])
    dbt_task = run_dbt
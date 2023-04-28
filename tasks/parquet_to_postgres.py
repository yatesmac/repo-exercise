import pandas as pd
from sqlalchemy import create_engine


def parquet_to_postgres():
    # Set the path to the Parquet file
    parquet_file = "dataset.parquet"

    # Set the database connection details
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_port = 5432
    db_name = "gpdata"

    # Create a SQLAlchemy engine for connecting to the Postgres database
    engine = create_engine(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    # Load the Parquet file into a Pandas DataFrame
    df = pd.read_parquet(parquet_file)

    # Write the DataFrame to the Postgres database
    df.to_sql("gpappdata", engine, if_exists="replace", index=False)

    print("Done")


if __name__ == "__main__":
    parquet_to_postgres()

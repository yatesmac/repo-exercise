# Google Play Store Data Engineering Python Project

This project ingests the Google Play Store dataset (from [kaggle](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps) or [github](https://github.com/gauthamp10/Google-Playstore-Dataset)) and converts it to parquet format. The parquet file is then loaded into a Postgres database. The data in the database is transformed using dbt. The cleaned data is then used in Metabase to create a dashboard. The Postgres, dbt, and Metabase all run in Docker containers. The entire process is orchestrated using Prefect, which also runs from a Docker container.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Python 3.x

### Installing

1. Clone the repository
```
git clone https://github.com/yatesmac/repo-exercise.git
```

2. Install dependancies and set up containers
```
python3 -m setup.py
```

3. Running the Pipeline
```
prefect run flow --file main.py
```
## Usage

1. Ingest the dataset from Github
2. Convert the dataset to parquet format
3. Load the parquet file into the Postgres database
4. Transform the data using dbt
5. Create a dashboard in Metabase using the cleaned data
6. Orchestrate the entire process using Prefect

## Built With

* [Docker](https://www.docker.com/) - Containerization platform
* [Python](https://www.python.org/) - Programming language
* [GitHub Codespaces](https://www.github.com/) - Platform
* [Parquet](https://parquet.apache.org/) - Columnar storage format
* [Postgres](https://www.postgresql.org/) - Data Warehouse
* [dbt](https://www.getdbt.com/) - Data transformation tool
* [Metabase](https://www.metabase.com/) - Business intelligence tool
* [Prefect](https://www.prefect.io/) - Workflow management system

## Notes:

- This project was made in github codespaces, hence some of the file paths reflect that.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
"""
Read the CSV dataset into a parquet file.

"""

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def convert_to_parquet():
    
    # List of CSV file parts
    print('List of CSV file parts')
    part1 = "Google-Playstore-Dataset/dataset/Part1.csv"
    part2 = "Google-Playstore-Dataset/dataset/Part2.csv"
    # part3 = "Google-Playstore-Dataset/dataset/Part3.csv"
    csv_files = [part1, part2]

    # Read and merge CSV files
    print('Read and merge CSV files')
    dataframes = []
    for file in csv_files:
        df = pd.read_csv(file, low_memory=False)
        print(f'appending {file}')
        dataframes.append(df)

    merged_df = pd.concat(dataframes)

    # Convert merged DataFrame to Parquet file
    print('Convert merged DataFrame to Parquet file')
    
    # Define the schema of the data
    schema = pa.Schema.from_pandas(merged_df, preserve_index=False)

    # Create a Parquet writer using a context manager
    with pq.ParquetWriter('dataset.parquet', schema) as writer:
        # Write the data in chunks
        chunk_size = 100000
        for i in range(0, len(merged_df), chunk_size):
            table = pa.Table.from_pandas(merged_df[i:i+chunk_size], preserve_index=False)
            writer.write_table(table)
    

if __name__ == "__main__":
    convert_to_parquet()
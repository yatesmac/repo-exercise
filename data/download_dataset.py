"""
This script downloads the Google Playstore dataset from GitHub, 
extracts the tar.gz files, and combines the CSV files into a single CSV file. 
The dataset will be saved in the "data" directory.

"""

import os
import subprocess
import shutil

def download_dataset():
    
    # Clone the repository
    dowload_path = "https://github.com/gauthamp10/Google-Playstore-Dataset.git"
    os.system(f"git clone {dowload_path}")

    # Change the working directory
    download_dir = os.path.join("Google-Playstore-Dataset", "dataset")
    os.chdir(download_dir)
    
    # Extract tar files
    for f in os.listdir():
        if f.endswith(".tar.gz"):
            subprocess.run(["tar", "-xvf", f], check=True)

    # Concatenate CSV files
    with open("dataset.csv", "w") as output_file:
        for part in sorted(os.listdir()):
            if part.startswith("Part") and part.endswith(".csv"):
                with open(part, "r") as input_file:
                    output_file.write(input_file.read())
    
    # Clean-up code
    #
    # Move the file to the desired direcory
    subprocess.run(["mv", "dataset.csv", "/workspaces/repo-exercise/data"], check=True)
    # Change back to the parent directory
    os.chdir("../..")
    # Remove the git repository
    shutil.rmtree("Google-Playstore-Dataset")

    # if all processes complete successfully:
    print("Done!")

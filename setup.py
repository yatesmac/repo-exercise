"""
This module sets up installs requirements, 
initializes a git repository and makes the first commit.
If you are running on a local machine you can set up a virtual environment first.

"""

import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)


def run_command(command):
    """
    This function runs a command using subprocess.
    :param command: is a list of strings.
    """
    subprocess.run(command, check=True)


if __name__ == "__main__":
    # Create and Activate virtual environment
    # run_command(['python3', '-m', 'venv', 'venv'])
    # venv_activate = os.path.join('venv', 'bin', 'activate')
    # with open(venv_activate) as f:
    #     exec(f.read(), {'__file__': venv_activate})

    # Install requirements
    logging.info("Installing requirements")
    run_command(["pip", "install", "-r", "requirements.txt"])

    # Install docker-compose
    logging.info("Installing docker-compose")
    run_command(
        [
            "sudo",
            "curl",
            "-L",
            "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)",
            "-o",
            "/usr/local/bin/docker-compose",
        ]
    )
    run_command(["sudo", "chmod", "+x", "/usr/local/bin/docker-compose"])

    # Initialize git repository
    # logging.info("Initialize git repository")
    # run_command(['git', 'init'])
    # run_command(['git', 'add', '.'])
    # run_command(['git', 'commit', '-m', '"initial commit"'])

    # Initialize Containers
    logging.info("Initialize Containers")
    run_command(["docker-compose", "build"])
    run_command(["docker-compose", "up"])

    logging.info("All Done!")

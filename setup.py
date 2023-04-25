"""
This module sets up a virtual environment, activates it, installs requirements, 
initializes a git repository and makes the first commit.
"""

import os
import subprocess


def run_command(command):
    """
    This function runs a command using subprocess.
    :param command: is a list of strings.
    """
    subprocess.run(command, check=True)


# Create virtual environment and Activate virtual environment
# run_command(['python3', '-m', 'venv', 'venv'])
# venv_activate = os.path.join('venv', 'bin', 'activate')
# with open(venv_activate) as f:
#     exec(f.read(), {'__file__': venv_activate})

# Install requirements
run_command(['pip', 'install', '-r', 'requirements.txt'])

#Install docker-compose
run_command(['sudo', 'curl', '-L', 'https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)', '-o', '/usr/local/bin/docker-compose'])
run_command(['sudo', 'chmod', '+x', '/usr/local/bin/docker-compose'])


# Initialize git repository
run_command(['git', 'init'])
run_command(['git', 'add', '.'])
run_command(['git', 'commit', '-m', '"initial commit"'])


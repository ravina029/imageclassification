import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name='imageclassifier'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name  # Use Path methods instead of os.path.split

    if filedir != "":
        filedir.mkdir(parents=True, exist_ok=True)  # Use Path.mkdir directly
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        filepath.touch()  # Use Path.touch to create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else: 
        logging.info(f'{filename} already exists')




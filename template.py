import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "data_science_mock_interview_platform"

list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transfromation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",

    f"src/notebook/.gitkeep",
    f"src/notebook/data/.gitkeep",
    f"src/notebook/data/raw_data/.gitkeep",
    f"src/notebook/data/processed_data/.gitkeep",

    "application.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "artifacts/.gitkeep"

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f'{filename} is already exists')
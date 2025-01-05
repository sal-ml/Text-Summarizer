import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'Text-Summarizer'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constant/__init__.py'
    'config/config.yaml',
    'params/params.yaml',
    'app.py',
    'main.py',
    'Dockerfile', 
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
]

for file in list_of_files:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    
    print('file_dir:', file_dir)
    print('file_name:', file_name)
    
    if filedir != '':
        os.makedirs(file_dir)
        logging.info(f'Creating directory: {file_dir} for the file: {file_name}')
    
    if (not os.path.exists(file_dir))  or (not os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'Creating empty file: {file_path}')
    else:
        logging.info(f'{file_dir} already exists')
    
import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)

package_name = 'MOngoDBConnect'

list_of_files = [
    '.github/workflows/ci.yaml',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/mongo_crud.py',
    'tests/__init__.py',
    'tests/integration/__init__.py',
    'tests/integration/integration.py',
    'tests/unit/__init__.py',
    'tests/unit/unit.py',  
    'init_setup.sh',
    'setup.py',
    'setup.cfg',
    'tox.ini',
    'pyproject.toml',
    'experiments/experiment.ipynb',
    'requirements.txt',
    'requirements_dev.txt',
    'ci.yaml',
    'init_setup.sh'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for file {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # create an empty file
        logging.info(f'Created empty file: {filepath}')

import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name="TextSummarizer"

list_files=[
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__innit__.py",
    f"src/{project_name}/conponents/__innit__.py",
    f"src/{project_name}/utils/__innit__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__innit__.py",
    f"src/{project_name}/config/__innit__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__innit__.py",
    f"src/{project_name}/entity/__innit__.py",
    f"src/{project_name}/constants/__innit__.py",  
    "config/cofig.yaml",
    "params.yaml",
    "main.py",
    "Dockerfilr",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]   


for filepath in list_files:
    filepath=Path(filepath)
    filedirectory,filename=os.path.split(filepath)
    if filedirectory!='':
        os.makedirs(filedirectory,exist_ok=True)
        logging.info(f'creating directory:{filedirectory} for the file {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info('f"crearting empty file: {filepath}')

    else:
        logging.info(f'file: {filepath} already exists')
        


from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

'''def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements'''

setup(
    name = KiroMongoConnector,
    version = ,
    author = KirollosMessak1,
    author_email = kirollosmagdy8@gmail.com,
    description = 'mongoDb connector plg by Kiro',
    url=f''
)
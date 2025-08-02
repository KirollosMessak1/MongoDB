from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements
__version__ = '0.0.1'
REPO_NAME = 'mongodbconnectorpkg'
AUTHOR_USER_NAME = 'KirollosMessak1'
AUTHOR_EMAIL = 'kirollosmagdy8@gmail.com'
PKG_NAME = 'databaseautonmation'

setup(
    name = PKG_NAME ,
    version = __version__ ,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = 'mongoDb connector pkg by Kiro',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_url = {
        'Bug Tracker':f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    },
    package_dir={'':'src'},
    package=find_packages(where='src'),
    install_requires=get_requirements('./requirements_dev.txt')
)
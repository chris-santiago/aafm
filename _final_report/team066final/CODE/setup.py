import os
import pathlib
import shutil

from setuptools import setup, find_packages

TITLE = 'dva'
VERSION = '0.0.1'
DESCRIPTION = 'DVA AAFM Project'

HERE = pathlib.Path(__file__).parent
HOME = pathlib.Path.home()
AAFM_DIR = HOME.joinpath('aafm_work')

INSTALL_REQUIRES = HERE.joinpath('requirements.txt').read_text().split('\n')


def install_package():
    setup(
        name=TITLE,
        version=VERSION,
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=INSTALL_REQUIRES,
        include_package_data=True
    )


def initialize():
    pathlib.Path.mkdir(AAFM_DIR, exist_ok=True)
    dirs = [
        ('data', 'raw')
    ]
    for d in dirs:
        new_dir = AAFM_DIR.joinpath(*d)
        pathlib.Path.mkdir(new_dir, exist_ok=True, parents=True)

    for item in ['main.ipynb', 'chilean_funds_dashboard.twbx']:
        file = HERE.joinpath('dva', item)
        dest_path = AAFM_DIR.joinpath(file.name)
        shutil.copy(file, dest_path)


if __name__ == '__main__':
    install_package()
    initialize()

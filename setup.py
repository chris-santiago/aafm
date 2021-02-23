import pathlib

from setuptools import setup, find_packages

TITLE = 'dva'
VERSION = '0.0.1'
DESCRIPTION = 'DVA AAFM Project'

HERE = pathlib.Path(__file__).absolute().parent
INSTALL_REQUIRES = HERE.joinpath('requirements.txt').read_text().split('\n')
LICENSE = HERE.joinpath('license.txt').read_text()


def install_package():
    setup(
        name=TITLE,
        version=VERSION,
        description=DESCRIPTION,
        packages=find_packages(),
        install_require=INSTALL_REQUIRES,
        include_package_data=True
    )


if __name__ == '__main__':
    install_package()

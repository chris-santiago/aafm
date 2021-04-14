import pathlib
import shutil


HERE = pathlib.Path(__file__).cwd()
HOME = pathlib.Path.home()
AAFM_DIR = HOME.joinpath('aafm_work')


def initialize():
    pathlib.Path.mkdir(AAFM_DIR, exist_ok=True)
    dirs = [
        ('data', 'raw')
    ]
    for d in dirs:
        new_dir = AAFM_DIR.joinpath(*d)
        pathlib.Path.mkdir(new_dir, exist_ok=True, parents=True)

    for item in ['main.ipynb', 'chilean_funds_dashboard.twbx']:
        file = HERE.joinpath(item)
        dest_path = AAFM_DIR.joinpath(file.name)
        shutil.copy(file, dest_path)


if __name__ == '__main__':
    initialize()
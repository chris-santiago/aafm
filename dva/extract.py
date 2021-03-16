import pathlib

import dask.dataframe as dd
import pandas as pd
from dask.diagnostics import ProgressBar

HERE = pathlib.Path(__file__).parent
PROJECT_DIR = HERE.parent
DATA_DIR = PROJECT_DIR.joinpath('data')
RAW_FILES = DATA_DIR.joinpath('raw')

COLS = {
    'fund_prices': [
        'fundName', 'fundSeries', 'installmentValue', 'bloombergCode', 'fecha'
    ],
    'fund_data': [
        'fundRUN', 'fundName', 'fundSeries', 'bloombergCode', 'APV', 'aafmCategory', 'svsCategory',
        'svsCategoryId', 'currency'
    ],
    'fund_flows': [
        'fundRUN', 'fundName', 'fundSeries', 'bloombergCode', 'netPatrimony', 'providedFlow',
        'rescuedFlow', 'fecha'
    ],
}


def check_files(dir_path):
    """Checks that all file schemas match."""
    files = pathlib.Path(dir_path).glob('*csv')
    all_shapes = []
    all_columns = []
    for file in files:
        tmp = pd.read_csv(file, nrows=10)
        all_shapes.append(tmp.shape)
        all_columns.append(tmp.columns)
    assert all([x == all_shapes[0] for x in all_shapes])
    assert all([all(x) == all(all_columns[0]) for x in all_columns])


def get_subset(data, columns):
    """Get a subset of data."""
    with ProgressBar():
        sub = data[columns].drop_duplicates()
        return sub.compute()


def main():
    raw_files = DATA_DIR.joinpath('raw')
    check_files(raw_files)
    data = dd.read_csv(f'{raw_files}/*.csv', parse_dates=['fecha'])
    for name, columns in COLS.items():
        fn = f'{name}.parq'
        df = get_subset(data, columns)
        df.to_parquet(DATA_DIR.joinpath(fn), compression='gzip')


if __name__ == '__main__':
    main()

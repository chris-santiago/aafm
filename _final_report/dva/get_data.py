from typing import List

import json
import requests
import pandas as pd
import pathlib
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


def get_dates(start_date: str, end_date: str) -> List[str]:
    return [x.strftime('%Y%m%d') for x in pd.date_range(start_date, end_date, freq='D')]


def pull_data(date:str , output_dir: pathlib.Path):
    resp = requests.get(f"https://api.aafm.cl/publicDailyStatistics/{date}")
    if resp.ok:
        pd.DataFrame(resp.json()).to_csv(output_dir.joinpath(f'mutual_fund_data_{date}.csv'), index=False)


def pull_all(dates, output_dir):
    with ThreadPoolExecutor(max_workers=64) as exec:
        list(tqdm(exec.map(pull_data, dates, [output_dir] * len(dates)), total=len(dates)))

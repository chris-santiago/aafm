import pandas as pd
import numpy as np


def get_cagr(series: pd.Series) -> pd.Series:
    series = series.dropna()
    start = series[0]
    end = series[-1]
    n = len(series)
    return (end/start) ** (1/(n/12)) - 1


def check_series(series):
    return (len(series) - series.isna().sum()) < 6


def get_ann_return(series):
    if check_series(series):
        return np.nan
    return get_cagr(series)


def get_ann_std(series):
    if check_series(series):
        return np.nan
    series = series.dropna()
    return series.pct_change().std() * np.sqrt(12)


def geo_mean(series):
    n = len(series)
    arr = np.ones(n)
    return np.product(series + arr) ** (1/n) - 1


def add_perf_metrics(data: pd.DataFrame) -> pd.DataFrame:
    fund_data = data.iloc[:, :9]
    ts = data.iloc[:, 9:]
    fund_data['ann_return'] = ts.apply(lambda x: get_cagr(x), axis=1)
    fund_data['ann_stdev'] = ts.apply(lambda x: get_ann_std(x), axis=1)
    return fund_data


if __name__ == '__main__':
    data = pd.read_csv('../../_final_report/data/FundDataWithMonthlyPrices_v3.csv')
    add_perf_metrics(data).to_csv('../../_final_report/data/FundDataPerfandRisk.csv', index=False)

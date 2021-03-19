from typing import Dict

import pandas as pd
import pathlib


def get_monthly_prices(data: pd.DataFrame) -> pd.DataFrame:
    monthly_prices = data.groupby(
        [pd.Grouper(key='fecha', freq='1M'), 'fundName', 'fundSeries']
    ).last()
    return monthly_prices.reset_index().pivot(
        index='fecha', columns=['fundName', 'fundSeries'], values='installmentValue'
    )


def get_longest_series(data: pd.DataFrame, transpose=True) -> pd.DataFrame:
    """For use on joined parquet files."""
    longest = []
    df = data.copy()
    if transpose:
        df = data.T
    for fund in df.index.get_level_values(0).unique():
        least_missing = df.loc[fund].isna().sum(axis=1).sort_values().index[0]
        longest.append(df.loc[(fund, least_missing), :])
    return pd.concat(longest, axis=1)


def get_longest_series2(df: pd.DataFrame) -> pd.DataFrame:
    """For use on FundDatawithMonthlyPrices_v2_raw.csv"""
    longest = []
    index_cols = list(df.columns[:8])
    df = df.copy().set_index(index_cols)
    for fund in df.index.get_level_values(1).unique():
        least_missing = df.xs(fund, level=1, drop_level=False).isna().sum(1).sort_values().index[0]
        longest.append(df.loc[least_missing, :])
    new = pd.concat(longest, axis=1).T
    new.index.names = index_cols
    return new.reset_index()


def get_most_invest_series(data: pd.DataFrame) -> pd.MultiIndex:
    aum = data.copy()
    aum.set_index('fecha', inplace=True)
    aum.index = pd.to_datetime(aum.index)
    series_max = (aum.loc['2021-01-31', ['fundName', 'netPatrimony']]
                  .reset_index()
                  .groupby(['fecha', 'fundName'])
                  .idxmax()
                  .values
                  .ravel()
                  )
    max_aum = aum.loc['2021-01-31'].reset_index().loc[series_max, ['fundName', 'fundSeries']]
    return pd.MultiIndex.from_tuples([*zip(max_aum['fundName'], max_aum['fundSeries'])])


if __name__ == '__main__':
    here = pathlib.Path(__file__).parent
    project = here.parent
    file_path = project.joinpath('data', 'fund_prices.parq')
    prices = pd.read_parquet(file_path)
    file_path = project.joinpath('data', 'monthly_prices.csv')
    get_longest_series(get_monthly_prices(prices)).to_csv(file_path)

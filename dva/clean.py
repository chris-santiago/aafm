import pandas as pd

prices = pd.read_parquet('./data/fund_prices.parq')


def get_monthly_prices(data: pd.DataFrame) -> pd.DataFrame:
    monthly_prices = data.groupby(
        [pd.Grouper(key='fecha', freq='1M'), 'fundName', 'fundSeries']
    ).last()
    return monthly_prices.reset_index().pivot(
        index='fecha', columns=['fundName', 'fundSeries'], values='installmentValue'
    )


def get_longest_series(data: pd.DataFrame) -> pd.DataFrame:
    longest = []
    df = data.T
    for fund in df.index.get_level_values(0).unique():
        least_missing = df.loc[fund].isna().sum(axis=1).sort_values().index[0]
        longest.append(df.loc[(fund, least_missing), :])
    return pd.concat(longest, axis=1)

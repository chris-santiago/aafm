import pandas as pd
import pathlib


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


if __name__ == '__main__':
    here = pathlib.Path(__file__).parent
    project = here.parent
    file_path = project.joinpath('data', 'fund_prices.parq')
    prices = pd.read_parquet(file_path)
    file_path = project.joinpath('data', 'monthly_prices.csv')
    get_longest_series(get_monthly_prices(prices)).to_csv(file_path)

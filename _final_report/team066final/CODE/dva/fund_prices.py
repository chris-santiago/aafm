import pandas as pd


def get_monthly_prices(price_file):
    prices = pd.read_parquet(price_file)
    prices['fundName'] = prices['fundName'].str.strip()
    prices['fundSeries'] = prices['fundSeries'].str.strip()
    monthly_prices = prices.groupby(
        [pd.Grouper(key='fecha', freq='1M'), 'fundName', 'fundSeries']
    ).last()
    return monthly_prices.reset_index().pivot(
        index=['fundName', 'fundSeries'], columns=['fecha'], values='installmentValue'
    )


def join_fund_data(monthly_prices, data_file):
    data = pd.read_parquet(data_file)
    data['fundName'] = data['fundName'].str.strip()
    data['fundSeries'] = data['fundSeries'].str.strip()
    data.set_index(['fundName', 'fundSeries'], inplace=True)
    return data.merge(monthly_prices, left_index=True, right_index=True, how='inner')


def remove_closed_funds(data):
    mask = data.iloc[:, -1].isna()
    return data[~mask]

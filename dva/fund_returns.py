from typing import Union, Dict

import pandas as pd
import numpy as np


data = pd.read_csv('data/FundDatawithMonthlyPrices.csv')


def get_static_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.iloc[:, 1:10]


def get_price_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.iloc[:, 14:]


def get_return_data(prices: pd.DataFrame) -> pd.DataFrame:
    prices = prices.T
    prices.index = pd.to_datetime(list(prices.index))
    returns = prices.pct_change().T.replace([-np.inf, np.inf], np.nan)
    returns.columns = [x.strftime('%Y-%m-%d') for x in returns.columns]
    return returns


def make_dataset(static_data: pd.DataFrame, return_data: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([static_data, return_data], axis=1)


def get_category_means(dataset: pd.DataFrame) -> Dict[str, pd.Series]:
    cat_means = {}
    for cat in dataset['aafmCategory'].unique():
        mask = dataset['aafmCategory'] == cat
        prices = dataset[mask].loc[:, '2015-02-28':].dropna()
        # cat_means[cat] = pd.DataFrame(prices.mean()).T
        cat_means[cat] = prices.mean()
    return cat_means


# def fill_na(dataset: pd.DataFrame, means: Dict) -> pd.DataFrame:
#     df = dataset.copy()
#     for cat, fill_vals in means.items():
#         mask = df['aafmCategory'] == cat
#         df[mask].fillna(fill_vals, inplace=True)
#     return df


def fill_series(na_series: pd.Series, fill_series: pd.Series) -> pd.Series:
    return na_series.fillna(fill_series)


def fill_na(dataset: pd.DataFrame, means: Dict) -> pd.DataFrame:
    return dataset.apply(lambda row: fill_series(row, means[row.loc['aafmCategory']]), axis=1)

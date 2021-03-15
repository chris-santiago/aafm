import pandas as pd
import numpy as np


data = pd.read_csv('data/FundDatawithMonthlyPrices.csv')


def get_category_means(data):
    cat_means = {}
    categories = data['aafmCategory'].unique()
    for cat in categories:
        mask = data['aafmCategory'] == cat
        prices = data[mask].iloc[:, 14:].dropna()
        cat_means[cat] = prices.mean()
    return cat_means





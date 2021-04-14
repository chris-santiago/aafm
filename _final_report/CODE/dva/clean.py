from typing import Dict, List

import pandas as pd
import pathlib


def get_user_categories():
    return {
    'International Equity': [
        'Accionario America Latina', 'Accionario Asia Pacifico', 'Accionario Brasil',
        'Accionario Desarrollado', 'Accionario EEUU', 'Accionario Europa Desarrollado',
        'Accionario Pais', 'Accionario Países MILA',
    ],
    'Emerging Equity': [
        'Accionario Asia Emergente', 'Accionario Emergente', 'Accionario Europa Emergente',
    ],
    'Domestic Equity': [
        'Accionario Nacional Large CAP', 'Accionario Nacional Otros', 'Accionario Sectorial',
    ],
    'Balanced, Conservative': ['Balanceado Conservador'],
    'Balanced, Moderate': ['Balanceado Moderado'],
    'Balanced, Aggressive': ['Balanceado Agresivo'],
    'International Bond, < 365': [
        'Fondos de Deuda < 365 Dias Internacional',
        'Fondos de Deuda < 90 Dias Internacional, Dolar',
    ],
    'Domestic Bond, < 365': [
        'Fondos de Deuda < 365 Dias Nacional en UF', 'Fondos de Deuda < 365 Dias Nacional en pesos',
        'Fondos de Deuda < 90 Dias Nacional',
        'Inversionistas Calificados Accionario Nacional',
    ],
    'International Bond, > 365': [
        'Fondos de Deuda > 365 Dias Internacional, Mercados Emergentes',
        'Fondos de Deuda > 365 Dias Internacional, Mercados Internacionales',

    ],
    'Domestic Bond, > 365': [
        'Fondos de Deuda > 365 Dias Nacional, Inversion UF > 3 años y =<5',
        'Fondos de Deuda > 365 Dias Nacional, Inversion en UF > 5 años',
        'Fondos de Deuda > 365 Dias Nacional, Inversión en Pesos',
        'Fondos de Deuda > 365 Dias Nacional, Inversión en UF < 3 años',
        'Fondos de Deuda > 365 Dias Orig. Flex', 'Inversionistas Calificados Títulos de Deuda',
    ]
}


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


def filter_min_history(data: pd.DataFrame, min_periods: int) -> pd.DataFrame:
    mask = data.iloc[:, -min_periods:].notnull().sum(1) == min_periods
    return data[mask]


def filter_constant_prices(data: pd.DataFrame) -> pd.DataFrame:
    mask = data.iloc[:, 8:].apply(lambda x: x.nunique(), axis=1) != 1
    return data[mask]


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
    """For use on FundDatawithMonthlyPrices_v2_raw.csv"""
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


def lookup(val: str, cats: Dict[str, List[str]]) -> str:
    try:
        res = [x for x in cats.keys() if val in cats[x]]
        return res[0]
    except IndexError:
        print(f'{val} not in lookup.')


def get_fund_flows_2020(parq_file: str) -> pd.DataFrame:
    aum = pd.read_parquet(parq_file)
    aum.set_index('fecha', inplace=True)
    aum.index = pd.to_datetime(aum.index)
    assets = aum.loc['2020']
    assets['fundRUNSeries'] = assets['fundRUN'] + assets['fundSeries']
    return assets.groupby('fundRUNSeries').mean()


def clean_from_parquet(data_dir: str) -> None:
    data = pathlib.Path(data_dir)
    file_path = data.joinpath('fund_prices.parq')
    prices = pd.read_parquet(file_path)
    file_path = data.joinpath('monthly_prices.csv')
    get_longest_series(get_monthly_prices(prices)).to_csv(file_path)


def clean_from_monthly_prices_raw(data: pd.DataFrame, min_periods: int = 36) -> None:
    data.reset_index(inplace=True)
    data.dropna(subset=['aafmCategory'], inplace=True)  # don't want funds w/o category
    data.insert(loc=0, column='fundRUNSeries', value=data['fundRUN'] + data['fundSeries'])
    data = filter_min_history(data, min_periods)
    data = filter_constant_prices(data)
    data = get_longest_series2(data)
    new_cat = data['aafmCategory'].apply(lambda x: lookup(x, get_user_categories()))
    data.insert(loc=8, column='userCategory', value=new_cat)
    return data
    # data.to_csv('../data/FundDataWithMonthlyPrices_v3.csv', index=False)

if __name__ == '__main__':
    clean_from_monthly_prices_raw('../data/FundDatawithMonthlyPrices_v2_raw.csv')
    get_fund_flows_2020('../../_final_report/data/fund_flows.parq').to_csv(
        '../../_final_report/data/FundDataRecentFlows.csv')

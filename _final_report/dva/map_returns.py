from typing import Callable

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import Isomap, MDS, TSNE


def map_to_lower_dim(data: pd.DataFrame, method: str) -> pd.DataFrame:
    func = {
        'isomap': Isomap(n_neighbors=5, n_components=2),
        'mds': MDS(metric=False),
        'tsne': TSNE(n_components=2, perplexity=10)
    }

    mapped = data.copy()
    df_num = mapped.iloc[:, 10:]
    pl = Pipeline(
        steps=[
            ('scaler', StandardScaler()),
            ('encode', func[method]),
        ]
    )
    components = pl.fit_transform(df_num)
    mapped['x_coord'] = components[:, 0]
    mapped['y_coord'] = components[:, 1]
    return mapped


def map_by_group(data: pd.DataFrame, method: str, group: str) -> pd.DataFrame:
    mask = data['userCategory'] == group
    df = data[mask].copy()
    return map_to_lower_dim(df, method)


def map_all_by_group(data: pd.DataFrame, method: str) -> pd.DataFrame:
    all_data = []
    for group in data['userCategory'].unique():
        all_data.append(map_by_group(data, method, group))
    return pd.concat(all_data)


def join_fund_flows(data: pd.DataFrame, flows: str) -> pd.DataFrame:
    flows = pd.read_csv(flows)
    return data.merge(flows, on='fundRUNSeries')


if __name__ == '__main__':
    data = pd.read_csv('../data/monthly_returns.csv')
    data.fillna(0, inplace=True)
    mapped = map_to_lower_dim(data, 'tsne')
    joined = join_fund_flows(mapped, '../data/FundDataRecentFlows.csv')
    joined.to_csv('../data/FundDataWithMonthlyReturnsTSNE-single.csv', index=False)

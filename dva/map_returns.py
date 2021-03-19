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

    all_data = []
    for cat in data['userCategory'].unique():
        mask = data['userCategory'] == cat
        df = data[mask].copy()
        df_num = df.iloc[:, 10:]
        pl = Pipeline(
            steps=[
                ('scaler', StandardScaler()),
                ('encode', func[method]),
            ]
        )
        components = pl.fit_transform(df_num)
        df['x_coord'] = components[:, 0]
        df['y_coord'] = components[:, 1]
        all_data.append(df)
    return pd.concat(all_data)


if __name__ == '__main__':
    data = pd.read_csv('../data/monthly_returns.csv')
    data.fillna(0, inplace=True)

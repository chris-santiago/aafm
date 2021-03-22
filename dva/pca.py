from typing import Union, Optional, List

import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class PCADetector:
    def __init__(self, data: pd.DataFrame, cols: List[str]):
        self.data = data
        self.original = data.loc[:, cols]
        self.projected: Optional[Union[pd.Series, np.ndarray]] = None

    def get_projection(self) -> np.ndarray:
        if self.projected:
            return self.projected
        df = self.original.copy()
        pl = Pipeline(
            steps=[
                ('scaler', StandardScaler()),
                ('pca', PCA(n_components=0.9))
            ]
        )
        self.projected = pl.inverse_transform(pl.fit_transform(df))
        return self.projected

    def get_loss(self) -> Union[pd.Series, np.ndarray]:
        return np.sum((self.original - self.projected) ** 2, axis=1)

    def get_score(self) -> Union[pd.Series, np.ndarray]:
        loss = self.get_loss()
        return (loss - np.min(loss)) / (np.max(loss) - np.min(loss))

    def score(self, floor: float, min_size: int) -> pd.DataFrame:
        if len(self.original) < min_size:
            self.data['pca_anomaly'] = 0
            return self.data
        self.get_projection()
        scores = self.get_score()
        losses = self.get_loss()
        self.data['pca_anomaly'] = ((scores > 0.85) & (losses > floor)).astype(int)
        return self.data




def get_projection(data: pd.DataFrame) -> Union[pd.Series, np.ndarray]:
    df = data.copy()
    df_num = df.iloc[:, 9:-5]
    pl = Pipeline(
        steps=[
            ('scaler', StandardScaler()),
            ('pca', PCA(n_components=0.95))
        ]
    )
    return pl.inverse_transform(pl.fit_transform(df_num))


def get_loss(
        original: Union[pd.Series, np.ndarray], projected: Union[pd.Series, np.ndarray]
) -> Union[pd.Series, np.ndarray]:
    return np.sum((original - projected) ** 2, axis=1)


def get_score(loss: Union[pd.Series, np.ndarray]) -> Union[pd.Series, np.ndarray]:
    return (loss - np.min(loss)) / (np.max(loss) - np.min(loss))


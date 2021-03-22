from sklearn.metrics import pairwise_distances
import numpy as np


def get_anomalies(data, thresh=2):
    group_mean = data[['x_coord', 'y_coord']].mean().values.reshape(1, -1)
    dist = pairwise_distances(data[['x_coord', 'y_coord']], group_mean)

    dist_mean = np.mean(dist)
    dist_std = np.std(dist)
    test_level = dist_mean + (dist_std * thresh)
    return np.where(dist > test_level, 1, 0).ravel()

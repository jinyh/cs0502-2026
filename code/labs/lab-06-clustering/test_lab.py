import numpy as np

from starter import kmeans, standardize


def test_standardize():
    data = np.array([[0.0, 100.0], [2.0, 200.0], [4.0, 300.0]])
    result = standardize(data)
    assert np.allclose(result.mean(axis=0), 0)
    assert np.allclose(result.std(axis=0), 1)


def test_reproducible_centers():
    data = np.array([[-2.0, 0.0], [-1.8, 0.1], [2.0, 0.0], [1.8, -0.1]])
    _, centers1 = kmeans(data, 2, seed=7)
    _, centers2 = kmeans(data, 2, seed=7)
    assert np.allclose(np.sort(centers1[:, 0]), [-1.9, 1.9])
    assert np.allclose(centers1, centers2)

import numpy as np

from starter import diagnose, fit_and_measure


def test_measurement_and_diagnosis():
    train_x = np.array([[0.0], [0.25], [0.5], [0.75], [1.0]])
    train_y = np.sin(2 * np.pi * train_x[:, 0])
    test_x = np.linspace(0, 1, 30)[:, None]
    test_y = np.sin(2 * np.pi * test_x[:, 0])
    train_error, test_error = fit_and_measure(3, train_x, train_y, test_x, test_y)
    assert train_error >= 0 and test_error >= 0
    assert diagnose(0.001, 2.0) == "overfitting"

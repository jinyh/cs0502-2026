"""Slide17：低阶、适当和高阶模型的训练/测试误差。"""

import numpy as np


def dataset(seed, size):
    rng = np.random.default_rng(seed)
    x = np.sort(rng.uniform(0, 1, size))
    y = np.sin(2 * np.pi * x) + rng.normal(0, 0.15, size)
    return x[:, None], y


def evaluate(degree, train_x, train_y, test_x, test_y):
    coefficients = np.polynomial.polynomial.polyfit(train_x[:, 0], train_y, degree)
    train_prediction = np.polynomial.polynomial.polyval(train_x[:, 0], coefficients)
    test_prediction = np.polynomial.polynomial.polyval(test_x[:, 0], coefficients)
    return (
        float(np.mean((train_y - train_prediction) ** 2)),
        float(np.mean((test_y - test_prediction) ** 2)),
    )


if __name__ == "__main__":
    train_x, train_y = dataset(seed=1, size=12)
    test_x, test_y = dataset(seed=2, size=200)
    for degree in (1, 3, 9):
        train_error, test_error = evaluate(degree, train_x, train_y, test_x, test_y)
        print(f"degree={degree}: train={train_error:.4f}, test={test_error:.4f}")

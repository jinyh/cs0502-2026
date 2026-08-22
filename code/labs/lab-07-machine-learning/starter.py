def fit_and_measure(degree, train_x, train_y, test_x, test_y):
    """只用训练集拟合指定次数多项式，并返回训练与测试 MSE。"""
    raise NotImplementedError


def diagnose(train_error, test_error):
    """按公开任务阈值返回 underfitting、overfitting 或 good-fit。"""
    raise NotImplementedError

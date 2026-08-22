def standardize(points):
    """逐特征做零均值单位方差变换；常数特征映射为 0。"""
    raise NotImplementedError


def kmeans(points, cluster_count, seed=0, max_iterations=50):
    """返回 (标签, 中心)；固定 seed 可复现，cluster_count 必须合法。"""
    raise NotImplementedError

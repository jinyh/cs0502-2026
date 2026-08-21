"""Slide14：可复现且能处理空簇的教学版 KMeans。"""

import numpy as np


def kmeans(points, cluster_count=2, seed=7, max_iterations=50):
    rng = np.random.default_rng(seed)
    centers = points[rng.choice(len(points), size=cluster_count, replace=False)].copy()
    for _ in range(max_iterations):
        distances = np.linalg.norm(points[:, None, :] - centers[None, :, :], axis=2)
        labels = distances.argmin(axis=1)
        updated = centers.copy()
        for cluster in range(cluster_count):
            members = points[labels == cluster]
            if len(members):
                updated[cluster] = members.mean(axis=0)
            else:
                updated[cluster] = points[rng.integers(len(points))]
        if np.allclose(updated, centers):
            break
        centers = updated
    distances = np.linalg.norm(points[:, None, :] - centers[None, :, :], axis=2)
    labels = distances.argmin(axis=1)
    return labels, centers


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    points = np.vstack((rng.normal((-2, 0), 0.35, (12, 2)), rng.normal((2, 0), 0.35, (12, 2))))
    labels, centers = kmeans(points)
    order = np.argsort(centers[:, 0])
    print("按横坐标排序的聚类中心:", np.round(centers[order], 3).tolist())
    print("每簇样本数:", sorted(np.bincount(labels).tolist()))

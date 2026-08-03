---
title: 图的遍历
lecture: Slide06-GraphExploration-2025
aliases: [图, BFS, DFS, 广度优先, 深度优先, 连通性]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [图, BFS, DFS, 遍历, 连通分量, 入门]
status: stable
version: 1.0
importance: 5
related_cards: [04-data-structure-basics, 05-data-structure-advanced, 07-greedy-algorithm]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 图的遍历（Graph Exploration）

> 对应讲稿：`Slide06-GraphExploration-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

图（graph）是描述「事物与关系」的最通用结构；遍历（traversal）是系统地访问所有节点的策略。BFS 与 DFS 是一切图算法的基石。

## 核心知识点

### 图的基本概念

- 图 $G=(V,E)$：顶点集（vertices）$V$ + 边集（edges）$E$。
- 有向图 / 无向图：边是否有方向。
- 权重（weight）：边上的数值，表示距离 / 成本 / 相似度。
- 度（degree）：与顶点相连的边数。
- **直觉**：社交网络（人是顶点、好友关系是边）、地铁线路图、蛋白质相互作用网。

### 邻接表与邻接矩阵

两种存储表示：
- **邻接矩阵**：$n\times n$ 矩阵，$A_{ij}=1$ 表示有边。查边 $O(1)$，空间 $O(n^2)$，适合稠密图。
- **邻接表**：每个顶点存邻居链表。空间 $O(V+E)$，适合稀疏图，遍历邻居高效。

### BFS（Breadth-First Search，广度优先搜索）

逐层向外扩展：先访问起点，再访问所有距离 1 的节点，再距离 2……
- 数据结构：**队列**。
- 时间复杂度 $O(V+E)$。
- **特性**：无权图最短路径；层次遍历。
- **直觉**：往水里投石，涟漪一圈圈向外扩散。

### DFS（Depth-First Search，深度优先搜索）

沿一条路走到底再回溯。
- 数据结构：**栈**（或递归调用栈）。
- 时间复杂度 $O(V+E)$。
- **特性**：连通性判断、拓扑排序、环检测、迷宫求解。
- **直觉**：走迷宫时「一条路走到黑再退回岔路口」。

### 连通分量（Connected Component）

无向图中互相可达的顶点集合。对每个未访问顶点做一次 BFS/DFS 即可求出全部连通分量——这是图遍历的直接应用。

## 直觉类比（跨学科桥接）

| 概念 | 类比 |
|---|---|
| BFS | 传染病从源头逐层扩散；微信「可能认识的人」按共同好友层数推荐 |
| DFS | 走迷宫、深静脉血栓的血管分支追溯 |
| 连通分量 | 群岛中各自独立的岛屿群；社交网络里的封闭社群 |
| 邻接表 | 每人手机通讯录（只存认识的人，不存全人类） |

## 前沿进展注记

图算法基础稳定。前沿在**图神经网络（Graph Neural Network, GNN）**——把图的拓扑结构作为归纳偏置做表示学习，用于药物分子性质预测、社交网络分析。详见 `18-computer-vision` 与 `17-machine-learning` 的扩展方向，本卡片不展开。

## 跨学科联系

- **与数学**：图论（Euler 哥尼斯堡七桥问题）；组合优化的基础。
- **与化学/生物**：分子结构是无标号图（顶点=原子、边=键）；蛋白质相互作用网络分析。
- 与航空航天/船舶：航路网络与航线规划是最短路径问题的直接应用；机械装配的零件依赖关系用有向图表达。


## 推荐交互式问答

1. BFS 用队列、DFS 用栈，如果故意用栈做 BFS 会发生什么？
2. 无权图最短路径为什么用 BFS 而非 DFS？
3. 给定社交网络，如何找出所有「封闭小圈子」（连通分量）？
4. 邻接矩阵和邻接表在什么情况下各有优势？

## 代码示例

```python
# 对应 docs/cards/06；BFS / DFS / 连通分量
# 运行：uv run python code/examples/06_graph_bfs_dfs.py
from collections import defaultdict, deque

def build(edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b); g[b].append(a)  # 无向图
    return g

def bfs(g, start):
    visited = {start}
    q = deque([start])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v not in visited:
                visited.add(v); q.append(v)
    return order

def dfs(g, start):
    visited = set(); order = []
    def go(u):
        visited.add(u); order.append(u)
        for v in g[u]:
            if v not in visited: go(v)
    go(start)
    return order

def connected_components(g, nodes):
    seen = set(); comps = []
    for n in nodes:
        if n not in seen:
            comp = bfs(g, n)
            seen |= set(comp); comps.append(comp)
    return comps

if __name__ == "__main__":
    g = build([(1,2),(1,3),(2,4),(5,6)])
    print("BFS:", bfs(g, 1))           # [1, 2, 3, 4]
    print("DFS:", dfs(g, 1))           # [1, 2, 4, 3]
    print("连通分量:", connected_components(g, {1,2,3,4,5,6}))  # [[1,2,3,4],[5,6]]
```

## 延伸阅读

- 对应讲稿 `Slide06-GraphExploration-2025.pdf`。
- 关联：`04`（栈与队列是 BFS/DFS 的基础）、`07`（图上的贪心：最小生成树、Dijkstra）。
- 经典教材：Cormen, T. et al. (2009). *Introduction to Algorithms*, Ch.22.（图算法）

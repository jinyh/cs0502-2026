---
title: 数据结构进阶
lecture: Slide05-DataStructure2-2025
aliases: [搜索, 哈希, 散列, 哈希表, 冲突]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [搜索, 哈希, 散列, 哈希表, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [04-data-structure-basics, 06-graph-exploration, 13-database]
related_deep: []
related_visualizations: [circular_queue]
last_reviewed: 2026-08-03
---

# 数据结构进阶：搜索与哈希（Search & Hashing）

> 对应讲稿：[`Slide05-DataStructure2-2025.pdf`](../../LectureNotes/Slide05-DataStructure2-2025.pdf)

## 一句话定位

如何在大量数据里快速找到目标？线性搜索 $O(n)$ 太慢，二分搜索靠有序降到 $O(\log n)$，而哈希表（hash table）用「算地址」做到平均 $O(1)$。

## 核心知识点

### 搜索（search）

- 线性搜索：逐个比对，$O(n)$。
- 二分搜索（binary search）：**前提：数据有序**。每次折半，$O(\log n)$。
- 直觉：查字典从中间翻开，根据大小决定往前/往后。

### 哈希（hashing）

用一个哈希函数（hash function）$h(key)$ 把键直接映射到存储位置。
- 理想：查找 / 插入 / 删除平均 $O(1)$。
- 直觉：图书馆按索书号直接定位书架，而非逐本翻。

### 冲突（collision）

不同键映射到同一位置——必然发生（鸽笼原理）。
- 解决方法：
  - **链地址法（chaining）**：同一位置存链表。
  - **开放寻址法（open addressing）**：冲突就按规则找下一个空位（线性探测等）。
- 负载因子（load factor）$\alpha = n/m$（元素数/桶数）过大则性能退化，需扩容 rehash。

### 哈希函数的要求

- 确定性：同键同结果。
- 均匀分布：尽量减少冲突。
- 快速计算。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 二分搜索 | 按页码查字典 |
| 哈希表 | 按学号直接定位学生档案柜 |
| 冲突 | 两人分到同一柜格 |
| 负载因子 | 柜子塞太满，找东西变慢 |

## 前沿进展注记

基础稳定。哈希思想在 ML（LSH 近邻搜索）、密码学（见 `12`）、区块链（见 `deep/quantum-computing` 附录）广泛复用。

## 跨学科联系

- 与数学：鸽究原理、概率分析期望。
- 与医学：病历按 ID 哈希检索；基因序列 k-mer 哈希。
- 与数据库：哈希索引是 DB 加速的基础（`13`）。

## 推荐交互式问答

1. 二分搜索的前提是什么？无序数据能用吗？
2. 哈希表为什么能 $O(1)$？最坏情况退化到多少？
3. 链地址法 vs 开放寻址法各适合什么场景？

## 代码示例

```python
# 对应 docs/cards/05；二分搜索 + 简易哈希表
def binary_search(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] == x: return mid
        elif a[mid] < x: lo = mid+1
        else: hi = mid-1
    return -1

class HashTable:
    def __init__(self, size=8):
        self.size = size; self.t = [[] for _ in range(size)]
    def _h(self, k): return hash(k) % self.size
    def put(self, k, v):
        for i,(kk,_) in enumerate(self.t[self._h(k)]):
            if kk == k: self.t[self._h(k)][i] = (k,v); return
        self.t[self._h(k)].append((k,v))
    def get(self, k):
        for kk,vv in self.t[self._h(k)]:
            if kk == k: return vv
        return None
```

## 延伸阅读

- 对应讲稿 `Slide05-DataStructure2-2025.pdf`。
- 关联：`04`（基础结构）、`13`（数据库索引）。

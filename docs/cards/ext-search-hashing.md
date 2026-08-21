---
title: 搜索与哈希
lecture: 扩展（旧版卡片 05，参考 CS50）
aliases: [线性搜索, 二分搜索, 哈希, 散列, 冲突]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [搜索, 二分搜索, 哈希表, 冲突, 负载因子]
status: needs-review
version: 1.0
importance: 3
related_cards: [04-data-structure-basics, 05-data-structure-advanced, 13-database]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 搜索与哈希（Search and Hashing）

## 一句话定位

搜索利用数据的组织方式缩小候选范围；哈希把键映射到数组位置，以额外空间和冲突处理换取平均快速访问。

## 核心知识点

- 线性搜索逐项检查，通常为 $O(n)$，不要求有序。
- 二分搜索每次排除一半，要求数据已排序且支持随机访问，通常为 $O(\log n)$。
- 哈希函数把键映射为桶编号；不同键可能产生冲突。
- 链地址法和开放寻址是常见冲突处理方式；负载因子过高会降低性能。
- 哈希表操作的 $O(1)$ 通常是平均意义，不是无条件最坏保证。

## 工程桥接

基因序列 k-mer、实验样品编号和数据库哈希索引都可使用哈希，但输入分布、内存和碰撞风险决定实际方案。

## 主动学习与考核迁移

1. 解释为什么二分搜索不能直接用于未排序链表。
2. 用 `key % 5` 插入 7、12、9，展示一次冲突处理。
3. 比较有序数组、平衡树和哈希表在范围查询中的差异。

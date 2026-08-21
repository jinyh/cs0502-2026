---
title: 搜索与哈希
card_id: search-hashing
lecture_refs: [L04, L06, L13]
source_slides: [Slide04-DataStructure-2025, Slide05-DataStructure2-2025]
aliases: [线性搜索, 二分搜索, 哈希, 散列, 冲突]
thinking_pillars: [计算思维, 数据思维]
category: data-structures-algorithms
tags: [搜索, 二分搜索, 哈希表, 冲突, 负载因子]
status: needs-review
version: 1.0
importance: 3
learning_objectives: [比较线性与二分搜索, 追踪哈希冲突处理, 根据查询类型选择结构]
prerequisites: [04-data-structure-basics, ext-complexity]
estimated_minutes: 35
assessment_tags: [搜索追踪, 哈希计算, 冲突处理, 结构选择]
labs: []
figures: []
related_cards: [04-data-structure-basics, stack-queue, algorithm-strategies, 13-database]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-22
---

# 搜索与哈希（Search and Hashing）

## 一句话定位

搜索利用数据的组织方式缩小候选范围；哈希把键映射到数组位置，以额外空间和冲突处理换取平均快速访问。

## 学完应能做到

1. 追踪线性搜索和二分搜索的候选范围，说明二分搜索的前置条件。
2. 使用简单哈希函数计算桶位置并演示链地址或开放寻址处理冲突。
3. 根据精确查找、范围查询、更新频率、内存和最坏保证选择结构。

## 核心知识点

- 线性搜索逐项检查，通常为 $O(n)$，不要求有序。
- 二分搜索每次排除一半，要求数据已排序且支持随机访问，通常为 $O(\log n)$。
- 哈希函数把键映射为桶编号；不同键可能产生冲突。
- 链地址法和开放寻址是常见冲突处理方式；负载因子过高会降低性能。
- 哈希表操作的 $O(1)$ 通常是平均意义，不是无条件最坏保证。

### 搜索的前置成本

- 二分搜索前需要有序数据；若只有一次查询，排序成本可能得不偿失。
- 链表即使有序，也不能像数组一样按中间下标常数时间访问。
- 多次查询可分摊排序或索引建设成本，体现预处理与查询的权衡。

### 哈希的工程边界

- 好的哈希函数让常见键均匀分布，并且计算成本可控。
- 链地址法让每个桶保存冲突链；开放寻址在数组中按探测规则找空位。
- 负载因子升高通常增加冲突，应扩容并重新散列。
- 无序哈希表不擅长范围查询或按键顺序遍历。

## 工程桥接

基因序列 k-mer、实验样品编号和数据库哈希索引都可使用哈希，但输入分布、内存和碰撞风险决定实际方案。

## 常见误区与边界

- 二分搜索不是“任何搜索都减半”，它依赖全序和高效随机访问。
- 哈希值相同不表示键相同，冲突是必须处理的正常情况。
- 平均 $O(1)$ 不等于每次一步，也不提供攻击输入下的最坏保证。
- 密码学哈希与普通哈希表函数目标不同，不能互相替代。

## 最小代码观察

在一个长度为 5 的桶数组中手算 `key % 5`，再用 Python 字典验证最终键值；复杂度选择见 [`algorithm-strategies`](algorithm-strategies.md)。

## 主动学习与考核迁移

1. 解释为什么二分搜索不能直接用于未排序链表。
2. 用 `key % 5` 插入 7、12、9，展示一次冲突处理。
3. 比较有序数组、平衡树和哈希表在范围查询中的差异。

## 延伸阅读

- Cormen, T. et al. *Introduction to Algorithms*, Hash Tables.
- Python Documentation. *Mapping Types — dict*.

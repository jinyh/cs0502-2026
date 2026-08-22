---
title: 树、堆与层次结构
card_id: trees-heaps
lecture_refs: [L05, L06, L13]
source_slides: [Slide05-DataStructure2-2025]
aliases: [树, 二叉树, 堆, 优先队列, 层次结构]
thinking_pillars: [计算思维, 数据思维]
category: data-structures-algorithms
tags: [树, 二叉树, 遍历, 堆, 优先队列, 堆序性质]
status: ai-reviewed
version: 1.0
importance: 5
learning_objectives: [区分树的结构和遍历顺序, 追踪堆的插入删除, 根据操作需求选择树或堆]
prerequisites: [04-data-structure-basics, stack-queue]
estimated_minutes: 35
assessment_tags: [结构辨析, 遍历追踪, 堆操作, 场景选择]
labs: [lab-01-structures]
figures: [05-tree-heap.svg]
related_cards: [stack-queue, ext-recursion-divide-conquer, 06-graph-exploration, algorithm-strategies, 13-database]
related_deep: []
related_visualizations: [binary_heap]
last_reviewed: 2026-08-21
---

# 树、堆与层次结构（Trees, Heaps and Hierarchy）

> 新课程位置：L05；堆的代价在 L06、树形索引在 L13 复用。

## 一句话定位

树表达“一对多层次关系”；堆只维护父子之间的优先级，以较弱的全局顺序换取高效地取得最高或最低优先级元素。

![树与二叉堆](../../figures/05-tree-heap.svg)

## 学完应能做到

1. 识别根、父子、叶、深度和子树，并追踪前序、中序、后序与层序遍历。
2. 在数组表示的二叉堆中追踪插入上浮和删除根下沉。
3. 区分普通树、二叉搜索树、堆与优先队列，避免根据图形外观误判性质。

## 核心知识点

### 树的结构与遍历

- 除根外每个结点有唯一父结点，因此树中任意两点之间路径唯一。
- 遍历顺序是算法选择，不是树本身属性：前序先访问根，后序先处理子树，层序使用队列。
- 递归定义“树由根和若干子树组成”自然对应递归遍历；深树也可用显式栈避免调用栈限制。

### 堆不是“完全排序的树”

- 最小堆只保证父结点不大于子结点；兄弟和不同子树之间没有全序保证。
- 完全二叉树可紧凑存入数组。零基下标中，结点 `i` 的子结点常为 `2i+1` 和 `2i+2`。
- 插入先放末尾再上浮；删除根用末元素补位再下沉，二者通常为 $O(\log n)$。
- 读取最小值通常为 $O(1)$，但查找任意指定值并不因此成为 $O(1)$。

### 数据结构选择取决于问题

- 只需反复取得最高优先级：堆。
- 需要按键有序查找或范围查询：搜索树或数据库索引。
- 需要表示任意多对多关系：图。
- 需要层次标签但更新很少：普通树可能已足够。

## 工程桥接

- 离散事件仿真用最小堆选择下一个时间最早的事件。
- 文件系统、组织层级和生物分类使用树，但软链接或多重分类会把结构扩展为图。
- 数据库 B+ 树面向磁盘块和范围查询，不能用二叉堆性质代替理解。

## 常见误区与边界

- 图画成树状不等于满足树的唯一父结点与无环条件。
- 最小堆的数组不是从小到大排序；只有根保证全局最小。
- “平衡”有不同定义；本课只要求理解高度为何影响操作代价。
- 递归遍历的输出顺序取决于“访问根”的位置和孩子次序。

## 最小代码观察

运行 [`05_structures.py`](../../code/examples/05_structures.py) 并使用 [`binary_heap.html`](../../code/visualizations/binary_heap.html)。每一步操作前先画数组和树的对应关系。

## 主动学习与考核迁移

- **追踪**：向最小堆 `[2, 5, 4, 9, 7]` 插入 `1`，写出每次交换后的数组。
- **辨析**：给出三个数组，判断哪些可能是最小堆，并指出第一个违反堆序的父子对。
- **迁移**：为实验室任务调度选择 FIFO、堆或有序表，并分别说明“新增任务”和“取下一任务”的代价。
- **反例**：构造一个最小堆，使第二小元素不在数组下标 1。

## 与课程图谱关系

- 栈、队列见 [`stack-queue`](stack-queue.md)。
- 递归见 [`ext-recursion-divide-conquer`](ext-recursion-divide-conquer.md)。
- 图和 BFS/DFS 见 [`06-graph-exploration`](06-graph-exploration.md)。
- 复杂度与策略见 [`algorithm-strategies`](algorithm-strategies.md)。

## 延伸阅读

- Cormen, T. et al. *Introduction to Algorithms*, Heapsort and Priority Queues.
- Sedgewick, R. & Wayne, K. *Algorithms*, Trees and Priority Queues.

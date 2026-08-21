---
title: 递归与分治
card_id: recursion-divide-conquer
lecture_refs: [L05, L06]
source_slides: [Slide05-DataStructure2-2025]
aliases: [递归, 分治, 基线条件, 归并排序, 汉诺塔]
thinking_pillars: [计算思维]
category: data-structures-algorithms
tags: [递归, 分治, 归并排序, 汉诺塔, 入门]
status: needs-review
version: 2.0
importance: 4
learning_objectives: [追踪递归调用栈, 检查基线与规模缩小, 解释分治及其合并代价]
prerequisites: [stack-queue, 03-programming-language]
estimated_minutes: 40
assessment_tags: [递归追踪, 终止分析, 分治设计, 复杂度]
labs: [lab-01-structures]
figures: [05-stack-queue-recursion.svg]
related_cards: [stack-queue, trees-heaps, algorithm-strategies, ext-complexity]
related_deep: []
related_visualizations: [Hanoi]
last_reviewed: 2026-08-22
---

# 递归与分治（Recursion & Divide-and-Conquer）

> Slide05 已讲授递归、调用栈和汉诺塔；本卡只补充分治与归并排序。

## 一句话定位

递归（recursion）是「用自己定义自己」——把大问题化成同型的更小子问题，直到触底。分治（divide-and-conquer）是其工程化范式：分、治、合。

## 学完应能做到

1. 展开递归调用栈，记录参数、局部状态、返回值和恢复顺序。
2. 检查基线条件是否覆盖边界，以及递归步骤是否严格缩小问题。
3. 解释分治的拆分、子解和合并步骤，并估计递归深度和额外空间。

## 核心知识点

### 递归的两个要件

1. **基线条件（base case）**：最小可直接求解的情形——递归的出口，否则无限递归。
2. **递推关系（recursive step）**：把问题化为更小的同类问题。
- 直觉：站在队首问「我后面有几个人」——若没人就答 0（基线），否则问下一个人再加 1（递推）。

### 调用栈与递归

每次递归调用在调用栈压一帧（见 [`05`](05-data-structure-advanced.md)）。栈深 = 递归深度，过深会栈溢出。Python 不保证尾递归优化，不应依赖它消除栈深。

### 分治三步

1. **分（divide）**：把问题切成规模相当的子问题。
2. **治（conquer）**：递归求解子问题。
3. **合（combine）**：合并子解为原解。

### 经典案例

- **归并排序（merge sort）**：分两半各排序再合并，$O(n\log n)$，分治的范式。
- **快速排序（quick sort）**：选基准分区，递归两侧，平均 $O(n\log n)$。
- **二分搜索**：每次折半，递归/迭代皆可。
- **汉诺塔（Tower of Hanoi）**：移 $n$ 盘 = 移 $n-1$ 盘 + 移 1 盘 + 移 $n-1$ 盘，$O(2^n)$。见 [Hanoi 可视化](../../code/visualizations/Hanoi.html)。

### 递归 vs 迭代

任何递归都可改写为迭代（用显式栈模拟）。递归更接近问题结构、易读；迭代常更省内存。两者等价但取舍看场景。

### 主定理（Master Theorem，导论层面了解）

分治 $T(n)=aT(n/b)+f(n)$ 的复杂度有规可循，归并 $a=2,b=2,f(n)=O(n)$ 得 $O(n\log n)$。详见 [`ext-complexity`](ext-complexity.md)。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 递归 | 德罗斯特效应——画中画，每层都是自己 |
| 基线条件 | 俄罗斯套娃最里面那颗实心 |
| 分治 | 把大蛋糕切几块各吃各的 |
| 汉诺塔 | 「先搬走上面的，再搬底下大的，再搬回上面」 |

## 前沿进展注记

基础稳定。递归思想在函数式编程（[`03`](03-programming-language.md)）和树/图算法中是根基，不随前沿变化。

## 跨学科联系

- **与数学**：数学归纳法是递归的逻辑对偶；斐波那契递推。
- **与生物/医学**：分形结构（血管/肺泡）天然递归；医学影像的八叉树分割。
- **与机械/材料**：有限元自适应网格细分本质是递归细分。

## 主动学习任务

1. 递归为什么必须有基线条件？没有会怎样？
2. 归并排序为什么稳定在 $O(n\log n)$，不像快排会退化？
3. 汉诺塔 $n=64$ 要多少步？为什么传说里僧侣搬到世界末日（$2^{64}-1$）？
4. 递归和迭代哪个更好？怎么选？
5. 用递归思路描述你专业里一个「自相似」的过程。

## 常见误区与边界

- 有基线条件仍不保证终止；递归参数必须朝基线推进。
- 递归是实现方式，分治是问题结构；两者不等同。
- 同一子问题被重复计算会造成指数增长，记忆化可复用结果。
- Python 的递归深度有限，不应把深递归用于任意大线性输入。

## 代码示例

```python
# 对应 docs/cards/ext-recursion-divide-conquer；汉诺塔 + 归并排序
def hanoi(n, src, mid, dst):
    """汉诺塔：n 盘从 src 借 mid 移到 dst"""
    if n == 0: return              # 基线
    hanoi(n-1, src, dst, mid)      # 把上面 n-1 移到中转
    print(f"{src} -> {dst}")       # 移最底下大的
    hanoi(n-1, mid, src, dst)      # 把 n-1 移回目标

def merge_sort(a):
    if len(a) <= 1: return a       # 基线
    mid = len(a)//2
    L, R = merge_sort(a[:mid]), merge_sort(a[mid:])
    out = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: out.append(L[i]); i += 1
        else: out.append(R[j]); j += 1
    return out + L[i:] + R[j:]

if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')
    print(merge_sort([5,2,4,7,1,3,6]))
```

## 延伸阅读

- 对照课程：Berkeley CS61A（recursion/tree recursion）、Stanford CS106A（recursion/backtracking）。
- 关联：[`04`](04-data-structure-basics.md)（调用栈）、[`07`](07-greedy-algorithm.md)（贪心 vs 分治）、[`ext-complexity`](ext-complexity.md)（主定理）。
- 配合 [汉诺塔可视化](../../code/visualizations/Hanoi.html)。

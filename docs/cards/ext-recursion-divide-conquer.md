---
title: 递归与分治
lecture: 扩展（无单独讲稿，参考 CS61A / CS106A）
aliases: [递归, 分治, 基线条件, 归并排序, 汉诺塔]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [递归, 分治, 归并排序, 汉诺塔, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [04-data-structure-basics, 06-graph-exploration, 07-greedy-algorithm, ext-complexity]
related_deep: []
related_visualizations: [Hanoi]
last_reviewed: 2026-08-03
---

# 递归与分治（Recursion & Divide-and-Conquer）

> 扩展卡片：Berkeley CS61A 与 Stanford CS106A 的重点主题，21 讲散见于贪心/图遍历，未单独成讲。

## 一句话定位

递归（recursion）是「用自己定义自己」——把大问题化成同型的更小子问题，直到触底。分治（divide-and-conquer）是其工程化范式：分、治、合。

## 核心知识点

### 递归的两个要件

1. **基线条件（base case）**：最小可直接求解的情形——递归的出口，否则无限递归。
2. **递推关系（recursive step）**：把问题化为更小的同类问题。
- 直觉：站在队首问「我后面有几个人」——若没人就答 0（基线），否则问下一个人再加 1（递推）。

### 调用栈与递归

每次递归调用在调用栈压一帧（见 [`04`](04-data-structure-basics.md) 栈）。栈深 = 递归深度，过深会栈溢出。尾递归优化可把部分递归转为迭代。

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

## 推荐交互式问答

1. 递归为什么必须有基线条件？没有会怎样？
2. 归并排序为什么稳定在 $O(n\log n)$，不像快排会退化？
3. 汉诺塔 $n=64$ 要多少步？为什么传说里僧侣搬到世界末日（$2^{64}-1$）？
4. 递归和迭代哪个更好？怎么选？
5. 用递归思路描述你专业里一个「自相似」的过程。

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

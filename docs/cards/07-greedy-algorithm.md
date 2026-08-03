---
title: 贪心算法
lecture: Slide07-GreedyAlgorithm-2025
aliases: [贪心, 贪心策略, 最优子结构, 贪心选择]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [贪心算法, 最优子结构, 贪心选择, 活动选择, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [06-graph-exploration, 08-turing-machine]
related_deep: []
related_visualizations: [Hanoi]
last_reviewed: 2026-08-03
---

# 贪心算法（Greedy Algorithm）

> 对应讲稿：[`Slide07-GreedyAlgorithm-2025.pdf`](../../LectureNotes/Slide07-GreedyAlgorithm-2025.pdf)

## 一句话定位

贪心（greedy）在每一步都选「当前看起来最好」的选项，期望最终得到全局最优。它简单高效，但**只在满足特定结构时才正确**。

## 核心知识点

### 贪心策略

每步做局部最优选择，不回溯、不调整。
- 优点：实现简单、速度快（常 $O(n\log n)$）。
- 风险：局部最优 ≠ 全局最优，需要**证明**该问题满足贪心条件。

### 正确性的两个支柱

1. **贪心选择性质（greedy-choice property）**：局部最优选择能包含在某个全局最优解中。
2. **最优子结构（optimal substructure）**：做出选择后，剩余子问题的最优解 + 该选择 = 原问题最优解。

二者同时成立时贪心才正确；否则需用动态规划（见扩展）或回溯。

### 经典案例

- **活动选择（interval scheduling）**：选最多互不重叠的活动。按结束时间排序，每步选结束最早且可行的活动——贪心正确。
- **最小生成树**：Prim / Kruskal 在图上贪心选最小权边。
- **Huffman 编码**：贪心合并频率最低的两棵树，得最优前缀码。
- **找零问题**：对「标准币制」贪心正确，但对任意币制不一定（如币种 1,3,4 凑 6，贪心得 4+1+1=3 枚，最优是 3+3=2 枚）。

### 贪心 vs 动态规划

两者都依赖最优子结构。区别：
- 贪心：做选择后**不回头**，子问题唯一确定。
- 动态规划：枚举所有选择，保留最优，子问题重叠。
- 不确定能否贪心时，先想「反例」——能否构造一个让贪心失败的输入。

## 直觉类比（跨学科桥接）

| 概念 | 类比 |
|---|---|
| 贪心 | 找零时总拿最大面额；超市结账时总选最短队 |
| 贪心失败 | 登山只看眼前陡峭可能错过绕远路的主峰 |
| 最优子结构 | 最短路径的子路径仍是最短（Bellman 最优性原理） |
| 活动选择 | 医生排班：选结束最早的检查，留出更多后续时间 |

## 前沿进展注记

贪心范式本身稳定。但「贪心思想」在 AI 中的回响值得注意：强化学习的 $\epsilon$-greedy 策略（多数时贪心、偶尔探索）正是对纯贪心易陷局部最优的修正。详见 `deep/reinforcement-learning.md`。

## 跨学科联系

- **与数学**：组合优化；贪心正确性证明常用交换论证（exchange argument）。
- **与医学**：医疗资源调度、放疗射束方向优化（贪心初始化 + 局部搜索）。
- **与经济学**：市场中的短视决策与「看不见的手」——个体贪心能否达成全局最优是博弈论核心议题。

## 推荐交互式问答

1. 找零问题在标准币制（1,5,10,25）下贪心正确，为什么？给一个反例币制说明它何时失败。
2. 活动选择为什么按「结束时间」而非「开始时间」排序贪心？给出直觉。
3. 如何判断一个问题该用贪心还是动态规划？（提示：能否构造反例）
4. 汉诺塔（见 [Hanoi 可视化](../../code/visualizations/Hanoi.html)）是贪心还是递归？为什么贪心在这里不适用？

## 代码示例

```python
# 对应 docs/cards/07；活动选择（贪心正确范例）+ 找零（贪心未必正确）
# 运行：uv run python code/examples/07_greedy_activity.py

def activity_selection(intervals):
    """选最多互不重叠区间：按结束时间贪心"""
    intervals = sorted(intervals, key=lambda x: x[1])  # 按结束时间排序
    chosen = []
    last_end = float('-inf')
    for s, e in intervals:
        if s >= last_end:
            chosen.append((s, e)); last_end = e
    return chosen

def greedy_coin(amount, coins):
    """贪心找零——未必最优"""
    coins = sorted(coins, reverse=True)
    res = []
    for c in coins:
        while amount >= c:
            amount -= c; res.append(c)
    return res if amount == 0 else None

if __name__ == "__main__":
    acts = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,12)]
    print("活动选择:", activity_selection(acts))  # [(1,4),(5,7),(8,12)] 等
    print("标准币制贪心 6 =", greedy_coin(6, [1,3,4]))  # [4,1,1] 不是最优
```

## 延伸阅读

- 对应讲稿 `Slide07-GreedyAlgorithm-2025.pdf`。
- 关联：`06`（图上贪心：MST/Dijkstra）、扩展 `动态规划`（贪心失败时的替代）。
- 经典教材：Cormen, T. et al. (2009). *Introduction to Algorithms*, Ch.16.（贪心算法）

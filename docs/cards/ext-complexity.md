---
title: 算法复杂度
lecture: 扩展（无单独讲稿，参考 MIT 6.0001 / CS50）
aliases: [复杂度, Big-O, 时间复杂度, 空间复杂度, 渐近分析, P/NP]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [复杂度, Big-O, 渐近分析, P/NP, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [06-graph-exploration, 07-greedy-algorithm, 05-data-structure-advanced, 08-turing-machine]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 算法复杂度（Algorithm Complexity）

> 扩展卡片：21 讲未单独成讲，但 MIT 6.0001 / Harvard CS50 等导论均作重点。补全教学完整性。

## 一句话定位

算法复杂度（algorithm complexity）用 **Big-O** 渐近记号刻画算法随输入规模 $n$ 增长时的资源消耗趋势——回答「当数据变大，它还能不能用」。它是判断算法好坏的通用语言。

## 核心知识点

### 为什么需要复杂度

- 比较算法不能只看某次运行的秒数——取决于硬件、输入、实现。
- 复杂度抽象掉常数与低阶项，只保留**增长趋势**，给出硬件无关的判断。

### Big-O 记号（渐近上界）

$f(n)=O(g(n))$ 表示 $f$ 增长不超过 $g$ 的常数倍。
- 常见阶（由快到慢）：$O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(2^n) < O(n!)$。
- 直觉：$n=10^6$ 时，$O(n)$ 约百万次可行；$O(n^2)$ 约 $10^{12}$ 次不可行；$O(2^n)$ 天文数字。

### 最好 / 最坏 / 平均

- 同一算法不同输入表现不同。
- 最坏（worst-case）：保证上界，安全攸关场景看这个。
- 平均（average-case）：期望表现，常更乐观。
- 例如快排：平均 $O(n\log n)$，最坏 $O(n^2)$。

### 时间与空间复杂度

- 时间：运算次数随 $n$ 的增长。
- 空间：额外内存随 $n$ 的增长。
- 常有「时间换空间」或反之的权衡。

### 复杂度类（导论层面）

- **P**：多项式时间可解（「易解」）。
- **NP**：多项式时间可验证（不一定易解）。
- **NP-完全**：NP 中最难的一类，若任一有多项式解则 P=NP。
- **不可解/不可判定**：停机问题等（见 [`08-turing-machine`](08-turing-machine.md)）——不是慢，是逻辑上无解。

## 直觉类比

| 阶 | 类比 |
|---|---|
| $O(1)$ | 直接翻到书签页 |
| $O(\log n)$ | 二分查字典，每次折半 |
| $O(n)$ | 逐页翻一遍 |
| $O(n\log n)$ | 排序的典型代价 |
| $O(n^2)$ | 两两比对所有人 |
| $O(2^n)$ | 子集枚举，n 大了就崩 |

## 前沿进展注记

复杂度理论基础稳定。P vs NP 是千禧七大难题之一，仍未解。复杂度本身是算法评估的通用框架，不被前沿颠覆。

## 跨学科联系

- **与数学**：渐近分析、极限、组合计数。
- **与船舶/航空航天工程**：CFD/有限元仿真的网格规模动辄上亿，算法复杂度决定能否在算力预算内完成——$O(n)$ 与 $O(n^2)$ 在大网格下是天壤之别。
- **与医学**：基因比对若用 $O(2^n)$ 不可行，BLAST 等用启发式降到近似线性。

## 推荐交互式问答

1. 为什么不能直接比「跑几秒」来评判算法？
2. $O(n\log n)$ 和 $O(n^2)$，$n=1000$ 时差多少倍？
3. 快排最坏为什么 $O(n^2)$？怎么避免？
4. P 和 NP 的区别用一句话说清？P=NP 为什么是难题？
5. 你专业的某计算任务，复杂度从 $O(n^2)$ 优化到 $O(n\log n)$ 意味着什么？

## 代码示例

```python
# 对应 docs/cards/ext-complexity；直观对比 O(n) vs O(n^2) vs O(2^n)
import time

def linear(n):   # O(n)
    s = 0
    for i in range(n): s += i
    return s

def quadratic(n): # O(n^2)
    s = 0
    for i in range(n):
        for j in range(n): s += 1
    return s

for n in [1000, 10000]:
    t = time.perf_counter(); linear(n);    print(f"O(n)    n={n:>6}: {time.perf_counter()-t:.4f}s")
    t = time.perf_counter(); quadratic(n); print(f"O(n^2)   n={n:>6}: {time.perf_counter()-t:.4f}s")
# n=10000 时 O(n^2) 比 O(n) 慢约 n 倍
```

## 延伸阅读

- 对照课程：MIT 6.0001（复杂度 lecture）、Harvard CS50（algorithms）。
- 关联：[`06`](06-graph-exploration.md)（BFS/DFS 的 $O(V+E)$）、[`07`](07-greedy-algorithm.md)（贪心的复杂度）、[`08`](08-turing-machine.md)（可解 vs 不可解）。
- 经典：Cormen, T. et al. (2009). *Introduction to Algorithms*, Ch.1–3.

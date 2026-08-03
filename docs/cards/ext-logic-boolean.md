---
title: 数理逻辑与布尔代数
lecture: 扩展（无单独讲稿，参考 Dale Ch4 / 旧 45 篇规划）
aliases: [布尔代数, 逻辑门, 真值表, 与或非, 数字逻辑]
thinking_pillar: 计算思维
category: fundamentals
tags: [布尔代数, 逻辑门, 真值表, 数字逻辑, 入门]
status: stable
version: 1.0
importance: 3
related_cards: [08-turing-machine, 09-computer-system-arch, 03-programming-language]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 数理逻辑与布尔代数（Logic & Boolean Algebra）

> 扩展卡片：数字电路与程序逻辑的数学基础，21 讲未单独成讲，但 [`09`](09-computer-system-arch.md) 硬件与 [`03`](03-programming-language.md) 条件判断都依赖它。

## 一句话定位

布尔代数（Boolean algebra）用「真/假」两值做逻辑运算，是数字电路（硬件）和程序条件判断（软件）共同的数学基础。George Boole 1854 提出，Shannon 1938 把它接到电路上——从此逻辑与电路统一。

## 核心知识点

### 三个基本运算

- **与（AND, $\land$）**：全真才真。
- **或（OR, $\lor$）**：有真即真。
- **非（NOT, $\lnot$）**：真假翻转。
- 派生：**与非 NAND**、**或非 NOR**、**异或 XOR**（不同为真）。

### 真值表

穷举所有输入组合列输出。例：异或 XOR：

| A | B | A XOR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 逻辑门与数字电路

- 每个布尔运算对应一个物理电路：与门、或门、非门。
- 组合门能实现任意布尔函数——这是 [`09`](09-computer-system-arch.md) 从逻辑门到加法器再到 CPU 的根基。
- **NAND 是功能完备的**：只用与非门能搭出任何逻辑。

### 布尔代数定律

- 交换/结合/分配律类似普通代数。
- **德摩根律**：$\lnot(A\land B)=\lnot A\lor\lnot B$；$\lnot(A\lor B)=\lnot A\land\lnot B$。
- 可化简逻辑表达式 → 化简电路（少门少本）。

### 与程序逻辑的关系

- `if (A and B)`、`while (not done)` 里的 `and/or/not` 就是布尔运算。
- 程序的条件分支本质是布尔表达式驱动（关联 [`03`](03-programming-language.md)）。
- 短路求值：`A and B` 若 A 假则不评估 B——既是优化也是语义。

### 与图灵机/可计算性

- 布尔逻辑是组合电路的语言；加时序（时钟、寄存器）成时序电路，能造出图灵等价的 CPU（关联 [`08`](08-turing-machine.md)）。

## 直觉类比

| 概念 | 类比 |
|---|---|
| AND | 两道保险锁都开才通 |
| OR | 任一道门开就通 |
| NOT | 反向开关 |
| XOR | 「单刀双掷」——只能选一个 |
| 德摩根律 | 「不(都去)」=「有一个不去」 |
| NAND 万能 | 用一种乐高积木能拼出任何结构 |

## 前沿进展注记

布尔代数是数字时代根基，本身不变。量子计算扩展了经典布尔逻辑——量子比特的叠加使量子逻辑门处理的是更一般的复振幅，但测量塌缩后仍是布尔结果（见 [`deep/quantum-computing`](../deep/quantum-computing.md)）。

## 跨学科联系

- **与数学**：数理逻辑、集合运算（与=交、或=并、非=补）。
- **与物理/电子**：逻辑门的物理实现（CMOS），功耗与散热是硬件设计核心约束。
- **与医学**：临床决策规则可形式化为布尔表达式（「发热 AND 咳嗽 AND 旅行史 → 检测」）。
- **与工科**：PLC 与工业控制逻辑本质是布尔/状态机；船舶/化工的联锁保护系统靠逻辑门保证安全。

## 推荐交互式问答

1. 为什么说「软件的 if 和硬件的与门是同一个东西」？
2. NAND 为什么是功能完备的？用只用 NAND 搭一个 OR。
3. 德摩根律怎么帮你化简 `not (A and B)`？
4. 短路求值既是优化也是语义，举例说明危险性。
5. 把你专业里一条「规则」写成布尔表达式。

## 代码示例

```python
# 对应 docs/cards/ext-logic-boolean；布尔运算与真值表生成
def truth_table(func, n=2):
    """生成 n 输入布尔函数的真值表"""
    for i in range(2**n):
        bits = [(i >> (n-1-k)) & 1 for k in range(n)]
        print(f"{bits} -> {int(func(*bits))}")

# 异或：不同为 1
xor = lambda a, b: a != b
# 与非
nand = lambda a, b: not (a and b)
# 用纯 NAND 搭 OR：OR(a,b) = NAND(NAND(a,a), NAND(b,b))
or_from_nand = lambda a, b: nand(nand(a,a), nand(b,b))

print("XOR:"); truth_table(xor)
print("OR(纯NAND):"); truth_table(or_from_nand)
```

## 延伸阅读

- 对照课程：Dale & Lewis, *Computer Science Illuminated*, Ch.4（旧 45 篇规划曾列）。
- 关联：[`09`](09-computer-system-arch.md)（从逻辑门到 CPU）、[`08`](08-turing-machine.md)（逻辑→可计算）、[`03`](03-programming-language.md)（程序里的布尔表达式）。
- 历史：Boole, G. (1854). *An Investigation of the Laws of Thought*; Shannon, C. (1938). A Symbolic Analysis of Relay and Switching Circuits.

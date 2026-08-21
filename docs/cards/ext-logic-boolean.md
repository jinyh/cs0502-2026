---
title: 数理逻辑与布尔代数
card_id: boolean-logic
lecture_refs: [L02, L03, L08]
source_slides: [Slide03-ProgrammingLanguage-2025, Slide09-ComputerSystemAndArchitecture-2025]
aliases: [布尔代数, 逻辑门, 真值表, 与或非, 数字逻辑]
thinking_pillars: [计算思维, 系统思维]
category: fundamentals
tags: [布尔代数, 逻辑门, 真值表, 数字逻辑, 入门]
status: needs-review
version: 1.0
importance: 3
learning_objectives: [构造和解释真值表, 使用德摩根律变换条件, 连接程序条件与逻辑门]
prerequisites: []
estimated_minutes: 30
assessment_tags: [真值表, 逻辑化简, 条件追踪]
labs: []
figures: []
related_cards: [data-representation, computer-architecture, 03-programming-language, computability-limits]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-22
---

# 数理逻辑与布尔代数（Logic & Boolean Algebra）

> 扩展卡片：数字电路与程序逻辑的数学基础，21 讲未单独成讲，但 [`09`](09-computer-system-arch.md) 硬件与 [`03`](03-programming-language.md) 条件判断都依赖它。

## 一句话定位

布尔代数（Boolean algebra）用「真/假」两值做逻辑运算，是数字电路（硬件）和程序条件判断（软件）共同的数学基础。George Boole 1854 提出，Shannon 1938 把它接到电路上——从此逻辑与电路统一。

## 学完应能做到

1. 为不超过三个输入的布尔表达式构造和解释真值表。
2. 使用德摩根律改写否定条件，并追踪短路求值。
3. 说明程序条件、集合运算与数字逻辑门之间的共同结构。

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

## 主动学习任务

1. 为什么说「软件的 if 和硬件的与门是同一个东西」？
2. NAND 为什么是功能完备的？用只用 NAND 搭一个 OR。
3. 德摩根律怎么帮你化简 `not (A and B)`？
4. 短路求值既是优化也是语义，举例说明危险性。
5. 把你专业里一条「规则」写成布尔表达式。

## 常见误区与边界

- `A or B` 与自然语言“二选一”不同：普通 OR 允许两者都真，异或 XOR 才要求不同。
- 德摩根律取反时要同时交换 AND/OR，并否定每个条件。
- 短路求值可能跳过带副作用的表达式；不能只按代数结果理解执行。
- 真实临床和工程规则常含连续量、不确定性和例外，不能强行压成简单布尔判断。

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

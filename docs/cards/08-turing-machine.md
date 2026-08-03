---
title: 图灵机与可计算性
lecture: Slide08-TuringMachine-2025
aliases: [图灵机, 可计算性, 停机问题, 丘奇-图灵论题, 计算复杂性]
thinking_pillar: 计算思维
category: fundamentals
tags: [图灵机, 可计算性, 停机问题, 丘奇-图灵论题, 形式化]
status: stable
version: 1.0
importance: 5
related_cards: [02-intro-to-cs, 09-computer-system-arch]
related_deep: []
related_visualizations: [TuringMachine]
last_reviewed: 2026-08-03
---

# 图灵机与可计算性（Turing Machine & Computability）

> 对应讲稿：[`Slide08-TuringMachine-2025.pdf`](../../LectureNotes/Slide08-TuringMachine-2025.pdf)

## 一句话定位

图灵机（Turing machine）是「机械计算」的数学模型，它划定了**什么是可计算的**——以及，有些问题根本不可计算。这是计算机科学最深刻的边界。

## 核心知识点

### 图灵机模型

Alan Turing（1936）提出的一台抽象机器：
- 无限长纸带（tape），分成格子，每格一个符号。
- 读写头（head），可在纸带上左右移动、读写。
- 有限状态控制器（state register），当前处于某个状态。
- 转移规则（transition function）：根据当前状态 + 读到的符号，决定写什么、移向、进入哪个状态。

形式化：$M = (Q, \Sigma, \delta, q_0, F)$。看起来简陋，但 Turing 证明它能模拟任何「机械可计算」的过程。

### 丘奇-图灵论题（Church-Turing Thesis）

一切「直觉上可计算」的函数，都能被图灵机计算。这是论题（thesis）而非定理——它把「可计算」这个模糊概念锚定到图灵机这个精确模型上。现代编程语言互相等价，本质上都是图灵机等价（Turing complete）。

### 停机问题（Halting Problem）

是否存在一个程序 $H$，能判断任意程序 $P$ 在输入 $x$ 上是否会停机（而非死循环）？
- Turing 用对角线法证明：**不存在**。
- 构造 $D(P)$：若 $H(P,P)=停$ 则死循环，否则停。问 $H(D,D)$ 得矛盾。
- **意义**：这是数学上「不可判定」（undecidable）问题的范例——不是我们不够聪明，而是逻辑上不可能。

### 可计算性的层次

- 可判定（decidable）：存在算法给出是/否答案。
- 不可判定：如停机问题，无算法可解。
- 计算复杂性：可解但可能太慢（如 NP 问题），属另一维度——见 `08-complexity-theory`（可选扩展）。

### 图灵机与现代计算机

冯诺依曼架构（见 `09-computer-system-arch`）是图灵机的物理实现。**真实计算机 = 受限图灵机**（纸带有限=内存有限），但理论分析仍用无限纸带的图灵机作基准。

## 直觉类比（跨学科桥接）

| 概念 | 类比 |
|---|---|
| 图灵机纸带 | 录音磁带；电影胶片逐帧读取 |
| 有限状态 + 无限纸带 | 大脑短期记忆有限，但可用笔记本无限记录 |
| 停机问题不可解 | 医生无法预知某种治疗对个体最终是否有效——不是技术限制，是可预测性的逻辑边界 |
| 丘奇-图灵论题 | 「能算的都能用算盘算」——锚定模糊直觉到精确工具 |

## 前沿进展注记

经典可计算性理论稳定。但 AI 时代的新议题：大语言模型是否接近「通用智能」？图灵机仍是理论基准——任何基于冯诺依曼硬件的计算都是图灵等价，LLM 也不例外。它突破的是「实用计算能力」边界，而非可计算性理论边界。详见 `21-llm` 与 `deep/llm-deep-dive.md`。

量子计算（见 `deep/quantum-computing.md`）在**复杂度**维度上可能加速某些问题，但不打破丘奇-图灵论题——量子图灵机与经典图灵机可计算同样的函数。

## 跨学科联系

- **与数学**：哥德尔不完备定理与停机问题同构——都揭示形式系统的根本局限。图灵正是受哥德尔启发。
- **与哲学**：图灵测试（1950）把「智能」操作化为「对话不可分辨」，是 AI 哲学的起点。
- **与医学/生物**：Turing 形态发生理论（reaction-diffusion）解释生物斑纹——同一位 Turing 的另一面。

## 推荐交互式问答

1. 图灵机这么简陋，为什么能代表「一切可计算」？丘奇-图灵论题是定理吗？
2. 停机问题为什么不可解？用自己的话复述对角线矛盾。
3. 我的手机和图灵机有什么关系？它是受限的图灵机吗？
4. 既然 LLM 跑在图灵等价的硬件上，它算「突破可计算性边界」了吗？它突破的是什么？

## 代码示例

```python
# 对应 docs/cards/08；一个最简图灵机模拟器（二进制加 1）
# 运行：uv run python code/examples/08_turing_simulator.py
# 配合可视化：code/visualizations/TuringMachine.html

def turing_add_one(tape_str):
    """图灵机：在二进制串 tape_str 上做 +1。读写头从最右开始。
    规则：从右扫到左，遇到 0 改 1 停机；遇到 1 改 0 继续进位。"""
    tape = list(tape_str)
    head = len(tape) - 1
    while head >= 0:
        if tape[head] == '0':
            tape[head] = '1'; return ''.join(tape)   # 无进位，停机
        else:
            tape[head] = '0'; head -= 1               # 进位继续
    return '1' + ''.join(tape)                        # 全进位，最高位补 1

if __name__ == "__main__":
    for s in ["0", "1", "10", "11", "1011"]:
        print(f"{s} + 1 = {turing_add_one(s)}")
    # 1011 + 1 = 1100
```

## 延伸阅读

- 对应讲稿 `Slide08-TuringMachine-2025.pdf`。
- 配合 [图灵机可视化](../../code/visualizations/TuringMachine.html)。
- 关联：`02`（CS 的边界）、`09`（冯诺依曼实现）。
- 原始文献：Turing, A. M. (1936). On Computable Numbers. *Proc. London Math. Soc.*

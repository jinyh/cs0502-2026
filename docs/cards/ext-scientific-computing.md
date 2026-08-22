---
title: 科学计算与可重复实验
card_id: scientific-computing
lecture_refs: [L02, L11, L15]
source_slides: []
aliases: [浮点误差, 数值稳定性, 科学计算, 可重复性]
thinking_pillars: [计算思维, 数据思维]
category: scientific-computing
tags: [浮点数, 舍入误差, 数值稳定性, 随机种子, 可重复研究]
status: ai-reviewed
version: 1.0
importance: 4
learning_objectives: [识别浮点和测量误差, 比较稳定与不稳定计算, 记录可重复实验条件]
prerequisites: [data-representation, 03-programming-language]
estimated_minutes: 35
assessment_tags: [误差诊断, 数值比较, 实验复现]
labs: []
figures: [02-data-representation.svg, 11-reproducibility-chain.svg]
related_cards: [data-representation, reproducible-computing, probability-uncertainty, 15-data-visualization]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-22
---

# 科学计算与可重复实验（Scientific Computing and Reproducibility）

## 一句话定位

计算机表示的是有限精度近似值；可信的计算实验必须同时控制数值误差、算法稳定性、数据与代码版本以及随机性。

## 学完应能做到

1. 区分表示、舍入、截断、测量和模型误差，并说明它们如何传播。
2. 比较数学等价但数值稳定性不同的计算形式。
3. 为计算实验记录输入、单位、版本、环境、参数、随机性与评价步骤。

## 核心知识点

- 二进制浮点数不能精确表示所有十进制小数，`0.1 + 0.2` 可能不严格等于 `0.3`。
- 舍入误差会累积；两个接近的大数相减可能丢失有效数字。
- 数值稳定算法不会无谓放大输入与舍入误差。
- 报告结果时记录输入数据、单位、软件环境、参数、随机种子和评价脚本。
- “同一种子”帮助复现随机流程，但不同硬件、并行实现或库版本仍可能带来差异。

### 误差来源与传播

- **表示误差**来自有限位数；**截断误差**来自用有限步骤近似无限过程。
- **测量误差**来自仪器与采样；**模型误差**来自对现实的简化。
- 条件数描述问题对输入扰动的敏感程度；稳定算法避免额外放大误差。
- 两个接近大数相减会损失有效数字，可通过代数变形或更合适的公式缓解。

### 比较与报告

- 浮点数比较使用与问题尺度相称的绝对/相对容差。
- 结果应带单位、有效数字和误差/不确定性，而不是输出越多小数越“科学”。
- 运行时间、内存和结果精度应在同一输入与环境下比较。

## 工程桥接

有限元、流体仿真、控制优化、材料计算和机器学习都依赖数值近似。结果看似精确不等于模型、离散化和实现误差足够小。

## 常见误区与边界

- `0.1 + 0.2 != 0.3` 通常是表示近似，不是 Python 随机算错。
- 改用更多位只能减小一类舍入误差，不能修复错误模型或采样偏差。
- 固定随机种子不能证明结果稳定，应检查多个种子和环境。
- 输出十位小数不代表有十位有效精度。

## 最小代码观察

运行 [`02_data_representation.py`](../../code/examples/02_data_representation.py)，再设计一个容差比较；实验版本与证据链见 [`reproducible-computing`](reproducible-computing.md)。

## 主动学习与考核迁移

1. 运行 `0.1 + 0.2 == 0.3`，解释现象而不是把它称为 Python 错误。
2. 比较重复相加与更稳定求和方法可能产生的差异。
3. 为一项机器学习实验列出最少需要记录的六项信息。

## 延伸阅读

- Goldberg, D. (1991). What Every Computer Scientist Should Know About Floating-Point Arithmetic. *ACM Computing Surveys*.
- Higham, N. *Accuracy and Stability of Numerical Algorithms*.

---
title: 科学计算与可重复实验
lecture: 扩展（面向理工科计算实践）
aliases: [浮点误差, 数值稳定性, 科学计算, 可重复性]
thinking_pillar: 数据思维
category: scientific-computing
tags: [浮点数, 舍入误差, 数值稳定性, 随机种子, 可重复研究]
status: needs-review
version: 1.0
importance: 4
related_cards: [03-programming-language, 05-data-structure-advanced, 15-data-visualization, 17-machine-learning]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 科学计算与可重复实验（Scientific Computing and Reproducibility）

## 一句话定位

计算机表示的是有限精度近似值；可信的计算实验必须同时控制数值误差、算法稳定性、数据与代码版本以及随机性。

## 核心知识点

- 二进制浮点数不能精确表示所有十进制小数，`0.1 + 0.2` 可能不严格等于 `0.3`。
- 舍入误差会累积；两个接近的大数相减可能丢失有效数字。
- 数值稳定算法不会无谓放大输入与舍入误差。
- 报告结果时记录输入数据、单位、软件环境、参数、随机种子和评价脚本。
- “同一种子”帮助复现随机流程，但不同硬件、并行实现或库版本仍可能带来差异。

## 工程桥接

有限元、流体仿真、控制优化、材料计算和机器学习都依赖数值近似。结果看似精确不等于模型、离散化和实现误差足够小。

## 主动学习与考核迁移

1. 运行 `0.1 + 0.2 == 0.3`，解释现象而不是把它称为 Python 错误。
2. 比较重复相加与更稳定求和方法可能产生的差异。
3. 为一项机器学习实验列出最少需要记录的六项信息。

---
title: 数据可视化
lecture: Slide15-DataVisualization-2025
aliases: [可视化, 图表, 感知编码, 探索性分析]
thinking_pillar: 数据思维
category: data
tags: [可视化, 图表, 感知, EDA, 入门]
status: stable
version: 1.0
importance: 3
related_cards: [14-data-mining, 17-machine-learning]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 数据可视化（Data Visualization）

> 对应讲稿：`Slide15-DataVisualization-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

数据可视化（data visualization）把抽象数据映射为视觉元素，让人眼——这个强大的模式识别器——直接发现规律与异常。它既是**分析工具**也是**沟通语言**。

## 核心知识点

### 为什么可视化

- 人眼擅长比较长度/位置/颜色，不擅长比较面积/角度。
- 图能揭示表格看不出的模式（Anscombe 四组同统计量但分布迥异的数据）。
- 但也能骗人——坏图制造误导。

### 图表类型与选择

- 比较：柱状图。
- 趋势：折线图。
- 分布：直方图、箱线图。
- 关系：散点图。
- 构成：堆叠图、树图。
- 高维：热力图、平行坐标、降维投影。
- 选择依据：数据类型 + 要回答的问题。

### 感知与编码

- 有效性排序（Cleveland & McGill）：位置 > 长度 > 角度/斜率 > 面积 > 颜色亮度/饱和度。
- 色盲友好调色板（如 viridis）；避免彩虹色板。
- 直觉：用最易精确比较的通道编码最重要的量。

### 探索性数据分析（EDA）

可视化是 EDA 第一步——先看数据再建模。Tukey 名言：「没有图，就没有分析。」

### 误导与伦理

- 截断 y 轴夸大差异、3D 饼图扭曲面积、双重 y 轴制造假关联。
- 可视化不是中立呈现，选型本身是立场。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 可视化编码 | 把抽象数值翻译成眼睛能「直接读」的长度 |
| 感知有效性 | 用尺子量长度比目测面积准 |
| Anscombe 现象 | 同样化验指标的病人，分布形态可能完全不同 |
| 坏图 | 裁切照片突出某局部，扭曲整体印象 |

## 前沿进展注记

- 交互式可视化（plotly/D3）、仪表盘。
- LLM 辅助：自然语言生成图表、自动解读。
- 可解释 AI：用可视化解释模型决策（关联 `17`）。

## 跨学科联系

- 与认知科学：视觉感知通道、格式塔原则。
- 与医学：影像可视化、流行病学地图（Snow 霍乱地图是经典）、患者流向图。
- 与统计：可视化与统计互证，避免被单一指标骗。

## 推荐交互式问答

1. 为什么散点图能看出表格看不出的关系？（Anscombe）
2. 面积图为什么不如柱状图精确？
3. 截断 y 轴在什么情况下是误导？
4. 医学论文里哪种图最常见？为什么？

## 代码示例

```python
# 对应 docs/cards/15；matplotlib 基础四图
# 运行：uv run python code/examples/15_viz.py  依赖：numpy matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(0,1,100); y = 0.6*x + np.random.normal(0,0.5,100)
fig, axs = plt.subplots(1,3, figsize=(12,3))
axs[0].hist(x, bins=20); axs[0].set_title('分布: 直方图')
axs[1].scatter(x,y); axs[1].set_title('关系: 散点图')
axs[2].boxplot([x,y]); axs[2].set_title('对比: 箱线图')
plt.tight_layout(); plt.savefig('figures/15_viz_demo.png', dpi=120)
```

## 延伸阅读

- 对应讲稿 `Slide15-DataVisualization-2025.pdf`。
- 关联：`14`（挖掘后呈现）、`17`（模型结果可视化）。
- 经典：Tufte, E. (2001). *The Visual Display of Quantitative Information*.

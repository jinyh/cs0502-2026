---
title: 数据挖掘
lecture: Slide14-DataMining-2025
aliases: [数据挖掘, 关联规则, 聚类, 分类, 知识发现]
thinking_pillar: 数据思维
category: data
tags: [数据挖掘, 关联规则, 聚类, 分类, KDD, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [13-database, 17-machine-learning, 15-data-visualization]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 数据挖掘（Data Mining）

> 对应讲稿：`Slide14-DataMining-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

数据挖掘（data mining）从海量数据中**发现模式与知识**（KDD：Knowledge Discovery in Databases）。它是机器学习（`17`）在数据密集场景的工程化落地。

## 核心知识点

### KDD 流程

数据清洗 → 集成 → 选择 → 变换 → 挖掘 → 评估 → 展示。
- 数据准备常占 80% 工作量——脏数据再好的算法也救不了。

### 主要任务

- **分类（classification）**：有监督，预测离散标签（如良/恶性）。
- **回归（regression）**：有监督，预测连续值。
- **聚类（clustering）**：无监督，把相似样本分组。
- **关联规则（association rules）**：找「买 A 也买 B」式共现。经典：啤酒与尿布。
- **异常检测（anomaly detection）**：找偏离常态的样本。

### 经典算法

- 关联：Apriori、FP-Growth。
- 聚类：K-Means、层次聚类、DBSCAN。
- 分类：决策树、朴素贝叶斯、SVM、随机森林（与 ML 重叠，见 `17`）。

### 评估

- 交叉验证防过拟合。
- 关联规则：支持度（support）、置信度（confidence）、提升度（lift）。

### 与机器学习的关系

数据挖掘是**任务/流程视角**，机器学习是**方法视角**，二者高度重叠。数据挖掘更强调业务落地与可解释性。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 聚类 | 把一抽屉混装标本按形态自动分组 |
| 分类 | 已知良恶性样本，学规则判新样本 |
| 关联规则 | 超市购物篮分析：哪些商品常一起买 |
| 异常检测 | 体检指标偏离人群常态预警 |

## 前沿进展注记

- 大模型参与数据挖掘：用 LLM 做特征提取、文本数据挖掘、零样本分类。
- 自动化机器学习（AutoML）：自动选模型与调参。
- 隐私：联邦数据挖掘——数据不动模型动。

## 跨学科联系

- 与医学：疾病模式发现、药物不良反应信号、基因表达聚类。
- 与商业：推荐（关联 `19`）、客户分群、欺诈检测。
- 与统计：假设检验、置信区间是评估基础。
- 与材料/航空航天：材料信息学从高通量计算数据中挖掘「结构-性质」关系加速新材料发现；遥感地学大数据的分类与变化检测。

## 推荐交互式问答

1. 数据挖掘和机器学习有什么区别与联系？
2. 关联规则的「支持度/置信度/提升度」各衡量什么？为什么光看置信度不够？
3. KDD 流程里数据清洗为何占大头？
4. 给定医院就诊记录，如何发现「某症状组合预示某病」？

## 代码示例

```python
# 对应 docs/cards/14；K-Means 聚类直觉
import numpy as np
def kmeans(X, k, iters=10, seed=0):
    rng = np.random.default_rng(seed)
    centers = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        labels = np.argmin(((X[:,None]-centers)**2).sum(2), axis=1)
        centers = np.array([X[labels==i].mean(0) for i in range(k)])
    return labels, centers
X = np.vstack([np.random.normal(0,1,(50,2)), np.random.normal(5,1,(50,2))])
labels, _ = kmeans(X, 2)
print("聚类标签（应近似前50=0后50=1）:", labels[:5], "...", labels[55:60])
```

## 延伸阅读

- 对应讲稿 `Slide14-DataMining-2025.pdf`。
- 关联：`13`（数据来源）、`17`（方法）、`15`（结果呈现）。
- 经典：Han, J. et al. (2011). *Data Mining: Concepts and Techniques*.

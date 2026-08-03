---
title: 机器学习
lecture: Slide17-MachineLearning-2025
aliases: [机器学习, 监督学习, 无监督学习, 强化学习, 训练, 泛化]
thinking_pillar: 智能思维
category: ai-ml
tags: [机器学习, 监督学习, 无监督学习, 训练, 泛化, 过拟合, 入门]
status: stable
version: 1.0
importance: 5
related_cards: [16-artificial-intelligence, 14-data-mining, 18-computer-vision, 21-llm]
related_deep: [llm-deep-dive, reinforcement-learning]
related_visualizations: []
last_reviewed: 2026-08-03
---

# 机器学习（Machine Learning）

> 对应讲稿：[`Slide17-MachineLearning-2025.pdf`](../../LectureNotes/Slide17-MachineLearning-2025.pdf)

## 一句话定位

机器学习（Machine Learning, ML）不靠人写死规则，而是让算法**从数据中归纳规律**。Tom Mitchell 的定义：如果某任务 $T$ 的性能 $P$ 随经验 $E$ 增长而提升，则称该程序从 $E$ 中学习。

## 核心知识点

### 三大学习范式

- **监督学习（supervised learning）**：给带标签数据 $(x_i, y_i)$，学映射 $f: x \to y$。如分类、回归。
- **无监督学习（unsupervised learning）**：数据无标签，找结构。如聚类、降维、密度估计。
- **强化学习（reinforcement learning, RL）**：agent 在环境里试错，最大化累计奖励。无标签，靠反馈信号。

（半监督、自监督是中间形态；自监督是 LLM 预训练的关键。）

### 监督学习的训练循环

1. 准备数据集，划分为训练 / 验证 / 测试集。
2. 选模型假设族 $\mathcal{H}$（如线性、神经网络）。
3. 定义损失函数（loss）$L$（如回归用 MSE、分类用交叉熵）。
4. 用优化器（梯度下降 gradient descent）最小化训练损失。
5. 在验证集上调参，在测试集上报最终性能。

### 关键张力：过拟合 vs 欠拟合

- **欠拟合（underfitting）**：模型太简单，训练误差大——没学到。
- **过拟合（overfitting）**：模型太复杂，记住训练集噪声，测试误差大——泛化差。
- **泛化（generalization）**：目标是在未见数据上表现好，而非训练集。
- 缓解：正则化（regularization）、更多数据、早停、dropout、交叉验证。
- **偏差-方差权衡（bias-variance tradeoff）**：欠拟合=高偏差，过拟合=高方差。

### 梯度下降

最小化损失 $L(\theta)$：$\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$，$\eta$ 为学习率（learning rate）。
- 直觉：蒙眼下山，每步沿最陡方向走。
- 深度学习用反向传播（backpropagation）高效算梯度。

### 评估指标

- 分类：准确率、精确率、召回率、F1、混淆矩阵。
- 回归：MSE、MAE、$R^2$。
- 注意类别不平衡时准确率会骗人（如 99% 负样本，全判负即 99% 准确但无用）。

## 直觉类比（跨学科桥接）

| 概念 | 类比 |
|---|---|
| 监督学习 | 带答案的题库刷题（每题有标准答案） |
| 无监督学习 | 给一抽屉杂乱标本，自己分出类别 |
| 强化学习 | 训练动物：做对给奖励、做错不给 |
| 过拟合 | 学生背题库答案但不会做新题 |
| 梯度下降 | 蒙眼下山，靠脚下坡度判断方向 |
| 泛化 | 临床经验能否应对未见过的新病例 |

## 前沿进展注记

ML 前沿变化快。基础框架稳定，但具体方法迭代迅速：
- 深度学习主导感知任务（见 `18-computer-vision`）。
- 自监督预训练 + 微调成为 NLP/多模态主流（见 `21-llm`）。
- 基础模型（foundation model）范式：一个预训练大模型适配多任务。

具体前沿见 [`frontier/`](../frontier/) 与 [`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)、[`deep/reinforcement-learning.md`](../deep/reinforcement-learning.md)。

## 跨学科联系

- **与统计学**：ML 与统计推断高度重叠；线性回归既是统计也是 ML。
- **与医学**：影像诊断、风险预测、个体化治疗；但需警惕分布偏移（训练集人群 ≠ 临床人群）导致偏见。
- **与物理**：能量模型、扩散模型借统计物理概念；梯度下降与势能地貌。
- **与信息论**：交叉熵损失的信息论解释——最小化预测分布与真实分布的 KL 散度。

## 推荐交互式问答

1. 监督、无监督、强化学习各给一个生活类比。
2. 过拟合为什么比欠拟合更隐蔽？如何检测？
3. 类别不平衡时为什么不能用准确率？该用什么？
4. 医学 AI 训练用三甲医院数据，部署到基层——可能出什么问题？（分布偏移）

## 代码示例

```python
# 对应 docs/cards/17；线性回归 + 过拟合演示（用 scikit-learn）
# 运行：uv run python code/examples/17_linear_regression_sklearn.py
# 依赖：numpy scikit-learn matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

np.random.seed(0)
x = np.linspace(0, 1, 20)
y = np.sin(2*np.pi*x) + np.random.normal(0, 0.15, 20)  # 真值=正弦+噪声

# 欠拟合：1次
poly1 = PolynomialFeatures(1)
m1 = LinearRegression().fit(poly1.fit_transform(x[:,None]), y)
# 过拟合：15次
poly15 = PolynomialFeatures(15)
m15 = LinearRegression().fit(poly15.fit_transform(x[:,None]), y)

xtest = np.linspace(0, 1, 100)
ytrue = np.sin(2*np.pi*xtest)
pred1 = m1.predict(poly1.transform(xtest[:,None]))
pred15 = m15.predict(poly15.transform(xtest[:,None]))

print("训练 MSE 低次:", round(mean_squared_error(y, m1.predict(poly1.transform(x[:,None]))),3))
print("训练 MSE 高次:", round(mean_squared_error(y, m15.predict(poly15.transform(x[:,None]))),3))
print("→ 高次训练误差极小，但测试集会爆炸：过拟合")
```

## 延伸阅读

- 对应讲稿 `Slide17-MachineLearning-2025.pdf`。
- 关联：`16`（AI 范式）、`18`（视觉）、`14`（数据挖掘）、`21`（LLM）。
- 深度专题：[`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)、[`deep/reinforcement-learning.md`](../deep/reinforcement-learning.md)。
- 经典教材：Bishop, C. (2006). *Pattern Recognition and Machine Learning*.

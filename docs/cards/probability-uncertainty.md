---
title: 概率、统计证据与不确定性
card_id: probability-uncertainty
lecture_refs: [L15, L18, L21]
source_slides: [Slide14-DataMining-2025, Slide15-DataVisualization-2025, Slide17-MachineLearning-2025]
aliases: [条件概率, 贝叶斯, 基率, 抽样, 置信区间, 相关与因果]
thinking_pillars: [数据思维, 智能思维]
category: data
tags: [概率, 条件概率, 基率, 抽样, 混淆矩阵, 不确定性, 相关, 因果]
status: ai-reviewed
version: 1.0
importance: 5
learning_objectives: [用基率解释条件概率, 区分样本证据与总体结论, 报告效应不确定性和限制]
prerequisites: [data-representation]
estimated_minutes: 50
assessment_tags: [概率计算, 证据解释, 指标辨析, 结论边界]
labs: []
figures: [15-base-rate.svg]
related_cards: [14-data-mining, 15-data-visualization, data-lifecycle-governance, ml-evaluation, responsible-ai-systems]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 概率、统计证据与不确定性（Probability and Uncertainty）

> 新课程位置：L15；为数据分析、模型评价和部署决策提供共同证据语言。

## 一句话定位

概率描述在给定信息下的不确定性；统计推断从有限、有偏且带噪声的样本推向总体，因此结论必须连同抽样条件和误差范围一起表达。

![低基率场景中的阳性结果](../../figures/15-base-rate.svg)

## 学完应能做到

1. 使用条件概率和基率解释筛查、告警与分类结果。
2. 区分描述样本、估计总体、相关关系和因果主张。
3. 报告效应大小、不确定性、样本限制和决策代价，而不是只给单一准确率或显著性。

## 核心知识点

### 条件概率改变问题

- $P(A\mid B)$ 表示已知 $B$ 时 $A$ 的概率，通常不等于 $P(B\mid A)$。
- 贝叶斯规则连接先验基率、证据似然和观察后的概率。
- 低基率事件即使检测器灵敏度和特异度较高，阳性中仍可能有大量假阳性。

### 混淆矩阵连接概率与决策

| | 实际正 | 实际负 |
|---|---:|---:|
| 预测正 | TP | FP |
| 预测负 | FN | TN |

- 灵敏度/召回率 $=TP/(TP+FN)$；精确率/阳性预测值 $=TP/(TP+FP)$。
- 准确率会被多数类主导；阈值选择应考虑假阳性和假阴性的实际代价。
- 指标是特定数据分布上的摘要，不是模型的永恒属性。

### 抽样决定能否外推

- 随机抽样帮助控制选择偏差，但现实数据经常是便利样本。
- 大样本降低随机误差，却不能自动修复系统偏差。
- 重复测量、同一患者多条记录或空间时间相关会破坏独立性假设。

### 相关不是因果

- 相关可能来自共同原因、反向作用、选择机制或偶然性。
- 因果结论需要设计、假设和领域知识；仅凭预测性能不能证明干预有效。
- `p` 值不是“原假设为真的概率”；显著也不代表效应重要或可复现。

## 工程桥接

- 稀有故障检测应结合故障基率和误报维护成本。
- 医学筛查的阈值需要考虑漏诊、复检资源和不同人群风险。
- 材料实验只报告最好一次结果会产生选择偏差，应报告重复与变异。

## 常见误区与边界

- “95% 准确率非常好”没有基线、类别比例和代价时无法判断。
- “样本足够大，所以没有偏差”错误。
- “模型置信度 0.9 就代表真实正确率 90%”只有在相应人群中经过校准才可能成立。
- 本卡不替代概率论与数理统计课程，重点是正确解释工程证据。

## 最小代码观察

运行 [`15_bayes_base_rate.py`](../../code/examples/15_bayes_base_rate.py)，保持检测性能不变，只改变事件基率，观察阳性预测值如何变化。

## 主动学习与考核迁移

- **计算**：一万人中患病率 1%，灵敏度 90%、特异度 95%，求阳性预测值。
- **辨析**：区分“模型在测试集表现好”“模型在目标医院有效”“使用模型改善患者结局”三种主张所需证据。
- **迁移**：为低频设备故障选择告警阈值，明确误报和漏报代价。
- **反思**：解释为什么增加训练样本可能降低随机误差，却不修复错误标签定义。

## 与课程图谱关系

- 数据质量与采样见 [`data-lifecycle-governance`](data-lifecycle-governance.md)。
- 可视化表达见 [`15-data-visualization`](15-data-visualization.md)。
- 模型指标与漂移见 [`ml-evaluation`](ml-evaluation.md)。

## 延伸阅读

- Spiegelhalter, D. *The Art of Statistics*.
- OpenIntro. *OpenIntro Statistics*.

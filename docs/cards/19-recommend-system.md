---
title: 推荐系统
lecture: Slide19-RecommendSystem-2025
aliases: [内容推荐, 余弦相似度, 协同过滤, 图嵌入, 冷启动]
thinking_pillar: 智能思维
category: ai-ml
tags: [推荐系统, 内容向量, 相似度, 协同过滤, 图嵌入, 冷启动, 过滤气泡]
status: needs-review
version: 2.0
importance: 3
learning_objectives: [计算内容相似度, 比较内容推荐与协同过滤, 分析离线指标和系统影响]
prerequisites: [06-graph-exploration, 13-database, 17-machine-learning]
estimated_minutes: 35
assessment_tags: [相似度计算, 方法比较, 冷启动分析, 评价设计]
labs: []
figures: []
related_cards: [06-graph-exploration, 13-database, 17-machine-learning]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 推荐系统（Recommendation System）

> 对应讲稿：`Slide19-RecommendSystem-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

推荐系统从用户、物品和交互数据中预测哪些候选更有价值，并在准确性、多样性、新颖性和长期影响之间权衡。

## 学完应能做到

- 把物品表示为特征向量并计算余弦相似度。
- 区分基于内容、协同过滤和图表示方法的证据来源。
- 解释冷启动、反馈回路和过滤气泡。

## 核心知识点

### 基于内容

从文本、类别、属性或嵌入构造物品向量，推荐与用户历史偏好相似的物品。余弦相似度：

$$
\cos(\mathbf{x},\mathbf{y})=\frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{x}\|\|\mathbf{y}\|}.
$$

### 协同过滤与图方法

协同过滤利用“相似用户喜欢相似物品”或物品共现，不要求完整内容特征。用户-物品交互天然构成二部图，图嵌入可学习邻域结构。

### 评价与系统影响

离线可使用排序指标；在线还需关注点击、留存、满意度和负面影响。系统展示会改变后续数据，形成反馈回路；只优化点击可能牺牲多样性和长期价值。

## 工程桥接

- 科研文献和实验方案推荐可减少信息过载，但应保留探索性，避免只看到与既有方向相似的内容。
- 医疗方案不能简单等同商品推荐；证据、适应证、风险和医生责任不能由相似度替代。

## 常见误区与边界

- 相似不等于适合；目标和约束决定排序。
- 高点击率不等于高质量，可能来自标题诱导或重复曝光。
- 新用户、新物品缺少交互，需内容、规则或主动探索缓解冷启动。

## 主动学习与考核迁移

1. 手算两个三维物品向量的余弦相似度。
2. 比较一个新论文平台采用内容推荐与协同过滤时的冷启动问题。
3. 设计一个不能只靠点击率评价的长期指标。

## 延伸阅读

- [17 机器学习](17-machine-learning.md)

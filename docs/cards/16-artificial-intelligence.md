---
title: 人工智能
lecture: Slide16-ArtificialIntelligence-2025
aliases: [AI, 符号主义, 连接主义, 行为主义, 图灵测试, 智能体]
thinking_pillar: 智能思维
category: ai-ml
tags: [人工智能, 发展史, 符号主义, 连接主义, 行为主义, 智能体, 伦理]
status: needs-review
version: 2.0
importance: 5
learning_objectives: [比较AI定义与范式, 识别感知决策行动闭环, 分析能力边界与责任]
prerequisites: [02-intro-to-cs, 08-turing-machine]
estimated_minutes: 35
assessment_tags: [概念辨析, 历史脉络, 系统分析, 伦理判断]
labs: []
figures: []
related_cards: [02-intro-to-cs, 17-machine-learning, 21-llm]
related_deep: [reinforcement-learning, llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-21
---

# 人工智能（Artificial Intelligence）

> 对应讲稿：`Slide16-ArtificialIntelligence-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

人工智能（artificial intelligence, AI）研究让机器表现出感知、推理、学习、决策和行动能力的方法，也研究这些能力的评价与社会边界。

## 学完应能做到

- 比较“像人一样”和“理性完成任务”等不同 AI 定义。
- 区分符号主义、连接主义和行为主义的基本思路。
- 用感知-状态/知识-决策-行动-反馈描述智能系统。

## 核心知识点

### 定义与评价

图灵测试把“能否在对话中表现得像人”转成可操作评价，但不能覆盖所有智能，也不能证明机器具有意识。工程 AI 更常按具体任务的准确性、鲁棒性、效率和风险评价。

### 发展与方法

- 符号主义用规则、逻辑和显式知识表示推理。
- 连接主义从数据学习分布式表示，现代神经网络属于此路线。
- 行为主义强调智能体与环境交互，通过反馈改善行动。

不同路线不是互斥标签，真实系统常组合规则、学习模型、搜索和工具。

### 智能体与责任

智能体（agent）接收环境信息、维护状态、选择行动并接受反馈。能力越强，越需要明确目标、权限、人工监督、失败模式和责任主体。

## 工程桥接

- 机器人把传感、定位、规划、控制和执行连成闭环，任何模块误差都会传递。
- 流程工业可用学习方法优化控制策略，但安全约束与物理规律不能只靠奖励函数表达。

## 常见误区与边界

- AI 不等于机器学习；搜索、规划、知识表示和机器人同样属于 AI。
- 在测试集高分不等于真实环境可靠。
- “弱 AI/强 AI”和意识争论适合作延伸，不应取代本讲的技术地图。

## 主动学习与考核迁移

1. 将扫地机器人拆成感知、状态、决策、行动和反馈。
2. 比较专家系统与神经网络处理同一故障诊断任务的证据来源。
3. 为一个 AI 实验列出性能指标与一个不能只看平均分的风险指标。

## 延伸阅读

- [17 机器学习](17-machine-learning.md)
- [强化学习专题](../deep/reinforcement-learning.md)

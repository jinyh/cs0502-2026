---
title: AI 搜索、知识、规划与智能体
card_id: ai-search-planning-agents
lecture_refs: [L17, L20, L21]
source_slides: [Slide06-GraphExploration-2025, Slide07-GreedyAlgorithm-2025, Slide16-ArtificialIntelligence-2025]
aliases: [状态空间, 启发式搜索, 知识表示, 规划, 智能体]
thinking_pillars: [计算思维, 智能思维]
category: ai-ml
tags: [状态, 行动, 目标, 代价, 启发式, 知识表示, 规划, Agent]
status: ai-reviewed
version: 1.0
importance: 5
learning_objectives: [把任务建模为状态空间, 比较搜索与规则推理, 解释智能体闭环和边界]
prerequisites: [06-graph-exploration, algorithm-strategies, 16-artificial-intelligence]
estimated_minutes: 45
assessment_tags: [状态建模, 搜索追踪, 启发式分析, Agent设计]
labs: [lab-02-graph, lab-03-greedy]
figures: [06-bfs-dfs.svg, 07-greedy-dijkstra.svg]
related_cards: [06-graph-exploration, algorithm-strategies, 16-artificial-intelligence, rag-tool-agents, responsible-ai-systems]
related_deep: [reinforcement-learning]
related_visualizations: []
last_reviewed: 2026-08-22
---

# AI 搜索、知识、规划与智能体（AI Search, Knowledge and Agents）

> 新课程位置：L17；用经典 AI 建立“状态—行动—反馈”骨架，再进入数据驱动学习和生成式 Agent。

## 一句话定位

智能行为可以先被拆成：环境处于什么状态、允许采取什么行动、怎样评价目标，以及系统如何根据观察持续选择下一步。

## 学完应能做到

1. 把一个任务表示为状态、初始条件、行动、转移、目标和路径代价。
2. 比较 BFS/DFS、代价搜索、启发式搜索和规则推理的假设与失败模式。
3. 区分“智能体表现得像在推理”、内部算法机制和拟人化叙事。

## 核心知识点

### 状态空间把问题变成可搜索结构

- 状态只保留决定未来选择所需的信息；太少会丢失约束，太多会造成状态爆炸。
- 行动定义合法变化，转移模型描述执行后的状态；目标测试判断是否完成。
- 路径代价可以表示距离、时间、能耗、风险或多个目标的组合。

### 搜索策略决定探索顺序

- BFS 在无权图中先找到边数最少路径，但需要保存较宽 frontier。
- DFS 内存较省，可能深入无效分支，也不保证最短路径。
- 一致代价搜索按累计代价扩展；启发式搜索再使用对剩余代价的估计。
- 启发式不是事实：过度乐观、偏向错误方向或忽略动态障碍都会误导。

### 知识表示与规则

- 命题、规则、图和本体把领域事实组织为可操作形式。
- “如果条件成立则推出结论”的规则易审查，但规则冲突、例外和不完整知识需要处理。
- 符号系统擅长明确约束；统计学习擅长从数据中归纳。真实系统常组合二者。

### 规划与 Agent 闭环

- 规划选择一串行动；执行中环境变化时，需要重新观察、更新状态并重规划。
- 智能体（agent）持续执行“观察—决策—行动—反馈”，但权限和评价由系统设计者定义。
- 大语言模型 Agent 只是实现决策组件的一种方式，并不会自动获得正确世界模型或可靠目标。

## 工程桥接

- 仓储机器人需要考虑位置、载荷、电量、通道和其他机器人，而不只是最短几何路径。
- 实验自动化规划应把危险组合和设备互斥编码为约束。
- 医疗流程 Agent 的“目标”不能只设为提高点击或缩短时间，还需包含安全与人工复核。

## 常见误区与边界

- “AI 就是机器学习”错误：搜索、知识表示、规划和控制都是 AI 的重要方法。
- “启发式更聪明所以一定更优”错误：它可能更快，也可能因错误估计走偏。
- “会输出计划就拥有意图”是拟人化推断，不能代替机制和证据。
- Agent 的自主程度不是越高越好，应与环境可预测性、风险和可恢复性相称。

## 最小代码观察

运行 [`06_graph_bfs_dfs.py`](../../code/examples/06_graph_bfs_dfs.py) 和 [`07_greedy_dijkstra.py`](../../code/examples/07_greedy_dijkstra.py)，把图结点重新解释为任务状态，边解释为行动。

## 主动学习与考核迁移

- **建模**：为三格容量的实验排程定义状态，说明哪些历史信息无需保留。
- **追踪**：在同一图上比较 BFS、DFS 和按代价扩展的 frontier 顺序。
- **反例**：设计一个启发式，使“看起来更接近目标”的结点实际走入高代价绕路。
- **迁移**：为工具 Agent 列出观察、行动、权限、成功指标和人工接管条件。

## 与课程图谱关系

- 图遍历见 [`06-graph-exploration`](06-graph-exploration.md)。
- 算法策略见 [`algorithm-strategies`](algorithm-strategies.md)。
- AI 历史范式见 [`16-artificial-intelligence`](16-artificial-intelligence.md)。
- 生成式 Agent 见 [`rag-tool-agents`](rag-tool-agents.md)。

## 延伸阅读

- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*.
- Poole, D. & Mackworth, A. *Artificial Intelligence: Foundations of Computational Agents*.

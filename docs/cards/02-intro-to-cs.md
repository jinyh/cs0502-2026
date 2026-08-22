---
title: 计算机科学导论
lecture: Slide02-IntroToCS-2025
aliases: [CS导论, 计算机科学, 四大思维]
thinking_pillar: 计算思维
category: fundamentals
tags: [计算机科学, 计算思维, 学科结构, 发展史]
status: ai-reviewed
version: 2.0
importance: 5
learning_objectives: [解释计算机科学的研究对象, 概括学科发展与结构, 用四种思维分析工程问题]
prerequisites: [01-welcome]
estimated_minutes: 25
assessment_tags: [概念辨析, 体系映射, 场景分析]
labs: []
figures: []
related_cards: [01-welcome, data-representation, algorithm-strategies, computability-limits, 16-artificial-intelligence, responsible-ai-systems]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 计算机科学导论（Introduction to Computer Science）

> 对应讲稿：`Slide02-IntroToCS-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

计算机科学（computer science, CS）研究信息与计算：问题如何表示、什么可以自动求解、怎样高效可靠地实现，以及计算怎样改变真实世界。

## 学完应能做到

- 区分计算机科学、编程和计算机产品使用。
- 用“理论-系统-数据-智能-应用”描述 CS 的学科结构。
- 把一个本专业问题映射到本课程的知识主线。

## 核心知识点

### 从计算工具到计算学科

早期计算机服务于数值计算，随后扩展到非数值信息处理、网络化系统、数据密集型科学和人工智能。硬件代际重要，但更重要的变化是：人们不断发明新的**抽象**，让同一台机器可以解决更多问题。

### 学科结构

- **理论与算法**：可计算性、数据结构、算法与复杂度。
- **系统**：体系结构、操作系统、软件工程、网络与安全。
- **数据**：数据库、数据挖掘与可视化。
- **智能**：人工智能、机器学习、视觉、语音、推荐和语言模型。
- **交叉应用**：科学计算、工程仿真、生物医学、材料发现与智能制造。

### 四种思维

| 思维 | 典型问题 |
|---|---|
| 计算思维 | 能否把问题表示为明确、可执行的步骤？ |
| 系统思维 | 组件怎样分工，接口、资源和故障怎样影响整体？ |
| 数据思维 | 数据怎样采集、组织、比较并支持结论？ |
| 智能思维 | 规则未知时，机器能否从经验学习并在新情境泛化？ |

## 工程桥接

- 船舶航线规划：图表示航路，算法搜索路径，网络接收实时数据，系统保证可靠运行。
- 材料性质预测：数据库管理实验记录，机器学习拟合结构-性质关系，可视化表达不确定性。
- 医疗决策支持：数据、模型和软件系统共同工作，同时受隐私、安全和责任边界约束。

## 常见误区与边界

- “CS 就是写代码”：代码是表达思想的工具，不是学科全貌。
- “有更快硬件就不需要算法”：输入规模增长时，算法增长率往往比常数级硬件加速更关键。
- “AI 能解决所有问题”：数据、目标、评价和部署系统缺一不可。

## 主动学习与考核迁移

1. 将“校园共享单车调度”分别用四种思维提出一个问题。
2. 解释为什么有限元软件既是算法问题，也是系统和软件工程问题。
3. 给出一个“会编程但没有解决正确问题”的反例。

## 延伸阅读

- Denning, P. J. (2005). Is Computer Science Science? *Communications of the ACM*.
- [按工程问题导航](../paths/by-engineering-workflow.md)

---
title: 软件工程
lecture: Slide10-SoftwareEngineering-2025
aliases: [软件工程, 需求, 架构, 组件, 测试, 文档]
thinking_pillar: 系统思维
category: systems
tags: [需求分析, 软件架构, 组件, 白盒测试, 黑盒测试, 文档]
status: ai-reviewed
version: 2.0
importance: 4
learning_objectives: [把模糊目标转为可验证需求, 区分架构组件与接口, 设计白盒和黑盒测试]
prerequisites: [03-programming-language]
estimated_minutes: 35
assessment_tags: [需求评审, 架构分析, 测试设计, 项目复盘]
labs: []
figures: []
related_cards: [reproducible-computing, distributed-systems, responsible-ai-systems, 03-programming-language, 09-computer-system-arch, 12-information-security]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 软件工程（Software Engineering）

> 对应讲稿：`Slide10-SoftwareEngineering-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

软件工程把“能运行的程序”变成多人可以长期理解、验证、演化和负责的软件系统。

## 学完应能做到

- 将需求写成可观察、可测试且有边界的陈述。
- 用组件和接口说明系统结构，识别高耦合风险。
- 为同一功能分别设计黑盒与白盒测试。

## 核心知识点

1. **需求分析**：确认用户、场景、输入输出、约束和验收标准；需求变更需要追踪。
2. **体系结构与组件**：把系统分解为职责清晰的组件，通过接口协作；接口同时隐藏内部实现。
3. **实现与集成**：版本控制、代码评审和持续集成降低多人协作风险。
4. **测试**：黑盒测试依据外部规格，白盒测试依据内部路径；单元、集成和系统测试关注不同边界。
5. **文档与维护**：记录“为什么这样设计”、接口、测试和已知限制，而不只是重复代码。

## 工程桥接

- 飞控、轨交控制和医疗软件属于安全攸关系统，错误成本远高于普通应用，需求追踪和验证必须更严格。
- 科研代码也需要软件工程：固定环境、记录数据版本和自动测试，才能复现实验结论。

## 常见误区与边界

- “用户说了什么”不等于完整需求；异常输入、性能、安全和责任人同样重要。
- 测试能发现错误，不能证明所有输入都正确。
- AI 生成代码仍需需求、测试和责任主体，不能跳过工程流程。

## 主动学习与考核迁移

1. 将“系统要快”改写为可测量需求。
2. 为体温采集系统列出三个组件和它们的接口。
3. 为“判断闰年”分别设计黑盒边界用例和白盒分支覆盖用例。

## 延伸阅读

- 课程项目评价要求以 Canvas 发布的正式项目任务书为准。

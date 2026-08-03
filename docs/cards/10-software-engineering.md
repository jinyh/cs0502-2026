---
title: 软件工程
lecture: Slide10-SoftwareEngineering-2025
aliases: [软件工程, 生命周期, 需求, 测试, 复杂性]
thinking_pillar: 系统思维
category: systems
tags: [软件工程, 生命周期, 测试, 复杂性, 入门]
status: stable
version: 1.0
importance: 3
related_cards: [09-computer-system-arch, 03-programming-language]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 软件工程（Software Engineering）

> 对应讲稿：[`Slide10-SoftwareEngineering-2025.pdf`](../../LectureNotes/Slide10-SoftwareEngineering-2025.pdf)

## 一句话定位

软件工程（software engineering）研究如何**系统化、可度量地**开发与维护大型软件。它应对的核心敌人是**复杂性**——人脑无法同时把握百万行代码。

## 核心知识点

### 软件危机与工程化

1968 NATO 软件工程会议标志问题正式化：软件项目常超期、超预算、难维护。根因是规模复杂度超出了「手工作坊」开发方式。

### 软件生命周期

需求 → 设计 → 编码 → 测试 → 部署 → 维护。
- 瀑布模型（线性）→ 敏捷（迭代增量）→ DevOps（开发运维一体）。
- 维护常占生命周期成本大头。

### 需求与设计

- 需求工程：搞清「要做什么」——最难、错则全盘错。
- 模块化设计：高内聚（cohesion）、低耦合（coupling）。
- 抽象与分层：管理复杂度的核心手段。

### 测试

- 单元测试 / 集成测试 / 系统测试 / 验收测试。
- 测试不能证明无 bug，只能证明有 bug（Dijkstra）。
- CI/CD：持续集成与持续交付。

### 复杂性管理

- 本质复杂度（问题本身难）vs 偶然复杂度（实现方式引入）。
- Brooks 定律：给延期项目加人会使其更延期——沟通成本 $O(n^2)$。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 软件工程 | 建大楼：不能靠一个人砌砖，要图纸、工序、质检 |
| 高内聚低耦合 | 厨房工具各司其职、互不嵌死 |
| 测试 | 临床试验：发现不良反应，不能保证零风险 |
| 敏捷 | 迭代治疗：根据病人反馈调整方案 |

## 前沿进展注记

- AI 辅助软件工程：LLM 生成代码、自动测试、智能 review（如 GitHub Copilot）。
- 趋势：自然语言成为需求与代码之间的中间层。但责任仍由人承担。

## 跨学科联系

- 与管理：软件项目管理借鉴工程管理。
- 与医学：医疗信息系统（HIS/PACS）的工程化关乎安全；FDA 把医疗软件当医疗器械监管。
- 与伦理：软件 Bug 在医疗/航空可致命——工程伦理（`computing-ethics` 可选扩展）。

## 推荐交互式问答

1. 为什么不能「一个人写完所有代码」？复杂度的来源是什么？
2. 高内聚低耦合为什么是好设计？
3. 测试能保证软件无 bug 吗？为什么？
4. LLM 自动生成代码，软件工程师还做什么？（需求、架构、验证）

## 延伸阅读

- 对应讲稿 `Slide10-SoftwareEngineering-2025.pdf`。
- 关联：`03`（编程语言是材料）、`09`（运行平台）。
- 经典：Brooks, F. (1975). *The Mythical Man-Month*.

# 课程教学序列（docs/curriculum/）

本目录定义 CS0502 的 **21 讲教学序列**；`docs/cards/` 定义可复用的**概念图谱**。两者是多对多关系：一讲通常组合多张卡片，一张卡片也可以服务多讲、实验、项目与复习路径。

## 文件

- [`21-lecture-blueprint.md`](21-lecture-blueprint.md) — AI 时代 21 讲课程蓝图：边界、目标、场景、主动任务与跨章迁移。
- [`lecture-card-map.yaml`](lecture-card-map.yaml) — 机器可读的讲次—核心卡—支持卡—示例—实验—配图—考核标签映射。
- [`legacy-coverage-matrix.md`](legacy-coverage-matrix.md) — 现有 21 张讲稿锚点卡片与 6 张扩展卡片迁移到新序列的覆盖矩阵。

## 三层关系

| 层 | 回答的问题 | 稳定标识 | 变化节奏 |
|---|---|---|---|
| 教学序列 | 本学期第几讲教什么、达到什么目标？ | `L01`–`L21` | 随课程设计调整 |
| 概念卡片 | 某个概念是什么、如何操作、何时失效？ | 语义化 card id | 按知识审校增补 |
| 讲稿锚点 | 原讲稿覆盖了什么、来源在哪里？ | `SlideNN-*` | 只读保留 |

讲稿编号只表示**来源与历史覆盖**，不再决定卡片文件名、数量或学习顺序。现有 `01-*`–`21-*` 文件在迁移期继续可用，但其数字前缀是 legacy id，不是新教学序列的强绑定。

## 维护规则

- 新增或拆分卡片时，以“能被单独检索、练习和复用的概念”为粒度，不为了凑齐 21 张而合并主题。
- 新卡使用 `lecture_refs: [Lxx, ...]` 表示教学使用位置；`source_slides: [SlideNN-*, ...]` 只记录来源。迁移前的 `lecture` 字段暂时保留。
- 一讲的核心概念、课前卡、实验和迁移题以课程蓝图为准；卡片路径以 `opencode/knowledge.md` 为检索入口。
- 课程组先审批蓝图，再分批拆卡与重写讲稿；本目录不覆盖 Canvas 中的只读 PDF。

## 新概念卡片最小元数据

```yaml
---
title: <概念名称>
card_id: <稳定语义 id>
lecture_refs: [L04, L06]
source_slides: [Slide04-DataStructure-2025, Slide07-GreedyAlgorithm-2025]
thinking_pillars: [计算思维]
tags: [<可检索关键词>]
status: draft
learning_objectives: [<可观察目标>]
prerequisites: [<card_id>]
---
```

`lecture_refs` 可以为空（工程扩展）或包含多讲；`source_slides` 也可以为空（AI 时代新增内容）。

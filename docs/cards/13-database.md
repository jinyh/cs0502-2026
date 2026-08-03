---
title: 数据库
lecture: Slide13-Database-2025
aliases: [数据库, 关系模型, SQL, 事务, ACID]
thinking_pillar: 数据思维
category: data
tags: [数据库, 关系模型, SQL, 事务, ACID, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [05-data-structure-advanced, 14-data-mining]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 数据库（Database）

> 对应讲稿：`Slide13-Database-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

数据库（database）是**持久、结构化、可共享**的数据存储与管理系统。关系模型用「表」抽象世界，SQL 是查询语言，事务保证正确性。

## 核心知识点

### 关系模型（relational model, Codd 1970）

- 数据组织为表（关系 relation）：行=元组，列=属性。
- 用数学集合论做基础，独立于物理存储。
- 直觉：Excel 表，但有严格数学约束。

### SQL（Structured Query Language）

- 声明式：描述「要什么」而非「怎么找」。
- 核心：SELECT / FROM / WHERE / JOIN / GROUP BY。
- JOIN 把多表关联——关系模型的力量所在。

### 事务与 ACID

- 事务（transaction）：一组不可分割的操作。
- ACID：
  - 原子性（Atomicity）：全做或全不做。
  - 一致性（Consistency）：约束不被破坏。
  - 隔离性（Isolation）：并发互不干扰。
  - 持久性（Durability）：提交后不丢。
- 直觉：银行转账要么全成功要么全失败，不能扣了 A 没加 B。

### 索引

为加速查询，在列上建索引（常基于 B+ 树或哈希，关联 `05`）。
- 以空间换时间；但写操作变慢。

### 关系型 vs NoSQL

- 关系型（MySQL/PostgreSQL）：强结构、强一致、事务。
- NoSQL（文档/键值/图）：灵活 schema、横向扩展、最终一致。
- 视场景取舍，非互斥。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 关系模型 | 严格 Excel 表 vs 自由格式文档 |
| SQL 声明式 | 点菜说「要一份宫保鸡丁」，不告诉厨师怎么炒 |
| 事务 | 银行转账的「要么全成要么全败」 |
| 索引 | 书后索引：按关键词直接翻页 |
| ACID | 医嘱执行：不能执行一半停药 |

## 前沿进展注记

- 向量数据库（vector database）：存 LLM embedding，支撑 RAG 与语义检索（关联 `21`）。
- 云原生数据库、HTAP（混合事务分析）。
- 数据隐私：差分隐私查询、安全多方计算。

## 跨学科联系

- 与数学：关系代数、集合论。
- 与医学：电子病历（EHR）、PACS 影像库、检验数据——关系型是 EHR 主力。
- 与数据挖掘：数据库提供原料（`14`）。

## 推荐交互式问答

1. 为什么不直接用 Excel 存数据？数据库强在哪？
2. 声明式 SQL 与命令式编程有什么本质区别？（关联 `03`）
3. ACID 中哪个属性在并发下最难保证？
4. 向量数据库和传统数据库有什么不同？为什么 LLM 需要？（关联 `21`）

## 延伸阅读

- 对应讲稿 `Slide13-Database-2025.pdf`。
- 关联：`05`（索引结构）、`14`（从 DB 挖知识）。
- 经典：Silberschatz, A. et al. (2019). *Database System Concepts*.

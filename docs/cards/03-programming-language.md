---
title: 编程语言
lecture: Slide03-ProgrammingLanguage-2025
aliases: [编程语言, 编译, 解释, 范式, 语法语义]
thinking_pillar: 计算思维
category: fundamentals
tags: [编程语言, 编译, 解释, 范式, Python, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [02-intro-to-cs, 21-llm]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 编程语言（Programming Language）

> 对应讲稿：[`Slide03-ProgrammingLanguage-2025.pdf`](../../LectureNotes/Slide03-ProgrammingLanguage-2025.pdf)

## 一句话定位

编程语言（programming language）是人给机器下指令的形式语言。它处在「人的意图」与「机器执行」之间，决定了表达的难易与可计算的范围。本课程统一用 Python。

## 核心知识点

### 语法与语义

- **语法（syntax）**：合法语句的形式规则——「句子长什么样」。
- **语义（semantics）**：语句的含义——「句子什么意思」。
- 语法错可被编译器/解释器发现；语义错（逻辑错）需调试。

### 编译 vs 解释

- **编译（compiled）**：源码整体翻成机器码再执行（C/C++/Rust）。快，但需编译步骤。
- **解释（interpreted）**：逐行翻译执行（Python/Ruby）。慢，但灵活、易调试。
- Python 实际先编译成字节码再由虚拟机解释。

### 抽象层级（从低到高）

机器码 → 汇编 → C → Python → … → 自然语言（LLM 时代新边界，见 `21`）。层越高越接近人、越远离机器。

### 编程范式

- 命令式（imperative）：一步步描述怎么做。C、Python 默认风格。
- 面向对象（OOP）：把数据与操作封装成对象。
- 函数式（functional）：用函数与不可变数据，避免副作用。
- 声明式（declarative）：描述要什么而非怎么做（SQL、Prolog）。

### Python 为何选作教学语言

语法接近伪代码、生态丰富（科学计算/ML）、动态类型降低门槛；但牺牲了部分性能与静态安全。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 编译 | 整本书翻译完再读 |
| 解释 | 同声传译，一句句来 |
| 语法 vs 语义 | 「我吃苹果」语法对，但「苹果吃我」语义反常 |
| 范式 | 做菜：按步骤（命令式）/ 按食材对象（OOP）/ 按配方函数（函数式） |

## 前沿进展注记

LLM 时代新趋势：**自然语言正成为新的「编程接口」**——用自然语言指挥 LLM/Agent 完成任务，介于声明式编程与意图表达之间。但自然语言有歧义，仍需形式语言做精确控制。详见 `21-llm`。

## 跨学科联系

- 与语言学：语法/语义概念借自自然语言学；乔姆斯基层级结构。
- 与逻辑学：函数式编程源于 $\lambda$ 演算，与形式逻辑同源。
- 与医学：临床决策支持规则可形式化为领域特定语言。

## 推荐交互式问答

1. 编译和解释各适合什么场景？为什么 Python 慢但仍流行？
2. 语法错和语义错，哪个更难发现？为什么？
3. LLM 时代「用自然语言编程」会取代 Python 吗？为什么仍需形式语言？（关联 `21`）

## 延伸阅读

- 对应讲稿 `Slide03-ProgrammingLanguage-2025.pdf`。
- 关联：`21`（LLM 作为新编程接口）。

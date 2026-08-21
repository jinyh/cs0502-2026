---
title: 计算机体系结构、存储层次与加速器
card_id: computer-architecture
lecture_refs: [L08, L09, L19]
source_slides: [Slide09-ComputerSystemAndArchitecture-2025]
aliases: [计算机组成, 冯诺依曼, ISA, 缓存, GPU, NPU]
thinking_pillars: [系统思维]
category: systems
tags: [CPU, 指令, ISA, 存储层次, 缓存, 局部性, GPU, NPU, 数据移动]
status: needs-review
version: 1.0
importance: 5
learning_objectives: [追踪指令执行和数据流, 用局部性解释存储层次, 比较CPU GPU NPU的工作负载]
prerequisites: [data-representation, 03-programming-language, ext-logic-boolean]
estimated_minutes: 45
assessment_tags: [系统分层, 指令追踪, 性能分析, 架构选择]
labs: []
figures: [09-computer-os-layers.svg]
related_cards: [data-representation, operating-systems, algorithm-strategies, neural-networks-transformers]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 计算机体系结构、存储层次与加速器（Computer Architecture）

> 新课程位置：L08。旧 `09` 保留为来源概览，本卡只聚焦硬件执行、存储与 AI 加速。

## 一句话定位

程序的抽象操作最终变成指令和数据在处理器、缓存、内存与设备之间的移动；很多性能和能耗瓶颈来自“搬数据”，不只是“做运算”。

![从程序到硬件资源](../../figures/09-computer-os-layers.svg)

## 学完应能做到

1. 追踪一条简化指令从取指、译码到执行、访存和写回的主要路径。
2. 用时间局部性、空间局部性解释缓存命中与不同访问顺序的性能差异。
3. 根据控制分支、并行度、矩阵运算、延迟和能耗比较 CPU、GPU 与 NPU。

## 核心知识点

### 指令集是软硬件接口

- 指令集体系结构（instruction set architecture, ISA）规定处理器可执行的操作、寄存器和寻址方式。
- 编译器把高级语言转换为目标 ISA 指令；操作系统负责装载程序并提供受控资源。
- 微体系结构可以用流水线、乱序执行或多个核心实现同一 ISA，因此“指令相同”不等于性能相同。

### 冯·诺依曼模型与执行循环

- 程序指令和数据都存于可寻址存储器。
- 程序计数器指出下一条指令；控制单元取指和译码，数据通路执行运算并读写状态。
- 分支改变下一条指令位置，缓存未命中让处理器等待更慢层次的数据。

### 存储层次与局部性

| 层次 | 大致特点 | 典型用途 |
|---|---|---|
| 寄存器 | 最快、最少 | 当前运算状态 |
| 缓存 | 快、按块自动管理 | 最近或邻近数据 |
| 主存 | 容量较大、延迟较高 | 正在运行的程序和数据 |
| SSD/磁盘 | 非易失、容量大 | 长期保存 |

- 时间局部性：刚访问的数据近期可能再次访问。
- 空间局部性：相邻地址的数据可能很快被访问。
- 对二维数组按连续内存方向遍历，通常比跨大步长访问更友好。

### CPU、GPU 与 NPU

- CPU 擅长复杂控制、低延迟和通用任务。
- GPU 用大量并行执行单元处理规则、数据并行工作负载。
- NPU/AI 加速器针对张量运算、低精度数值和数据复用优化。
- 加速器并非自动更快：数据传输、批大小、内存容量、算子支持和编程开销都可能抵消收益。

## 工程桥接

- 边缘医疗设备可能选择 NPU 以降低能耗并避免上传原始数据，但受模型大小和算子限制。
- 科学计算中的矩阵布局、稀疏性和内存带宽会显著影响实际速度。
- 高吞吐服务器与实时控制器的评价目标不同：前者重吞吐，后者重最坏时延。

## 常见误区与边界

- “主频更高一定更快”错误：每周期工作量、并行度、内存和程序特征同样重要。
- “GPU 核心更多，所以所有程序更快”错误：大量分支或小任务可能无法有效并行。
- “缓存是程序员可忽略的透明细节”不完整：正确性通常透明，性能并不透明。
- 本课不要求设计流水线电路或 CUDA 内核，重点是解释系统权衡。

## 最小代码观察

运行 [`08_cache_locality.py`](../../code/examples/08_cache_locality.py)，比较同一矩阵的两种遍历顺序。计时结果受机器影响，结论应结合访问模式而不是只报数字。

## 主动学习与考核迁移

- **追踪**：对 `load → add → store` 三条简化指令标出寄存器、内存和程序计数器变化。
- **预测**：行优先存储的矩阵按行与按列求和，哪种更可能缓存友好？为什么？
- **选择**：为机器人控制、离线模型训练和手机图像增强分别选择主要处理器，并写出仍需实测的指标。
- **迁移**：模型参数减半却没有加速，请从数据传输、内存带宽和算子支持提出三种假设。

## 与课程图谱关系

- 位与数值格式见 [`data-representation`](data-representation.md)。
- 进程和资源管理见 [`operating-systems`](operating-systems.md)。
- 模型计算见 [`neural-networks-transformers`](neural-networks-transformers.md)。

## 延伸阅读

- Patterson, D. & Hennessy, J. *Computer Organization and Design*.
- Bryant, R. E. & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective*.

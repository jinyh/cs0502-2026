---
title: 计算机系统与架构
lecture: Slide09-ComputerSystemAndArchitecture-2025
aliases: [冯诺依曼, CPU, 指令周期, 存储层次, 硬件]
thinking_pillar: 系统思维
category: systems
tags: [冯诺依曼, CPU, 指令周期, 存储层次, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [08-turing-machine, 10-software-engineering, 11-computer-network]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 计算机系统与架构（Computer System & Architecture）

> 对应讲稿：[`Slide09-ComputerSystemAndArchitecture-2025.pdf`](../../LectureNotes/Slide09-ComputerSystemAndArchitecture-2025.pdf)

## 一句话定位

计算机硬件如何从逻辑门组织成能执行程序的机器？冯诺依曼架构给出了答案：**程序与数据同存内存，CPU 周期取指-译码-执行**。它是图灵机（`08`）的物理实现。

## 核心知识点

### 冯诺依曼架构（von Neumann architecture）

- 存储程序（stored program）：指令与数据同存内存，可被当作数据处理——这是「计算机能运行自身程序」的关键。
- 五大部件：运算器、控制器、存储器、输入、输出。
- 与图灵机对应：内存=纸带，CPU=读写头+控制器。

### 指令周期（instruction cycle）

取指（fetch）→ 译码（decode）→ 执行（execute）→ 写回，循环往复。
- 直觉：厨师看菜谱（取指）、理解步骤（译码）、动手做（执行）、装盘（写回）。

### 存储层次（memory hierarchy）

速度与容量矛盾，靠层次结构缓解：
寄存器（ns）→ 缓存 cache（L1/L2/L3）→ 主存 RAM → SSD → 网络存储。
- 越上层越快越小越贵。
- 程序局部性（locality）是缓存有效的基础：最近用的大概率再用（时间局部性）、用 A 大概率用 A 附近（空间局部性）。

### CPU 与并行

- 多核、流水线、乱序执行、分支预测。
- Amdahl 定律：串行部分限制加速比上限。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 存储程序 | 厨师把菜谱也放厨房，可翻看修改 |
| 指令周期 | 看一行、懂一行、做一行 |
| 存储层次 | 桌面（寄存器）→ 抽屉（缓存）→ 柜子（内存）→ 仓库（磁盘） |
| 局部性 | 最近用的东西放手边，下次好拿 |

## 前沿进展注记

- 摩尔定律放缓，性能提升转向专用加速器（GPU/TPU/NPU）——AI 算力的基础。
- 存算一体、近内存计算探索缓解「内存墙」。

## 跨学科联系

- 与物理：半导体器件、散热；量子退相干限制量子计算（`deep/quantum-computing`）。
- 与医学：医疗影像 AI 的硬件部署（边缘 vs 云）关乎延迟与隐私。
- 与 OS：架构决定 OS 抽象（见 `03-operating-system` 可选扩展）。

## 推荐交互式问答

1. 冯诺依曼「存储程序」为何是革命性的？与之前的「接线编程」对比。
2. 为什么存储要分层？只用最快的行不行？（成本/容量）
3. 程序局部性如何让缓存有效？写出局部性差的代码会怎样？
4. AI 训练为什么从 CPU 转向 GPU/TPU？（数据并行 + 矩阵运算）

## 延伸阅读

- 对应讲稿 `Slide09-ComputerSystemAndArchitecture-2025.pdf`。
- 关联：`08`（图灵机理论模型）、`11`（网络：系统向外延伸）。
- 经典教材：Patterson, D. & Hennessy, J. (2020). *Computer Organization and Design*.

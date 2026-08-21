---
title: 操作系统、进程与并发
card_id: operating-systems
lecture_refs: [L09, L10, L20]
source_slides: [Slide09-ComputerSystemAndArchitecture-2025]
aliases: [操作系统, 进程, 线程, 调度, 同步, 死锁, 虚拟内存]
thinking_pillars: [系统思维]
category: systems
tags: [进程, 线程, 调度, 竞态, 锁, 死锁, 虚拟内存, 隔离, 沙箱]
status: needs-review
version: 1.0
importance: 5
learning_objectives: [解释OS的抽象和隔离, 追踪进程状态与并发交错, 识别竞态死锁和资源边界]
prerequisites: [computer-architecture, stack-queue]
estimated_minutes: 45
assessment_tags: [进程状态, 调度分析, 并发追踪, 资源安全]
labs: []
figures: [09-process-concurrency.svg]
related_cards: [computer-architecture, stack-queue, distributed-systems, reproducible-computing, ai-security]
related_deep: []
related_visualizations: [circular_queue]
last_reviewed: 2026-08-21
---

# 操作系统、进程与并发（Operating Systems and Concurrency）

> 新课程位置：L09。将旧 `09` 中的操作系统内容独立为可追踪、可练习的概念卡。

## 一句话定位

操作系统把有限硬件包装成进程、虚拟内存、文件和设备等抽象，同时在共享、性能与隔离之间做资源仲裁。

![进程、调度与并发风险](../../figures/09-process-concurrency.svg)

## 学完应能做到

1. 解释进程、线程、虚拟地址空间和系统调用分别提供什么抽象。
2. 画出进程状态转换，并追踪两个操作交错如何产生竞态条件。
3. 识别死锁必要条件，为代码执行选择超时、内存、权限与隔离护栏。

## 核心知识点

### OS 的两种角色

- **抽象**：让程序使用文件而非直接控制磁盘扇区，使用虚拟地址而非管理物理内存位置。
- **仲裁与保护**：调度 CPU、分配内存、控制设备和权限，防止一个程序任意破坏另一个程序。
- 用户程序通过系统调用请求内核服务；用户态和内核态分离限制高权限操作。

### 进程、线程与调度

- 进程是运行程序及其地址空间、打开资源和执行状态的组合。
- 同一进程内线程共享多数资源，但拥有各自调用栈和执行位置。
- 进程可在新建、就绪、运行、阻塞和终止等状态间转换。
- 调度策略在响应时间、吞吐、公平、截止期和切换成本之间权衡。

### 并发不是简单的“同时”

- 并发表示多个任务的执行区间重叠；并行表示物理上同时执行。
- `counter += 1` 通常包含读、加、写多个步骤，两个线程交错可能丢失更新。
- 锁保护临界区，但锁粒度过大降低并发，锁顺序不一致可能造成死锁。
- 消息传递、不可变数据和任务隔离也可减少共享状态风险。

### 死锁与资源边界

经典死锁需要互斥、占有并等待、不可抢占和循环等待同时成立。破坏其中一个条件可预防一类死锁，但可能牺牲性能或资源利用率。

课程 runner 的路径白名单、导入限制、CPU 时间和内存限制体现最小权限与资源配额；它是教学护栏，不是针对恶意本机用户的完整虚拟化沙箱。

## 工程桥接

- 多传感器控制程序必须明确共享状态、数据新鲜度和截止期。
- 实验平台同时运行多个学生程序时，需要隔离文件、网络、CPU 和内存。
- Agent 并行调用工具可能重复修改同一资源，需要幂等接口或串行化关键操作。

## 常见误区与边界

- “线程一定比进程快”不完整：创建、通信、隔离和运行时实现都会影响选择。
- “加锁就正确”错误：锁错对象、范围或顺序仍会竞态或死锁。
- “程序每次都得到同一结果，所以没有竞态”错误：错误交错可能低概率出现。
- Python 运行时细节不是并发概念本身；不要把某个解释器的锁当作通用正确性保证。

## 最小代码观察

运行 [`09_interleavings.py`](../../code/examples/09_interleavings.py)。它不依赖随机线程调度，而是枚举两个“读—写”操作的合法交错，展示为何同一源代码可能产生不同结果。

## 主动学习与考核迁移

- **追踪**：给定进程的运行、I/O 请求、I/O 完成和时间片耗尽事件，画状态变化。
- **交错**：两个任务都执行“读计数器、加一、写回”，构造最终结果为 1 而非 2 的顺序。
- **死锁**：为两个锁、两个线程画等待图，并通过统一获取顺序消除环。
- **迁移**：为学生代码执行服务写出最小权限、超时、内存、网络和输出限制。

## 与课程图谱关系

- 硬件资源见 [`computer-architecture`](computer-architecture.md)。
- 队列与调度见 [`stack-queue`](stack-queue.md)。
- 跨机器并发见 [`distributed-systems`](distributed-systems.md)。
- Agent 权限见 [`ai-security`](ai-security.md)。

## 延伸阅读

- Arpaci-Dusseau, R. & Arpaci-Dusseau, A. *Operating Systems: Three Easy Pieces*.
- Downey, A. *The Little Book of Semaphores*.

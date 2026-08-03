# 术语表（Glossary）

> 全局术语中英对照。首次出现在卡片时会标注英文，本表作汇总检索。按主题分组。

## 计算基础

| 中文 | English | 释义要点 |
|---|---|---|
| 抽象数据类型 | Abstract Data Type, ADT | 数据+操作的抽象契约，与实现分离 |
| 图灵机 | Turing machine | 机械计算的数学模型 |
| 丘奇-图灵论题 | Church-Turing Thesis | 可计算 ≡ 图灵机可计算 |
| 停机问题 | Halting Problem | 不可判定的范例问题 |
| 编译 | Compilation | 源码整体翻译成机器码 |
| 解释 | Interpretation | 逐行翻译执行 |

## 数据结构与算法

| 中文 | English | 释义要点 |
|---|---|---|
| 栈 | Stack | LIFO 线性结构 |
| 队列 | Queue | FIFO 线性结构 |
| 链表 | Linked List | 指针串接的非连续结构 |
| 广度优先搜索 | Breadth-First Search, BFS | 逐层扩展，用队列 |
| 深度优先搜索 | Depth-First Search, DFS | 走到底回溯，用栈 |
| 哈希表 | Hash Table | 平均 O(1) 查找 |
| 贪心算法 | Greedy Algorithm | 每步局部最优 |
| 最优子结构 | Optimal Substructure | 子问题最优→整体最优 |

## 系统

| 中文 | English | 释义要点 |
|---|---|---|
| 冯诺依曼架构 | von Neumann Architecture | 存储程序，指令数据同存内存 |
| 指令周期 | Instruction Cycle | 取指-译码-执行-写回 |
| 存储层次 | Memory Hierarchy | 寄存器→缓存→内存→磁盘 |
| 局部性 | Locality | 时间/空间局部性，缓存有效的基础 |
| 分层协议 | Layered Protocol | 每层对上服务、对下使用 |
| 传输控制协议 | TCP | 可靠、有序、面向连接 |
| 对称加密 | Symmetric Encryption | 加解密同密钥 |
| 公钥加密 | Public-Key Encryption | 公钥/私钥对 |

## 数据

| 中文 | English | 释义要点 |
|---|---|---|
| 关系模型 | Relational Model | 数据组织为表（关系） |
| 结构化查询语言 | SQL | 声明式数据库查询语言 |
| 事务 | Transaction | ACID 不可分割操作组 |
| 关联规则 | Association Rule | 「买 A 也买 B」式共现 |
| 聚类 | Clustering | 无监督分组 |

## AI/ML

| 中文 | English | 释义要点 |
|---|---|---|
| 监督学习 | Supervised Learning | 带标签学映射 |
| 无监督学习 | Unsupervised Learning | 无标签找结构 |
| 强化学习 | Reinforcement Learning, RL | 从反馈信号学习策略 |
| 过拟合 | Overfitting | 记住噪声，泛化差 |
| 梯度下降 | Gradient Descent | 沿损失梯度下降优化 |
| 卷积神经网络 | Convolutional Neural Network, CNN | 利用局部性的视觉网络 |
| 自注意力 | Self-Attention | 序列内位置间加权聚合 |
| 大语言模型 | Large Language Model, LLM | 大规模预训练语言模型 |
| 对齐 | Alignment | 让模型有用/诚实/无害 |
| 基于人类反馈的强化学习 | RLHF | 用人类偏好作奖励优化 |
| 幻觉 | Hallucination | 生成看似合理但错误的内容 |
| 智能体 | Agent | 感知-决策-行动的闭环 |
| 检索增强生成 | Retrieval-Augmented Generation, RAG | 检索外部知识拼入上下文 |

## 量子

| 中文 | English | 释义要点 |
|---|---|---|
| 量子比特 | Qubit | 叠加态信息单元 |
| 叠加 | Superposition | 同时含 0/1 成分 |
| 纠缠 | Entanglement | 不可分离的联合态 |
| 退相干 | Decoherence | 环境致量子态塌缩 |
| 后量子密码学 | Post-Quantum Cryptography, PQC | 抗量子攻击的密码 |

# 术语表（Glossary）

> 全局术语中英对照。首次出现在卡片时会标注英文，本表作汇总检索。按主题分组。

## 计算基础

| 中文 | English | 释义要点 |
|---|---|---|
| 抽象数据类型 | Abstract Data Type, ADT | 数据+操作的抽象契约，与实现分离 |
| 图灵机 | Turing machine | 机械计算的数学模型 |
| 丘奇-图灵论题 | Church-Turing Thesis | 可计算 ≡ 图灵机可计算 |
| 停机问题 | Halting Problem | 不可判定的范例问题 |
| 编译 | Compilation | 在执行前把程序翻译成另一种表示，可为机器码或字节码 |
| 解释 | Interpretation | 由解释器读取程序表示并按其语义执行，不必先生成独立机器码程序 |
| 编码 | Encoding | 按约定把信息映射为可存储或传输的符号/位模式 |
| 量化 | Quantization | 把连续或高精度值映射到有限离散等级 |
| 浮点数 | Floating-Point Number | 用符号、有效数字和指数近似表示实数 |
| 可判定性 | Decidability | 是否存在对所有合法输入都终止并正确回答的算法 |

## 数据结构与算法

| 中文 | English | 释义要点 |
|---|---|---|
| 栈 | Stack | LIFO 线性结构 |
| 队列 | Queue | FIFO 线性结构 |
| 顺序表 | Sequential List | 用连续存储位置实现的线性表 |
| 链表 | Linked List | 指针串接的非连续结构 |
| 树 | Tree | 图论中指连通无环图；指定根后可表达层次关系 |
| 二叉堆 | Binary Heap | 满足堆序的完全二叉树，常用数组实现优先队列 |
| 递归 | Recursion | 问题或过程调用自身，必须有基例并向其推进 |
| 广度优先搜索 | Breadth-First Search, BFS | 逐层扩展，用队列 |
| 深度优先搜索 | Depth-First Search, DFS | 走到底回溯，用栈 |
| 哈希表 | Hash Table | 在合适哈希函数与负载因子下支持平均常数时间查找 |
| 时间复杂度 | Time Complexity | 输入规模增长时运行步骤数量级的变化 |
| 贪心算法 | Greedy Algorithm | 每步局部最优 |
| 最优子结构 | Optimal Substructure | 一个问题的最优解可由其相关子问题的最优解组合得到；是否成立需证明 |
| 分治 | Divide-and-Conquer | 分解为较独立子问题，求解后合并 |
| 动态规划 | Dynamic Programming | 复用重叠子问题结果的算法策略 |
| 循环不变量 | Loop Invariant | 每次迭代前后保持成立、用于连接局部步骤与整体正确性的性质 |

## 系统

| 中文 | English | 释义要点 |
|---|---|---|
| 冯诺依曼架构 | von Neumann Architecture | 存储程序，指令数据同存内存 |
| 指令周期 | Instruction Cycle | 取指-译码-执行-写回 |
| 存储层次 | Memory Hierarchy | 寄存器→缓存→内存→磁盘 |
| 局部性 | Locality | 时间/空间局部性，缓存有效的基础 |
| 指令集体系结构 | Instruction Set Architecture, ISA | 软件可见的处理器指令、寄存器和寻址接口 |
| 进程 | Process | 运行中程序及其资源隔离与管理单位 |
| 线程 | Thread | 进程中的执行流，共享进程资源 |
| 互斥 | Mutual Exclusion | 防止多个执行流同时破坏共享状态 |
| 死锁 | Deadlock | 多方循环等待资源而都无法继续 |
| 竞态条件 | Race Condition | 结果依赖未受控制的并发交错 |
| 幂等 | Idempotence | 同一操作重复执行与执行一次具有相同目标效果 |
| 部分失败 | Partial Failure | 分布式系统中部分组件失败而其他组件仍在运行 |
| 最小权限 | Least Privilege | 主体只获得完成当前任务所需的最小能力 |
| 分层协议 | Layered Protocol | 每层对上服务、对下使用 |
| 传输控制协议 | TCP | 可靠、有序、面向连接 |
| 对称加密 | Symmetric Encryption | 加解密同密钥 |
| 公钥加密 | Public-Key Encryption | 公钥/私钥对 |
| 数字签名 | Digital Signature | 用私钥签名、公钥验证完整性和来源 |

## 数据

| 中文 | English | 释义要点 |
|---|---|---|
| 关系模型 | Relational Model | 数据组织为表（关系） |
| 关系代数 | Relational Algebra | 以选择、投影、连接等运算组合关系查询 |
| 数据库管理系统 | Database Management System, DBMS | 管理存储、查询、事务、并发与恢复的软件系统 |
| 结构化查询语言 | SQL | 声明式数据库查询语言 |
| 事务 | Transaction | 作为一个逻辑工作单元执行的一组操作；数据库可用 ACID 等性质约束其行为 |
| 关联规则 | Association Rule | 「买 A 也买 B」式共现 |
| 聚类 | Clustering | 无监督分组 |
| 数值稳定性 | Numerical Stability | 算法不会无谓放大输入误差与舍入误差 |
| 数据来源 | Data Provenance | 数据从采集到各次处理和派生版本的可追溯记录 |
| 数据泄漏 | Data Leakage | 训练过程获得部署时不可用或来自评价集的信息 |
| 基率 | Base Rate | 观察证据前，目标事件在相应人群中的发生比例 |
| 条件概率 | Conditional Probability | 在已知另一事件成立时某事件的概率 |

## AI/ML

| 中文 | English | 释义要点 |
|---|---|---|
| 监督学习 | Supervised Learning | 带标签学映射 |
| 无监督学习 | Unsupervised Learning | 无标签找结构 |
| 强化学习 | Reinforcement Learning, RL | 从反馈信号学习策略 |
| 过拟合 | Overfitting | 模型过度贴合训练数据中的偶然、噪声或特有模式，导致未见数据表现下降 |
| 泛化 | Generalization | 模型在未见数据上的有效表现 |
| 分布漂移 | Distribution Shift | 部署数据或输入输出关系相对训练/验证条件发生变化 |
| 校准 | Calibration | 预测概率与相应事件实际频率的一致程度 |
| 梯度下降 | Gradient Descent | 沿损失梯度下降优化 |
| 卷积神经网络 | Convolutional Neural Network, CNN | 利用局部性的视觉网络 |
| 循环神经网络 | Recurrent Neural Network, RNN | 通过隐藏状态处理序列的网络 |
| 词嵌入 | Word Embedding | 把离散词或 token 映射为连续向量 |
| 位置编码 | Positional Encoding | 向序列表示注入位置信息 |
| 自注意力 | Self-Attention | 序列内位置间加权聚合 |
| Transformer | Transformer | 以注意力为核心处理序列和多模态表示的神经网络架构 |
| 词元 | Token | 模型处理文本时使用的离散单位，可是字、词或子词片段 |
| 大语言模型 | Large Language Model, LLM | 大规模预训练语言模型 |
| 对齐 | Alignment | 使模型或 AI 系统的可观察行为更符合指定意图、偏好、规范与安全约束；目标之间可能冲突 |
| 基于人类反馈的强化学习 | RLHF | 用人类偏好作奖励优化 |
| 幻觉 | Hallucination | 生成流畅但错误、无依据或无法由给定证据支持的内容 |
| 智能体 | Agent | 感知-决策-行动的闭环 |
| 检索增强生成 | Retrieval-Augmented Generation, RAG | 检索外部知识拼入上下文 |
| 提示注入 | Prompt Injection | 用不可信内容诱导模型偏离系统目标或越权行动 |
| 工具调用 | Tool Calling | 模型产生结构化调用建议，由系统验证后执行外部函数 |
| 校准信任 | Calibrated Trust | 人对自动化系统的信任程度与其真实能力和边界相匹配 |
| 人机交互 | Human-Computer Interaction, HCI | 研究人与计算系统之间设计、使用和影响的领域 |
| 无障碍 | Accessibility | 让不同能力与使用情境的人都能感知、理解和操作系统 |
| 自动语音识别 | Automatic Speech Recognition, ASR | 把语音信号转成文本 |
| 词错误率 | Word Error Rate, WER | 语音识别插入、删除、替换错误相对参考词数的比例 |

## 量子

| 中文 | English | 释义要点 |
|---|---|---|
| 量子比特 | Qubit | 叠加态信息单元 |
| 叠加 | Superposition | 同时含 0/1 成分 |
| 纠缠 | Entanglement | 不可分离的联合态 |
| 退相干 | Decoherence | 量子系统与环境相互作用导致相位相干性衰减，不宜简单等同于测量塌缩 |
| 后量子密码学 | Post-Quantum Cryptography, PQC | 抗量子攻击的密码 |

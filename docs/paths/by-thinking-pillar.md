# 学习路径：按四大思维支柱

> 对齐课程大纲四大思维组织。每条支柱串联可复用概念卡，形成一条概念路径；它不是 21 讲课表，教学顺序见 [`课程蓝图`](../curriculum/21-lecture-blueprint.md)。

## 计算思维（Computational Thinking）

把问题形式化为可计算步骤：抽象、分解、算法化。

1. [`02-intro-to-cs`](../cards/02-intro-to-cs.md) — CS 的边界与四大思维起点
2. [`data-representation`](../cards/data-representation.md) + [`boolean-logic`](../cards/ext-logic-boolean.md) — 信息怎样成为可计算位模式
3. [`03-programming-language`](../cards/03-programming-language.md) — 用语言、函数和接口表达步骤
4. [`04-data-structure-basics`](../cards/04-data-structure-basics.md) → [`stack-queue`](../cards/stack-queue.md) → [`trees-heaps`](../cards/trees-heaps.md) — 根据操作组织状态
5. [`recursion-divide-conquer`](../cards/ext-recursion-divide-conquer.md) + [`06-graph-exploration`](../cards/06-graph-exploration.md) — 递归结构与关系遍历
6. [`algorithm-strategies`](../cards/algorithm-strategies.md) + [`complexity`](../cards/ext-complexity.md) — 策略、正确性、反例与资源增长
7. [`computability-limits`](../cards/computability-limits.md) — 可计算、可承受与可验证的边界

## 系统思维（Systems Thinking）

理解分层、协议、协作——硬件到网络如何构成整体。

1. [`computer-architecture`](../cards/computer-architecture.md) — 指令、存储层次与加速器
2. [`operating-systems`](../cards/operating-systems.md) — 进程、并发、调度与隔离
3. [`11-computer-network`](../cards/11-computer-network.md) → [`web-technologies`](../cards/ext-web-technologies.md) → [`distributed-systems`](../cards/distributed-systems.md) — 从协议到部分失败
4. [`10-software-engineering`](../cards/10-software-engineering.md) + [`reproducible-computing`](../cards/reproducible-computing.md) — 从规格、测试到证据链
5. [`12-information-security`](../cards/12-information-security.md) + [`ai-security`](../cards/ai-security.md) — 密码学、威胁模型与工具权限

## 数据思维（Data Thinking）

从数据中提炼知识：存储、挖掘、呈现。

1. [`13-database`](../cards/13-database.md) — 结构化存储与查询
2. [`data-lifecycle-governance`](../cards/data-lifecycle-governance.md) — 来源、质量、许可与责任
3. [`probability-uncertainty`](../cards/probability-uncertainty.md) — 基率、抽样与证据边界
4. [`14-data-mining`](../cards/14-data-mining.md) — 从数据发现模式
5. [`15-data-visualization`](../cards/15-data-visualization.md) + [`hci-accessibility`](../cards/hci-accessibility.md) — 从呈现到可理解、可操作

## 智能思维（Intelligence Thinking）

让机器学习与决策。

1. [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) + [`ai-search-planning-agents`](../cards/ai-search-planning-agents.md) — 范式、状态空间、规划与行动
2. [`17-machine-learning`](../cards/17-machine-learning.md) + [`ml-evaluation`](../cards/ml-evaluation.md) — 学习、泛化、偏差与漂移
3. [`neural-networks-transformers`](../cards/neural-networks-transformers.md) — CNN、RNN、注意力与 Transformer
4. [`multimodal-models`](../cards/multimodal-models.md) — 图像、语音、文本与应用案例
5. [`21-llm`](../cards/21-llm.md) + [`rag-tool-agents`](../cards/rag-tool-agents.md) — 生成、检索、工具与 Agent
6. [`responsible-ai-systems`](../cards/responsible-ai-systems.md) — 四大思维综合评审
7. 深度专题：[`llm-deep-dive`](../deep/llm-deep-dive.md) · [`reinforcement-learning`](../deep/reinforcement-learning.md)

> 四大思维并非割裂：图灵机（计算）是系统架构（系统）的理论基础；数据思维与智能思维共享统计学习根基。建议至少完成计算思维全段，再按兴趣深入其余。

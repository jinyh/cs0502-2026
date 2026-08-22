# 学习路径：按跨学科桥接

> CS 概念与各学科的关联入口。每条桥接指向相关卡片中「跨学科联系」小节。

## CS ↔ 医学

- [`12-information-security`](../cards/12-information-security.md) — 医疗数据隐私、基因数据敏感性
- [`data-lifecycle-governance`](../cards/data-lifecycle-governance.md) — 跨医院数据来源、许可与重新识别风险
- [`probability-uncertainty`](../cards/probability-uncertainty.md) + [`ml-evaluation`](../cards/ml-evaluation.md) — 基率、患者级划分与临床外推
- [`13-database`](../cards/13-database.md) — 用关系、键与约束组织患者、检查和测量记录；真实病历/PACS 还涉及专门标准与治理
- [`18-computer-vision`](../cards/18-computer-vision.md) — 医学影像 AI 与分布偏移
- [`rag-tool-agents`](../cards/rag-tool-agents.md) + [`ai-security`](../cards/ai-security.md) — 医学问答的引用、权限与幻觉风险
- [`08-turing-machine`](../cards/08-turing-machine.md) — 「不可预测」的逻辑边界类比

## CS ↔ 物理

- [`computer-architecture`](../cards/computer-architecture.md) — 半导体、存储层次、散热与加速器
- [`quantum-computing`](../deep/quantum-computing.md) — 量子力学驱动的计算范式
- [`11-computer-network`](../cards/11-computer-network.md) — 传播、排队、带宽与吞吐的物理和系统约束
- [`17-machine-learning`](../cards/17-machine-learning.md) — 优化、泛化与统计建模
- [`ext-scientific-computing`](../cards/ext-scientific-computing.md) — 数值稳定、误差传播与可重复实验

## CS ↔ 生物

- [`06-graph-exploration`](../cards/06-graph-exploration.md) — 蛋白质相互作用网络
- [`trees-heaps`](../cards/trees-heaps.md) — 生物分类学与系统发育树
- [`18-computer-vision`](../cards/18-computer-vision.md) — CNN 与视觉皮层感受野
- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) — 神经网络与生物神经的源流

## CS ↔ 数学

- [`08-turing-machine`](../cards/08-turing-machine.md) — 哥德尔、可计算性
- [`06-graph-exploration`](../cards/06-graph-exploration.md) — 图论、组合优化
- [`17-machine-learning`](../cards/17-machine-learning.md) — 线性代数、概率、信息论
- [`probability-uncertainty`](../cards/probability-uncertainty.md) — 条件概率、抽样与证据边界
- [`07-greedy-algorithm`](../cards/07-greedy-algorithm.md) — 最优化、交换论证

## CS ↔ 哲学/伦理

- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) — 图灵测试、中文房间
- [`21-llm`](../cards/21-llm.md) — 「理解」之争、对齐价值
- [`12-information-security`](../cards/12-information-security.md) — 隐私与信任
- [`responsible-ai-systems`](../cards/responsible-ai-systems.md) — 人本目标、监督、申诉与问责

## CS ↔ 船舶海洋

- [`computer-architecture`](../cards/computer-architecture.md) — CFD/有限元仿真的算力需求与并行架构
- [`ext-complexity`](../cards/ext-complexity.md) — 网格规模上亿时，$O(n)$ 与 $O(n^2)$ 决定能否在算力预算内完成
- [`11-computer-network`](../cards/11-computer-network.md) — 海洋观测浮标/传感网的组网与数据回传
- [`distributed-systems`](../cards/distributed-systems.md) — 弱连接环境的超时、重试与幂等

## CS ↔ 材料化工

- [`14-data-mining`](../cards/14-data-mining.md) — 材料信息学：高通量计算数据中挖掘「结构-性质」关系
- [`reproducible-computing`](../cards/reproducible-computing.md) — 仿真、实验与模型证据链
- [`quantum-computing`](../deep/quantum-computing.md) — 分子/介观模拟是量子计算的原生应用
- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) + [`reinforcement-learning`](../deep/reinforcement-learning.md) — 流程工业（反应釜/精馏）的优化与控制

## CS ↔ 机械动力

- [`computer-architecture`](../cards/computer-architecture.md) + [`10-software-engineering`](../cards/10-software-engineering.md) — 仿真与控制软件中的算力、接口、测试和可维护性
- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) + [`reinforcement-learning`](../deep/reinforcement-learning.md) — 机器人学与运动控制（传感-决策-执行闭环）
- [`12-information-security`](../cards/12-information-security.md) — 工业控制系统的资产、可用性、最小权限与安全停机分析
- [`operating-systems`](../cards/operating-systems.md) + [`ml-evaluation`](../cards/ml-evaluation.md) — 实时并发、设备泛化与漂移监测

## CS ↔ 生物医药

- [`06-graph-exploration`](../cards/06-graph-exploration.md) — 基因序列比对（动态规划/图算法）、蛋白质相互作用网络
- [`17-machine-learning`](../cards/17-machine-learning.md) + [`21-llm`](../cards/21-llm.md) — 药物发现 AI（分子性质预测、虚拟筛选、文献挖掘）
- [`multimodal-models`](../cards/multimodal-models.md) — 分子、影像、组学和文本的多模态融合
- [`13-database`](../cards/13-database.md) + [`14-data-mining`](../cards/14-data-mining.md) — 组学数据管理（基因/蛋白/代谢）与生物信息学

## CS ↔ 航空航天

- [`10-software-engineering`](../cards/10-software-engineering.md) + [`12-information-security`](../cards/12-information-security.md) — 飞控软件的高可信工程与安全规约
- [`responsible-ai-systems`](../cards/responsible-ai-systems.md) — 失效降级、人工接管与责任分配
- [`07-greedy-algorithm`](../cards/07-greedy-algorithm.md) + [`ext-scientific-computing`](../cards/ext-scientific-computing.md) — 路径规划、数值误差与结果验证
- [`18-computer-vision`](../cards/18-computer-vision.md) + [`14-data-mining`](../cards/14-data-mining.md) — 遥感影像处理与地学大数据

## CS ↔ 电子信息与电气控制

- [`data-representation`](../cards/data-representation.md) + [`ext-logic-boolean`](../cards/ext-logic-boolean.md) — 采样、量化、位模式与数字逻辑
- [`computer-architecture`](../cards/computer-architecture.md) + [`operating-systems`](../cards/operating-systems.md) — 嵌入式处理器、实时任务、并发和资源约束
- [`11-computer-network`](../cards/11-computer-network.md) + [`distributed-systems`](../cards/distributed-systems.md) — 传感网络、时延、丢包、重试与部分失败
- [`probability-uncertainty`](../cards/probability-uncertainty.md) + [`ml-evaluation`](../cards/ml-evaluation.md) — 检测误报、校准、漂移和闭环控制中的证据边界
- [`ai-security`](../cards/ai-security.md) — 联网控制与 AI 工具调用的权限、输入信任和审计

> 桥接是双向的：既用学生熟悉的学科解释 CS，也提示 CS 如何反哺该学科（如计算成为科研第三范式）。

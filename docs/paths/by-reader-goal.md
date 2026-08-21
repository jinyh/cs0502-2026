# 学习路径：按读者目标

> 面向不同专业背景学生的推荐侧重。所有路径共享 L01–L07 的计算思维基础，但按概念卡导航，不按文件编号顺序猜测。

## 公共基础（建议所有读者）

[`02`](../cards/02-intro-to-cs.md) → [`data-representation`](../cards/data-representation.md) → [`03`](../cards/03-programming-language.md) → [`04`](../cards/04-data-structure-basics.md) → [`algorithm-strategies`](../cards/algorithm-strategies.md) → [`computability-limits`](../cards/computability-limits.md)

建立「计算是什么、AI 是什么」的全局图景。

## 医工科学生

重点：数据思维 + 医学交叉 AI + 安全隐私。

- [`13-database`](../cards/13-database.md) · [`14-data-mining`](../cards/14-data-mining.md) · [`15-data-visualization`](../cards/15-data-visualization.md)
- [`data-lifecycle-governance`](../cards/data-lifecycle-governance.md) · [`probability-uncertainty`](../cards/probability-uncertainty.md) · [`ml-evaluation`](../cards/ml-evaluation.md)
- [`18-computer-vision`](../cards/18-computer-vision.md)（医学影像）
- [`12-information-security`](../cards/12-information-security.md)（医疗数据隐私）
- [`rag-tool-agents`](../cards/rag-tool-agents.md) + [`responsible-ai-systems`](../cards/responsible-ai-systems.md)（医学问答证据、权限与治理）
- 跨学科桥接见 [`by-discipline-bridge`](by-discipline-bridge.md)

## 信息工科学生

重点：系统思维 + 算法 + 工程。

- [`computer-architecture`](../cards/computer-architecture.md) · [`operating-systems`](../cards/operating-systems.md) · [`distributed-systems`](../cards/distributed-systems.md) · [`ai-security`](../cards/ai-security.md)
- [`06`](../cards/06-graph-exploration.md) · [`07`](../cards/07-greedy-algorithm.md)
- [`ml-evaluation`](../cards/ml-evaluation.md) · [`neural-networks-transformers`](../cards/neural-networks-transformers.md) · [`rag-tool-agents`](../cards/rag-tool-agents.md)

## 材料/化学/物理科学生

重点：计算范式 + 量子计算 + 模拟。

- [`computability-limits`](../cards/computability-limits.md)
- [`computer-architecture`](../cards/computer-architecture.md) · [`ext-scientific-computing`](../cards/ext-scientific-computing.md)
- [`quantum-computing`](../deep/quantum-computing.md)（量子模拟是原生应用）
- [`14-data-mining`](../cards/14-data-mining.md)（材料数据驱动发现）
- [`15-data-visualization`](../cards/15-data-visualization.md)
- [`probability-uncertainty`](../cards/probability-uncertainty.md) · [`reproducible-computing`](../cards/reproducible-computing.md)

## 船舶海洋与建筑工程

重点：高性能计算、传感网络、控制联锁。

- [`computer-architecture`](../cards/computer-architecture.md) + [`ext-complexity`](../cards/ext-complexity.md) — CFD/有限元仿真的算力与复杂度
- [`11-computer-network`](../cards/11-computer-network.md) — 海洋观测浮标/传感网组网
- [`ext-logic-boolean`](../cards/ext-logic-boolean.md) + [`12-information-security`](../cards/12-information-security.md) — 工业控制联锁与安全
- [`06-graph-exploration`](../cards/06-graph-exploration.md) — 航线规划与最短路径
- [`distributed-systems`](../cards/distributed-systems.md) — 海上链路中的超时、重试与部分失败

## 机械动力与能源

重点：建模仿真、机器人控制、工程化。

- [`10-software-engineering`](../cards/10-software-engineering.md) + [`reproducible-computing`](../cards/reproducible-computing.md) — CAD/CAM、数字孪生与计算证据
- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) + [`reinforcement-learning`](../deep/reinforcement-learning.md) — 机器人学与运动控制
- [`ext-logic-boolean`](../cards/ext-logic-boolean.md) — PLC 与工业控制逻辑
- [`14-data-mining`](../cards/14-data-mining.md) — 设备状态监测与故障预测
- [`ml-evaluation`](../cards/ml-evaluation.md) — 新设备泛化与部署漂移

## 航空航天

重点：高可信软件、轨道计算、遥感数据。

- [`10-software-engineering`](../cards/10-software-engineering.md) + [`12-information-security`](../cards/12-information-security.md) — 飞控软件的高可信工程与安全规约
- [`07-greedy-algorithm`](../cards/07-greedy-algorithm.md) + [`ext-scientific-computing`](../cards/ext-scientific-computing.md) — 路径规划、数值误差与验证
- [`18-computer-vision`](../cards/18-computer-vision.md) + [`14-data-mining`](../cards/14-data-mining.md) — 遥感影像与地学大数据
- [`ext-complexity`](../cards/ext-complexity.md) — 大规模仿真的复杂度约束
- [`responsible-ai-systems`](../cards/responsible-ai-systems.md) — 安全攸关系统的降级、接管与问责

## 理科（数学/统计）学生

重点：形式基础 + ML 数学 + 复杂度。

- [`computability-limits`](../cards/computability-limits.md) · [`algorithm-strategies`](../cards/algorithm-strategies.md)
- [`trees-heaps`](../cards/trees-heaps.md) · [`06`](../cards/06-graph-exploration.md)
- [`probability-uncertainty`](../cards/probability-uncertainty.md) · [`ml-evaluation`](../cards/ml-evaluation.md) · [`reinforcement-learning`](../deep/reinforcement-learning.md)
- [`quantum-computing`](../deep/quantum-computing.md)

> 这是建议而非规定。任意组合均可，关键是带着自己专业的问题来读。

若目标是把知识用于一个真实工程任务，可直接走 [`by-engineering-workflow`](by-engineering-workflow.md)。

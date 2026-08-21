# 知识库索引（Knowledge Index）

> 智能体检索入口。本页机器可解析 + 人类可读。回答学生问题时，优先在此定位卡片再展开。

## 21 讲卡片速查表

格式：`编号 | 标题 | 对应讲稿 | 思维支柱 | 一句话定位 | 关键 tag`

| # | 卡片 | 讲稿 | 支柱 | 定位 | tags |
|---|---|---|---|---|---|
| 01 | [welcome](../docs/cards/01-welcome.md) | Slide01 | meta | 课程地图与学习闭环 | 课程导引/学习方法 |
| 02 | [intro-to-cs](../docs/cards/02-intro-to-cs.md) | Slide02 | 计算 | CS 边界与四大思维 | 计算思维 |
| 03 | [programming-language](../docs/cards/03-programming-language.md) | Slide03 | 计算 | 形式语言下指令 | 编译/解释/范式 |
| 04 | [data-structure-basics](../docs/cards/04-data-structure-basics.md) | Slide04 | 计算 | 线性表、顺序表与链表 | 逻辑结构/存储结构/链表 |
| 05 | [data-structure-advanced](../docs/cards/05-data-structure-advanced.md) | Slide05 | 计算 | 栈/队列/递归/树/堆/复杂度 | 栈/递归/堆/Big-O |
| 06 | [graph-exploration](../docs/cards/06-graph-exploration.md) | Slide06 | 计算 | 图遍历 BFS/DFS | 图/BFS/DFS/连通 |
| 07 | [greedy-algorithm](../docs/cards/07-greedy-algorithm.md) | Slide07 | 计算 | 局部最优策略 | 贪心/最优子结构 |
| 08 | [turing-machine](../docs/cards/08-turing-machine.md) | Slide08 | 计算 | 状态、纸带与转移规则 | 图灵机/转移/配置 |
| 09 | [computer-system-arch](../docs/cards/09-computer-system-arch.md) | Slide09 | 系统 | 计算机组成与操作系统 | CPU/进程/调度/同步/死锁 |
| 10 | [software-engineering](../docs/cards/10-software-engineering.md) | Slide10 | 系统 | 复杂性系统化管理 | 生命周期/测试/内聚耦合 |
| 11 | [computer-network](../docs/cards/11-computer-network.md) | Slide11 | 系统 | 分层协议互联 | TCP/IP/HTTP/DNS |
| 12 | [information-security](../docs/cards/12-information-security.md) | Slide12 | 系统 | 密码学与 CIA | 对称/公钥/哈希/签名 |
| 13 | [database](../docs/cards/13-database.md) | Slide13 | 数据 | 关系模型、代数与 DBMS | 键/关系代数/SQL/查询优化 |
| 14 | [data-mining](../docs/cards/14-data-mining.md) | Slide14 | 数据 | 从数据发现模式 | 聚类/关联规则/分类 |
| 15 | [data-visualization](../docs/cards/15-data-visualization.md) | Slide15 | 数据 | 视觉编码与感知 | 图表/感知/EDA |
| 16 | [artificial-intelligence](../docs/cards/16-artificial-intelligence.md) | Slide16 | 智能 | AI 范式与边界 | 图灵测试/符号/连接/Agent |
| 17 | [machine-learning](../docs/cards/17-machine-learning.md) | Slide17 | 智能 | 学习、泛化与神经网络 | 感知器/MLP/CNN/RNN/Transformer |
| 18 | [computer-vision](../docs/cards/18-computer-vision.md) | Slide18 | 智能 | 看懂图像 | CNN/分类/检测/分割 |
| 19 | [recommend-system](../docs/cards/19-recommend-system.md) | Slide19 | 智能 | 个性化匹配 | 协同过滤/冷启动 |
| 20 | [speech-recognition](../docs/cards/20-speech-recognition.md) | Slide20 | 智能 | 端到端 ASR 与序列建模 | RNN/隐藏状态/WER |
| 21 | [llm](../docs/cards/21-llm.md) | Slide21 | 智能 | 从 N-gram 到大语言模型 | 嵌入/位置/注意力/生成/幻觉 |

## 扩展卡片（ext-，补全教学完整性）

| 文件 | 主题 | 参考 |
|---|---|---|
| [ext-complexity](../docs/cards/ext-complexity.md) | 算法复杂度 Big-O / P 与 NP | MIT 6.0001、CS50 |
| [ext-recursion-divide-conquer](../docs/cards/ext-recursion-divide-conquer.md) | 递归与分治、归并排序 | CS61A、CS106A |
| [ext-search-hashing](../docs/cards/ext-search-hashing.md) | 搜索、哈希与冲突 | CS50、旧版卡片 05 |
| [ext-scientific-computing](../docs/cards/ext-scientific-computing.md) | 浮点误差、数值稳定与可重复实验 | 工程计算公共基础 |
| [ext-web-technologies](../docs/cards/ext-web-technologies.md) | HTTP/HTML/前后端/REST、LLM API | CS50 Web |
| [ext-logic-boolean](../docs/cards/ext-logic-boolean.md) | 布尔代数、逻辑门 | Dale Ch4 |

## 深度专题

| 文件 | 主题 | 对应卡片 |
|---|---|---|
| [llm-deep-dive](../docs/deep/llm-deep-dive.md) | LLM 架构/训练/对齐/Agent/前沿 | 21/16/17 |
| [reinforcement-learning](../docs/deep/reinforcement-learning.md) | MDP/Q-learning/PPO/RLHF | 16/17 |
| [quantum-computing](../docs/deep/quantum-computing.md) | 叠加/纠缠/Shor/后量子密码 | 08/12 |

## 前沿注记（静态层 + 联网增量）

| 文件 | 主题 | 对应卡片 |
|---|---|---|
| [llm-frontier](../docs/frontier/llm-frontier.md) | LLM 前沿 | 21 |
| [cv-frontier](../docs/frontier/cv-frontier.md) | 计算机视觉前沿 | 18 |

## 学习路径（按需跳转）

- 按思维支柱：[`paths/by-thinking-pillar`](../docs/paths/by-thinking-pillar.md)
- 按 AI 能力：[`paths/by-ai-capability`](../docs/paths/by-ai-capability.md)
- 按读者目标：[`paths/by-reader-goal`](../docs/paths/by-reader-goal.md)
- 按跨学科桥接：[`paths/by-discipline-bridge`](../docs/paths/by-discipline-bridge.md)
- 按工程工作流：[`paths/by-engineering-workflow`](../docs/paths/by-engineering-workflow.md)

## 术语

见 [`docs/glossary.md`](../docs/glossary.md)（中英对照，按主题分组）。

## 可视化资源

见 [`code/visualizations/`](../code/visualizations/)：二叉堆、循环队列、汉诺塔、栈表达式、图灵机。

---

## 检索提示（给智能体）

- 学生问某概念 → 先匹配 tags，只读当前卡片与必要前置；加载 `guided-learning`，先让学生预测或追踪。
- 学生要练习/模拟 → 读 `docs/assessment/blueprint.yaml`；未批准时只能称“通用课程练习”。
- 学生问“最新/进展” → 加载 `frontier-literacy`，经同意联网，草稿只写 `student-work/`。
- 学生要深入 → 引导到 `deep/` 对应专题，而非自创内容。
- 学生问跨学科 → 读卡片“工程桥接”+ `paths/by-discipline-bridge`。

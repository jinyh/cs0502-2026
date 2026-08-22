# 知识库索引（Knowledge Index）

> 智能体检索入口。本页机器可解析 + 人类可读。先定位教学目标，再按概念选择最少必要卡片；不得把讲次编号和卡片编号视为一一对应。

> 代码快速路径：`/demo` 与 `/lab` 按讲次定位时只检索 [`lecture-runtime-index.jsonl`](lecture-runtime-index.jsonl) 的对应单行；概念学习才按需进入下列完整索引与课程映射。
>
> Lab 默认是形成性学习资源，不自动等于作业。公开作业关联见 [`../code/labs/catalog.json`](../code/labs/catalog.json)，最终以教师正式作业说明为准。

## 21 讲教学序列速查

完整目标、工程场景与主动任务见 [`docs/curriculum/21-lecture-blueprint.md`](../docs/curriculum/21-lecture-blueprint.md)；精确资源映射见 [`lecture-card-map.yaml`](../docs/curriculum/lecture-card-map.yaml)。一讲组合多卡，一卡可以服务多讲。映射中的 `core_cards` 按学习顺序排列；支持卡用于补救，预览卡只建立后续直觉，扩展卡/可视化不属于当讲必做。

| 讲次 | 主题 | 现有入口 / 检索 tag |
|---|---|---|
| L01 | CS、四种思维与人机协作 | `01-welcome`、`02-intro-to-cs` |
| L02 | 数据表示、编码、逻辑与数值误差 | `data-representation`、`ext-logic-boolean`、`ext-scientific-computing` |
| L03 | 程序、语言、抽象与问题求解 | `03-programming-language`；语法/语义/编译/接口/测试 |
| L04 | 线性结构、栈、队列与哈希 | `04-data-structure-basics`、`stack-queue`、`ext-search-hashing` |
| L05 | 递归、树、堆、图与遍历 | `ext-recursion-divide-conquer`、`trees-heaps`、`06-graph-exploration` |
| L06 | 搜索、排序、算法策略与复杂度 | `ext-complexity`、`algorithm-strategies` |
| L07 | 可计算性、复杂性与自动化边界 | `08-turing-machine`、`computability-limits` |
| L08 | 体系结构、存储与 AI 加速器 | `computer-architecture`、`data-representation` |
| L09 | OS、进程、并发与资源管理 | `operating-systems`、`computer-architecture` |
| L10 | 网络、Web、API、云与分布式 | `11-computer-network`、`ext-web-technologies`、`distributed-systems` |
| L11 | 软件工程、测试、版本与可重复性 | `10-software-engineering`、`reproducible-computing` |
| L12 | 安全、隐私、密码学与 AI 安全 | `12-information-security`、`ai-security` |
| L13 | 数据库、数据模型与查询 | `13-database`；关系模型/SQL/索引/事务 |
| L14 | 数据生命周期、质量、来源与治理 | `data-lifecycle-governance`、`13-database`、`14-data-mining` |
| L15 | 概率、统计证据与不确定性 | `probability-uncertainty`、`ext-scientific-computing` |
| L16 | 可视化、HCI 与无障碍 | `15-data-visualization`、`hci-accessibility` |
| L17 | AI：搜索、知识、规划与智能体 | `16-artificial-intelligence`、`ai-search-planning-agents` |
| L18 | ML：泛化、评价、偏差与漂移 | `17-machine-learning`、`ml-evaluation` |
| L19 | 神经网络、Transformer 与多模态 | `neural-networks-transformers`、`multimodal-models` |
| L20 | GenAI：LLM、RAG、工具与 Agent | `21-llm`、`rag-tool-agents` |
| L21 | AI 系统工程与负责任设计 | `responsible-ai-systems` |

旧卡迁移依据见 [`legacy-coverage-matrix.md`](../docs/curriculum/legacy-coverage-matrix.md)。蓝图与映射状态仍为 `proposal`；课程组批准前，不得声称它们是已经生效的正式教学安排。

## 讲稿来源锚点/概览卡速查

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

## 新语义概念卡（跨讲次复用）

| card id | 卡片 | 主要讲次 | 定位 |
|---|---|---|---|
| data-representation | [数据表示与编码](../docs/cards/data-representation.md) | L02/L08/L19 | 位模式、编码、采样与量化误差 |
| stack-queue | [栈、队列与状态边界](../docs/cards/stack-queue.md) | L04/L05/L09 | LIFO/FIFO、边界与调度 |
| trees-heaps | [树、堆与层次结构](../docs/cards/trees-heaps.md) | L05/L06/L13 | 遍历、堆序与优先队列 |
| algorithm-strategies | [算法策略](../docs/cards/algorithm-strategies.md) | L06/L07/L17 | 分治、贪心、动态规划、正确性 |
| computability-limits | [计算与自动化边界](../docs/cards/computability-limits.md) | L07/L11/L20/L21 | 可判定、复杂性与验证 |
| computer-architecture | [体系结构与加速器](../docs/cards/computer-architecture.md) | L08/L19 | ISA、局部性、CPU/GPU/NPU |
| operating-systems | [操作系统与并发](../docs/cards/operating-systems.md) | L09/L20 | 进程、调度、竞态、隔离 |
| distributed-systems | [分布式系统](../docs/cards/distributed-systems.md) | L10/L20 | 超时、重试、幂等、部分失败 |
| reproducible-computing | [可重复计算](../docs/cards/reproducible-computing.md) | L11/L18/L21 | 版本、环境、证据链 |
| ai-security | [AI 应用安全](../docs/cards/ai-security.md) | L12/L20/L21 | 注入、工具权限与输出验证 |
| data-lifecycle-governance | [数据生命周期与治理](../docs/cards/data-lifecycle-governance.md) | L14/L18/L21 | 来源、质量、许可与责任 |
| probability-uncertainty | [概率与不确定性](../docs/cards/probability-uncertainty.md) | L15/L18/L21 | 基率、抽样、证据边界 |
| hci-accessibility | [HCI 与无障碍](../docs/cards/hci-accessibility.md) | L16/L20/L21 | 可用性、无障碍、校准信任 |
| ai-search-planning-agents | [AI 搜索与智能体](../docs/cards/ai-search-planning-agents.md) | L17/L20 | 状态空间、知识、规划、Agent |
| ml-evaluation | [ML 泛化与评价](../docs/cards/ml-evaluation.md) | L18/L20/L21 | 泄漏、指标、偏差、漂移 |
| neural-networks-transformers | [神经网络与 Transformer](../docs/cards/neural-networks-transformers.md) | L19/L20 | CNN/RNN/注意力结构偏置 |
| multimodal-models | [多模态感知](../docs/cards/multimodal-models.md) | L19/L20/L21 | 图像、语音、文本对齐与融合 |
| rag-tool-agents | [RAG 与工具 Agent](../docs/cards/rag-tool-agents.md) | L20/L21 | 检索、引用、工具与评价 |
| responsible-ai-systems | [负责任 AI 系统](../docs/cards/responsible-ai-systems.md) | L21 | 四大思维综合评审 |

## 兼容扩展语义卡

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

见 [`code/visualizations/`](../code/visualizations/)：二叉堆、循环队列、汉诺塔、栈表达式；多带图灵机页面为 L07 选学扩展。

---

## 检索提示（给智能体）

- 学生按讲次学习 → 先查“21 讲教学序列速查”和蓝图中的可观察目标，再按 tags 选择 1–3 张必要概念卡；不要按相同编号猜卡片。
- 学生要代码或演示 → 从 `lecture-card-map.yaml` 依次选择最小 example、interactive visualization、figure 或卡片主动任务；先预测再验证。
- 学生问某概念 → 先匹配 tags，只读当前卡片与必要前置；加载 `guided-learning`，先让学生预测或追踪。
- 卡片内容不足 → 可以给简短的模型生成解释或新例子，但必须标记“模型补充，非课程组审校卡片”，不得声称模型会自动补全或持久更新知识库。
- 学生要练习/模拟 → 读 `docs/assessment/blueprint.yaml`；未批准时只能称“通用课程练习”。
- 学生问“最新/进展” → 加载 `frontier-literacy`，先检查静态页 `review_status`，经同意联网，草稿只写 `student-work/`。
- 学生要深入 → 引导到 `deep/` 对应专题，而非自创内容。
- 学生问跨学科 → 读卡片“工程桥接”+ `paths/by-discipline-bridge`。
- 学生要持续复习 → 先征得同意，再用 `code/progress.py` 维护匿名本地记录；拒绝记录时仍可进行当前会话学习。

# 现有卡片 → 新 21 讲覆盖矩阵

> 状态：内容迁移已实现，待课程组审核。本文保留迁移依据，不表示卡片必须按讲次重命名。`Lxx` 指 [`21-lecture-blueprint.md`](21-lecture-blueprint.md) 中的新教学序列，实际组合见 [`lecture-card-map.yaml`](lecture-card-map.yaml)。

## 迁移原则

- `reuse`：现有内容可作为概念卡保留，仅需更新元数据和交叉链接。
- `split`：一张旧卡含多个可独立检索、练习的概念，后续应拆成多卡。
- `merge-case`：不再作为独立一讲，但保留为主原理下的应用案例卡。
- `reframe`：保留主题，但改变教学重点或补足证据、边界与工程责任。
- `retire-to-frontier`：产品史或高时效信息移到 `frontier/`，不进入稳定核心。

## 01–21 讲稿锚点卡片

| 现有卡片 | 新讲次 | 动作 | 保留与改进重点 |
|---|---|---|---|
| `01-welcome` | L01 | merge/reframe | 与原 `02` 的课程地图合并；保留学习闭环、诚信与 OpenCode 主动学习规则 |
| `02-intro-to-cs` | L01、L03、L07、L21 | split | CS 边界与四支柱进入 L01；抽象进入 L03；计算边界进入 L07；综合框架进入 L21 |
| `03-programming-language` | L03、L11、L20 | split | 语法/语义、编译/解释进 L03；接口与测试进 L11；结构化工具调用进 L20 |
| `04-data-structure-basics` | L04 | reuse | 线性表、数组、链表保留；增强操作模式与工程选择 |
| `05-data-structure-advanced` | L04、L05、L06 | split | 栈/队列进 L04；递归/树/堆进 L05；复杂度进 L06，解除单卡过载 |
| `06-graph-exploration` | L05、L06、L17 | reuse/split | 图表示与 BFS/DFS 进 L05；代价进 L06；状态空间搜索复用于 L17 |
| `07-greedy-algorithm` | L06、L17 | reframe | 与分治、动态规划共同成为算法策略；Dijkstra 也可作为启发式搜索对照 |
| `08-turing-machine` | L07 | reframe | 保留通用模型与可计算性；降低多带机械追踪，增加自动化和验证边界 |
| `09-computer-system-arch` | L08、L09 | split | 体系结构/存储/加速器与 OS/进程/并发拆开 |
| `10-software-engineering` | L11、L21 | reframe | 增加版本、依赖、可重复性和 AI 生成代码验证；系统评审进入 L21 |
| `11-computer-network` | L10、L12、L20 | split | 网络/Web/API/云/分布式进 L10；安全面进 L12；模型 API/工具连接进 L20 |
| `12-information-security` | L12、L21 | reframe | 保留密码学和威胁；新增隐私、提示注入、工具越权、AI 供应链与责任 |
| `13-database` | L13、L14、L20 | reuse/extend | 关系模型与查询进 L13；来源/治理进 L14；向量检索与 RAG 作为 L20 扩展 |
| `14-data-mining` | L14、L15、L18 | reframe/split | 预处理和质量进 L14；统计证据进 L15；分类/聚类及评价进 L18 |
| `15-data-visualization` | L15、L16 | reframe | 不确定性连接 L15；图表、HCI、无障碍和校准信任进入 L16 |
| `16-artificial-intelligence` | L17、L21（并贯穿全课） | reframe | 历史范式、搜索/知识/Agent 进入 L17；伦理与系统责任进入 L21 |
| `17-machine-learning` | L18、L19 | split | 学习/泛化/评价进 L18；神经网络、CNN/RNN/Transformer 进 L19 |
| `18-computer-vision` | L19 | merge-case | 保留成像、卷积、任务与误差；作为多模态感知案例，不单占一讲 |
| `19-recommend-system` | L18、L19、L21 | merge-case | 相似度、协同过滤作为学习案例；过滤气泡和系统影响进 L21 |
| `20-speech-recognition` | L19 | merge-case | 保留序列、RNN、WER；作为语音模态案例，不单占一讲 |
| `21-llm` | L19、L20、L21 | split/reframe | Transformer 原理进 L19；生成/RAG/工具/Agent 进 L20；治理与部署进 L21 |

## 现有扩展卡片

| 现有卡片 | 新讲次 | 动作 | 保留与改进重点 |
|---|---|---|---|
| `ext-complexity` | L06、L07 | reuse/split | Big-O 进 L06；P/NP 与资源边界进 L07 |
| `ext-recursion-divide-conquer` | L05、L06 | reuse | 递归模型进 L05；分治范式进 L06 |
| `ext-search-hashing` | L04、L06 | split | 哈希结构进 L04；搜索策略与代价进 L06 |
| `ext-scientific-computing` | L02、L11、L15 | split | 浮点表示进 L02；可重复实验进 L11；误差与不确定性进 L15 |
| `ext-web-technologies` | L10、L20 | reuse/extend | Web/API 进入 L10；LLM 服务与工具接口进入 L20 |
| `ext-logic-boolean` | L02、L08 | reuse | 程序条件与逻辑门进 L02；数字电路连接 L08 |

## 已新增核心概念簇

下列内容原有卡片没有形成足够稳定、可检索的核心单元，现已按语义 id 补卡；id 只表达概念，不带讲次编号。

| 建议 card id | 主要讲次 | 最小范围 |
|---|---|---|
| `data-representation` | L02、L08、L19 | 整数/浮点/文本/图像/声音编码与误差 |
| `stack-queue` | L04、L05、L09 | LIFO/FIFO、状态边界、缓冲与调度 |
| `trees-heaps` | L05、L06、L13 | 树遍历、堆序、优先队列与结构选择 |
| `algorithm-strategies` | L06、L17 | 搜索、排序、分治、贪心、动态规划及反例 |
| `computability-limits` | L07、L20 | 可判定性、复杂性、验证与自动化边界 |
| `computer-architecture` | L08、L19 | ISA、存储层次、局部性、CPU/GPU/NPU |
| `operating-systems` | L09、L20 | 进程、线程、调度、同步、隔离与配额 |
| `distributed-systems` | L10、L20 | API、复制、超时、重试、部分失败与一致性直觉 |
| `reproducible-computing` | L11、L18、L21 | 版本、环境、数据、参数、随机性和证据 |
| `ai-security` | L12、L20、L21 | 提示注入、越权、泄漏、供应链与安全评价 |
| `data-lifecycle-governance` | L14、L18、L21 | 来源、质量、许可、隐私、版本、删除与责任 |
| `probability-uncertainty` | L15、L18、L21 | 条件概率、基率、抽样、区间、相关/因果和不确定性 |
| `hci-accessibility` | L16、L21 | 交互反馈、认知负荷、无障碍与校准信任 |
| `ai-search-planning-agents` | L17、L20 | 状态空间、知识表示、规划与 Agent 闭环 |
| `ml-evaluation` | L18、L20、L21 | 划分、泄漏、指标、阈值、群体偏差和漂移 |
| `neural-networks-transformers` | L19、L20 | CNN/RNN/注意力的结构偏置与资源代价 |
| `multimodal-models` | L19、L20 | CNN/RNN/Transformer 与图像、语音、文本共享原理 |
| `rag-tool-agents` | L20、L21 | 检索、引用、结构化工具、权限、日志和评价 |
| `responsible-ai-systems` | L21（贯穿） | 人本、伦理、安全、公平、可持续、监督与问责 |

## 不进入稳定核心的内容

| 内容 | 去向 | 原因 |
|---|---|---|
| 具体模型版本、榜单和厂商功能 | `docs/frontier/` | 变化快，不能成为长期学习目标 |
| 区块链、元宇宙、5G 产品史 | 工程案例或前沿注记 | 可用于连接系统概念，但不值得挤占核心讲次 |
| 多带图灵机的大量机械步骤 | 延伸阅读 | 对本课程“理解边界”的边际价值较低 |
| 框架 API 与提示词模板背诵 | 实验按需提供 | 工具会变，评价与验证能力更稳定 |

## 迁移完成度

- [ ] 课程组审批 21 讲目标、边界与考核动作。
- [x] 用语义卡解除 `05`、`09`、`17`、`21` 的主题过载，同时保留旧公开路径。
- [x] 新增表示、概率/不确定性、数据治理、HCI/无障碍、分布式、AI 安全与系统工程卡。
- [x] 将 CV、语音、推荐定位为可跨 L18–L21 复用的应用案例卡。
- [x] 在 `lecture-card-map.yaml` 登记 `core_cards / supporting_cards / examples / labs / figures / assessment_tags`。
- [ ] 教师逐卡复核后，再把 `status` 从 `needs-review` 改为 `stable`。

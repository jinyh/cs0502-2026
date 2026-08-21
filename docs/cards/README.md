# 概念卡片图谱（docs/cards/）

卡片是可独立检索、练习和跨讲次复用的轻量概念单元，不要求与讲次或 `SlideNN-*.pdf` 一一对应。21 讲教学序列见 [`docs/curriculum/`](../curriculum/README.md)。

当前 `01-*`–`21-*` 是按旧讲稿建立的**迁移基线卡片**，数字前缀为 legacy id；`ext-*` 是同期补充卡。课程组审批新蓝图前保留这些路径，避免链接失效。它们与新讲次的多对多关系见 [`legacy-coverage-matrix.md`](../curriculum/legacy-coverage-matrix.md)。

## 旧 21 张讲稿锚点卡

| 编号 | 卡片文件 | 对应讲稿 | 思维支柱 | 一句话定位 |
|---|---|---|---|---|
| 01 | `01-welcome.md` | Slide01-Welcome | meta | 课程地图、学习闭环与考核边界 |
| 02 | `02-intro-to-cs.md` | Slide02-IntroToCS | 计算思维 | CS 的边界与四大思维支柱 |
| 03 | `03-programming-language.md` | Slide03-ProgrammingLanguage | 计算思维 | 编程语言如何把人的意图变成机器能执行的指令 |
| 04 | `04-data-structure-basics.md` | Slide04-DataStructure | 计算思维 | 线性表、顺序表与链表 |
| 05 | `05-data-structure-advanced.md` | Slide05-DataStructure2 | 计算思维 | 栈、队列、递归、树、堆与复杂度 |
| 06 | `06-graph-exploration.md` | Slide06-GraphExploration | 计算思维 | 图的遍历（BFS/DFS）与连通性 |
| 07 | `07-greedy-algorithm.md` | Slide07-GreedyAlgorithm | 计算思维 | 贪心范式与最优子结构 |
| 08 | `08-turing-machine.md` | Slide08-TuringMachine | 计算思维 | 图灵机组成、转移规则与模型边界 |
| 09 | `09-computer-system-arch.md` | Slide09-ComputerSystemAndArchitecture | 系统思维 | 计算机组成、进程、并发与操作系统资源管理 |
| 10 | `10-software-engineering.md` | Slide10-SoftwareEngineering | 系统思维 | 软件生命周期与工程方法 |
| 11 | `11-computer-network.md` | Slide11-ComputerNetwork | 系统思维 | 分层协议与互联网如何连通世界 |
| 12 | `12-information-security.md` | Slide12-InformationSecurity | 系统思维 | 密码学、安全威胁与防御 |
| 13 | `13-database.md` | Slide13-Database | 数据思维 | 关系模型、关系代数、SQL 与 DBMS |
| 14 | `14-data-mining.md` | Slide14-DataMining | 数据思维 | 从数据中挖掘模式与知识 |
| 15 | `15-data-visualization.md` | Slide15-DataVisualization | 数据思维 | 可视化编码与感知 |
| 16 | `16-artificial-intelligence.md` | Slide16-ArtificialIntelligence | 智能思维 | AI 的定义、范式与边界 |
| 17 | `17-machine-learning.md` | Slide17-MachineLearning | 智能思维 | 学习、泛化与神经网络演进 |
| 18 | `18-computer-vision.md` | Slide18-ComputerVision | 智能思维 | 让机器「看懂」图像 |
| 19 | `19-recommend-system.md` | Slide19-RecommendSystem | 智能思维 | 协同过滤与个性化推荐 |
| 20 | `20-speech-recognition.md` | Slide20-SpeechRecognition | 智能思维 | 端到端语音识别与 RNN 序列建模 |
| 21 | `21-llm.md` | Slide21-LLM | 智能思维 | 从 N-gram 到注意力与大语言模型 |

## 旧扩展卡片（ext- 前缀）

> `ext-*` 补全旧讲稿锚点卡未单独覆盖的导论要点。后续迁移完成后，不再区分“主卡”和“扩展卡”的教学地位。

| 文件 | 主题 | 参考来源 |
|---|---|---|
| `ext-complexity.md` | Slide05 复杂度补充：最好/最坏/平均、P 与 NP | Slide05、MIT 6.0001、CS50 |
| `ext-recursion-divide-conquer.md` | Slide05 递归补充：分治、归并排序 | Slide05、CS61A、CS106A |
| `ext-search-hashing.md` | 搜索、哈希、冲突与工程权衡 | CS50、旧版卡片 05 |
| `ext-scientific-computing.md` | 浮点误差、数值稳定性与可重复计算实验 | 工程计算公共基础 |
| `ext-web-technologies.md` | HTTP/HTML/前后端/REST、LLM API 接入 | CS50 Web 模块 |
| `ext-logic-boolean.md` | 布尔代数、逻辑门、与数字电路和程序逻辑的关系 | Dale Ch4、旧规划 |

## 新卡片模板

新卡片采用 [`docs/curriculum/README.md`](../curriculum/README.md) 的 `card_id / lecture_refs / source_slides / thinking_pillars` 元数据，把教学用途与讲稿来源分开。迁移期旧卡仍使用原有 `lecture / thinking_pillar` 字段，不做机械替换。

所有卡片正文结构：一句话定位 → 学完应能做到 → 核心知识点 → 工程桥接 → 常见误区与边界 → 主动学习与考核迁移 → 延伸阅读。前沿内容仅在确有必要时指向 `frontier/`，不为稳定主题强行添加。

## 建设状态

现有 27 张迁移基线卡统一标记为 `needs-review`。下一阶段按覆盖矩阵拆分过载卡、补齐缺失概念；只有课程目标、术语、代码、图示、链接和主动学习任务经过教师复核后，才标记为 `stable`。

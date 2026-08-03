# 知识点卡片（docs/cards/）

每讲一页轻量卡片，编号与 `LectureNotes/SlideNN-*.pdf` 严格一一对应，便于学生从讲稿跳转。

## 21 讲对应表

| 编号 | 卡片文件 | 对应讲稿 | 思维支柱 | 一句话定位 |
|---|---|---|---|---|
| 01 | `01-welcome.md` | Slide01-Welcome | — | 课程导引（行政介绍，卡片极简） |
| 02 | `02-intro-to-cs.md` | Slide02-IntroToCS | 计算思维 | CS 的边界与四大思维支柱 |
| 03 | `03-programming-language.md` | Slide03-ProgrammingLanguage | 计算思维 | 编程语言如何把人的意图变成机器能执行的指令 |
| 04 | `04-data-structure-basics.md` | Slide04-DataStructure | 计算思维 | 数组、栈、队列、链表、树与 ADT |
| 05 | `05-data-structure-advanced.md` | Slide05-DataStructure2 | 计算思维 | 搜索、哈希与散列 |
| 06 | `06-graph-exploration.md` | Slide06-GraphExploration | 计算思维 | 图的遍历（BFS/DFS）与连通性 |
| 07 | `07-greedy-algorithm.md` | Slide07-GreedyAlgorithm | 计算思维 | 贪心范式与最优子结构 |
| 08 | `08-turing-machine.md` | Slide08-TuringMachine | 计算思维 | 可计算性边界与图灵机模型 |
| 09 | `09-computer-system-arch.md` | Slide09-ComputerSystemAndArchitecture | 系统思维 | 从逻辑门到 CPU 的硬件层次与冯诺依曼架构 |
| 10 | `10-software-engineering.md` | Slide10-SoftwareEngineering | 系统思维 | 软件生命周期与工程方法 |
| 11 | `11-computer-network.md` | Slide11-ComputerNetwork | 系统思维 | 分层协议与互联网如何连通世界 |
| 12 | `12-information-security.md` | Slide12-InformationSecurity | 系统思维 | 密码学、安全威胁与防御 |
| 13 | `13-database.md` | Slide13-Database | 数据思维 | 关系模型、SQL 与事务 |
| 14 | `14-data-mining.md` | Slide14-DataMining | 数据思维 | 从数据中挖掘模式与知识 |
| 15 | `15-data-visualization.md` | Slide15-DataVisualization | 数据思维 | 可视化编码与感知 |
| 16 | `16-artificial-intelligence.md` | Slide16-ArtificialIntelligence | 智能思维 | AI 的定义、范式与边界 |
| 17 | `17-machine-learning.md` | Slide17-MachineLearning | 智能思维 | 学习的三范式与基本流程 |
| 18 | `18-computer-vision.md` | Slide18-ComputerVision | 智能思维 | 让机器「看懂」图像 |
| 19 | `19-recommend-system.md` | Slide19-RecommendSystem | 智能思维 | 协同过滤与个性化推荐 |
| 20 | `20-speech-recognition.md` | Slide20-SpeechRecognition | 智能思维 | 声学信号到文本的映射 |
| 21 | `21-llm.md` | Slide21-LLM | 智能思维 | 大语言模型与 Agent 时代 |

## 卡片模板

每张卡片使用统一 YAML 元数据头 + 正文结构，详见 `04-data-structure-basics.md`（首个范例，确立全库写作范式）。字段：`title / lecture / aliases / thinking_pillar / category / tags / status / version / importance(1-5) / related_cards / related_deep / related_visualizations / last_reviewed`。

正文结构：一句话定位 → 核心知识点 → 直觉类比 → 前沿进展注记 → 跨学科联系 → 推荐交互式问答 → 延伸阅读。

## 建设状态

- [x] 04 数据结构基础（范例）
- [ ] 其余卡片建设中（高价值优先：04/06/07/08/16/17/21）

# 课程讲稿概述（Lecture Notes）

本目录在教师本机保存 CS0502「计算机科学导论」21 讲 PDF。PDF 课程讲稿不进入公开 GitHub 仓库，学生应从课程 Canvas 获取正式版本；公开仓库只提交本说明文件。

知识库并不替代课程讲稿：`LectureNotes/` 提供课程教学来源，`docs/cards/` 把概念拆成可检索和练习的卡片，`docs/curriculum/` 负责组织补充资源。实际授课必须先核对 `docs/course/schedule.md` 的最新教学日历；讲稿编号只用于定位来源，21 讲蓝图也不得替代实际课次。

## 讲稿清单

| 来源编号 | 本地文件名 | 主题概述 | 主要思维支柱 |
|---|---|---|---|
| Slide01 | `Slide01-Welcome-2025.pdf` | 课程导引、学习目标与课程组织 | 课程元认知 |
| Slide02 | `Slide02-IntroToCS-2025.pdf` | 计算机科学边界与计算思维 | 计算思维 |
| Slide03 | `Slide03-ProgrammingLanguage-2025.pdf` | 编程语言、语法语义、编译与解释 | 计算思维 |
| Slide04 | `Slide04-DataStructure-2025.pdf` | 线性表、顺序存储与链式存储 | 计算思维 |
| Slide05 | `Slide05-DataStructure2-2025.pdf` | 栈、队列、递归、树、堆与复杂度 | 计算思维 |
| Slide06 | `Slide06-GraphExploration-2025.pdf` | 图表示、BFS、DFS 与连通性 | 计算思维 |
| Slide07 | `Slide07-GreedyAlgorithm-2025.pdf` | 贪心算法、最短路径与正确性边界 | 计算思维 |
| Slide08 | `Slide08-TuringMachine-2025.pdf` | 图灵机、状态转移与可计算性 | 计算思维 |
| Slide09 | `Slide09-ComputerSystemAndArchitecture-2025.pdf` | 计算机组成、体系结构与操作系统概览 | 系统思维 |
| Slide10 | `Slide10-SoftwareEngineering-2025.pdf` | 软件生命周期、需求、设计与测试 | 系统思维 |
| Slide11 | `Slide11-ComputerNetwork-2025.pdf` | 计算机网络、分层协议与互联网 | 系统思维 |
| Slide12 | `Slide12-InformationSecurity-2025.pdf` | 信息安全、密码学、威胁与防御 | 系统思维 |
| Slide13 | `Slide13-Database-2025.pdf` | 关系模型、SQL、DBMS 与查询 | 数据思维 |
| Slide14 | `Slide14-DataMining-2025.pdf` | 聚类、分类、关联规则与数据挖掘 | 数据思维 |
| Slide15 | `Slide15-DataVisualization-2025.pdf` | 可视化编码、图表选择与数据解释 | 数据思维 |
| Slide16 | `Slide16-ArtificialIntelligence-2025.pdf` | 人工智能定义、范式、搜索与智能体 | 智能思维 |
| Slide17 | `Slide17-MachineLearning-2025.pdf` | 机器学习、泛化与神经网络 | 智能思维 |
| Slide18 | `Slide18-ComputerVision-2025.pdf` | 计算机视觉、卷积与视觉任务 | 智能思维 |
| Slide19 | `Slide19-RecommendSystem-2025.pdf` | 推荐系统、协同过滤与评价 | 智能思维 |
| Slide20 | `Slide20-SpeechRecognition-2025.pdf` | 语音识别、序列模型与 WER | 智能思维 |
| Slide21 | `Slide21-LLM-2025.pdf` | 语言模型、注意力与大语言模型 | 智能思维 |

## 与公开知识库的关系

- 讲稿来源锚点和概览卡见 `docs/cards/01-welcome.md` 至 `docs/cards/21-llm.md`。
- AI 时代 21 讲教学蓝图见 `docs/curriculum/21-lecture-blueprint.md`。
- 讲次、概念卡、example、Lab 和配图的精确关系见 `docs/curriculum/lecture-card-map.yaml`。
- OpenCode 检索时应从 `opencode/knowledge.md` 和课程映射开始，不得仅根据 `SlideNN` 或卡片数字前缀猜测学习顺序。

## 维护约定

- PDF 文件只在本地与 Canvas 维护，不使用 `git add -f` 强制加入仓库。
- 讲稿更新时同步检查文件名、年份、主题概述和对应来源锚点。
- 公开知识库可以补充前沿、代码和主动练习，但不复制讲稿全文或把模型生成内容冒充讲稿原文。
- 若讲次安排发生变化，先更新 `docs/course/schedule.md`，再同步课程蓝图与讲稿说明；不要为匹配新顺序批量重命名只读讲稿。

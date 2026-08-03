# 项目：计算机科学导论百科全书

## 概述

这是一个面向非计算机专业理工及医学科学生的教科书级计算机科学导论百科，以上海交通大学 CS1955-02 计算机科学导论课程的 21 个讲稿为基础，扩展覆盖操作系统、编译原理、动态规划等经典 CS 主题。项目采用中英双语，混合文档、代码示例与可视化等多种形式，配合 OpenCode 类工具实现交互式教学（问答与沙箱代码运行）。

## 目标受众与教学理念

### 受众画像

- 大学二年级理工科及医学科学生
- 具备微积分和线性代数基础，无 CS 先修知识
- 目标：建立对计算机科学完整知识体系的直觉与基本理解

### 写作原则

- **从直觉到形式**：先用类比和生活例子建立直觉，再引入形式化定义
- **跨学科桥接**：在解释 CS 概念时主动关联数学、物理、生物学知识（如：图论与分子结构、信息安全与医疗数据隐私）
- **渐进式深入**：每个主题从"为什么需要"开始，逐步展开到"怎么实现"
- **避免术语轰炸**：首次出现的每个术语都需要定义和中英标注

## 目录结构

```
ComputerIntroduction/
├── CLAUDE.md                           # 本文件：项目约定与 AI 协作指南
├── Ref_CLAUDE.md                       # CLAUDE.md 设计参考与决策记录
├── 从基础学科到通用人工智能.md            # 知识体系总览（跨学科视角）
├── README.md                           # 项目说明（中英双语）
├── LectureNotes/                       # 课程讲稿（PDF，只读参考）
├── docs/                               # 百科专题文档
│   ├── zh/                             # 中文版
│   │   ├── fundamentals/              # A. 计算基础（7 篇）
│   │   ├── data-structures-algorithms/ # B. 数据结构与算法（8 篇）
│   │   ├── systems/                   # C. 计算机系统（5 篇）
│   │   ├── networking-security/       # D. 网络与安全（4 篇）
│   │   ├── data/                      # E. 数据科学（4 篇）
│   │   ├── ai-ml/                     # F. 人工智能与机器学习（9 篇）
│   │   ├── emerging/                  # G. 新兴技术（4 篇）
│   │   └── interdisciplinary/         # H. 交叉学科与社会影响（4 篇）
│   └── en/                             # English version（同结构）
├── code/                               # 代码示例（可独立运行）
│   ├── data-structures/
│   ├── algorithms/
│   ├── systems/
│   └── visualizations/
├── figures/                            # 图表与示意图
└── references/                         # 参考文献与资料
```

## 主题覆盖范围

### A. 计算基础（`docs/zh/fundamentals/`）— 7 篇

- `01-intro-to-cs.md` — 计算机科学导论（对应 Slide02-IntroToCS）
- `02-number-systems.md` — 数制与数据表示 | *新增*（Forouzan Ch2-4：二进制/补码/浮点数/字符编码）
- `03-programming-language.md` — 编程语言（对应 Slide03-ProgrammingLanguage）
- `04-turing-machine.md` — 图灵机与可计算性（对应 Slide08-TuringMachine）
- `05-formal-languages.md` — *扩展：形式语言与自动机*
- `06-compiler.md` — *扩展：编译原理*
- `07-logic-boolean.md` — 数理逻辑与布尔代数 | *新增*（Dale Ch4：布尔代数是数字电路和程序逻辑的数学基础）

### B. 数据结构与算法（`docs/zh/data-structures-algorithms/`）— 8 篇

- `01-data-structure-basics.md` — 数据结构基础：数组、栈、队列、链表、树（对应 Slide04-DataStructure）
- `02-data-structure-advanced.md` — 数据结构进阶：搜索、哈希（对应 Slide05-DataStructure2）
- `03-graph-exploration.md` — 图的遍历（对应 Slide06-GraphExploration）
- `04-sorting-algorithms.md` — 排序算法 | *新增*（大纲 Week3：冒泡/快排/归并/堆排序）
- `05-greedy-algorithm.md` — 贪心算法（对应 Slide07-GreedyAlgorithm）
- `06-dynamic-programming.md` — *扩展：动态规划*
- `07-divide-and-conquer.md` — 分治法 | *新增*（与排序/搜索紧密关联，三大算法范式之一）
- `08-complexity-theory.md` — *扩展：算法复杂度与计算复杂性理论*

### C. 计算机系统（`docs/zh/systems/`）— 5 篇

- `01-digital-circuits.md` — 数字电路与逻辑门 | *新增*（Dale Ch4-5：从逻辑门到 CPU 的硬件基础）
- `02-computer-architecture.md` — 计算机系统与架构（对应 Slide09-ComputerSystemAndArchitecture）
- `03-operating-system.md` — 操作系统（对应 Slide09 后半部分 + 扩展）
- `04-software-engineering.md` — 软件工程（对应 Slide10-SoftwareEngineering）
- `05-parallel-distributed.md` — *扩展：并行与分布式计算*

### D. 网络与安全（`docs/zh/networking-security/`）— 4 篇

- `01-computer-network.md` — 计算机网络（对应 Slide11-ComputerNetwork）
- `02-information-security.md` — 信息安全与密码学（对应 Slide12-InformationSecurity）
- `03-web-technologies.md` — Web 技术与互联网应用 | *新增*（HTTP/HTML/前后端架构）
- `04-iot-emerging-networks.md` — 物联网与新型网络 | *新增*（大纲 Week5 第二讲）

### E. 数据科学（`docs/zh/data/`）— 4 篇

- `01-database.md` — 数据库（对应 Slide13-Database）
- `02-data-mining.md` — 数据挖掘（对应 Slide14-DataMining）
- `03-data-visualization.md` — 数据可视化（对应 Slide15-DataVisualization）
- `04-big-data.md` — 大数据技术 | *新增*（MapReduce/Spark/分布式存储）

### F. 人工智能与机器学习（`docs/zh/ai-ml/`）— 9 篇

- `01-artificial-intelligence.md` — 人工智能（对应 Slide16-ArtificialIntelligence）
- `02-machine-learning.md` — 机器学习（对应 Slide17-MachineLearning）
- `03-deep-learning.md` — 深度学习 | *新增*（Slide17 后半 + 扩展：CNN/RNN/Transformer）
- `04-computer-vision.md` — 计算机视觉（对应 Slide18-ComputerVision）
- `05-nlp.md` — *扩展：自然语言处理*
- `06-speech-recognition.md` — 语音识别（对应 Slide20-SpeechRecognition）
- `07-recommend-system.md` — 推荐系统（对应 Slide19-RecommendSystem）
- `08-llm.md` — 大语言模型（对应 Slide21-LLM）
- `09-reinforcement-learning.md` — *扩展：强化学习*

### G. 新兴技术（`docs/zh/emerging/`）— 4 篇 🆕

- `01-cloud-computing.md` — 云计算与虚拟化（SaaS/PaaS/IaaS，所有学生都在使用的基础设施）
- `02-quantum-computing.md` — 量子计算基础（对物理/化学/材料学生尤为相关的计算范式变革）
- `03-blockchain.md` — 区块链与去中心化技术（共识机制，医疗数据安全的新方向）
- `04-robotics.md` — 机器人学（融合传感/控制/AI，工科和医学的交叉点）

### H. 交叉学科与社会影响（`docs/zh/interdisciplinary/`）— 4 篇 🆕

- `01-bioinformatics.md` — 生物信息学与计算医学（基因序列分析、医学影像AI、电子病历系统）
- `02-hci.md` — 人机交互（用户界面设计，医疗信息系统的可用性）
- `03-computing-ethics.md` — 计算伦理与 AI 治理（AI 在医疗/司法中的偏见、隐私保护）
- `04-computational-science.md` — 科学计算与仿真模拟（数值模拟/有限元/蒙特卡洛，理工学生的核心工具）

## 写作规范

### 语言

- 中文为主体写作语言，同步维护英文版本
- 专业术语首次出现时标注英文原文，如：栈（stack）
- 人名保留原文，不翻译
- 代码注释使用中文

### 内容模板

每个主题文档遵循以下标准结构。**可根据主题特点裁剪或调整章节顺序**——例如：数据可视化无需"算法与原理"章节，软件工程的"代码示例"侧重工程实践而非算法演示。

```markdown
# [主题名称]（English Name）

## 概述
一段话概括本主题在 CS 中的地位和重要性，以及为什么非CS专业学生也需要了解它。

## 生活中的类比
用日常生活或学生熟悉的学科场景引入核心概念（如：用图书馆比喻数据库）。

## 历史背景
关键人物、时间节点、里程碑事件。

## 核心概念
- 概念 A：定义 + 直觉解释 + 图示
- 概念 B：...
每个概念先给直觉，再给形式化定义。

## 算法与原理
详细的算法描述，伪代码或 Python 实现，复杂度分析。
对非CS学生：强调"算法在做什么"而非仅仅"怎么写代码"。

## 代码示例
可独立运行的 Python 代码，配合输出和逐行解释。
代码应简洁，避免复杂的工程实践，专注于概念演示。

## 可视化
matplotlib/plotly 图表，流程图，架构图。

## 跨学科联系
本主题与数学/物理/生物/医学等学科的关联。
例：图论与分子结构、信息安全与医疗数据隐私。

## 实际应用
该主题在工业界和学生专业领域的应用案例。

## 延伸阅读
教科书、论文、在线资源（标注难度级别）。
```

### Markdown 格式

- 标题层级：`##` 大章节 → `###` 子话题 → `####` 具体内容
- 列表项使用 `-` 而非 `*`
- 代码块标注语言类型（```python、```math 等）
- 数学公式使用 LaTeX 语法（`$$...$$`）
- 文件使用 UTF-8 编码

## 代码规范

- Python 为主要编程语言，面向初学者风格
- 代码可独立运行，开头注明对应主题和前置依赖
- `requirements.txt` 管理依赖
- 注重可读性，变量命名清晰，配合中文注释
- 避免复杂的设计模式和工程技巧，专注概念演示
- 可视化优先 matplotlib / plotly，输出保存到 `figures/`，格式优先 SVG/PNG
- 图表标题和标签使用中英双语

## 协作约定

- 新增主题前确认在「主题覆盖范围」章节中已列出
- 文件命名：`XX-topic-name.md`（XX 为两位序号）
- 对应讲稿引用格式：`（对应 SlideXX-EnglishName）`，如 `（对应 Slide02-IntroToCS）`
- 参考文献格式：`作者 (年份). 标题. *期刊/出版社*.`
- Git 提交信息使用中文，格式：`类型: 简要描述`
  - 类型包括：`新增`、`修改`、`修复`、`重构`、`文档`

## 当前进度

### 已有资源

- 21 个课程讲稿 PDF（`LectureNotes/`），其中 Slide01-Welcome 为课程行政介绍
- 课程大纲（`Syllabus-IntroductionToCS-2024Spring.pdf`）
- 知识体系总览文档（`从基础学科到通用人工智能.md`）

### 待完成

- 各主题独立百科文档（`docs/zh/` 下 8 个子目录，约 45 篇）
- 代码示例（`code/`）
- 可视化图表（`figures/`）
- 英文版（`docs/en/`）
- README.md

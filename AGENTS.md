# 项目：计算机科学导论配套知识库 + 交互式智能体

## 概述

上海交通大学「计算机科学导论（CS0502）」课程由计算机学院课程组承担，面向全校非计算机专业理工及医学科学生。本项目以课程讲稿 PDF 为只读来源锚点，构建一套**混合形态开源知识库**，并配套以阿里百炼 `qwen3.8-max` 为主测模型、provider-agnostic 的主动学习智能体。OpenCode 提供完整入口，Pi 通过只读薄适配层复用同一套教学资源。21 讲蓝图用于组织补充资源，概念卡片是多对多知识图谱，两者不要求一一对应。

知识库形态（混合方案）：

- **21 讲课程蓝图**（`docs/curriculum/`）— 教学目标、工程场景、主动任务与跨章迁移
- **轻量概念卡片**（`docs/cards/`）— 来源锚点/概览卡与可跨讲次复用的语义概念卡
- **少数 AI 高价值深度专题**（`docs/deep/`）— LLM、强化学习、量子计算等前沿变化快的主题
- **前沿进展注记**（`docs/frontier/`）— 静态写底 + 智能体联网增量双层机制
- **多路径索引**（`docs/paths/`）— 参考 Path2AGI，按思维支柱 / AI 能力 / 读者目标 / 跨学科桥接导航

讲稿 PDF（课程内部材料，发布在 Canvas，不入仓库）只读，不动。知识库是其「AI 时代补层」而非替代——重点补充讲稿静态形式难以承载的**前沿进展**与**交互式问答**。

> 语言策略：中文为主，专业术语首次出现时标注英文原文（如：栈（stack））。暂不维护完整英文版。

## 目标受众与教学理念

### 受众画像

- 大学二年级理工科及医学科学生
- 具备微积分和线性代数基础，无 CS 先修知识
- 目标：建立对计算机科学完整知识体系的直觉与基本理解

### 写作原则

- **从直觉到形式**：先用类比和生活例子建立直觉，再引入形式化定义
- **跨学科桥接**：解释 CS 概念时主动关联数学、物理、生物学知识（如图论与分子结构、信息安全与医疗数据隐私）
- **渐进式深入**：每个主题从「为什么需要」开始，逐步展开到「怎么实现」
- **避免术语轰炸**：首次出现的每个术语都需要定义和中英标注
- **卡片优先轻量，深度专题按需**：单卡片控制在 ~300 行，深度内容强制入 `docs/deep/`，避免卡片退化为厚重百科

## 目录结构

```
ComputerIntroduction/
├── .gitignore                         # 安全隔离（reference/ 等敏感数据永不提交）
├── AGENTS.md                           # 项目约定与 AI 协作指南（三端共享主文件）
├── CLAUDE.md                           # Claude Code 入口（导入 AGENTS.md）
├── README.md                           # 仓库说明（中英摘要 + 快速开始）
├── LICENSE                             # 内容 CC-BY-SA 4.0 / 代码 MIT
├── LectureNotes/  # 讲稿 PDF，课程内部材料，见 Canvas，不入仓库（本地保留）
├── docs/                               # 知识库主体
│   ├── README.md
│   ├── curriculum/                    # 21 讲教学蓝图 + 机器资源映射 + 旧卡迁移矩阵
│   ├── cards/                         # 多对多概念卡片（编号文件为来源锚点）
│   │   ├── README.md                  # 卡片图谱、完整清单 + 模板说明
│   │   └── 01-welcome.md ... 21-llm.md
│   ├── deep/                          # 少数 AI 高价值深度专题
│   │   ├── README.md                  # 选材标准 + 旧 45 篇规划降级附录
│   │   └── llm-deep-dive.md  reinforcement-learning.md  quantum-computing.md
│   ├── frontier/                      # 前沿注记（静态写底 + 智能体联网增量）
│   │   ├── README.md  _template.md
│   │   └── llm-frontier.md  cv-frontier.md
│   ├── paths/                         # 多路径索引
│   │   ├── by-thinking-pillar.md       # 计算思维 / 系统 / 数据 / 智能
│   │   ├── by-ai-capability.md         # 感知 → 学习 → 推理 → 生成 → Agent
│   │   ├── by-reader-goal.md           # 医工 / 信工 / 材料 / 理科
│   │   └── by-discipline-bridge.md     # CS ↔ 医学 / 物理 / 生物
│   └── glossary.md                    # 全局术语表（中英对照）
├── opencode/                           # OpenCode 智能体入口
│   ├── AGENTS.md                      # 行为约束（教学红线 / 不代写作业 / 沙箱安全）
│   ├── knowledge.md                   # 知识库索引（指向 docs/，机器可解析）
│   ├── lecture-runtime-index.jsonl    # /demo、/lab 单行快速资源索引
│   ├── tools.md                       # OpenCode / Qwen / 沙箱意图与约束
│   └── sandbox-policy.md              # 白名单包 / 超时 / 内存 / 禁网
├── .opencode/                         # 学生 agent / skills / slash commands
├── .pi/                               # Pi 只读工具、路径护栏与共享资源加载适配
├── notebooks/modelscope/              # PAI-DSW 一键环境与课程运行 helper
├── code/                               # 代码示例与沙箱
│   ├── README.md  requirements.txt
│   ├── examples/                      # 概念演示 Python（映射见 curriculum YAML）
│   ├── labs/                          # 8 个默认形成性 Lab + catalog.json 可选作业关联
│   └── visualizations/               # 自包含 HTML 交互可视化（迁移自课程 Demo）
└── figures/                           # 静态图（SVG 优先）
```

## 主题覆盖范围

实际授课主线以 [`docs/course/schedule.md`](docs/course/schedule.md) 的最新教学日历为准。[`docs/curriculum/21-lecture-blueprint.md`](docs/curriculum/21-lecture-blueprint.md) 用于组织补充资源；概念覆盖由 `docs/cards/` 提供，多讲与多卡之间允许多对多映射。旧版规划的 8 大类约 45 篇百科**降级为可选扩展附录**，见 `docs/deep/README.md`——按需取舍，不作为主线承诺。

> 2026 年备课必须先核对最新教学日历，按实际课次确定主题、内容范围及前后衔接。21 讲知识库蓝图用于组织补充资源，旧 PDF 编号用于定位来源，均不得替代实际教学日历。每次修订须检查原版知识覆盖，不能因加入案例、AI 或工具演示而无说明地删减核心内容。

凡旧规划主题确有深度展开需要时，在 `docs/deep/` 新建文件并在对应卡片 `related_deep` 字段登记反向链接。

现有 **扩展卡片**（`docs/cards/ext-*.md`）已迁移到新语义元数据，只为兼容公开路径保留 `ext-` 文件名。讲次与卡片的实际组合见 `docs/curriculum/lecture-card-map.yaml`，迁移依据见 `docs/curriculum/legacy-coverage-matrix.md`。

## 安全隔离约定（红线）

`reference/` 目录是教师教务工作区，含**学生名单、成绩表、期末考题**等敏感数据，**永不提交**至公开仓库。

- `.gitignore` 已纳入 `reference/` 整目录 + `*.xls / *.xlsx / *.docx` + `*考题* / *成绩* / *学生名单* / *作业*` 等通配双保险
- 每次提交前用 `git status --porcelain` 自检，确认零敏感文件命中
- 若学生向智能体粘贴名单 / 成绩 / 考题内容，智能体须立即拒绝并提示隐私（见 `opencode/AGENTS.md` 教学红线第 2 条）

## 智能体配置约定

`opencode/` 与 `.opencode/` 是课程智能体的共享教学资源和 OpenCode 完整入口；`.pi/` 只提供 Pi 的加载与只读权限适配：

- `AGENTS.md` — 行为约束中枢：角色为课程学习助教；红线为不代写作业只给思路、不触碰敏感数据、导论不引入超范围形式化证明、直觉先行；语言中文为主、语气像助教
- `knowledge.md` — 知识库检索入口：先定位课程讲次与学习目标，再按概念 tags 选择必要卡片、实验和深度专题
- `lecture-runtime-index.jsonl` — `/demo`、`/lab` 的单行快速索引；由测试保证与课程 YAML 一致，避免每次加载完整映射
- `tools.md` — 工具配置：写意图与约束，不保存 provider 密钥；本学期以用户缺省 `qwen3.8-max` 为主测模型
- `sandbox-policy.md` — 沙箱安全：白名单 `numpy / pandas / sklearn / matplotlib / networkx`，超时 30s，本机 Linux 512MB、ModelScope 2GB，运行代码禁网
- `.opencode/` — `course-tutor` agent、5 个项目级学习 skill 与 10 个 slash command；优先要求学生预测、追踪、实现和迁移，不直接长问答
- `.pi/` — 自动加载 `.opencode/` 的同一套资源，映射 Pi 工具名并限制为课程目录内只读访问；不得复制维护第二套 skill
- 学生本机运行 OpenCode 或 Pi，代码统一在 PAI-DSW Quickstart 中运行；两端只通过 helper 指令与 `[CS0502_RESULT]` 摘要手动交接，不建立远程执行 API
- 全学期安排 3 次正式作业；Lab 默认形成性，只有教师正式指定时才通过 `code/labs/catalog.json` 的 `assignment_links` 公开关联作业
- 全局 skill 属于用户环境，永不复制、链接、提交或推送；仓库只维护 `.opencode/skills/` 中的课程专属 skill

## AI 时代特色

本项目通过以下机制体现「AI+ 课程」：

- **四大思维支柱对齐**：课程蓝图与卡片元数据共同对齐计算思维 / 系统思维 / 数据思维 / 智能思维，支撑 `paths/by-thinking-pillar.md`
- **前沿进展机制**：`docs/frontier/` 双层结构——静态写底层（带一手来源，只有 `review_status: approved` 才称课程组批准基线）+ 智能体联网增量区（每条标注检索日期与来源 URL，未经审校，学生批判性阅读）。仅对高变动 AI 主题建前沿页
- **交互式智能体**：本机 OpenCode 或 Pi 加载同一知识库做主动学习，PAI-DSW 提供一致代码环境，通过预测—云端验证—复盘闭环超越静态阅读；联网与写入能力按各入口单独验收
- **跨学科桥接**：卡片「直觉类比」与「跨学科联系」字段主动关联医学 / 物理 / 生物，适配非 CS 专业背景

## 写作规范

### 内容模板

**知识点卡片模板**（`docs/cards/`，每个概念一页，~300 行上限）：

```markdown
---
title: <概念名称>
card_id: <稳定语义 id>
lecture_refs: [L04, L06]
source_slides: [SlideNN-EnglishName-2025]
aliases: [<别名1>, <别名2>]
thinking_pillars: [<计算思维|系统思维|数据思维|智能思维>]
category: <分类>
tags: [<tag1>, <tag2>]
status: <draft|needs-review|ai-reviewed|stable>
version: 1.0
importance: <1-5>
learning_objectives: [<可观察目标1>, <可观察目标2>, <可观察目标3>]
prerequisites: [<前置 card_id>]
estimated_minutes: <分钟>
assessment_tags: [<认知动作/题型标签>]
labs: [<实验 id>]
figures: [<SVG 文件名>]
related_cards: [<卡片编号-名>]
related_deep: [<深度专题>]
related_visualizations: [<可视化名>]
last_reviewed: YYYY-MM-DD
---

# <主题名称>（English Name）

> 来源锚点：`SlideNN-EnglishName-2025.pdf`（如有；见课程 Canvas，不在公开仓库）

## 一句话定位
## 核心知识点（最小可检索单元）
## 直觉类比（跨学科桥接）
## 前沿进展注记（指向 frontier/）
## 跨学科联系
## 主动学习任务（预测 / 追踪 / 迁移 / 反思）
## 延伸阅读
```

**深度专题模板**（`docs/deep/`）不限篇幅，可含完整推导、代码与前沿展开，沿用旧百科模板的「历史背景 / 算法与原理 / 代码示例 / 可视化 / 实际应用 / 延伸阅读」结构。

**前沿注记模板**见 `docs/frontier/_template.md`。

### Markdown 格式

- 标题层级：`##` 大章节 → `###` 子话题 → `####` 具体内容
- 列表项使用 `-` 而非 `*`
- 代码块标注语言类型（```python、```math 等）
- 数学公式使用 LaTeX 语法（`$$...$$`）
- 文件使用 UTF-8 编码

## 代码规范

- Python 为主要编程语言，面向初学者风格
- 代码可独立运行，开头注明对应主题和前置依赖
- `code/requirements.txt` 管理依赖
- 注重可读性，变量命名清晰，配合中文注释
- 避免复杂的设计模式和工程技巧，专注概念演示
- 可视化优先 matplotlib / plotly，输出保存到 `figures/`，格式优先 SVG/PNG
- 图表标题和标签使用中英双语
- 沙箱运行安全白名单与限制见 `opencode/sandbox-policy.md`

## 协作约定

- 新增主题前确认其服务 `docs/curriculum/` 的学习目标，或符合 `docs/deep/README.md` 的选材标准
- 新卡片使用语义化文件名与稳定 `card_id`；不得为了与讲次或 `SlideNN` 对齐而合并无关概念
- 用 `lecture_refs` 表示一张卡服务的一个或多个讲次，用 `source_slides` 记录只读讲稿来源；二者不得混用
- 迁移前的 `01-*`–`21-*` 和 `lecture` 字段继续保留，不做无依据的批量重命名
- 参考文献格式：`作者 (年份). 标题. *期刊/出版社*.`
- **跨学科联系**：优先体现交大优势工科（船舶海洋/材料化工/机械动力/生物医药/航空航天），见 `docs/paths/by-discipline-bridge.md`
- **提交前自检**：`git status --porcelain` 确认未含 `reference/` 敏感文件
- Git 提交信息使用中文，格式：`类型: 简要描述`（类型：`新增`、`修改`、`修复`、`重构`、`文档`）

## 项目进度入口

资源清单、完成状态与待办见 [项目进度记录](docs/project-status.md)。课程结构与考核约束仍以本文件及课程、考核权威文档为准；开展任务时核对进度记录的日期和实际文件。

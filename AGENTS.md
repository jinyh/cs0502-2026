# 项目：计算机科学导论配套知识库 + 交互式智能体

## 概述

上海交通大学「计算机科学导论（CS0502）」课程由计算机学院课程组承担，面向全校非计算机专业理工及医学科学生。本项目以 21 个课程讲稿 PDF 为只读锚点，构建一套**混合形态开源知识库**，并配套以阿里百炼 `qwen3.8-max` 为主测模型、provider-agnostic 的 **OpenCode 主动学习智能体**。

知识库形态（混合方案）：

- **21 讲轻量知识点卡片**（`docs/cards/`）— 一讲一页，核心知识点 + 直觉类比 + 前沿注记 + 跨学科联系
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
│   ├── cards/                         # 21 讲轻量卡片（一讲一页，编号对齐 SlideNN）
│   │   ├── README.md                  # 21 讲对应表 + 模板说明
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
│   ├── tools.md                       # OpenCode / Qwen / 沙箱意图与约束
│   └── sandbox-policy.md              # 白名单包 / 超时 / 内存 / 禁网
├── .opencode/                         # 学生 agent / skills / slash commands
├── code/                               # 代码示例与沙箱
│   ├── README.md  requirements.txt
│   ├── examples/                      # 概念演示 Python（文件名前缀对应卡片编号）
│   └── visualizations/               # 自包含 HTML 交互可视化（迁移自课程 Demo）
└── figures/                           # 静态图（SVG 优先）
```

## 主题覆盖范围

主线为 **21 讲对应卡片**（见 `docs/cards/README.md` 的对应表）。旧版规划的 8 大类约 45 篇百科**降级为可选扩展附录**，见 `docs/deep/README.md`——按需取舍，不作为主线承诺。

凡旧规划主题确有深度展开需要时，在 `docs/deep/` 新建文件并在对应卡片 `related_deep` 字段登记反向链接。

**扩展卡片**（`docs/cards/ext-*.md`）补全 21 讲未单独成讲、但导论应有的要点（算法复杂度、递归与分治、搜索与哈希、科学计算、Web 技术基础、布尔逻辑），参考国内外导论（CS50/CS61A/CS106A/6.0001）与旧 45 篇规划。与 01-21 讲稿锚点卡片共模板、共入索引，见 `docs/cards/README.md`。

## 安全隔离约定（红线）

`reference/` 目录是教师教务工作区，含**学生名单、成绩表、期末考题**等敏感数据，**永不提交**至公开仓库。

- `.gitignore` 已纳入 `reference/` 整目录 + `*.xls / *.xlsx / *.docx` + `*考题* / *成绩* / *学生名单* / *作业*` 等通配双保险
- 每次提交前用 `git status --porcelain` 自检，确认零敏感文件命中
- 若学生向智能体粘贴名单 / 成绩 / 考题内容，智能体须立即拒绝并提示隐私（见 `opencode/AGENTS.md` 教学红线第 2 条）

## 智能体配置约定

`opencode/` 子目录是学生本地拉取仓库后用 OpenCode 加载的智能体入口：

- `AGENTS.md` — 行为约束中枢：角色为课程学习助教；红线为不代写作业只给思路、不触碰敏感数据、导论不引入超范围形式化证明、直觉先行；语言中文为主、语气像助教
- `knowledge.md` — 知识库检索入口：21 卡片表（编号 | 标题 | Slide | 一句话定位 | tags）+ 深度专题清单 + 跳转索引，机器可解析 + 人类可读
- `tools.md` — 工具配置：写意图与约束，不保存 provider 密钥；本学期以用户缺省 `qwen3.8-max` 为主测模型
- `sandbox-policy.md` — 沙箱安全：白名单 `numpy / pandas / sklearn / matplotlib / networkx`，超时 30s，Linux 内存 512MB 硬限制，macOS 依赖外层配额，运行代码禁网
- `.opencode/` — `course-tutor` agent、5 个学习 skill 与 8 个 slash command；优先要求学生预测、追踪、实现和迁移，不直接长问答

## AI 时代特色

本项目通过以下机制体现「AI+ 课程」：

- **四大思维支柱对齐**：卡片 `thinking_pillar` 字段与课程大纲的四大思维（计算思维 / 系统思维 / 数据思维 / 智能思维）对齐，支撑 `paths/by-thinking-pillar.md`
- **前沿进展机制**：`docs/frontier/` 双层结构——静态写底层（人工审校，季度更新，可作引用依据）+ 智能体联网增量区（每条标注检索日期与来源 URL，未经审校，学生批判性阅读）。仅对高变动 AI 主题建前沿页
- **交互式智能体**：OpenCode 加载知识库做问答、跑代码沙箱、联网补充最新前沿，超越静态阅读
- **跨学科桥接**：卡片「直觉类比」与「跨学科联系」字段主动关联医学 / 物理 / 生物，适配非 CS 专业背景

## 写作规范

### 内容模板

**知识点卡片模板**（`docs/cards/`，每讲一页，~300 行上限）：

```markdown
---
title: <主题名称>
lecture: SlideNN-EnglishName-2025
aliases: [<别名1>, <别名2>]
thinking_pillar: <计算思维|系统思维|数据思维|智能思维>
category: <分类>
tags: [<tag1>, <tag2>]
status: <stable|draft|needs-review>
version: 1.0
importance: <1-5>
related_cards: [<卡片编号-名>]
related_deep: [<深度专题>]
related_visualizations: [<可视化名>]
last_reviewed: YYYY-MM-DD
---

# <主题名称>（English Name）

> 对应讲稿：`SlideNN-EnglishName-2025.pdf`（见课程 Canvas，不在公开仓库）

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

- 新增主题前确认在「主题覆盖范围」或 `docs/deep/README.md` 选材清单中已列出
- 文件命名：`XX-topic-name.md`（XX 为两位序号）；卡片与 `SlideNN` 编号一一对应
- 对应讲稿引用格式：`（对应 SlideXX-EnglishName）`，如 `（对应 Slide02-IntroToCS）`
- 参考文献格式：`作者 (年份). 标题. *期刊/出版社*.`
- **跨学科联系**：优先体现交大优势工科（船舶海洋/材料化工/机械动力/生物医药/航空航天），见 `docs/paths/by-discipline-bridge.md`
- **提交前自检**：`git status --porcelain` 确认未含 `reference/` 敏感文件
- Git 提交信息使用中文，格式：`类型: 简要描述`（类型：`新增`、`修改`、`修复`、`重构`、`文档`）

## 当前进度

### 已有资源

- 21 个课程讲稿 PDF（课程内部材料，发布在 Canvas，不入仓库）
- 课程大纲与教务材料（`reference/`，**不公开**，`.gitignore` 隔离）
- 5 个交互可视化 HTML（`code/visualizations/`，迁移自课程 Demo）
- 21 张知识点卡片（`docs/cards/`，已完成第二版重构，统一为 `needs-review`）+ 6 张扩展卡片
- 3 个深度专题（`docs/deep/`：LLM / 强化学习 / 量子计算）
- 2 个前沿注记页（`docs/frontier/`：LLM / CV，双层机制）
- 多路径索引（`docs/paths/` 五页）与 `glossary.md`
- 10 个概念示例、8 个核心实验、19 张 SVG 配图与跨平台 runner
- OpenCode 配置全套（`course-tutor` agent / 5 skills / 8 slash commands）
- `README.md` 与 `LICENSE`（内容 CC-BY-SA 4.0 / 代码 MIT）

### 待完成

- 教师审批 `docs/assessment/blueprint.yaml` 后再启用“按正式考核结构校准”的 `/mock`
- 发布前由任课教师抽查 21 张 `needs-review` 主卡与新增扩展卡
- 二期可选：mkdocs 静态站点 + GitHub Pages；英文版；更多深度专题

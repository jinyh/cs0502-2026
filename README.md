# 计算机科学导论配套知识库 + 主动学习智能体

> Shanghai Jiao Tong University · CS0502 Introduction to Computer Science
> Open-source companion knowledge base + active-learning OpenCode tutor.

本项目面向上海交通大学非计算机专业理工及医学学生，以 21 份课程讲稿为只读锚点，提供知识点卡片、概念代码、交互可视化、核心实验、考核迁移训练和 OpenCode 学习助教。知识库补充讲稿，不替代课堂与教师发布的正式材料。

## 你会在这里找到什么

```text
docs/cards/          21 张主线卡片 + 6 张扩展卡片
docs/deep/           LLM、强化学习、量子计算深度专题
docs/frontier/       人工审校静态基线 + 学生前沿检索入口
docs/paths/          5 条学习导航，包括工程问题求解路径
docs/assessment/     脱敏考核蓝图、项目 rubric、进度 schema
code/examples/       10 个可独立运行的概念示例
code/labs/           8 个“预测—实现—测试—解释”核心实验
code/visualizations/ 5 个自包含交互页面
figures/             19 张可访问 SVG 概念图
.opencode/           学生 agent、5 个 skills、8 个 slash commands
opencode/            教学、安全和知识检索规则
```

讲稿 PDF 位于课程 Canvas，不进入公开仓库；`reference/` 是教师敏感工作区，也永不提交。

## 学生快速开始

### 1. 安装依赖并验证示例

```bash
uv sync
uv run pytest
uv run python code/runner.py code/examples/06_graph_bfs_dfs.py
```

`code/runner.py` 只接受课程示例、实验和 `student-work/` 下的 Python 文件，并检查路径、导入、危险调用、时间和内存限制。它是可信教学护栏，不是面向恶意代码的硬安全沙箱。

### 2. 启动 OpenCode

先按 OpenCode 与阿里云百炼官方文档在本机配置 provider 和凭据；凭据只进入环境变量或正式凭据存储，不写入仓库。本课程以用户缺省模型 `qwen3.8-max`（1M context）做主测，但课程 skills 与模型供应商解耦。

```bash
opencode . --agent course-tutor
```

不要从“把这一讲讲给我听”开始。选择一个学习动作：

| 命令 | 学生要做的事 |
|---|---|
| `/learn 06 BFS 与 DFS` | 先诊断、预测，再获得分级提示与迁移题 |
| `/practice 05 栈、队列与树` | 一次完成一道全新同构练习 |
| `/lab lab-02-graph` | 复制 starter 到 `student-work/` 后预测、实现、测试、解释 |
| `/review 本周内容` | 基于本地进度做主动回忆和间隔复习 |
| `/mock 02-15` | 按已批准蓝图模拟；未批准时只称通用课程练习 |
| `/project 路径规划项目` | 按 rubric 评审已有证据，不代做成品 |
| `/exam-notes 全课程` | 从已练内容整理静态开卷资料 |
| `/frontier LLM` | 先写判断，再经同意检索一手来源 |

OpenCode 可以帮助平时学习、作业辅导、项目评审与考前准备；正式期末考试现场禁用。正在计分的任务只提供分级提示、相似新题、测试和 rubric 反馈，不输出可直接提交的完整答案。

## 推荐学习顺序

1. 从 [`docs/paths/by-engineering-workflow.md`](docs/paths/by-engineering-workflow.md) 选择一个工程问题。
2. 阅读相应主卡的“一句话定位”和学习目标，先尝试诊断题。
3. 用图或交互页面做一次状态预测。
4. 运行对应 example，再完成 lab 的一个小任务。
5. 用 `/practice` 做变式迁移，用 `/review` 记录错因。
6. 考前用 `/exam-notes` 整理个人静态资料，而不是生成未经练习的万能小抄。

## 教师审核点

- 21 张主卡已按讲稿重构，但统一标为 `needs-review`；正式发布前需课程教师抽查术语边界与课堂口径。
- [`docs/assessment/blueprint.yaml`](docs/assessment/blueprint.yaml) 只是脱敏模板。只有教师填写权重、认知层级并把 `status` 改为 `approved` 后，`/mock` 才可宣称按课程考核结构校准。
- 前沿联网结果写入 `student-work/frontier-notes/`，不自动回写人工审校静态层。

## 安全与许可证

- 提交前运行 `git status --porcelain`，确认没有 `reference/`、名单、成绩、考题或凭据。
- 文档内容使用 CC BY-SA 4.0；代码与 OpenCode 配置使用 MIT，详见 [`LICENSE`](LICENSE)。
- 讲稿 PDF 版权归课程组所有，不随仓库发布。

## 致谢

- 知识库导航参考 Datawhale Path2AGI 的多路径组织思路。
- 交互可视化由课程原有 Demo 迁移并增加预测提示、状态一致性和可访问性修复。

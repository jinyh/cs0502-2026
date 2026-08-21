# 计算机科学导论配套知识库 + 交互式智能体

> Shanghai Jiao Tong University · CS0502-02 Introduction to Computer Science
> Open-source companion knowledge base + interactive OpenCode agent for the AI era.

本项目是上海交通大学「计算机科学导论（CS0502-02）」课程（计算机学院课程组承担，面向全校非计算机专业理工及医学科学生）的配套知识库，以 21 个课程讲稿 PDF 为只读锚点，补充**轻量知识点卡片 + 前沿进展注记 + 少数 AI 深度专题 + 多路径索引**，并配套 **OpenCode 交互式智能体**（GLM / DeepSeek）辅助学习，体现 AI+ 课程特色。

## 目录结构

```
# 讲稿 PDF 在课程 Canvas，不在公开仓库
AGENTS.md        Claude Code / Codex / OpenCode 共享项目协作规范
CLAUDE.md        Claude Code 入口（导入 AGENTS.md）
docs/
  cards/          21 讲轻量知识点卡片（一讲一页，对齐 SlideNN）
  deep/           AI 高价值深度专题（LLM / 强化学习 / 量子计算）
  frontier/       前沿注记（静态写底 + 智能体联网增量）
  paths/          多路径索引（按思维支柱 / AI 能力 / 读者目标 / 跨学科桥接）
  glossary.md     全局术语表（中英对照）
opencode/         OpenCode 智能体配置
  AGENTS.md       行为约束（教学红线 / 不代写 / 沙箱安全 / 直觉先行）
  knowledge.md    知识库检索索引
  tools.md        工具与 GLM/DeepSeek 接入
  sandbox-policy.md  沙箱安全策略
  prompts/        预设提示词
code/
  examples/       概念演示 Python（对应卡片编号）
  visualizations/ 自包含 HTML 交互可视化
figures/          静态图（SVG 优先）
```

## AI 协作工具入口

- 在仓库根目录启动 Codex 或 OpenCode：直接读取 `AGENTS.md`。
- 在仓库根目录启动 Claude Code：读取 `CLAUDE.md`，并由其导入 `AGENTS.md`。
- `opencode/AGENTS.md` 是学生课程助教的专用约束，不替代根目录的项目协作规范。

## 快速开始（学生）

### 1. 浏览知识库

直接阅读 `docs/cards/` 下任意卡片，或从 `docs/paths/` 选一条学习路径切入。

### 2. 用 OpenCode 智能体交互（推荐）

```bash
# 克隆本仓库
git clone <repo-url> && cd ComputerIntroduction

# 安装 OpenCode（参见 https://opencode.ai ，按其官方文档安装）
# 配置模型 API key（环境变量，勿提交）
export ZHIPU_API_KEY=...        # GLM-4.6
# export DEEPSEEK_API_KEY=...  # 备选 DeepSeek-V3

# 以 opencode/ 作为项目目录启动，加载其中的学生助教行为约束
opencode opencode
```

智能体会按需读取 `opencode/knowledge.md` 作为知识库索引，可：
- **问答**：「用医院场景解释 ADT 为什么抽象」（定位到 `docs/cards/04`）
- **跑沙箱**：运行 `code/examples/` 示例（遵守白名单/超时/禁网）
- **补前沿**：「LLM 最新进展」→ 读 `docs/frontier/llm-frontier.md` 静态层 + 联网增量

## 预设提示词

| 命令 | 用途 |
|---|---|
| `explain-concept` | 用直觉类比解释某概念 |
| `trace-lecture` | 对照某讲稿梳理脉络 |
| `frontier-update` | 联网补充某主题最新进展 |
| `homework-guard` | 作业护栏——引导思考但不代写 |

## 教学红线（智能体行为）

详见 `opencode/AGENTS.md`：
- **不代写作业**：只给思路、同类例题、代码 review，不输出可直接提交的答案。
- **不触碰敏感数据**：学生名单、成绩、考题不在公开仓库（`reference/` 已 `.gitignore`）。
- **直觉先行**：先类比再形式化定义。
- **导论边界**：不引入超纲形式化证明，深入引导到 `docs/deep/`。

## 安全与隐私

`reference/` 目录是教师教务工作区，含学生名单、成绩表、期末考题等敏感数据，**已通过 `.gitignore` 完全隔离，永不进入公开仓库**。每次提交前用 `git status --porcelain` 自检。

## 联调验证清单

本地配好 OpenCode + API key 后，按以下验证三条主链路：

1. **问答链路**：问「栈和队列的区别」→ 智能体应定位到 `docs/cards/04` 并引用其内容。
2. **沙箱链路**：请求运行 `code/examples/04_stack_queue.py`（待建）→ 应在白名单/超时约束下执行。
3. **前沿链路**：问「LLM 最新进展」→ 应读 `docs/frontier/llm-frontier.md` 静态层，联网追加增量，不修改静态层。
4. **红线链路**：粘贴一道作业题要求完整答案 → 应拒绝代写，改为引导思路。

静态已验证：21 卡片 + 3 深度专题 + 2 前沿页 + 4 路径 + 术语表 + 8 个 opencode 配置文件齐全，内部链接有效，`reference/` 零命中。

## 许可证

- **文档内容**（`docs/`）：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **代码**（`code/`、`opencode/` 配置）：MIT（见 `LICENSE`）
- **讲稿 PDF**：归课程组所有，发布在课程 Canvas，不在本仓库。

## 致谢

- 知识库组织参考 [Datawhale Path2AGI](https://github.com/datawhalechina/Path2AGI) 的多路径索引与元数据思路。
- 交互可视化迁移自课程原有 Demo。

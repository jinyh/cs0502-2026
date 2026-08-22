# 工具与模型接入

> 可执行配置位于仓库根目录 `opencode.json` 与 `.opencode/`。本页解释意图，不保存任何凭据。

## 模型

- 本学期主测：阿里百炼 `qwen3.8-max`；OpenCode 界面中的 `[1m]` 作为上下文/显示变体处理，不写入可移植 model ID。
- 课程 skill、commands 和运行器保持 provider-agnostic，也可兼容教师批准的 GLM / DeepSeek。
- 仓库不硬编码个人 provider 前缀、Workspace ID、Base URL 或 API Key。学生使用 OpenCode `/connect` 或本地环境注入凭据。

### 提供商连接示例

以下以阿里百炼为例说明交互流程，其他 OpenCode 支持的提供商操作相同：

1. 在仓库根目录运行 `opencode . --agent course-tutor`。
2. 在 OpenCode 中输入 `/connect`，选择阿里百炼或相应的 OpenAI-compatible provider，并按界面提示保存凭据。
3. 输入 `/models`，从该提供商公开的模型列表中选择课程使用的模型。
4. 输入 `/start L01` 验证课程 agent、commands 和本地知识库是否加载成功。

提供商名称、模型 ID 和 endpoint 以 OpenCode 与提供商当前文档为准。不要把 API Key 写入 `opencode.json`、Markdown、截图或 Git 提交。

## 本地知识库

从 `knowledge.md` 定位卡片。每轮只读取当前卡片、必要前置和一个关联实验/图示，长上下文是容量上限，不是一次加载整个知识库的理由。

## Python 实验

唯一入口：

```bash
uv run python code/runner.py run code/examples/06_graph_bfs_dfs.py
uv run python code/runner.py lab init lab-02-graph
uv run python code/runner.py lab test lab-02-graph
```

运行器检查路径、AST 导入与危险调用，并限制 CPU 时间、墙钟时间和内存。它是面向可信学生代码的教学护栏，不是抵御恶意用户的容器或虚拟机。

## 本地学习进度

学生明确同意后，智能体只通过 `uv run python code/progress.py ...` 管理 `student-work/progress.json`。不把身份、成绩、原始作业或考试内容写入进度文件。

## 配置隐私

项目配置默认拒绝未列出的工具和全局 MCP。不要在课堂投屏、共享日志或 issue 中输出 OpenCode 合并后的有效配置；该输出可能包含用户级 provider 或 MCP 凭据。

## 联网

默认关闭。只有 `frontier-literacy` 在学生明确同意后请求 `websearch/webfetch` 权限；结果写入 `student-work/frontier-notes/`，不得直接改正式前沿页。

## 明确不提供

- 不读取 `reference/`、`LectureNotes/`、`.env`、凭据或外部目录。
- 不发送邮件、不提交作业、不访问教务系统、不启动子智能体。
- 除 `student-work/` 外不写仓库文件。

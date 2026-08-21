# 工具与模型接入

> 可执行配置位于仓库根目录 `opencode.json` 与 `.opencode/`。本页解释意图，不保存任何凭据。

## 模型

- 本学期主测：阿里百炼 `qwen3.8-max`；OpenCode 界面中的 `[1m]` 作为上下文/显示变体处理，不写入可移植 model ID。
- 课程 skill、commands 和运行器保持 provider-agnostic，也可兼容教师批准的 GLM / DeepSeek。
- 仓库不硬编码个人 provider 前缀、Workspace ID、Base URL 或 API Key。学生使用 OpenCode `/connect` 或本地环境注入凭据。

## 本地知识库

从 `knowledge.md` 定位卡片。每轮只读取当前卡片、必要前置和一个关联实验/图示，长上下文是容量上限，不是一次加载整个知识库的理由。

## Python 实验

唯一入口：

```bash
uv run python code/runner.py code/examples/06_graph_bfs_dfs.py
```

运行器检查路径、AST 导入与危险调用，并限制 CPU 时间、墙钟时间和内存。它是面向可信学生代码的教学护栏，不是抵御恶意用户的容器或虚拟机。

## 联网

默认关闭。只有 `frontier-literacy` 在学生明确同意后请求 `websearch/webfetch` 权限；结果写入 `student-work/frontier-notes/`，不得直接改正式前沿页。

## 明确不提供

- 不读取 `reference/`、`LectureNotes/`、`.env`、凭据或外部目录。
- 不发送邮件、不提交作业、不访问教务系统、不启动子智能体。
- 除 `student-work/` 外不写仓库文件。

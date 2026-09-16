# 工具与模型接入

> 可执行配置位于仓库根目录 `opencode.json` 与 `.opencode/`。本页解释意图，不保存任何凭据。

本页的安装、权限与凭据步骤专用于 OpenCode。项目同时提供 [Pi 只读试用入口](../docs/pi-student-guide.md)，两端共用课程资源但分别实施权限；支持范围和测试结果见[学习智能体兼容性](../docs/agent-compatibility.md)。不要将 OpenCode 的权限配置视为其他 Agent 已生效的限制。

面向学生的下载、安装和首次验证步骤见[OpenCode 学生学习指南](../docs/student-guide.md)。完整仓库已经包含知识库、课程 agent、5 个 skill 和 10 个 slash command；skill 由 OpenCode 自动发现并按需加载，不需要单独安装。

## 模型

- 本学期主测：阿里百炼 `qwen3.8-max`；OpenCode 界面中的 `[1m]` 作为上下文/显示变体处理，不写入可移植 model ID。
- 课程 skill、commands 和运行器保持 provider-agnostic，也可兼容教师批准的 GLM / DeepSeek。
- 仓库不硬编码个人 provider 前缀、Workspace ID、Base URL 或 API Key。个人提供商配置放在 OpenCode 用户目录，凭据使用 `/connect` 保存。

### 个人百炼 API 配置

本课程个人百炼 API 示例使用自定义 Provider ID `bailian-course` 和北京地域的 OpenAI-compatible 服务。用户级配置文件位置如下：

- Windows：`%USERPROFILE%\.config\opencode\opencode.json`
- macOS：`~/.config/opencode/opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "bailian-course": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "阿里云百炼（课程）",
      "options": {
        "baseURL": "https://dashscope.aliyuncs.com/compatible-mode/v1"
      },
      "models": {
        "qwen3.8-max": {
          "name": "Qwen3.8 Max"
        }
      }
    }
  }
}
```

已有用户配置时，只把 `bailian-course` 合并到现有 `provider` 对象，不覆盖其他个人设置。API Key 不写在 JSON 中；在仓库根目录启动 OpenCode 后输入 `/connect`，选择 **Other**，使用 `bailian-course` 作为 Provider ID，再按提示保存密钥。输入 `/models` 选择 `Qwen3.8 Max`，用 `/start L01` 和 `/learn L01` 分别验证课程命令、知识库检索与 skill 加载。

本例是普通百炼 API，默认按量调用。API Key、地域与 Base URL 必须匹配；Coding Plan 的专属密钥和地址不能用于本例。获取密钥、用量与定价分别见[百炼 API Key 文档](https://help.aliyun.com/zh/model-studio/get-api-key)、[模型用量文档](https://help.aliyun.com/zh/model-studio/model-usage-statistics)和[模型价格](https://help.aliyun.com/zh/model-studio/model-pricing)。配置格式见 [OpenCode 用户配置](https://opencode.ai/docs/config/)与[自定义提供商](https://opencode.ai/docs/providers/#custom-provider)。以上链接与示例最后核验于 2026-09-12。

提供商界面、模型 ID 和 endpoint 以后如有变化，以 OpenCode 与百炼官方文档为准。不要把 API Key 写入仓库 `opencode.json`、Markdown、截图或 Git 提交，也不要输出包含凭据的合并后有效配置。

## 本地知识库

从 `knowledge.md` 定位卡片。项目级 skill 位于 `.opencode/skills/<name>/SKILL.md`，从仓库根目录启动时会被自动发现；每轮只加载当前任务需要的 skill、卡片、必要前置和一个关联实验或图示。长上下文是容量上限，不是一次加载整个知识库的理由。

## Python 实验（PAI-DSW）

本机 OpenCode 不执行课程 Python。学生在支持 `/mnt/workspace` 持久化的 PAI-DSW 中运行 [`../notebooks/modelscope/CS0502-quickstart.ipynb`](../notebooks/modelscope/CS0502-quickstart.ipynb)，使用：

```python
run_example("06_graph_bfs_dfs.py")
init_lab("lab-02-graph")
test_lab("lab-02-graph")
show_visualization("binary_heap.html")
```

OpenCode 先要求预测，再给 helper 调用；学生只贴回 `[CS0502_RESULT]` 摘要。运行器检查路径、AST 导入与危险调用，并限制 CPU 时间、墙钟时间和内存。它是面向可信学生代码的教学护栏，PAI-DSW 外层环境负责资源隔离。

## 本地学习进度

学生明确同意后，智能体只通过 `uv run --no-project python code/progress.py ...` 管理本机 `student-work/progress.json`，无需安装云端代码依赖。不把身份、成绩、原始作业或考试内容写入进度文件。

## 配置隐私

项目配置默认拒绝未列出的工具和全局 MCP。不要在课堂投屏、共享日志或 issue 中输出 OpenCode 合并后的有效配置；该输出可能包含用户级 provider 或 MCP 凭据。

模型凭据只配置在学生自己的电脑上。不要把 API Key 注入 PAI-DSW、写入 Notebook、`student-work/` 或运行摘要。

## 联网

默认关闭。只有 `frontier-literacy` 在学生明确同意后请求 `websearch/webfetch` 权限；结果写入 `student-work/frontier-notes/`，不得直接改正式前沿页。

## 明确不提供

- 不读取 `reference/`、`LectureNotes/`、`.env`、凭据或外部目录。
- 不发送邮件、不提交作业、不访问教务系统、不启动子智能体。
- 除 `student-work/` 外不写仓库文件。

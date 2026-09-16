# 学习智能体兼容性：OpenCode 与 Pi

> 最后核验：2026-09-16。目标是共用一套课程知识库与教学流程，为不同 Agent 提供各自的启动和工具适配。

## 当前支持范围

| 入口 | 当前状态 | 使用方式与边界 |
|---|---|---|
| OpenCode | 已有完整课程入口，继续保留 | 按[OpenCode 学生指南](student-guide.md)启动；课程 agent、权限、skills 和命令保持兼容 |
| Pi | 已提供只读试用入口 | 按[Pi 学生试用指南](pi-student-guide.md)从仓库根目录隔离启动；自动加载同一套 5 个 skills、10 个命令和助教规则，写入与联网功能暂不开放 |
| 其他 Agent | 课程内容可复用，运行入口未验证 | 需要分别验证规则加载、工具权限、命令语义与教学闭环后再列为支持 |

## 2026-09-16 本地测试

环境：macOS、Node.js 26.7.0、Pi 0.85.1（`@earendil-works/pi-coding-agent`）。本机 OpenCode 为 1.18.31。测试在临时目录中进行，只复制 Git 已跟踪或待提交且未被忽略的公开课程文本，不复制讲稿 PDF、`reference/` 或个人配置。

| 测试 | 结果 |
|---|---|
| 未信任项目时 | 不加载 `.pi/` 资源；学生入口使用 `--no-context-files`，也不加载根目录维护用 `AGENTS.md` |
| 个人 skills 自动发现 | 本机还发现 6 个非课程 skills；数量取决于个人环境 |
| 信任项目并加载适配层 | 成功加载现有 5 个 skills、10 个命令和 1 个项目扩展，0 个资源诊断、0 个扩展加载错误 |
| 隔离 CLI 启动 | 关闭默认 context、skills、prompts、extensions 并显式加载课程扩展后，仅显示 5 个课程 skills、10 个课程命令和 `course-tutor.ts` |
| 命令参数 | 10 个模板均能展开 `$ARGUMENTS`；OpenCode 的 `agent:` 元数据不会变成提示正文 |
| 项目工具护栏 | 7 项本地检查通过，包含外部目录、敏感路径、命令执行与写入拒绝，以及正常课程读取 |
| 百炼真实调用 | 尚未取得有效模型回复；不能据此判断教学表现或速度 |

这些检查证明现有教学文本可以被 Pi 加载。`.pi/extensions/course-tutor.ts` 会读取 `.opencode/agents/course-tutor.md` 的正文、映射工具名称，并在每次工具调用前检查路径；`.pi/settings.json` 只启用 `read / grep / find / ls`。OpenCode 的 `permission:` frontmatter 不会被当作 Pi 权限，Pi 的边界由该项目扩展独立实施。

本次还没有验证进度写入、联网检索、完整多轮学习、Windows 终端交互，也没有同条件的 OpenCode/Pi 速度对比。测试目录中的护栏检查不等于生产环境沙箱验证。

## 共用内容，分别适配入口

采用以下边界，避免出现两套逐渐分叉的教材和 skill：

- **知识与实验共用**：`docs/`、`figures/`、`code/`、PAI-DSW Notebook 与 `[CS0502_RESULT]` 协议保持同一来源。
- **教学流程共用**：`.opencode/skills/`、`.opencode/commands/` 与 `.opencode/agents/course-tutor.md` 是唯一维护源；Pi 项目扩展从这些路径加载，不复制教学内容，也不复制全局 skill。
- **工具适配独立**：OpenCode 使用 `glob/list`，Pi 使用 `find/ls`；Pi 项目扩展注入共享助教正文，并用独立路径护栏限制文件访问。
- **能力逐步开放**：Pi 当前只读，可以完成概念学习、预测、练习、资源定位与只读评审；进度写入、前沿笔记写入和联网检索保持降级，完成单独验收后再开放。
- **学生上下文精简**：Pi 学生入口关闭默认 context、skills、prompt templates 和 extensions，只显式加载课程适配扩展，由它注入助教规则与课程资源。根目录 `AGENTS.md` 服务仓库维护，不直接充当学生助教角色配置。
- **状态如实标注**：保留 OpenCode 完整入口；Pi 在真实教学与权限验收完成前保持只读试用状态。增加新 Agent 不代表同步开放其所有工具。

Pi 支持项目 skills、Markdown prompt templates 和 extensions，详情见 [Skills](https://pi.dev/docs/latest/skills)、[Prompt Templates](https://pi.dev/docs/latest/prompt-templates)与 [Extensions](https://pi.dev/docs/latest/extensions)。Pi 的项目“信任”决定是否加载项目资源，但信任本身不是沙箱；本项目依据 [Security](https://pi.dev/docs/latest/security) 在扩展中实现只读工具与路径限制。

## 复现与下一步验收

可重复的测试入口见 [`tests/pi-course-smoke.mjs`](https://github.com/jinyh/cs0502-2026/blob/main/tests/pi-course-smoke.mjs) 与[Pi 试测说明](https://github.com/jinyh/cs0502-2026/blob/main/tests/manual-pi-smoke.md)。离线检查直接加载仓库中的 `.pi` 适配层，无需 API Key，也不修改个人配置；真实调用需要教师自己的已配置模型账户。

首轮真实调用使用 `/start L06`、`/learn L15`、`/demo L05 图遍历`、`/lab lab-02-graph`：检查是否先诊断/预测、是否选中正确语义卡、是否使用单行运行索引、是否遵守 PAI-DSW 交接。完整验收再覆盖[现有课程烟雾测试](https://github.com/jinyh/cs0502-2026/blob/main/tests/manual-opencode-smoke.md)中的其他场景，尤其是进度同意、计分任务和前沿检索。

速度对比必须固定模型、服务地址、推理设置、任务和资源加载范围，并分别记录首字时间、整轮时间、工具调用次数与教学正确性。只有成功回复计入延迟结果；每种场景应重复测量，再讨论是否切换默认入口。

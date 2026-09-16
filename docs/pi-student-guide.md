# Pi 学生试用指南（拓展学习，可选）

Pi 入口与 OpenCode 共用课程知识库、5 个学习 skill、10 个学习命令和同一份助教行为规则。仓库中的 `.pi/` 只负责 Pi 的资源加载和只读权限适配，不复制 `.opencode/skills/` 或 `.opencode/commands/`。

> 当前状态：已用 Pi 0.85.1 完成本地资源加载、命令展开和路径护栏检查；真实模型教学回复与速度对比仍待完成。因此本页是试用入口，OpenCode 继续作为已经完整验收的课程入口。

## 安装 Pi

先安装 Node.js，再在终端运行：

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pi --version
```

也可以使用 [Pi 官方安装说明](https://pi.dev/docs/latest/)。模型与凭据属于个人配置：使用 Pi 的 `/login` 和 `/model`，或按 [Custom Models](https://pi.dev/docs/latest/models) 配置 OpenAI-compatible 服务。不要把 API Key 写入课程仓库、截图或聊天消息。

## 下载完整课程仓库

使用 Git：

```bash
git clone https://github.com/jinyh/cs0502-2026.git
cd cs0502-2026
```

使用 ZIP 时，解压后确认隐藏目录 `.pi/` 和 `.opencode/` 都存在。Pi 适配入口由以下两个文件组成：

- `.pi/settings.json`：只启用 `read / grep / find / ls`。
- `.pi/extensions/course-tutor.ts`：加载共享 skill、命令和助教规则，并限制可读取路径。

## 启动课程助教

必须从仓库根目录启动：

```bash
pi --no-context-files --no-skills --no-prompt-templates --no-extensions -e .pi/extensions/course-tutor.ts
```

`--no-context-files` 避免把仓库根目录面向维护者的 `AGENTS.md` 当成学生助教规则；其余 `--no-*` 参数关闭个人或其他项目资源的默认发现，`-e` 只加载课程适配扩展。该扩展随后加入本课程共享的 5 个 skills、10 个命令和助教规则。

Pi 首次发现项目级配置时会询问是否信任该项目。先确认当前目录是课程仓库并查看 `.pi/` 中上述两个文件，再选择信任；不信任时 Pi 不会加载课程适配层。

进入 Pi 后，启动信息应只显示 `course-tutor.ts`、5 个课程 skills 和 10 个课程 prompt templates。随后输入：

```text
/start L01
```

课程助教应说明 Pi 当前不写本地进度，并只提出一道短诊断题。再输入 `/learn L01`，检查它是否按需读取课程知识库，而不是一次加载全库。

## 当前只读边界

Pi 课程入口当前允许读取这些公开资源：`.opencode/`、`opencode/`、`docs/`、`code/`、`figures/`、`notebooks/modelscope/` 和 `student-work/`。适配层拒绝 `reference/`、`LectureNotes/`、`.git/`、环境变量文件、课程目录外路径以及所有写入、shell 和联网工具。

因此当前 Pi 可以使用 `/start`、`/learn`、`/demo`、`/lab`、`/practice`、`/mock` 和只读项目评审；以下功能会安全降级：

- 不创建或更新 `student-work/progress.json`，复习只依据当前会话或已有记录。
- 不写 `exam-notes.md` 或前沿草稿，只给可复制文本。
- 不联网检索前沿信息，只使用本地静态页并说明日期边界。
- 不在本机运行课程 Python；example、Lab 和可视化仍在 PAI-DSW 中运行。

项目信任决定 Pi 是否加载项目配置，但它本身不是沙箱；本课程的只读边界由项目扩展在每次工具调用前检查。若使用命令行参数覆盖工具列表，扩展仍会拒绝超出课程入口范围的调用。

## 更新与故障排查

Git 用户关闭 Pi 后运行 `git pull --ff-only`。ZIP 用户重新下载到新目录，不要只复制 `.pi/`，否则它可能与旧版共享 skill 不匹配。

| 现象 | 检查与处理 |
|---|---|
| 没有课程 skills 或 `/start` | 确认从仓库根目录用指南中的完整命令启动、`.pi/` 与 `.opencode/` 都存在，并已信任当前项目；之后输入 `/reload`。 |
| 提示读取路径被拒绝 | 只使用课程公开目录；讲稿和教师工作区不属于学生智能体可读范围。 |
| `/start` 没有保存学习进度 | 这是当前 Pi 只读入口的预期行为；需要持久进度时使用 OpenCode 入口。 |
| 找不到模型或认证失败 | 使用 `/login`、`/model` 检查个人 Pi 配置；不要把凭据或完整配置发到公开渠道。 |

详细的共用边界、测试证据和待验证项见[学习智能体兼容性：OpenCode 与 Pi](agent-compatibility.md)。

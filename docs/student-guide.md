# OpenCode 学生学习指南（拓展学习，可选）

这套智能体的目标不是替你回答问题，而是让你经历一次可检查的学习过程：**先预测或作答，再获得提示；先解释证据，再进入下一题**。

> OpenCode 是可选的课后助学工具，不是完成课程的必需软件。只有 Canvas 正式说明要求的活动才属于课程任务；正式期末考试现场禁止使用 OpenCode 和其他 LLM。

## 从零开始

完成下面五步后，你的电脑上会同时有课程知识库、课程 skill、学习命令和 OpenCode 助教配置。它们都包含在同一个 GitHub 仓库中，**不需要逐个下载或安装 skill**。

### 第一步：下载完整课程仓库

课程仓库地址是 [jinyh/cs0502-2026](https://github.com/jinyh/cs0502-2026)。请选择 Git 或 ZIP 其中一种方式。

#### 方式 A：直接下载 ZIP（适合第一次使用 GitHub）

1. 打开仓库页面，点击绿色的 **Code** 按钮，再点击 **Download ZIP**。
2. 解压下载的 `cs0502-2026-main.zip`，得到 `cs0502-2026-main` 文件夹。
3. 将这个文件夹移动到容易找到、路径中尽量不含中文或空格的位置。

macOS 的访达默认隐藏以 `.` 开头的目录。不要删除 `.opencode`；它包含课程 skill、命令和助教定义。需要查看隐藏文件时，在访达中按 `Command + Shift + .`。

#### 方式 B：使用 Git（方便以后更新）

如果还没有 Git，先安装 [Windows 版 Git](https://git-scm.com/download/win) 或 [macOS 版 Git](https://git-scm.com/download/mac)。然后打开 Windows PowerShell 或 macOS 终端，运行：

```bash
git clone https://github.com/jinyh/cs0502-2026.git
cd cs0502-2026
```

无论使用哪种方式，最终目录都应至少包含：

```text
cs0502-2026/
├── opencode.json
├── .opencode/
│   ├── agents/
│   ├── commands/
│   └── skills/
├── opencode/
├── docs/
├── code/
└── notebooks/
```

其中 `docs/` 是知识库主体，`.opencode/skills/` 内有 5 个课程 skill，`.opencode/commands/` 内有 10 个学习命令。OpenCode 从仓库根目录启动时会自动发现并按需加载它们。不要把 `.opencode/skills/` 复制到全局 skill 目录。

### 第二步：安装 OpenCode

#### Windows

先从 [Node.js 官网](https://nodejs.org/) 安装 LTS 版本。安装完成后重新打开 PowerShell，运行：

```powershell
npm install -g opencode-ai
opencode --version
```

第二条命令能显示版本号，就表示安装成功。

#### macOS

打开终端，使用 OpenCode 官方安装命令：

```bash
curl -fsSL https://opencode.ai/install | bash
opencode --version
```

如果安装程序提示重新打开终端，请照做后再运行版本检查。Linux 用户参见 [OpenCode 官方安装说明](https://opencode.ai/docs/#install)。

### 第三步：准备个人百炼 API

1. 登录阿里云，在[百炼控制台](https://bailian.console.aliyun.com/)开通模型服务。
2. 在控制台右上角选择 **华北 2（北京）**，按照[获取与配置 API Key](https://help.aliyun.com/zh/model-studio/get-api-key)创建个人 API Key。API Key 所属地域必须和服务地址一致。
3. 使用前阅读[模型价格](https://help.aliyun.com/zh/model-studio/model-pricing)。调用后可在百炼控制台的“模型用量”和“费用概览”查看 Token 用量与费用；统计可能有延迟。

本指南使用普通百炼 API 的按量调用方式。它和 Coding Plan 是两套凭据与服务地址，不能混用。不要把 API Key 发给同学，也不要写入课程仓库、截图、Notebook 或聊天消息。

### 第四步：添加个人模型配置

课程仓库的 `opencode.json` 只保存助教和安全配置。个人模型配置放在自己的 OpenCode 用户目录，不会进入 Git 仓库。

Windows 用户在 PowerShell 中运行：

```powershell
New-Item -ItemType Directory -Force "$HOME\.config\opencode"
notepad "$HOME\.config\opencode\opencode.json"
```

macOS 用户在终端中运行：

```bash
mkdir -p ~/.config/opencode
touch ~/.config/opencode/opencode.json
open -e ~/.config/opencode/opencode.json
```

在打开的文件中保存下面的配置。示例使用北京地域的 OpenAI-compatible 服务地址，并且不包含 API Key：

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

如果文件中已有其他配置，请把上面的 `bailian-course` 内容合并到现有 `provider` 对象中，保留原有字段，避免创建两个同名的 `provider`。其他地域必须同时改用该地域创建的 API Key 和对应 Base URL，具体地址以百炼文档为准。

### 第五步：连接密钥并验证课程助教

先进入刚才下载的仓库根目录。ZIP 用户的目录通常叫 `cs0502-2026-main`，Git 用户通常叫 `cs0502-2026`。如果 ZIP 仍在默认下载目录，可参考下面的命令；移动过文件夹时，请换成实际路径。

Windows PowerShell：

```powershell
cd "$HOME\Downloads\cs0502-2026-main"
Get-ChildItem -Force
opencode . --agent course-tutor
```

macOS 终端：

```bash
cd ~/Downloads/cs0502-2026-main
ls -la
opencode . --agent course-tutor
```

目录列表中应同时出现 `opencode.json` 和 `.opencode`。Git 用户如果已经在第一步运行过 `cd cs0502-2026`，可以直接运行最后一条启动命令。

进入 OpenCode 后：

1. 输入 `/connect`，选择列表末尾的 **Other**。
2. Provider ID 输入 `bailian-course`，必须和个人配置中的名称完全一致。
3. 按提示粘贴个人百炼 API Key。OpenCode 会把凭据保存在用户凭据存储中。
4. 输入 `/models`，选择 **阿里云百炼（课程） → Qwen3.8 Max**。
5. 输入 `/start L01`。课程助教应说明学习记录范围，并从一道诊断题开始。
6. 再输入 `/learn L01`，确认它能定位课程知识库并按需加载课程 skill。

课程的 agent、commands 和 skill 已配置完成，**不要运行 `/init`**，否则可能生成一份与课程规则重复的通用说明。以后也应始终从含有 `opencode.json` 的仓库根目录启动。

以上 OpenCode 与百炼配置依据 [OpenCode 配置文档](https://opencode.ai/docs/config/)、[OpenCode 自定义提供商文档](https://opencode.ai/docs/providers/#custom-provider)和[百炼 API 文档](https://help.aliyun.com/zh/model-studio/get-api-key)，最后核验于 2026-09-12。提供商界面或模型列表以后如有变化，以官方文档为准。

### 可选：启用学习记录和代码实验

本机不需要安装课程 Python 依赖。只有选择启用匿名学习进度时才需要安装 [`uv`](https://docs.astral.sh/uv/getting-started/installation/)；进度工具使用 `--no-project`，不会同步 NumPy、pandas 等云端依赖。首次使用 `/start 当前讲次或目标` 时，你可以选择是否启用匿名记录；拒绝不影响学习，只是不进行跨会话的间隔复习调度。

另按 [ModelScope Notebook 说明](https://modelscope.cn/docs/notebook/intro) 创建支持 `/mnt/workspace` 持久化的 PAI-DSW CPU Notebook，选择 Python 3.11+ 镜像，上传并从头运行 [`../notebooks/modelscope/CS0502-quickstart.ipynb`](../notebooks/modelscope/CS0502-quickstart.ipynb)。OpenCode 负责学习引导，PAI-DSW 负责代码运行；云端不保存模型 API Key。若云端不能访问 GitHub，先把课程组发布的仓库 ZIP 上传并解压为 `/mnt/workspace/CS0502`。

## 选择一个学习动作

| 想完成的事 | 命令示例 | 智能体如何引导 |
|---|---|---|
| 判断从哪里开始 | `/start L06` | 说明记录范围，只问一道诊断题，再推荐一个下一步 |
| 学懂一讲或概念 | `/learn L06 算法策略` | 定义可观察目标，诊断、预测、分级提示、迁移、总结 |
| 看代码或动画验证推理 | `/demo L05 图遍历` | 先预测，再到 PAI-DSW 运行 helper；没有代码时使用 HTML、图或主动任务 |
| 完成形成性实验 | `/lab lab-02-graph` | 预测公开测试，在 PAI-DSW 初始化副本，逐步实现和解释；是否计分看教师通知 |
| 做一道新题 | `/practice L05 图遍历` | 一次一题，作答前不展示答案或评分点 |
| 复习到期内容 | `/review 本周内容` | 从本地进度选择一道主动回忆题 |
| 做综合练习 | `/mock L02-L15` | 蓝图获批后按蓝图出题；否则固定生成四类通用练习 |
| 检查课程项目 | `/project student-work/my-project` | 按证据和 rubric 找第一个缺口，不代写成品 |
| 整理开卷资料 | `/exam-notes 全课程` | 只整理已经练习或当场成功回忆的内容，完成后自行打印 |
| 核验前沿变化 | `/frontier LLM` | 先写判断，征得同意后检索一手来源 |

不知道选什么时使用 `/start`，不要用“把整章讲给我听”开始。

## 推荐闭环

1. `/learn`：先暴露自己的理解和前置缺口。
2. `/demo`：对最小输入预测输出，再用代码、动画或图验证。
3. `/lab`：把概念落实为可测试的实现。
4. `/practice`：换数字、结构或工程场景，检查是否真正迁移。
5. `/review`：记录错因并在之后主动回忆。

时间紧时可以要求“快速模式”，但至少保留一次学生主动预测或作答。

## 本机与云端如何交接

1. 在本机 OpenCode 输入 `/demo` 或 `/lab`，先完成它要求的预测。
2. OpenCode 给出 `run_example(...)`、`init_lab(...)`、`test_lab(...)` 或 `show_visualization(...)`。
3. 在 PAI-DSW Quickstart 中运行该 helper。
4. 复制 `[CS0502_RESULT] ... [/CS0502_RESULT]` 摘要回 OpenCode；只在需要定位第一个失败时补充最小函数或少量日志。
5. OpenCode 根据证据给一个提示；修改仍在云端完成。

OpenCode 不能直接连接或控制你的 PAI-DSW。不要把整份项目、个人数据、API Key 或无关日志粘贴进对话。不同主题优先开启新会话；长会话可使用 `/compact`。

## 代码资源怎么选

- `code/examples/`：完整、可运行的概念演示；适合阅读、预测和修改输入。
- `code/labs/`：有待完成函数的形成性核心实验；修改运行器创建的 `student-work/labs/.../solution.py`。它们可以被选入作业，也可以不被选入。
- `code/visualizations/`：由 Quickstart 的 `show_visualization(...)` 内嵌显示；适合追踪栈、队列、堆、递归和图灵机状态。
- `figures/`：静态概念图；适合口头追踪和考前回忆。

完整 example 清单和运行命令见 [`../code/README.md`](../code/README.md)，Lab 结构见 [`../code/labs/README.md`](../code/labs/README.md)。讲次与卡片、代码、Lab 是多对多关系，智能体必须按 [`curriculum/lecture-card-map.yaml`](curriculum/lecture-card-map.yaml) 定位，不能根据文件名前缀猜测。

全学期安排 3 次正式计分作业，而不是每周作业。卡片主动任务、`/practice`、`/review` 和 Lab 默认不计分；某个 Lab 只有在教师正式作业说明中被明确指定后，才成为该次作业的一部分。

## 本地文件与隐私

本机和云端各有一个被 Git 忽略的 `student-work/`，职责不同：

- 本机：`progress.json`、`exam-notes.md`、`frontier-notes/`，供 OpenCode 做复习与资料整理。
- PAI-DSW `/mnt/workspace/CS0502/student-work/`：Lab、example 变式、生成图和课程项目代码。

云端持久化不等于备份。每周或重要实验后在 Quickstart 运行 `export_student_work()`，从文件浏览器下载 ZIP。

不要粘贴姓名、学号、成绩、当前考题或其他同学的作答。`reference/`、课程讲稿和教师工作区不属于学生智能体可读范围。

## 更新课程资源

使用 Git 下载的同学，在仓库根目录关闭 OpenCode 后运行：

```bash
git pull --ff-only
```

如果 Git 提示本地文件冲突，不要强行覆盖；先备份 `student-work/`，再向助教或课程组求助。

使用 ZIP 的同学应重新下载并解压到一个**新文件夹**，确认新版可以启动后，再把旧文件夹中的 `student-work/` 复制到新版根目录。保留旧文件夹作为备份，不要把旧版 `.opencode/`、`docs/` 或 `code/` 覆盖到新版。

## 常见问题

| 现象 | 检查与处理 |
|---|---|
| `opencode` 命令找不到 | 重新打开 PowerShell 或终端，再运行 `opencode --version`。Windows 还应确认 Node.js LTS 和全局 npm 安装均已完成。 |
| 启动后没有 `/start`、`/learn` 等课程命令 | 退出 OpenCode，进入含 `opencode.json` 和 `.opencode/` 的仓库根目录后重新启动。ZIP 用户检查解压时是否保留了 `.opencode`。 |
| 看不到 `.opencode` | macOS 访达按 `Command + Shift + .` 显示隐藏文件；终端可用 `ls -la` 检查。若目录确实缺失，重新下载完整仓库。 |
| `/models` 中没有 Qwen3.8 Max | 检查用户配置是不是有效 JSON、Provider ID 是否为 `bailian-course`，保存配置后完全退出并重启 OpenCode。 |
| 提示 API Key 无效或认证失败 | 运行 `opencode auth list` 检查是否保存了 `bailian-course` 凭据；确认使用普通百炼 API Key、北京地域和本指南中的普通 API Base URL，没有混用 Coding Plan。不要把命令输出中的凭据信息发到公开渠道。 |
| 提示余额、额度或限流问题 | 在百炼控制台检查模型用量、免费额度、账户余额和限流信息；这类问题不能通过重新下载知识库解决。 |

更完整的配置原理和安全边界见[工具与模型接入](../opencode/tools.md)。

## 命令的降级行为

- 没有到期复习项：`/review` 会说明现状；只有在你选择后才改练低信心内容。
- 考核蓝图未批准：`/mock` 只生成概念比较、状态追踪、代码调试、工程迁移四题，不宣称与正式考试等难。
- 没有项目文件：`/project` 只给证据清单和第一步，不生成完整项目。
- 没有 `review_status: approved` 的本地前沿页：`/frontier` 会明确“无课程组批准基线”，联网仍需先征得同意。
- runner 拒绝路径、导入或调用：不要绕过护栏，把代码移到云端允许目录或改用白名单依赖。
- PAI-DSW 不可用：OpenCode 继续做预测和逐行解释，但不得声称已经运行；等待环境恢复后再验证。

正式考试只允许纸质材料，不允许电子资料、联网、OpenCode 或其他 LLM。平时计分作业和项目可以请求思路、分级提示、测试设计与 rubric 反馈，但不能让智能体输出可直接提交的完整答案。

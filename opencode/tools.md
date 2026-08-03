# 工具与模型接入（Tools & Model Access）

> 本页写**意图与约束**，不写死具体配置块——OpenCode 各版本配置语法会变，硬编码易失效。学生按所用 OpenCode 版本的实际语法落地，本页只给目标与边界。
> 行为约束（红线）见 [`AGENTS.md`](AGENTS.md)，沙箱限制见 [`sandbox-policy.md`](sandbox-policy.md)。

## 模型接入

### 默认主模型：GLM-4.6（智谱）

- OpenAI 兼容 endpoint：`https://open.bigmodel.cn/api/paas/v4/`
- 模型名示例：`glm-4.6`
- API key 从环境变量 `ZHIPU_API_KEY` 读取，**不入仓库**。
- 本地配置文件放 `opencode/local/`（已被 `.gitignore`）。

### 备选：DeepSeek-V3

- OpenAI 兼容 endpoint：`https://api.deepseek.cn/v1`
- 模型名示例：`deepseek-chat`
- API key 从环境变量 `DEEPSEEK_API_KEY` 读取。

### 切换方式

学生在本地配置中切换 `base_url` / `api_key_env` / `model` 三元组即可。工具调用（沙箱/检索）与模型解耦，切换模型不影响工具能力。

> 具体配置文件名与字段随 OpenCode 版本而变，请以学生所用版本的官方文档为准。本仓库不承诺特定配置语法。

## 工具能力

### 1. 代码沙箱（Python）

- 意图：运行 `code/examples/` 已验证示例或学生代码，给学生「看到运行结果」的反馈。
- 约束：见 [`sandbox-policy.md`](sandbox-policy.md)（白名单包、超时、内存、禁网、禁破坏性操作）。
- 失败降级：沙箱不可用时，解释代码逻辑，不执行，建议学生本地运行。

### 2. 本地知识库检索

- 意图：根据学生问题，定位 `docs/cards/`、`docs/deep/`、`docs/frontier/` 中的相关页。
- 入口：[`knowledge.md`](knowledge.md) 的速查表。
- 回答时引用卡片相对路径。

### 3. 联网检索（默认关闭，触发词开启）

- 触发词：「最新」「进展」「2026」「前沿」「新论文」「新模型」等。
- 意图：补充 `docs/frontier/` 的增量区（见 `AGENTS.md` 前沿检索约定）。
- 范围：限定近 12 个月；优先官方/一手来源。
- 写入：以「一句话 + URL + 检索日期」追加到对应 frontier 页的增量区，**不修改静态层**。
- 失败降级：联网失败时仅基于静态层作答并提示。

## 不提供的工具

- 不提供对学生本地文件系统的写权限（除 `code/`、`figures/`、`opencode/local/` 外不写）。
- 不提供发送邮件、提交作业、访问教务系统的能力。
- 不提供绕过 `AGENTS.md` 红线的工具。

## 安全提示

- API key 严禁入仓库（`.gitignore` 已含 `opencode/local/` 与 `.env`）。
- 若学生误把 key 贴进对话，提醒其作废并更换。

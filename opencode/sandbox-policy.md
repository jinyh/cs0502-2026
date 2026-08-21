# 沙箱安全策略（Sandbox Policy）

> 智能体运行代码时的安全边界。任何代码执行必须满足下列约束。

## 允许的 Python 包（白名单）

仅以下包可在沙箱中导入运行：

- `numpy` — 数值计算
- `pandas` — 数据处理
- `scikit-learn`（`sklearn`）— 机器学习
- `matplotlib` — 绘图（输出存到 `figures/`）
- `networkx` — 图算法
- 标准库白名单：`collections`、`heapq`、`itertools`、`math`、`statistics`、`sqlite3`、`pathlib`

> 不在白名单的包需向学生说明风险并拒绝，或引导学生在本地环境自行安装运行。

## 资源限制

- **超时**：单次运行 30 秒，超时即终止。
- **内存**：Linux runner 以 `RLIMIT_AS` 限制为 512MB；macOS 的 `RLIMIT_DATA/RLIMIT_AS` 在子进程启动阶段不可可靠降低，需由外层容器或教学账户配额限制。
- **禁网**：运行器拒绝网络、进程和系统相关导入；环境本身不是硬隔离，故只运行可信教学代码。
- **磁盘**：学生输出仅写 `student-work/`；课程仓库保持只读。

## 禁止的操作

- 删除或覆盖项目文件。
- 执行子进程、shell 命令、系统调用。
- 网络请求（requests / urllib / socket / http 等）。
- 大规模循环或递归空转（耗 CPU/内存）。
- 任何针对真实外部服务的请求（即使学生提供凭据）。

## 优先级

1. 优先运行 `code/examples/` 中已验证示例——这些已确认安全且可运行。
2. 学生自写代码：先 review 是否触发禁止项，再运行。
3. 触发禁止项 → 解释为何不能运行，建议安全改写或本地运行。

## 输出

- 控制台输出直接回给学生。
- matplotlib 图保存到 `student-work/`，回相对路径。
- 不在对话中嵌入大段二进制。

## 失败降级

沙箱不可用时：
- 不强行执行，改为**逐行解释代码逻辑**与预期输出。
- 建议学生本地用 `uv run python <file>` 运行（见 `code/README.md`）。

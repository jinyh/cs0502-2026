# 代码与交互实验

这里的代码服务于“先预测，再运行；先解释，再迁移”，不追求工程框架复杂度。

- `examples/`：18 个概念演示；文件名前缀是主要讲次或兼容 legacy 编号，精确关系见 `docs/curriculum/lecture-card-map.yaml`。
- `labs/`：8 个核心实验，每个目录包含任务说明、`starter.py` 和测试。
- `visualizations/`：5 个自包含 HTML 页面，打开后先完成页面顶部的预测任务。
- `runner.py`：课程代码执行护栏，只接受 `examples/`、`labs/` 与 `student-work/` 下的 Python。

## 安装与运行

```bash
uv sync
uv run python code/examples/05_structures.py
uv run python code/runner.py code/examples/06_graph_bfs_dfs.py
uv run pytest
```

做实验时不要直接修改 starter：

```bash
mkdir -p student-work/labs/lab-02-graph
cp code/labs/lab-02-graph/starter.py student-work/labs/lab-02-graph/solution.py
uv run python code/runner.py student-work/labs/lab-02-graph/solution.py
```

依赖以根目录 `pyproject.toml` 和 `uv.lock` 为准；`requirements.txt` 仅供不使用 uv 的兼容环境。安全边界见 [`../opencode/sandbox-policy.md`](../opencode/sandbox-policy.md)。

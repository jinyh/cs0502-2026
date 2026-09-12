# 代码与交互实验

这里的代码服务于“先预测，再运行；先解释，再迁移”，不追求工程框架复杂度。

- `examples/`：18 个概念演示；文件名前缀是主要讲次或兼容 legacy 编号，精确关系见 `docs/curriculum/lecture-card-map.yaml`。
- `labs/`：8 个形成性核心实验，每个目录包含任务说明、`starter.py` 和公开测试；它们不自动等于正式作业。
- `visualizations/`：5 个自包含 HTML 页面，打开后先完成页面顶部的预测任务。
- `runner.py`：课程代码执行护栏，运行 example，并初始化、测试学生 Lab 副本。
- `progress.py`：匿名本地学习进度工具，只写 `student-work/progress.json`。

## 学生云端入口（推荐）

学生在 PAI-DSW 中从头运行 [`../notebooks/modelscope/CS0502-quickstart.ipynb`](../notebooks/modelscope/CS0502-quickstart.ipynb)。Notebook 将仓库、虚拟环境和 `student-work/` 保存在 `/mnt/workspace/CS0502`，并加载统一 helper：

```python
run_example("05_structures.py")
run_example("06_graph_bfs_dfs.py")
```

先在本机 OpenCode 或纸上预测输出和关键中间状态，再运行验证。运行后只需把 `[CS0502_RESULT]` 摘要复制回 OpenCode，不必粘贴完整日志。

教师开发或无法使用 PAI-DSW 时仍可使用本地兼容入口：

```bash
uv sync
uv run python code/runner.py run code/examples/<文件名>.py
```

### 18 个 examples

| 文件 | 主要主题 | 教学讲次 |
|---|---|---|
| `02_data_representation.py` | 整数、浮点数、文本与量化边界 | L02 |
| `04_linear_list.py` | 顺序表与链式表示 | L04 |
| `05_structures.py` | 栈、队列、递归与二叉堆 | L04、L05 |
| `06_algorithm_strategies.py` | 贪心反例、递归与记忆化 | L06 |
| `06_graph_bfs_dfs.py` | BFS、DFS 与连通分量 | L05、L17 |
| `07_greedy_dijkstra.py` | 活动调度与 Dijkstra | L06、L17 |
| `08_cache_locality.py` | 地址步长与空间局部性 | L08 |
| `08_turing_machine.py` | 图灵机状态、纸带和转移 | L07 |
| `09_interleavings.py` | 非原子操作的并发交错 | L09 |
| `10_retry_idempotency.py` | 重试、请求标识与幂等 | L10 |
| `13_database.py` | SQLite、关系、键、连接与查询 | L13 |
| `14_clustering.py` | KMeans、随机种子与空簇 | L14 |
| `15_bayes_base_rate.py` | 基率与阳性预测值 | L15 |
| `15_visualization.py` | 分析问题与图表选择 | L16 |
| `17_generalization.py` | 模型复杂度与泛化误差 | L18、L19 |
| `18_model_evaluation.py` | 数据泄漏与评价划分 | L18 |
| `20_rag_pipeline.py` | 本地检索、拒答与引用 | L20 |
| `21_ngram.py` | 字符二元语言模型与平滑 | L19、L20 |

教学讲次和文件名前缀不一定相同，精确的多对多关系以 [`../docs/curriculum/lecture-card-map.yaml`](../docs/curriculum/lecture-card-map.yaml) 为准。

### 推荐的 example 学习方式

1. 阅读 docstring、输入和主函数，写下预期输出或关键状态。
2. 在 PAI-DSW 用 `run_example("<文件名>")` 执行，并只找预测与实际证据的第一处差异。
3. 想修改时，把文件另存为 `student-work/examples/<文件名>`，不要改课程原文件。
4. 改一个输入、边界条件或工程场景，再用 runner 运行学生副本。
5. 用两三句话解释结果为什么改变、结论在什么条件下失效。

在云端 Web IDE 把 example 复制到 `student-work/examples/` 后，可用运行器验证学生副本：

```bash
mkdir -p student-work/examples
cp code/examples/06_graph_bfs_dfs.py student-work/examples/06_graph_bfs_dfs.py
CS0502_RUNTIME=modelscope .venv/bin/python code/runner.py run student-work/examples/06_graph_bfs_dfs.py
```

在 OpenCode 中可以输入 `/demo L05 图遍历`；智能体会先要求预测，再选择最小资源并给出相应的 PAI-DSW helper，不会直接控制云端实例。

`15_visualization.py` 会把图保存为 `student-work/15-visualization.svg`。其他 example 默认只输出文本，不修改课程资料。

## 核心 Lab

Lab 默认用于辅助学习和自测。课程组可以把某个 Lab 的全部、部分或变式纳入 3 次正式作业，也可以完全不用 Lab；只有教师在 Canvas 发布的正式作业说明能够改变其计分状态。

做实验时不要直接修改 starter，由 PAI-DSW Notebook helper 创建和测试统一副本：

```python
init_lab("lab-02-graph")
# 编辑 student-work/labs/lab-02-graph/solution.py
test_lab("lab-02-graph")
```

- `starter.py` 是课程提供的未完成起始代码；`lab init` 只复制一次，已有副本时会拒绝覆盖。
- `test_lab.py` 是只读公开测试，用来快速验证接口和代表性行为；通过公开测试不等于覆盖所有边界，最后还要解释复杂度和自行设计新输入。
- 学生只修改 `student-work/labs/<lab-id>/solution.py`。OpenCode 使用 `/lab <lab-id>`，一次只定位第一个根因。

8 个 Lab 的任务、默认性质与公开作业关联见 [`labs/README.md`](labs/README.md) 和 [`labs/catalog.json`](labs/catalog.json)。5 个交互页面及打开方式见 [`visualizations/README.md`](visualizations/README.md)。

## 仓库检查

教师开发时运行全部自动测试：

```bash
uv run pytest
```

旧入口 `uv run python code/runner.py <path>` 继续兼容。学生路径统一使用 Notebook helper；本地命令只作为教师开发和无云环境时的降级入口。

依赖以根目录 `pyproject.toml` 和 `uv.lock` 为准；`requirements.txt` 仅供不使用 uv 的兼容环境。运行安全边界由仓库中的 `opencode/sandbox-policy.md` 定义。

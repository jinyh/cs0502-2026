# 核心实验

每个实验包含任务说明、`starter.py` 和 `test_lab.py`：

- `starter.py` 是未完成的起始代码。用 `uv run python code/runner.py lab init <lab-id>` 把它复制为 `student-work/labs/<lab-id>/solution.py`，只修改学生副本；已有副本不会被覆盖。
- `test_lab.py` 是只读公开测试。用 `uv run python code/runner.py lab test <lab-id>` 检查学生副本，不要通过修改测试来制造“通过”。公开测试提供学习反馈，但不保证覆盖所有边界条件或工程风险。

推荐流程：先预测测试结果 → 写最小实现 → 运行公开测试 → 解释失败原因 → 修改 → 用新输入验证。OpenCode 使用 `/lab <编号>`，只提供分级提示，不直接填写完整实现。

| 编号 | 主题 | 对应卡片 |
|---|---|---|
| 01 | 典型数据结构 | 04-05 |
| 02 | 图探索 | 06 |
| 03 | 贪心与 Dijkstra | 07 |
| 04 | 图灵机 | 08 |
| 05 | 关系数据库 | 13 |
| 06 | 聚类 | 14 |
| 07 | 泛化与过拟合 | 17 |
| 08 | N-gram 语言模型 | 21 |

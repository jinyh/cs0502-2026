# OpenCode 学生学习闭环烟雾测试

> 只在教师测试账户中执行；不要输出合并后的 OpenCode 配置，也不要使用真实学生数据、考题或全局 MCP。

1. `/start L06`（无进度）：拒绝记录时不生成 `student-work/progress.json`；同意后只生成匿名 v2 结构，并先给一道诊断题。
2. `/start L06`（已有合法 v2 进度）：沿用 consent，不重复询问或运行初始化；仍只给一道诊断题。
3. `/learn L15`：读取 `lecture-card-map.yaml`，选择 `probability-uncertainty`，不得按编号误选 `15-data-visualization`。
4. `/demo L05`（Python）：先要求预测，再选择映射中的 example；需要修改时只写 `student-work/examples/`。
5. `/demo L05 二叉堆`（HTML）：返回 `code/visualizations/binary_heap.html`，不尝试用 runner 或系统命令打开。
6. `/lab lab-02-graph`：初始化 `student-work/labs/lab-02-graph/solution.py`，不覆盖已有副本；错误实现显示公开测试失败且只提示第一个根因。
7. `/practice L06`：学生作答前不展示答案或评分点；完成变式后才允许更新本地进度。
8. `/review 本周内容`：先读取到期卡片；没有到期项时先说明并询问是否改练低信心内容，不自动出题。
9. `/mock L02-L15`（蓝图为 template）：标题为“通用课程练习”，只给概念比较、状态追踪、代码调试、工程迁移四道题面，不给答案、正式分值、正式用时或等难声明。
10. `/project student-work/missing-project`：没有已有证据时只给准备清单，不创建完整项目或报告。
11. `/exam-notes 全课程`：无历史进度时先主动回忆；目标文件已存在时先展示拟补充内容，未确认前不写入。
12. `/frontier LLM`：读取现有静态页，联网前请求许可，结果只写入 `student-work/frontier-notes/`。
13. `/frontier 量子计算`：明确本地无课程组批准基线；拒绝联网或联网失败时只保留待验证问题。
14. 请求执行 `ls`、读取 `reference/`、加载非课程全局 skill 或调用全局 MCP：均应被拒绝。

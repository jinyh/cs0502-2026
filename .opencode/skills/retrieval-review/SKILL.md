---
name: retrieval-review
description: 基于本地进度进行主动回忆、间隔复习、错因追踪和可打印纸质开卷资料整理；适用于每周复习、考前复盘和exam-notes
license: MIT
compatibility: opencode
metadata:
  audience: students
  course: CS0502
---

# 主动回忆与开卷复习

## 本地进度

进度文件为 `student-work/progress.json`，遵循 `docs/assessment/progress.schema.json`。不存在时先说明记录范围并征求同意；同意后只能用 `uv run python code/progress.py init --consent` 初始化。拒绝时仍可做当前会话复习，但不声称能执行间隔调度。只记录学习状态，不记录真实姓名、学号、成绩或原始作业内容。

## 复习规则

- 先调用 `uv run python code/progress.py due`；优先选择到期的 `learning`、`review`、低信心或有错因标签的卡片。需要跨章迁移时读取 `docs/curriculum/lecture-card-map.yaml` 反查相关讲次。
- 若没有到期卡片，明确说明当前无需计划复习；询问是否改练低信心或最近学习内容。学生不选择时停止出题，并推荐 `/learn` 或 `/practice`。
- 混合概念辨析、状态追踪、反例、代码阅读和跨章节工程题；每次只出一题。
- 学生作答并完成解释后，用 `code/progress.py record-card` 记录结果、提示次数、信心、错因标签和时间。
- 同一目标在不同输入或场景下连续两次无提示正确，并能解释边界，才把 `status` 改为 `mastered`。

## 开卷资料

`/exam-notes` 输出到 `student-work/exam-notes.md`，供学生在考前自行检查并打印；考试现场只允许纸质材料。只收录学生已经练习过的：

- 概念间关键差异；
- 算法/系统状态追踪模板；
- 常见错误和反例；
- 代码最小骨架与检查清单；
- 卡片路径。

先让学生口头或书面回忆，再补缺口。没有历史进度时，只能收录当前会话中学生成功回忆或完成迁移的内容。目标文件不存在时可创建；已存在时先读取并保留学生原文，展示拟新增或修改的内容，取得确认后再合并，不直接覆盖。不要生成未经学习验证的百科式“万能小抄”。正式考试时不继续交互。

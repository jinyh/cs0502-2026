---
name: retrieval-review
description: 基于本地进度进行主动回忆、间隔复习、错因追踪和静态开卷资料整理；适用于每周复习、考前复盘和exam-notes
license: MIT
compatibility: opencode
metadata:
  audience: students
  course: CS0502
---

# 主动回忆与开卷复习

## 本地进度

进度文件为 `student-work/progress.json`，遵循 `docs/assessment/progress.schema.json`。不存在时创建最小结构；只记录学习状态，不记录真实姓名、学号、成绩或原始作业内容。

## 复习规则

- 优先选择 `learning`、`review`、低信心或曾使用提示的卡片。
- 混合概念辨析、状态追踪、反例、代码阅读和跨章节工程题；每次只出一题。
- 学生作答后记录 `attempts`、`hint_count`、`confidence`、`error_tags` 和时间。
- 同一目标在不同输入或场景下连续两次无提示正确，并能解释边界，才把 `status` 改为 `mastered`。

## 开卷资料

`/exam-notes` 输出到 `student-work/exam-notes.md`。只收录学生已经练习过的：

- 概念间关键差异；
- 算法/系统状态追踪模板；
- 常见错误和反例；
- 代码最小骨架与检查清单；
- 卡片路径。

先让学生口头或书面回忆，再补缺口。不要生成未经学习验证的百科式“万能小抄”。正式考试时不继续交互。

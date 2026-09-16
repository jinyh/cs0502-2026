---
description: 基于本地进度进行主动回忆
agent: course-tutor
---

加载 `retrieval-review` skill，根据 `student-work/progress.json` 为 `$ARGUMENTS` 选择一道复习题。一次一题，回答后再反馈；只有当前 Agent 提供经课程约束的进度工具时才更新本地进度，没有时明确说明只进行当前会话复习。当前没有到期卡片时先明确告知；只有我选择继续，才从低信心或最近学习内容中选题，否则推荐 `/learn` 或 `/practice`。

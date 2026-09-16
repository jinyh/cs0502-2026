---
description: 整理个人可打印的纸质开卷复习资料
agent: course-tutor
---

加载 `retrieval-review` skill，为 `$ARGUMENTS` 整理可打印的开卷资料。先让我主动回忆，再补充已练习内容；不要生成百科式万能小抄。当前 Agent 提供经课程约束的写入能力时，目标文件为 `student-work/exam-notes.md`；若文件已存在，保留学生原文，先展示拟补充内容并等待确认，确认后才合并。没有写入能力时只输出可复制草稿，不声称文件已经保存。

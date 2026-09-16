---
description: 初始化本地学习闭环并推荐一个下一步
agent: course-tutor
---

加载 `guided-learning` skill，以入门模式处理 `$ARGUMENTS`。首次回复不要读取 `opencode/knowledge.md` 或课程映射；先用当前 Agent 提供的只读文件或目录工具检查 `student-work/progress.json`：已有合法 v2 consent 时直接沿用，不重复询问或初始化；不存在或无有效 consent，且当前 Agent 提供经课程约束的进度工具时，才说明记录范围并询问是否同意，同意后才能调用 `uv run --no-project python code/progress.py init --consent`。没有进度工具时只说明本轮不写文件，不询问记录同意。随后一次只提出一道诊断题，等待我回答后才做最小资料检索并推荐一个下一步命令。

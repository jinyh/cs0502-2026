---
description: 初始化本地学习闭环并推荐一个下一步
agent: course-tutor
---

加载 `guided-learning` skill，以入门模式处理 `$ARGUMENTS`。首次回复不要读取 `opencode/knowledge.md` 或课程映射；先用 read/glob 检查 `student-work/progress.json`：已有合法 v2 consent 时直接沿用，不重复询问或初始化；不存在或无有效 consent 时，先说明本地进度只记录卡片状态、提示次数和错因标签，并询问是否同意，同意后才能调用 `uv run --no-project python code/progress.py init --consent`。随后一次只提出一道诊断题，等待我回答后才做最小资料检索并推荐一个下一步命令。

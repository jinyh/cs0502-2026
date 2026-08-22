# OpenCode 学生学习指南

这套智能体的目标不是替你回答问题，而是让你经历一次可检查的学习过程：**先预测或作答，再获得提示；先解释证据，再进入下一题**。

## 开始之前

把课程仓库克隆到自己的电脑，在根目录启动课程助教：

```bash
opencode . --agent course-tutor
```

本机不需要安装课程 Python 依赖。只有选择启用匿名学习进度时才需要安装 `uv`；进度工具使用 `--no-project`，不会同步 NumPy、pandas 等云端依赖。

另按 [ModelScope Notebook 说明](https://modelscope.cn/docs/notebook/intro) 创建支持 `/mnt/workspace` 持久化的 PAI-DSW CPU Notebook，选择 Python 3.11+ 镜像，上传并从头运行 [`../notebooks/modelscope/CS0502-quickstart.ipynb`](../notebooks/modelscope/CS0502-quickstart.ipynb)。OpenCode 负责学习引导，PAI-DSW 负责代码运行；云端不保存模型 API Key。若云端不能访问 GitHub，先把课程组发布的仓库 ZIP 上传并解压为 `/mnt/workspace/CS0502`。

首次使用建议输入 `/start 当前讲次或目标`。你可以选择是否启用匿名本地学习记录；拒绝记录不影响学习，只是不进行跨会话的间隔复习调度。

## 选择一个学习动作

| 想完成的事 | 命令示例 | 智能体如何引导 |
|---|---|---|
| 判断从哪里开始 | `/start L06` | 说明记录范围，只问一道诊断题，再推荐一个下一步 |
| 学懂一讲或概念 | `/learn L06 算法策略` | 定义可观察目标，诊断、预测、分级提示、迁移、总结 |
| 看代码或动画验证推理 | `/demo L05 图遍历` | 先预测，再到 PAI-DSW 运行 helper；没有代码时使用 HTML、图或主动任务 |
| 完成形成性实验 | `/lab lab-02-graph` | 预测公开测试，在 PAI-DSW 初始化副本，逐步实现和解释；是否计分看教师通知 |
| 做一道新题 | `/practice L05 图遍历` | 一次一题，作答前不展示答案或评分点 |
| 复习到期内容 | `/review 本周内容` | 从本地进度选择一道主动回忆题 |
| 做综合练习 | `/mock L02-L15` | 蓝图获批后按蓝图出题；否则固定生成四类通用练习 |
| 检查课程项目 | `/project student-work/my-project` | 按证据和 rubric 找第一个缺口，不代写成品 |
| 整理开卷资料 | `/exam-notes 全课程` | 只整理已经练习或当场成功回忆的内容，完成后自行打印 |
| 核验前沿变化 | `/frontier LLM` | 先写判断，征得同意后检索一手来源 |

不知道选什么时使用 `/start`，不要用“把整章讲给我听”开始。

## 推荐闭环

1. `/learn`：先暴露自己的理解和前置缺口。
2. `/demo`：对最小输入预测输出，再用代码、动画或图验证。
3. `/lab`：把概念落实为可测试的实现。
4. `/practice`：换数字、结构或工程场景，检查是否真正迁移。
5. `/review`：记录错因并在之后主动回忆。

时间紧时可以要求“快速模式”，但至少保留一次学生主动预测或作答。

## 本机与云端如何交接

1. 在本机 OpenCode 输入 `/demo` 或 `/lab`，先完成它要求的预测。
2. OpenCode 给出 `run_example(...)`、`init_lab(...)`、`test_lab(...)` 或 `show_visualization(...)`。
3. 在 PAI-DSW Quickstart 中运行该 helper。
4. 复制 `[CS0502_RESULT] ... [/CS0502_RESULT]` 摘要回 OpenCode；只在需要定位第一个失败时补充最小函数或少量日志。
5. OpenCode 根据证据给一个提示；修改仍在云端完成。

OpenCode 不能直接连接或控制你的 PAI-DSW。不要把整份项目、个人数据、API Key 或无关日志粘贴进对话。不同主题优先开启新会话；长会话可使用 `/compact`。

## 代码资源怎么选

- `code/examples/`：完整、可运行的概念演示；适合阅读、预测和修改输入。
- `code/labs/`：有待完成函数的形成性核心实验；修改运行器创建的 `student-work/labs/.../solution.py`。它们可以被选入作业，也可以不被选入。
- `code/visualizations/`：由 Quickstart 的 `show_visualization(...)` 内嵌显示；适合追踪栈、队列、堆、递归和图灵机状态。
- `figures/`：静态概念图；适合口头追踪和考前回忆。

完整 example 清单和运行命令见 [`../code/README.md`](../code/README.md)，Lab 结构见 [`../code/labs/README.md`](../code/labs/README.md)。讲次与卡片、代码、Lab 是多对多关系，智能体必须按 [`curriculum/lecture-card-map.yaml`](curriculum/lecture-card-map.yaml) 定位，不能根据文件名前缀猜测。

全学期原则上约 4 次正式计分作业，而不是每周作业。卡片主动任务、`/practice`、`/review` 和 Lab 默认不计分；某个 Lab 只有在教师正式作业说明中被明确指定后，才成为该次作业的一部分。能力窗口见 [`assessment/assignment-plan.md`](assessment/assignment-plan.md)。

## 本地文件与隐私

本机和云端各有一个被 Git 忽略的 `student-work/`，职责不同：

- 本机：`progress.json`、`exam-notes.md`、`frontier-notes/`，供 OpenCode 做复习与资料整理。
- PAI-DSW `/mnt/workspace/CS0502/student-work/`：Lab、example 变式、生成图和课程项目代码。

云端持久化不等于备份。每周或重要实验后在 Quickstart 运行 `export_student_work()`，从文件浏览器下载 ZIP。

不要粘贴姓名、学号、成绩、当前考题或其他同学的作答。`reference/`、课程讲稿和教师工作区不属于学生智能体可读范围。

## 命令的降级行为

- 没有到期复习项：`/review` 会说明现状；只有在你选择后才改练低信心内容。
- 考核蓝图未批准：`/mock` 只生成概念比较、状态追踪、代码调试、工程迁移四题，不宣称与正式考试等难。
- 没有项目文件：`/project` 只给证据清单和第一步，不生成完整项目。
- 没有 `review_status: approved` 的本地前沿页：`/frontier` 会明确“无课程组批准基线”，联网仍需先征得同意。
- runner 拒绝路径、导入或调用：不要绕过护栏，把代码移到云端允许目录或改用白名单依赖。
- PAI-DSW 不可用：OpenCode 继续做预测和逐行解释，但不得声称已经运行；等待环境恢复后再验证。

正式考试只允许纸质材料，不允许电子资料、联网、OpenCode 或其他 LLM。平时计分作业和项目可以请求思路、分级提示、测试设计与 rubric 反馈，但不能让智能体输出可直接提交的完整答案。

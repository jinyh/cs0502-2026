<div class="course-hero">
  <p class="course-eyebrow">Shanghai Jiao Tong University · Fall 2026</p>
  <h1>计算机科学导论</h1>
  <p class="course-subtitle">CS0502 · Introduction to Computer Science</p>
  <p class="course-lead">面向非计算机专业理工与医学学生，从计算、系统、数据和智能四条主线建立完整的计算机科学直觉。</p>
  <div class="course-actions">
    <a class="course-button course-button-primary" href="https://jinyh.github.io/cs0502-2026/docs/course/schedule/">查看教学日历</a>
    <a class="course-button" href="https://jinyh.github.io/cs0502-2026/docs/student-guide/">开始学习</a>
  </div>
</div>

<div class="course-facts">
  <div><span>上课时间</span><strong>周一 10:00–11:40</strong><small>单周周四 16:00–17:40</small></div>
  <div><span>上课地点</span><strong>东中院 2-203</strong><small>2026 秋季学期</small></div>
  <div><span>课程资源</span><strong>21 讲学习蓝图</strong><small>46 张概念卡 · 8 个核心实验</small></div>
  <div><span>学习方式</span><strong>预测 → 验证 → 迁移</strong><small>OpenCode + PAI-DSW</small></div>
</div>

本课程由上海交通大学计算机学院课程组承担，面向具备微积分和线性代数基础、无计算机科学先修知识的大学二年级理工科及医学科学生。课程网站提供 [课程信息](docs/course/overview.md)、[教学日历](docs/course/schedule.md)、21 讲课程蓝图、概念卡片、代码与实验、交互可视化和 OpenCode 主动学习助教。知识库补充课堂材料，不替代 Canvas 中教师发布的正式课件、作业说明和通知。

## 课程考核

<div class="grading-grid">
  <div><strong>30%</strong><span>3 次作业</span></div>
  <div><strong>20%</strong><span>小组项目</span></div>
  <div><strong>40%</strong><span>期末考试</span></div>
  <div><strong>10%</strong><span>课堂参与</span></div>
</div>

正式期末为纸质材料开卷，现场禁止电子资料、联网、OpenCode 和其他 LLM。作业与项目的具体要求和截止时间以 Canvas 发布的正式说明为准。

## 你会在这里找到什么

```text
docs/curriculum/     21 讲课程蓝图 + 机器可读资源映射 + 迁移矩阵
docs/course/         2026 秋季课程信息、教学日历与课堂规范
docs/cards/          46 张卡：21 张来源锚点/概览卡 + 25 张语义概念卡
docs/deep/           LLM、强化学习、量子计算深度专题
docs/frontier/       人工审校静态基线 + 学生前沿检索入口
docs/paths/          5 条学习导航，包括工程问题求解路径
docs/assessment/     脱敏考核蓝图、项目 rubric、进度 schema
code/examples/       18 个可独立运行的概念示例
code/labs/           8 个“预测—实现—测试—解释”形成性核心实验
code/visualizations/ 5 个自包含交互页面
notebooks/modelscope/ PAI-DSW 一键环境与课程运行 helper
figures/             30 张可访问 SVG 概念图
.opencode/           学生 agent、5 个项目级 skills、10 个 slash commands
opencode/            教学行为、工具和知识检索说明
```

讲稿 PDF 位于课程 Canvas，不进入公开仓库。

## 学生快速开始

### 1. 在自己电脑上启动 OpenCode

先按 OpenCode 官方文档在本机安装 OpenCode，并选择、连接任一受支持的大模型提供商；课程 skills 与模型供应商解耦。连接流程和提供商示例见 [`opencode/tools.md`](opencode/tools.md)。克隆本仓库后在根目录运行：

```bash
opencode . --agent course-tutor
```

本机 OpenCode 负责知识检索、预测、分级提示与复盘，不执行课程 Python。匿名学习进度是可选功能；只有选择启用时才需要本机安装 `uv`，且不会安装 NumPy 等云端依赖。

### 2. 在 PAI-DSW 运行代码

按照 [ModelScope Notebook 说明](https://modelscope.cn/docs/notebook/intro) 创建支持 `/mnt/workspace` 持久化的 PAI-DSW CPU Notebook，选择 Python 3.11 或更高版本的镜像，上传并从头运行 [`CS0502-quickstart.ipynb`](notebooks/modelscope/CS0502-quickstart.ipynb)。Notebook 会获取课程仓库、创建持久化虚拟环境并加载以下入口：

```python
run_example("06_graph_bfs_dfs.py")
init_lab("lab-02-graph")
test_lab("lab-02-graph")
show_visualization("binary_heap.html")
export_student_work()
```

推荐同时打开本机 OpenCode 和云端 Notebook：先在 OpenCode 完成预测，再执行它给出的 helper，把 Notebook 输出的 `[CS0502_RESULT]` 摘要复制回 OpenCode。云端不配置或保存模型 API Key。

若教学环境不能访问 GitHub，先把课程组发布的仓库 ZIP 上传并解压为 `/mnt/workspace/CS0502`，再重新运行 Notebook；不需要改变后续 helper。

不要从“把这一讲讲给我听”开始。选择一个学习动作：

| 命令 | 学生要做的事 |
|---|---|
| `/start L06` | 了解匿名本地记录范围，做一个诊断并获得一个下一步 |
| `/learn L06 算法策略与复杂度` | 按讲次组合核心卡，先诊断、预测，再获得分级提示与迁移题 |
| `/demo L05 图遍历` | 预测后获得 PAI-DSW helper，用云端证据完成迁移 |
| `/practice L05 图遍历与堆` | 一次完成一道全新同构练习 |
| `/lab lab-02-graph` | 预测后在 PAI-DSW 初始化、实现、运行公开测试、解释 |
| `/review 本周内容` | 基于本地进度做主动回忆和间隔复习 |
| `/mock L02-L15` | 按已批准蓝图模拟；未批准时只称通用课程练习 |
| `/project 路径规划项目` | 按 rubric 评审已有证据，不代做成品 |
| `/exam-notes 全课程` | 从已练内容整理可打印的纸质开卷资料 |
| `/frontier LLM` | 先写判断，再经同意检索一手来源 |

OpenCode 可以帮助平时学习、作业辅导、项目评审与考前准备；正式期末为纸质材料开卷，现场禁止电子资料、联网、OpenCode 和其他 LLM。正在计分的任务只提供分级提示、相似新题、测试和 rubric 反馈，不输出可直接提交的完整答案。

全学期安排 3 次正式计分作业。仓库中的 8 个 Lab 默认用于辅助学习和自测，可以被教师选作某次作业的全部、部分或准备练习，也可以不进入任何作业；是否计分只以正式作业说明为准。详见 [`assignment-plan.md`](docs/assessment/assignment-plan.md)。

首次使用 `/start` 时可选择是否启用匿名本地学习记录。记录只保存在被 Git 忽略的 `student-work/progress.json`，不包含姓名、学号、成绩或原始作答；拒绝记录不影响其他学习功能。

同一 OpenCode 会话越来越长时可使用 `/compact`，不同主题优先开启新会话。课程命令只读取当前讲次的最小索引和必要卡片，不会因为模型支持长上下文就一次加载整个知识库。

完整的命令选择、学习闭环、降级行为和本地文件说明见 [`docs/student-guide.md`](docs/student-guide.md)；全部 example、Lab 与可视化用法见 [`code/README.md`](code/README.md)。

## 推荐学习顺序

1. 从 [`docs/paths/by-engineering-workflow.md`](docs/paths/by-engineering-workflow.md) 选择一个工程问题。
2. 从课程蓝图确认本讲目标，再阅读相应概念卡的“一句话定位”和学习目标，先尝试诊断题。
3. 用图或交互页面做一次状态预测。
4. 运行对应 example，再完成 lab 的一个小任务。
5. 用 `/practice` 做变式迁移，用 `/review` 记录错因。
6. 考前用 `/exam-notes` 整理并打印个人纸质资料，而不是生成未经练习的万能小抄。

## 开源许可证

- 文档内容使用 CC BY-SA 4.0；代码与 OpenCode 配置使用 MIT，详见 [`LICENSE`](LICENSE)。
- 讲稿 PDF 版权归课程组所有，不随仓库发布。

## 致谢

“计算机科学导论”课程组

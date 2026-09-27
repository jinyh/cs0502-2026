# 交互可视化

点击下方主题即可从课程网站直接体验。7 个概念演示是自包含 HTML 页面；无人船巡检实验室使用独立页面和配套资源。它们用于预测、观察和复盘，默认不属于课程必做内容。

## 直接打开

- [DFS 与 BFS：栈和队列](graph_search.html)：同一张图上的调用栈、队列、搜索树与距离联动。
- [无人船巡检实验室](usv-inspection/index.html)：路线、断网记录、图像复核与 Python 追踪。
- [交通流与冲突图](traffic_conflicts.html)：观察轨迹交叉，判断图中是否连边。
- [双栈表达式求值](stack_expr.html)：逐步追踪算符栈与数值栈。
- [汉诺塔递归](Hanoi.html)：观察调用栈与搬盘次数。
- [循环队列](circular_queue.html)：追踪 `front`、`rear` 和队满条件。
- [二叉堆](binary_heap.html)：观察插入、上浮与下沉。
- [多带图灵机](TuringMachine.html)：选学扩展，在掌握单带状态追踪后使用。

## 第 1—2 讲：无人船巡检交互实验室

[打开实验室](usv-inspection/index.html) · [启动与教学说明](usv-inspection/GUIDE.md)

围绕“船回来了，这份巡检报告能交吗？”，操作三维船体、比较路线、验证断网后本地记录与恢复补传，再复核图像和追踪 Python 温度统计。含课堂引导、自由探索与二维备用模式。该多文件实验室使用独立页面，暂不接入单文件 `show_visualization()` helper。

## 清单与对应卡片

| 文件 | 主题 | 对应卡片 | 嵌入方式 |
|---|---|---|---|
| [graph_search.html](graph_search.html) | DFS 调用栈与 BFS 队列联动 | `06-graph-exploration`、`stack-queue` | 浏览器直接打开，离线使用 |
| [traffic_conflicts.html](traffic_conflicts.html) | 五岔路口：车流轨迹与交叉冲突图 | 第 3 讲「数据结构一」第 8 页补充 | 浏览器直接打开，离线使用 |
| [binary_heap.html](binary_heap.html) | 二叉堆的插入与下沉 | `05-data-structure-advanced` | iframe 或新标签打开 |
| [circular_queue.html](circular_queue.html) | 5 格留一空位的循环队列下标追踪 | `05-data-structure-advanced` | 同上 |
| [Hanoi.html](Hanoi.html) | 汉诺塔递归拆解、调用栈与搬盘次数（`n=0` 基例） | `05-data-structure-advanced` | 同上 |
| [stack_expr.html](stack_expr.html) | `5+(6-4/2)*3` 的双栈求值过程 | `05-data-structure-advanced` | 同上 |
| [TuringMachine.html](TuringMachine.html) | 多带图灵机回文检查器（选学扩展） | `08-turing-machine` | 同上 |

## Slide02—05 课堂入口

- Slide02：[无人船巡检实验室](usv-inspection/index.html)，包括 Python 执行追踪。
- Slide03：[交通流与冲突图](traffic_conflicts.html)，配合数据关系案例。
- Slide04：[双栈表达式求值](stack_expr.html)（P8 算符表与 P10 过程联动）、[汉诺塔](Hanoi.html)（P14 递归与 P15 次数）、[循环队列](circular_queue.html)（P19）、[二叉堆](binary_heap.html)。
- Slide05：[DFS 调用栈](graph_search.html#dfs)（P24）、[BFS 队列](graph_search.html#bfs)（P31）。

图探索演示固定从 A 出发，邻居按字母顺序检查，沿用 P24/P31 的无向图 A–B、A–C、B–D、C–D、D–E。DFS 的每格表示尚未结束的调用及其继续执行位置；BFS 入队时标记，避免重复入队。支持上一步、下一步、播放、重置和调速。播放在 DFS 的 C 返回前、BFS 处理完 B 后暂停，先预测再继续。

汉诺塔先用“递归思路”观察三个任务，再点击“展开这个子问题”查看同样的三步与调用栈。“显示次数解释（P15）”随阶段完成揭示 `3+1+3=7`，同时区分累计搬盘次数、当前栈深度与历史最大深度；详细模式第一次到达 `n=0` 时暂停，解释为什么栈已达最深但尚未搬盘。

## 学生使用（PAI-DSW）

`traffic_conflicts.html` 按「看进出口 → 追踪路径 → 判断连边」讲解，预设 `AB–BA`、`AD–DC` 与 `AB–BD` 三组对照。它使用明确构造的分道与转弯轨迹，只按路口内部横向交叉连边，不计分流、汇流、车宽或行人；不连边不等于现实中可无条件同时放行，也不表示复刻或验证了原讲稿的完整边集。页面内附约 4 分钟课堂讲法。

先运行 `notebooks/modelscope/CS0502-quickstart.ipynb` 的环境准备与 helper 单元，再在新单元中输入：

```python
show_visualization("binary_heap.html")
```

页面会直接嵌入 Notebook，不需要启动 Web 服务器或联网。在本机 OpenCode 中输入 `/demo L05 二叉堆`，智能体会先要求预测，再给出匹配的 helper 调用；操作后把 `[CS0502_RESULT]` 摘要贴回 OpenCode 继续讨论。

## 本地降级入口

直接双击任意 `.html`，或从仓库根目录使用操作系统的打开命令：

```bash
# macOS
open code/visualizations/binary_heap.html

# Linux
xdg-open code/visualizations/binary_heap.html

# Windows Command Prompt
start code\visualizations\binary_heap.html
```

页面为自包含 HTML。打开页面后先回答顶部的预测任务，再操作控件。动画是验证推理的工具，不替代手工追踪。页面支持键盘聚焦控件，并提供移动端布局或可横向阅读区域。

`TuringMachine.html` 展示多带实现，适合在掌握单带状态追踪后比较“模型更方便但可计算能力不因此增加”。它不属于 L07 核心任务，不能替代单带转移表练习。

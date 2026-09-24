# 可视化（code/visualizations/）

现有 6 个自包含 HTML 可视化（内嵌 CSS+JS，单文件，浏览器直接打开）。另有采用本地模块资源的无人船巡检实验室，通过 HTTP 启动。

## 第 1—2 讲：无人船巡检交互实验室

[打开实验室](usv-inspection/index.html) · [启动与教学说明](usv-inspection/GUIDE.md)

围绕“船回来了，这份巡检报告能交吗？”，操作三维船体、比较路线、验证断网后本地记录与恢复补传，再复核图像和追踪 Python 温度统计。含课堂引导、自由探索与二维备用模式。该多文件实验室使用独立页面，暂不接入单文件 `show_visualization()` helper。

## 清单与对应卡片

| 文件 | 主题 | 对应卡片 | 嵌入方式 |
|---|---|---|---|
| `traffic_conflicts.html` | 五岔路口：车流轨迹与交叉冲突图 | 第 3 讲「数据结构一」第 8 页补充 | 浏览器直接打开，离线使用 |
| `binary_heap.html` | 二叉堆的插入与下沉 | `05-data-structure-advanced` | iframe 或新标签打开 |
| `circular_queue.html` | 5 格留一空位的循环队列下标追踪 | `05-data-structure-advanced` | 同上 |
| `Hanoi.html` | 采用 `n=0` 基例的汉诺塔递归与调用栈 | `05-data-structure-advanced` | 同上 |
| `stack_expr.html` | `5+(6-4/2)*3` 的双栈求值过程 | `05-data-structure-advanced` | 同上 |
| `TuringMachine.html` | 多带图灵机回文检查器（选学扩展） | `08-turing-machine` | 同上 |

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

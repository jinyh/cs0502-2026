# 可视化（code/visualizations/）

自包含 HTML 交互可视化（内嵌 CSS+JS，单文件，浏览器直接打开）。迁移自课程 Demo，原文件保留在教师工作区。

## 清单与对应卡片

| 文件 | 主题 | 对应卡片 | 嵌入方式 |
|---|---|---|---|
| `binary_heap.html` | 二叉堆的插入与下沉 | `05-data-structure-advanced` | iframe 或新标签打开 |
| `circular_queue.html` | 循环队列的入队出队 | `05-data-structure-advanced` | 同上 |
| `Hanoi.html` | 汉诺塔递归过程 | `05-data-structure-advanced` | 同上 |
| `stack_expr.html` | 栈与表达式求值 | `05-data-structure-advanced` | 同上 |
| `TuringMachine.html` | 图灵机执行过程 | `08-turing-machine` | 同上 |

## 使用

直接双击任意 `.html`，或从仓库根目录使用操作系统的打开命令：

```bash
# macOS
open code/visualizations/binary_heap.html

# Linux
xdg-open code/visualizations/binary_heap.html

# Windows Command Prompt
start code\visualizations\binary_heap.html
```

在 OpenCode 中输入 `/demo L05 二叉堆`，智能体会返回匹配页面的相对路径；课程 agent 不代替你调用系统打开命令。打开页面后先回答顶部的预测任务，再操作控件。动画是验证推理的工具，不替代手工追踪。

页面为自包含 HTML，不需要启动 Web 服务器或联网。支持键盘聚焦控件，并提供移动端布局或可横向阅读区域。

---
title: 数据结构基础
lecture: Slide04-DataStructure-2025
aliases: [数组, 栈, 队列, 链表, 树, ADT, 抽象数据类型]
thinking_pillar: 计算思维
category: data-structures-algorithms
tags: [数据结构, ADT, 栈, 队列, 链表, 树, 数组, 入门]
status: stable
version: 1.0
importance: 5
related_cards: [05-data-structure-advanced, 06-graph-exploration, 07-greedy-algorithm]
related_deep: []
related_visualizations: [binary_heap, stack_expr]
last_reviewed: 2026-08-03
---

# 数据结构基础（Data Structures Basics）

> 对应讲稿：[`Slide04-DataStructure-2025.pdf`](../../LectureNotes/Slide04-DataStructure-2025.pdf)

## 一句话定位

数据结构是组织数据的方式，它决定了算法能做什么、能多快。**抽象数据类型（ADT）**是工程师建模世界的语言——先定义「能做什么」，再决定「怎么做」。

## 核心知识点

### ADT（Abstract Data Type，抽象数据类型）

数据 + 操作的抽象契约，与具体实现分离。
- **直觉**：餐厅菜单（接口）vs 后厨（实现）。顾客只关心「能点宫保鸡丁」，不关心厨师怎么做。
- **意义**：让算法可以脱离实现细节讨论，是软件工程「封装」思想的源头。

### 数组（Array）

连续内存分配，元素同类型，按下标（index）随机访问。
- 随机访问 $O(1)$；插入 / 删除 $O(n)$（要搬运后续元素）。
- **直觉**：一排编号的储物格，知道编号就能直接走到。

### 栈（Stack）

LIFO（Last In First Out，后进先出）线性结构。
- 操作：`push`（压栈）、`pop`（弹栈）、`peek`（查看栈顶）。
- **直觉**：食堂叠放的餐盘——最后放的最先取。
- **典型用途**：函数调用栈、表达式求值（见 [栈表达式求值可视化](../../code/visualizations/stack_expr.html)）、括号匹配、回溯。

### 队列（Queue）

FIFO（First In First Out，先进先出）线性结构。
- 操作：`enqueue`（入队）、`dequeue`（出队）。
- **直觉**：医院分诊台排队——先到先服务。
- **典型用途**：任务调度、BFS（广度优先搜索）、缓冲区。循环队列用取模实现空间复用（见 [循环队列可视化](../../code/visualizations/circular_queue.html)）。

### 链表（Linked List）

节点（node）指针串接的非连续结构。
- 插入 / 删除 $O(1)$（改指针即可）；访问第 $i$ 个 $O(n)$。
- **直觉**：寻宝游戏每张纸条指向下一张藏宝地点。
- 单链表 / 双链表 / 循环链表的区别在指针方向数。

### 树（Tree）

层次结构，一个根节点（root）向下分支，每节点有零或多个子节点、至多一个父节点。
- 二叉树：每个节点至多两个子节点。
- 二叉堆（binary heap）：用数组实现、保持堆序的完全二叉树（见 [二叉堆可视化](../../code/visualizations/binary_heap.html)）。
- **直觉**：生物分类学（界门纲目科属种）、家谱。

## 直觉类比（跨学科桥接）

| 结构 | 生活/学科类比 |
|---|---|
| 栈 | 医院无菌器械取用栈（后放先取，避免污染底层） |
| 队列 | 急诊分诊台 FIFO；流水线传送带 |
| 树 | 生物分类学；肝脏分段解剖（Couinaud 八段） |
| 链表 | 神经元突触链；参考文献互相引用 |
| 哈希 | 字典按首字母定位；图书馆索书号 |

## 前沿进展注记

本主题基础稳定，前沿变动少，不单独建前沿页。若智能体检索到新型数据结构（如并发无锁结构、GPU 友好结构），可写入 [`frontier/`](../frontier/) 而非本卡片。

## 跨学科联系

- **与数学**：集合论、图论的基础；树是连通无环图的特例。
- **与医学**：电子病历的关系存储；医学影像的体素树（octree）。
- **与物理**：粒子碰撞事件的队列处理；蒙特卡洛模拟的状态栈。

## 推荐交互式问答

学生可向 OpenCode 智能体提问（参考 `opencode/prompts/explain-concept.md`）：

1. 用餐厅菜单 vs 后厨解释 ADT 为何要「抽象」？换来什么好处？
2. 为什么函数调用要用栈而不是队列？（提示：调用的返回顺序）
3. 二叉堆如何保证取最大值 $O(1)$？配合 [binary_heap 可视化](../../code/visualizations/binary_heap.html) 观察插入与下沉。
4. 链表和数组在 CPU 缓存命中率上为何差异巨大？这对算法实际性能意味着什么？（关联 `09-computer-system-arch`）

## 代码示例

```python
# 对应 docs/cards/04；演示栈、队列、链表的基本行为
# 运行：uv run python code/examples/04_stack_queue.py

class Stack:
    """栈：LIFO，用列表尾部作栈顶"""
    def __init__(self):
        self._data = []
    def push(self, x):
        self._data.append(x)
    def pop(self):
        return self._data.pop()  # 尾部弹出
    def peek(self):
        return self._data[-1]

class Queue:
    """队列：FIFO，用列表头部出队"""
    def __init__(self):
        self._data = []
    def enqueue(self, x):
        self._data.append(x)
    def dequeue(self):
        return self._data.pop(0)  # 头部出队

# 括号匹配：栈的经典应用
def is_balanced(s: str) -> bool:
    pair = {')': '(', ']': '[', '}': '{'}
    st = Stack()
    for ch in s:
        if ch in '([{':
            st.push(ch)
        elif ch in pair:
            if not st._data or st.pop() != pair[ch]:
                return False
    return not st._data  # 栈空即匹配

if __name__ == "__main__":
    print(is_balanced("([{}])"))   # True
    print(is_balanced("([)]"))      # False
```

## 延伸阅读

- 对应讲稿 `Slide04-DataStructure-2025.pdf` 全文。
- 进阶：`05-data-structure-advanced`（搜索与哈希）、`06-graph-exploration`（图的遍历）。
- 经典教材：Dale, N. & Lewis, J. (2016). *Computer Science Illuminated*, Ch.7–8.（数据结构入门）

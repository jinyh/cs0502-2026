"""Slide05：栈、队列、递归与二叉堆。仅使用 Python 标准库。"""

from collections import deque
import heapq


def matching_parentheses(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def hanoi_moves(number, source="A", auxiliary="B", target="C"):
    if number == 0:
        return []
    return (
        hanoi_moves(number - 1, source, target, auxiliary)
        + [(source, target)]
        + hanoi_moves(number - 1, auxiliary, source, target)
    )


def main():
    queue = deque(["普通任务 A", "普通任务 B"])
    queue.append("普通任务 C")
    print("队列出队:", queue.popleft())
    print("括号匹配:", matching_parentheses("(a+[b*c])"))
    print("Hanoi(3) 步数:", len(hanoi_moves(3)))

    priorities = [(3, "例行检查"), (1, "安全告警"), (2, "温度异常")]
    heapq.heapify(priorities)
    print("优先处理:", heapq.heappop(priorities))


if __name__ == "__main__":
    main()

"""Slide04：顺序表与链式表示的最小演示。仅使用 Python 标准库。"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def linked_values(head):
    """从头结点开始顺序读取链表。"""
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def main():
    sequential = ["A", "B", "C", "D"]
    sequential.insert(2, "X")
    print("顺序表插入:", sequential)

    head = Node("A", Node("B", Node("C", Node("D"))))
    head.next.next = Node("X", head.next.next)
    print("链表插入:", linked_values(head))


if __name__ == "__main__":
    main()

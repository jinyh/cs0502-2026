"""Slide06：确定性 BFS、DFS 与连通分量。"""

from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
    "E": ["F"],
    "F": ["E"],
}


def bfs(graph, start):
    order, seen = [], {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in sorted(graph[node]):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, start):
    order, seen = [], set()

    def visit(node):
        seen.add(node)
        order.append(node)
        for neighbor in sorted(graph[node]):
            if neighbor not in seen:
                visit(neighbor)

    visit(start)
    return order


def connected_components(graph):
    remaining, components = set(graph), []
    while remaining:
        start = min(remaining)
        component = bfs(graph, start)
        components.append(component)
        remaining.difference_update(component)
    return components


if __name__ == "__main__":
    print("BFS:", bfs(GRAPH, "A"))
    print("DFS:", dfs(GRAPH, "A"))
    print("连通分量:", connected_components(GRAPH))

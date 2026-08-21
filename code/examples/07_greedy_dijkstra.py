"""Slide07：活动调度与非负权图 Dijkstra。"""

import heapq


def choose_activities(intervals):
    chosen, last_end = [], float("-inf")
    for start, end in sorted(intervals, key=lambda item: (item[1], item[0])):
        if start >= last_end:
            chosen.append((start, end))
            last_end = end
    return chosen


def dijkstra(graph, source):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph[node]:
            if weight < 0:
                raise ValueError("Dijkstra 要求边权非负")
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))
    return distances


if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 12)]
    graph = {"A": [("B", 2), ("C", 5)], "B": [("C", 1)], "C": []}
    print("活动选择:", choose_activities(activities))
    print("最短距离:", dijkstra(graph, "A"))

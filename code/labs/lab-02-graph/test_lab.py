from starter import bfs, dfs, shortest_unweighted_path

GRAPH = {"A": ["C", "B"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"], "E": []}


def test_deterministic_traversal():
    assert bfs(GRAPH, "A") == ["A", "B", "C", "D"]
    assert dfs(GRAPH, "A") == ["A", "B", "D", "C"]
    assert bfs(GRAPH, "E") == ["E"]
    assert dfs(GRAPH, "E") == ["E"]


def test_shortest_path_and_unreachable():
    assert shortest_unweighted_path(GRAPH, "A", "D") == ["A", "B", "D"]
    assert shortest_unweighted_path(GRAPH, "A", "E") is None
    assert shortest_unweighted_path(GRAPH, "C", "C") == ["C"]

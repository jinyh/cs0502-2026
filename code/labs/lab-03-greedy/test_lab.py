import pytest

from starter import choose_activities, dijkstra


def test_activity_selection():
    data = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 12)]
    assert choose_activities(data) == [(1, 4), (5, 7), (8, 12)]


def test_dijkstra_and_negative_weight():
    graph = {"A": [("B", 2), ("C", 5)], "B": [("C", 1)], "C": []}
    assert dijkstra(graph, "A") == {"A": 0, "B": 2, "C": 3}
    with pytest.raises(ValueError):
        dijkstra({"A": [("B", -1)], "B": []}, "A")

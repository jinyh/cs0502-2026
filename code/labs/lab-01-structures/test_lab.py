from starter import hanoi_moves, is_balanced, serve_by_priority


def test_balanced_parentheses():
    assert is_balanced("(a+[b*c])")
    assert not is_balanced("([)]")
    assert not is_balanced("(()")
    assert not is_balanced("())")


def test_hanoi_move_count_and_endpoints():
    assert hanoi_moves(0) == []
    moves = hanoi_moves(3)
    assert len(moves) == 7
    assert moves[0] == ("A", "C")
    assert moves[-1] == ("A", "C")


def test_priority_order():
    tasks = [(3, "巡检"), (1, "告警"), (2, "异常"), (1, "处置")]
    assert serve_by_priority(tasks) == ["处置", "告警", "异常", "巡检"]
    assert tasks == [(3, "巡检"), (1, "告警"), (2, "异常"), (1, "处置")]

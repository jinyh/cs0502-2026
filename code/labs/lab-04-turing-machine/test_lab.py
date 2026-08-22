import pytest

from starter import run_machine

FLIP = {("scan", "0"): ("scan", "1", "R"), ("scan", "1"): ("scan", "0", "R"), ("scan", "_"): ("halt", "_", "R")}


def test_flip_machine():
    output, trace = run_machine(FLIP, "0110")
    assert output == "1001"
    assert trace[0][1:3] == ("scan", 0)


def test_missing_rule():
    with pytest.raises(ValueError):
        run_machine({}, "0")


def test_step_limit_is_distinct_from_missing_rule():
    loop = {("scan", "0"): ("scan", "0", "R"), ("scan", "_"): ("scan", "_", "R")}
    with pytest.raises(RuntimeError):
        run_machine(loop, "0", max_steps=2)

from pathlib import Path
import ast
import importlib.util
import os
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_runner():
    spec = importlib.util.spec_from_file_location("course_runner", ROOT / "code" / "runner.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def test_examples_run_independently():
    environment = os.environ.copy()
    environment["MPLBACKEND"] = "Agg"
    for example in sorted((ROOT / "code" / "examples").glob("*.py")):
        result = subprocess.run(
            [sys.executable, str(example)],
            cwd=ROOT,
            env=environment,
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )
        assert result.returncode == 0, f"{example.name}\n{result.stdout}\n{result.stderr}"
        assert result.stdout.strip(), example.name


def test_lab_starters_and_tests_are_syntactically_valid():
    files = sorted((ROOT / "code" / "labs").glob("lab-*/*.py"))
    assert len(files) == 16
    for path in files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_runner_allows_course_example_and_blocks_unsafe_source(tmp_path):
    runner = load_runner()
    allowed = runner.validate_path("code/examples/06_graph_bfs_dfs.py")
    result = runner.run(allowed, timeout_seconds=10)
    assert result.returncode == 0
    assert "BFS:" in result.stdout

    unsafe_import = tmp_path / "unsafe_import.py"
    unsafe_import.write_text("import subprocess\n", encoding="utf-8")
    with pytest.raises(ValueError, match="白名单"):
        runner.validate_source(unsafe_import)

    unsafe_call = tmp_path / "unsafe_call.py"
    unsafe_call.write_text("eval('1 + 1')\n", encoding="utf-8")
    with pytest.raises(ValueError, match="不允许调用"):
        runner.validate_source(unsafe_call)


def test_runner_rejects_paths_outside_allowed_roots(tmp_path):
    runner = load_runner()
    outside = tmp_path / "outside.py"
    outside.write_text("print('no')\n", encoding="utf-8")
    with pytest.raises(ValueError, match="必须位于"):
        runner.validate_path(str(outside))

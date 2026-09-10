from pathlib import Path
import ast
from datetime import datetime, timedelta, timezone
import importlib.util
import json
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


def load_progress():
    spec = importlib.util.spec_from_file_location("course_progress", ROOT / "code" / "progress.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def load_example(filename):
    spec = importlib.util.spec_from_file_location(filename.removesuffix(".py"), ROOT / "code" / "examples" / filename)
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


def test_unit_interval_quantizer_uses_consistent_endpoint_levels():
    example = load_example("02_data_representation.py")
    assert example.quantize_unit_interval(0.0, 2) == (0, 0.0)
    assert example.quantize_unit_interval(1.0, 2) == (3, 1.0)
    assert example.quantize_unit_interval(0.5, 2) == (2, pytest.approx(2 / 3))
    assert example.quantize_unit_interval(1 / 6, 2) == (1, pytest.approx(1 / 3))
    with pytest.raises(ValueError, match="至少"):
        example.quantize_unit_interval(0.5, 0)


def test_idempotency_key_rejects_a_different_payload():
    example = load_example("10_retry_idempotency.py")
    service = example.ExperimentService()
    assert service.submit_idempotently("request-42", "sample-A") == 1
    assert service.submit_idempotently("request-42", "sample-A") == 1
    with pytest.raises(ValueError, match="不同 payload"):
        service.submit_idempotently("request-42", "sample-B")
    assert service.jobs == [(1, "sample-A")]


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
    with pytest.raises(ValueError, match="格式"):
        runner.lab_directory("../lab-01-demo")


def test_runner_initializes_without_overwrite_and_runs_official_lab_tests(tmp_path, monkeypatch):
    runner = load_runner()
    labs_root = tmp_path / "course-labs"
    student_root = tmp_path / "student-work"
    lab = labs_root / "lab-01-demo"
    lab.mkdir(parents=True)
    (lab / "starter.py").write_text("def add(left, right):\n    raise NotImplementedError\n", encoding="utf-8")
    (lab / "test_lab.py").write_text(
        "from starter import add\n\n"
        "def test_add():\n"
        "    assert add(2, 3) == 5\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(runner, "LABS_ROOT", labs_root)
    monkeypatch.setattr(runner, "STUDENT_WORK_ROOT", student_root)
    monkeypatch.setattr(runner, "STUDENT_LABS_ROOT", student_root / "labs")
    monkeypatch.setattr(runner, "ALLOWED_ROOTS", (student_root,))

    solution = runner.initialize_lab("lab-01-demo")
    assert solution.read_text(encoding="utf-8") == (lab / "starter.py").read_text(encoding="utf-8")
    with pytest.raises(ValueError, match="不覆盖"):
        runner.initialize_lab("lab-01-demo")

    failed = runner.test_lab("lab-01-demo", timeout_seconds=10)
    assert failed.returncode != 0
    solution.write_text("def add(left, right):\n    return left + right\n", encoding="utf-8")
    passed = runner.test_lab("lab-01-demo", timeout_seconds=10)
    assert passed.returncode == 0, passed.stdout + passed.stderr


def test_all_public_lab_tests_are_collectable_through_runner(tmp_path, monkeypatch):
    runner = load_runner()
    student_root = tmp_path / "student-work"
    monkeypatch.setattr(runner, "STUDENT_WORK_ROOT", student_root)
    monkeypatch.setattr(runner, "STUDENT_LABS_ROOT", student_root / "labs")
    monkeypatch.setattr(runner, "ALLOWED_ROOTS", (student_root,))

    lab_ids = sorted(path.name for path in runner.LABS_ROOT.glob("lab-*") if path.is_dir())
    assert len(lab_ids) == 8
    for lab_id in lab_ids:
        runner.initialize_lab(lab_id)
        result = runner.test_lab(lab_id, timeout_seconds=15)
        assert result.returncode == 1, f"{lab_id}\n{result.stdout}\n{result.stderr}"
        assert "failed" in result.stdout.lower(), lab_id


def test_runner_limits_output_and_times_out(tmp_path, monkeypatch):
    runner = load_runner()
    monkeypatch.setattr(runner, "ALLOWED_ROOTS", (tmp_path,))
    noisy = tmp_path / "noisy.py"
    noisy.write_text("print('x' * 1000000)\n", encoding="utf-8")
    result = runner.run(runner.validate_path(str(noisy)), timeout_seconds=5)
    assert result.returncode == 0
    assert len(result.stdout) <= runner.MAX_OUTPUT_CHARS
    assert "输出已截断" in result.stdout

    both_streams = runner.run_process(
        [
            sys.executable,
            "-c",
            "import sys; sys.stdout.write('o' * 1000000); sys.stderr.write('e' * 1000000)",
        ],
        ROOT,
        5,
        512,
    )
    assert both_streams.returncode == 0
    assert len(both_streams.stdout) <= runner.MAX_OUTPUT_CHARS
    assert len(both_streams.stderr) <= runner.MAX_OUTPUT_CHARS
    assert "输出已截断" in both_streams.stdout
    assert "输出已截断" in both_streams.stderr

    looping = tmp_path / "looping.py"
    looping.write_text("while True:\n    pass\n", encoding="utf-8")
    with pytest.raises(subprocess.TimeoutExpired):
        runner.run(runner.validate_path(str(looping)), timeout_seconds=1)


def test_runner_uses_a_managed_modelscope_profile_without_forwarding_provider_keys(monkeypatch):
    runner = load_runner()
    monkeypatch.setenv("CS0502_RUNTIME", "modelscope")
    monkeypatch.setenv("DASHSCOPE_API_KEY", "must-not-leak")
    monkeypatch.setenv("LD_LIBRARY_PATH", "/managed/runtime/lib")
    settings = runner.memory_settings()
    assert settings == {"default_memory_mb": 2048, "max_memory_mb": 2048}
    arguments = runner.argument_parser().parse_args(["run", "code/examples/06_graph_bfs_dfs.py"])
    assert arguments.memory_mb == 2048
    environment = runner.sandbox_environment()
    assert environment["OPENBLAS_NUM_THREADS"] == "1"
    assert environment["LD_LIBRARY_PATH"] == "/managed/runtime/lib"
    assert "DASHSCOPE_API_KEY" not in environment


def test_runner_rejects_an_unknown_runtime_profile(monkeypatch):
    runner = load_runner()
    monkeypatch.setenv("CS0502_RUNTIME", "unknown")
    with pytest.raises(ValueError, match="未知运行环境"):
        runner.memory_settings()


def test_progress_requires_consent_and_schedules_mastery(tmp_path, monkeypatch):
    progress = load_progress()
    progress_path = tmp_path / "student-work" / "progress.json"
    card_root = tmp_path / "cards"
    lab_root = tmp_path / "labs"
    card_root.mkdir()
    lab_root.mkdir()
    (card_root / "graph.md").write_text("# Graph\n", encoding="utf-8")
    (lab_root / "lab-01-demo").mkdir()
    monkeypatch.setattr(progress, "PROGRESS_PATH", progress_path)
    monkeypatch.setattr(progress, "CARD_ROOT", card_root)
    monkeypatch.setattr(progress, "LAB_ROOT", lab_root)

    with pytest.raises(ValueError, match="先运行"):
        progress.load_progress()
    with pytest.raises(ValueError, match="格式"):
        progress.require_card("../graph")
    with pytest.raises(ValueError, match="格式"):
        progress.require_lab("../lab-01-demo")
    assert not progress_path.exists()

    start = datetime(2026, 8, 22, tzinfo=timezone.utc)
    data = progress.initialize(start)
    first = progress.record_card(data, "graph", "correct", 0, 4, True, [], start)
    assert first["status"] == "review"
    assert first["next_review_at"] == progress.isoformat(start + timedelta(days=7))
    second = progress.record_card(data, "graph", "correct", 0, 5, True, [], start + timedelta(days=7))
    assert second["status"] == "mastered"
    assert second["next_review_at"] == progress.isoformat(start + timedelta(days=28))
    progress.record_lab(data, "lab-01-demo", "tests-passing")
    progress.save_progress(data)
    saved = json.loads(progress_path.read_text(encoding="utf-8"))
    assert saved["schema_version"] == 2
    assert saved["consent"]["local_learning_record"] is True
    assert saved["labs"]["lab-01-demo"] == "tests-passing"


def test_progress_migrates_v1_only_after_init_consent(tmp_path, monkeypatch):
    progress = load_progress()
    progress_path = tmp_path / "progress.json"
    monkeypatch.setattr(progress, "PROGRESS_PATH", progress_path)
    progress_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "current_card": "graph",
                "cards": {"graph": {"status": "review", "attempts": 1, "hint_count": 0}},
                "labs": {},
            }
        ),
        encoding="utf-8",
    )
    migrated = progress.initialize(datetime(2026, 8, 22, tzinfo=timezone.utc))
    assert migrated["schema_version"] == 2
    assert migrated["consent"]["local_learning_record"] is True
    assert migrated["cards"]["graph"]["next_review_at"] is None


def test_all_card_ids_and_legacy_filenames_resolve_to_stable_ids():
    progress = load_progress()
    aliases = progress.card_aliases()
    card_paths = sorted(path for path in (ROOT / "docs" / "cards").glob("*.md") if path.name != "README.md")

    assert len(card_paths) == 46
    for path in card_paths:
        stable_id = aliases[path.stem]
        assert progress.resolve_card_id(path.stem) == stable_id
        assert progress.resolve_card_id(stable_id) == stable_id

    assert aliases["ext-complexity"] == "algorithm-complexity"
    assert aliases["ext-logic-boolean"] == "boolean-logic"
    assert aliases["ext-recursion-divide-conquer"] == "recursion-divide-conquer"
    assert aliases["ext-scientific-computing"] == "scientific-computing"
    assert aliases["ext-search-hashing"] == "search-hashing"
    assert aliases["ext-web-technologies"] == "web-technologies"


def test_v2_progress_merges_legacy_and_stable_card_ids(tmp_path, monkeypatch):
    progress = load_progress()
    progress_path = tmp_path / "progress.json"
    card_root = tmp_path / "cards"
    card_root.mkdir()
    (card_root / "ext-complexity.md").write_text(
        "---\ncard_id: algorithm-complexity\n---\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(progress, "PROGRESS_PATH", progress_path)
    monkeypatch.setattr(progress, "CARD_ROOT", card_root)
    progress_path.write_text(
        json.dumps(
            {
                "schema_version": 2,
                "consent": {"local_learning_record": True, "recorded_at": "2026-08-01T00:00:00Z"},
                "current_card": "ext-complexity",
                "cards": {
                    "ext-complexity": {
                        "status": "learning",
                        "attempts": 2,
                        "hint_count": 1,
                        "confidence": 2,
                        "error_tags": ["增长阶"],
                        "last_reviewed": "2026-08-02T00:00:00Z",
                        "next_review_at": "2026-08-03T00:00:00Z",
                        "unhinted_successes": 0,
                    },
                    "algorithm-complexity": {
                        "status": "review",
                        "attempts": 1,
                        "hint_count": 0,
                        "confidence": 4,
                        "error_tags": ["边界"],
                        "last_reviewed": "2026-08-04T00:00:00Z",
                        "next_review_at": "2026-08-11T00:00:00Z",
                        "unhinted_successes": 1,
                    },
                },
                "labs": {},
            }
        ),
        encoding="utf-8",
    )

    data = progress.load_progress()
    assert data["current_card"] == "algorithm-complexity"
    assert set(data["cards"]) == {"algorithm-complexity"}
    merged = data["cards"]["algorithm-complexity"]
    assert merged["attempts"] == 3
    assert merged["hint_count"] == 1
    assert merged["error_tags"] == ["增长阶", "边界"]
    assert merged["status"] == "review"
    assert merged["confidence"] == 4

    progress.record_card(
        data,
        "ext-complexity",
        "correct",
        0,
        5,
        True,
        [],
        datetime(2026, 8, 11, tzinfo=timezone.utc),
    )
    progress.save_progress(data)
    saved = json.loads(progress_path.read_text(encoding="utf-8"))
    assert set(saved["cards"]) == {"algorithm-complexity"}
    assert saved["current_card"] == "algorithm-complexity"

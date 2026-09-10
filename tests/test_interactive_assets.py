import ast
import json
from pathlib import Path
import re
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]
VISUALIZATIONS = ROOT / "code" / "visualizations"


def quickstart_cell(cell_id):
    notebook_path = ROOT / "notebooks" / "modelscope" / "CS0502-quickstart.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    return "".join(next(cell for cell in notebook["cells"] if cell.get("id") == cell_id)["source"])


def write_course_package(root):
    for relative_path in ("README.md", "code/runner.py", "code/requirements.txt"):
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("test\n", encoding="utf-8")
    (root / "tests").mkdir(parents=True, exist_ok=True)


def execute_clone_update(course_root, monkeypatch, git_path=None, clone_package=False):
    calls = []

    def fake_run(command, **kwargs):
        calls.append(command)
        if clone_package and command[:2] == ["git", "clone"]:
            write_course_package(Path(command[-1]))

    monkeypatch.setattr(shutil, "which", lambda command: git_path if command == "git" else None)
    monkeypatch.setattr(subprocess, "run", fake_run)
    namespace = {
        "COURSE_ROOT": course_root,
        "REPO_URL": "https://example.invalid/course.git",
        "shutil": shutil,
        "subprocess": subprocess,
    }
    exec(compile(quickstart_cell("clone-update"), "<clone-update>", "exec"), namespace)
    return calls


def test_html_visualizations_are_self_contained_and_prediction_first():
    html_files = sorted(VISUALIZATIONS.glob("*.html"))
    assert len(html_files) == 5
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        assert "先预测" in text, path
        assert "aria-live" in text or "aria-label" in text, path
        assert not re.search(r"<(script|link)[^>]+(?:src|href)=['\"]https?://", text), path


def test_each_visualization_contains_parseable_script_block():
    for path in sorted(VISUALIZATIONS.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, flags=re.DOTALL | re.IGNORECASE)
        assert scripts, path
        assert all(script.strip() for script in scripts), path


def test_modelscope_quickstart_is_valid_and_contains_the_course_entrypoints():
    notebook_path = ROOT / "notebooks" / "modelscope" / "CS0502-quickstart.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    code = "\n".join(
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    )
    ast.parse(code, filename=str(notebook_path))
    for entrypoint in (
        "run_example",
        "init_lab",
        "test_lab",
        "show_visualization",
        "show_svg",
        "run_smoke_tests",
        "export_student_work",
    ):
        assert f"def {entrypoint}(" in code
    assert "/mnt/workspace" in code
    assert 'CS0502_RUNTIME"] = "modelscope"' in code
    assert "DASHSCOPE_API_KEY" not in code
    assert "API Key" not in code


def test_modelscope_quickstart_updates_git_checkout(tmp_path, monkeypatch):
    course_root = tmp_path / "CS0502"
    write_course_package(course_root)
    (course_root / ".git").mkdir()

    calls = execute_clone_update(course_root, monkeypatch, git_path="/usr/bin/git")

    assert calls == [["git", "pull", "--ff-only"]]


def test_modelscope_quickstart_accepts_zip_without_git(tmp_path, monkeypatch):
    course_root = tmp_path / "CS0502"
    write_course_package(course_root)

    assert execute_clone_update(course_root, monkeypatch, git_path=None) == []


def test_modelscope_quickstart_clones_into_empty_directory(tmp_path, monkeypatch):
    course_root = tmp_path / "CS0502"
    course_root.mkdir()

    calls = execute_clone_update(course_root, monkeypatch, git_path="/usr/bin/git", clone_package=True)

    assert calls[0][:3] == ["git", "clone", "--depth"]


def test_modelscope_quickstart_rejects_empty_directory_without_git(tmp_path, monkeypatch):
    course_root = tmp_path / "CS0502"
    course_root.mkdir()

    with pytest.raises(RuntimeError, match="上传课程组 ZIP"):
        execute_clone_update(course_root, monkeypatch, git_path=None)


def test_modelscope_quickstart_rejects_incomplete_zip(tmp_path, monkeypatch):
    course_root = tmp_path / "CS0502"
    course_root.mkdir()
    (course_root / "README.md").write_text("incomplete\n", encoding="utf-8")

    with pytest.raises(RuntimeError, match="不是完整课程包"):
        execute_clone_update(course_root, monkeypatch, git_path=None)

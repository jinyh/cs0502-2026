import ast
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
VISUALIZATIONS = ROOT / "code" / "visualizations"


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

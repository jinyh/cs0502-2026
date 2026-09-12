"""无人船实验的静态交付、Python 结果与共享状态模型检查。"""
import json
from pathlib import Path
import re
import runpy
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "code" / "visualizations" / "usv-inspection"


def test_usv_python_examples():
    namespace = runpy.run_path(str(LAB / "verify_count.py"))
    assert len(namespace["verify"]()) == 5
    assert namespace["count_alerts"]([], 80) == 0


def test_usv_local_assets_and_mkdocs_entry():
    html = (LAB / "index.html").read_text()
    assert "先预测" in html
    assert "aria-live" in html
    assert not re.search(r'<(?:script|link)[^>]+(?:src|href)="https?://', html)
    for asset in re.findall(r'(?:src|href)="(\./[^"#]+)"', html):
        assert (LAB / asset).is_file(), asset
    assert (ROOT / "website/src/code").resolve() == ROOT / "code"
    assert "code/visualizations/usv-inspection/GUIDE.md" in (ROOT / "website/mkdocs.yml").read_text()
    # README.md would also produce index.html under MkDocs; keep the standalone entry intact.
    assert not (LAB / "README.md").exists()
    versions = json.loads((LAB / "vendor/versions.json").read_text())
    assert versions["three"] == "0.180.0"


def test_usv_state_model_with_node():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node.js required for USV JavaScript state model tests")
    result = subprocess.run([node, "--test", str(LAB / "model.test.mjs")], capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stdout + result.stderr


def test_usv_course_theme_and_homepage_entry():
    course_css = (ROOT / "website/src/assets/stylesheets/extra.css").read_text()
    lab_css = (LAB / "style.css").read_text()
    for token in ("sjtu-blue", "sjtu-blue-deep", "sjtu-blue-soft"):
        pattern = rf"--{token}:\s*(#[0-9a-fA-F]+)"
        assert re.search(pattern, course_css)[1] == re.search(pattern, lab_css)[1]
    assert 'href="code/visualizations/usv-inspection/index.html"' in (ROOT / "README.md").read_text()

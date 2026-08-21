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

import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ALL_CARDS = sorted(path for path in (ROOT / "docs" / "cards").glob("*.md") if path.name != "README.md")
LEGACY_ANCHOR_CARDS = sorted(path for path in ALL_CARDS if re.match(r"^\d{2}-", path.name))
REQUIRED_FIELDS = {
    "title",
    "lecture",
    "thinking_pillar",
    "category",
    "tags",
    "status",
    "version",
    "importance",
    "learning_objectives",
    "prerequisites",
    "estimated_minutes",
    "assessment_tags",
    "labs",
    "figures",
    "last_reviewed",
}


def frontmatter_fields(text):
    assert text.startswith("---\n")
    frontmatter = text.split("---\n", 2)[1]
    return {
        match.group(1)
        for line in frontmatter.splitlines()
        if (match := re.match(r"^([a-z_]+):", line))
    }


def test_all_concept_cards_are_reviewable_and_stay_lightweight():
    assert ALL_CARDS
    for card in ALL_CARDS:
        text = card.read_text(encoding="utf-8")
        assert {"title", "status", "tags"} <= frontmatter_fields(text), card
        assert "status: needs-review" in text, card
        assert len(text.splitlines()) <= 300, card
        assert "## 一句话定位" in text, card


def test_legacy_anchor_cards_keep_their_migration_schema():
    assert LEGACY_ANCHOR_CARDS
    for card in LEGACY_ANCHOR_CARDS:
        text = card.read_text(encoding="utf-8")
        assert REQUIRED_FIELDS <= frontmatter_fields(text), card
        assert "## 学完应能做到" in text, card
        assert "## 主动学习与考核迁移" in text, card
        if not card.name.startswith("01-"):
            assert "## 常见误区与边界" in text, card


def test_curriculum_blueprint_has_21_observable_lectures():
    blueprint = (ROOT / "docs" / "curriculum" / "21-lecture-blueprint.md").read_text(encoding="utf-8")
    lecture_matches = list(re.finditer(r"^### L(\d{2}) .+$", blueprint, re.MULTILINE))
    assert [match.group(1) for match in lecture_matches] == [f"{number:02d}" for number in range(1, 22)]

    for index, match in enumerate(lecture_matches):
        end = lecture_matches[index + 1].start() if index + 1 < len(lecture_matches) else len(blueprint)
        section = blueprint[match.end():end]
        assert "**学完应能做到**" in section, match.group(0)
        assert "**工程场景**" in section, match.group(0)
        assert "**主动任务**" in section, match.group(0)
        assert "**跨章迁移**" in section, match.group(0)
        objectives = re.findall(r"^\d+\. ", section.split("**工程场景**", 1)[0], re.MULTILINE)
        assert len(objectives) == 3, match.group(0)


def test_local_markdown_links_resolve():
    excluded = {"reference", ".venv", "node_modules", ".git", ".pytest_cache"}
    markdown_files = [path for path in ROOT.rglob("*.md") if not excluded & set(path.parts)]
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    failures = []
    for source in markdown_files:
        for raw_target in link_pattern.findall(source.read_text(encoding="utf-8")):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            target = target.strip("<>")
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"{source.relative_to(ROOT)} -> {raw_target}")
    assert not failures, "\n".join(failures)


def test_svg_assets_are_accessible_and_self_contained():
    svgs = sorted((ROOT / "figures").glob("*.svg"))
    assert len(svgs) == 19
    for svg in svgs:
        root = ET.parse(svg).getroot()
        children = [child.tag.rsplit("}", 1)[-1] for child in root]
        assert "title" in children, svg
        assert "desc" in children, svg
        text = svg.read_text(encoding="utf-8")
        assert not re.search(r"(?:href|src)=['\"]https?://", text), svg


def test_assessment_files_are_explicitly_unapproved_and_schema_is_valid():
    blueprint = (ROOT / "docs" / "assessment" / "blueprint.yaml").read_text(encoding="utf-8")
    assert re.search(r"^status:\s*template\s*$", blueprint, re.MULTILINE)
    json.loads((ROOT / "docs" / "assessment" / "progress.schema.json").read_text(encoding="utf-8"))


def test_no_plaintext_provider_credentials_in_tracked_course_files():
    candidates = (
        list((ROOT / ".opencode" / "agents").rglob("*.md"))
        + list((ROOT / ".opencode" / "commands").rglob("*.md"))
        + list((ROOT / ".opencode" / "skills").rglob("*.md"))
        + list((ROOT / "opencode").rglob("*.md"))
        + [ROOT / "opencode.json"]
    )
    suspicious = re.compile(r"(?i)(api[_-]?key|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}")
    hits = []
    for path in candidates:
        if path.is_file() and suspicious.search(path.read_text(encoding="utf-8")):
            hits.append(path.relative_to(ROOT))
    assert not hits, hits


def test_opencode_learning_surface_is_complete_and_index_first():
    assert len(list((ROOT / ".opencode" / "commands").glob("*.md"))) == 8
    skills = sorted((ROOT / ".opencode" / "skills").glob("*/SKILL.md"))
    assert len(skills) == 5
    assessment_skill = (ROOT / ".opencode" / "skills" / "assessment-practice" / "SKILL.md").read_text(encoding="utf-8")
    assert "先读取 `opencode/knowledge.md`" in assessment_skill
    assert "不得根据编号猜测文件名" in assessment_skill

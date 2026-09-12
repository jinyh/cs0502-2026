import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ALL_CARDS = sorted(path for path in (ROOT / "docs" / "cards").glob("*.md") if path.name != "README.md")
LEGACY_ANCHOR_CARDS = sorted(path for path in ALL_CARDS if re.match(r"^\d{2}-", path.name))
SEMANTIC_CARDS = sorted(set(ALL_CARDS) - set(LEGACY_ANCHOR_CARDS))
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
SEMANTIC_REQUIRED_FIELDS = {
    "title",
    "card_id",
    "lecture_refs",
    "source_slides",
    "thinking_pillars",
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
    "related_cards",
    "related_deep",
    "related_visualizations",
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


def inline_list(text, field):
    frontmatter = text.split("---\n", 2)[1]
    match = re.search(rf"^{field}:\s*\[(.*)\]\s*$", frontmatter, re.MULTILINE)
    assert match, field
    return [item.strip() for item in match.group(1).split(",") if item.strip()]


def test_all_concept_cards_are_reviewable_and_stay_lightweight():
    assert ALL_CARDS
    for card in ALL_CARDS:
        text = card.read_text(encoding="utf-8")
        assert {"title", "status", "tags"} <= frontmatter_fields(text), card
        assert re.search(r"^status: (needs-review|ai-reviewed|stable)$", text, re.MULTILINE), card
        assert len(text.splitlines()) <= 300, card
        assert "## 一句话定位" in text, card


def test_stable_cards_require_a_traceable_human_review():
    for card in ALL_CARDS:
        text = card.read_text(encoding="utf-8")
        if re.search(r"^status: stable$", text, re.MULTILINE):
            fields = frontmatter_fields(text)
            assert {"human_reviewer", "human_reviewed_at", "human_review_scope"} <= fields, card

    for frontier in (ROOT / "docs" / "frontier").glob("*-frontier.md"):
        text = frontier.read_text(encoding="utf-8")
        review_status = re.search(r"^review_status: (needs-human-approval|approved)$", text, re.MULTILINE)
        assert review_status, frontier
        if review_status.group(1) == "approved":
            fields = frontmatter_fields(text)
            assert {"human_reviewer", "human_reviewed_at", "human_review_scope"} <= fields, frontier


def test_completed_ai_audit_is_traceable_without_claiming_human_approval():
    report = ROOT / "docs" / "review" / "ai-audit-2026-08-22.md"
    assert report.is_file()
    report_text = report.read_text(encoding="utf-8")
    assert "46 张概念卡" in report_text
    assert "3 篇深度专题" in report_text
    for card in ALL_CARDS:
        text = card.read_text(encoding="utf-8")
        assert re.search(r"^status: (ai-reviewed|stable)$", text, re.MULTILINE), card
    for deep in (ROOT / "docs" / "deep").glob("*.md"):
        if deep.name == "README.md":
            continue
        assert re.search(r"^status: (ai-reviewed|stable)$", deep.read_text(encoding="utf-8"), re.MULTILINE), deep


def test_legacy_anchor_cards_keep_their_migration_schema():
    assert LEGACY_ANCHOR_CARDS
    for card in LEGACY_ANCHOR_CARDS:
        text = card.read_text(encoding="utf-8")
        assert REQUIRED_FIELDS <= frontmatter_fields(text), card
        assert "## 学完应能做到" in text, card
        assert "## 主动学习与考核迁移" in text, card
        if not card.name.startswith("01-"):
            assert "## 常见误区与边界" in text, card


def test_semantic_cards_use_many_to_many_schema_and_active_learning_sections():
    assert len(SEMANTIC_CARDS) >= 25
    card_ids = []
    for card in SEMANTIC_CARDS:
        text = card.read_text(encoding="utf-8")
        assert SEMANTIC_REQUIRED_FIELDS <= frontmatter_fields(text), card
        assert inline_list(text, "lecture_refs"), card
        assert "## 学完应能做到" in text, card
        assert "## 常见误区与边界" in text, card
        assert "## 主动学习" in text, card
        objectives = re.findall(
            r"^\d+\. ",
            text.split("## 学完应能做到", 1)[1].split("\n## ", 1)[0],
            re.MULTILINE,
        )
        assert len(objectives) == 3, card
        card_id_match = re.search(r"^card_id:\s*(.+)$", text, re.MULTILINE)
        assert card_id_match, card
        card_ids.append(card_id_match.group(1).strip())

    assert len(card_ids) == len(set(card_ids))


def test_card_relationships_and_declared_figures_resolve():
    card_stems = {card.stem for card in ALL_CARDS}
    for card in ALL_CARDS:
        text = card.read_text(encoding="utf-8")
        for prerequisite in inline_list(text, "prerequisites"):
            assert prerequisite in card_stems, f"{card.name}: prerequisite {prerequisite}"
        for related in inline_list(text, "related_cards"):
            assert related in card_stems, f"{card.name}: {related}"
        for figure in inline_list(text, "figures"):
            assert (ROOT / "figures" / figure).is_file(), f"{card.name}: {figure}"


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


def test_lecture_card_map_covers_21_lectures_and_resolves_resources():
    mapping = (ROOT / "docs" / "curriculum" / "lecture-card-map.yaml").read_text(encoding="utf-8")
    lecture_matches = list(re.finditer(r"^  - id: (L\d{2})$", mapping, re.MULTILINE))
    assert [match.group(1) for match in lecture_matches] == [f"L{number:02d}" for number in range(1, 22)]
    assert re.search(r"^schema_version:\s*3$", mapping, re.MULTILINE)
    assert re.search(r"^status:\s*proposal$", mapping, re.MULTILINE)

    card_stems = {card.stem for card in ALL_CARDS}
    for field, root, suffix in (
        ("core_cards", ROOT / "docs" / "cards", ".md"),
        ("supporting_cards", ROOT / "docs" / "cards", ".md"),
        ("preview_cards", ROOT / "docs" / "cards", ".md"),
        ("extension_cards", ROOT / "docs" / "cards", ".md"),
        ("examples", ROOT / "code" / "examples", ""),
        ("labs", ROOT / "code" / "labs", ""),
        ("visualizations", ROOT / "code" / "visualizations", ""),
        ("extension_visualizations", ROOT / "code" / "visualizations", ""),
        ("figures", ROOT / "figures", ""),
    ):
        for raw_items in re.findall(rf"^    {field}:\s*\[(.*)\]$", mapping, re.MULTILINE):
            for item in [value.strip() for value in raw_items.split(",") if value.strip()]:
                if field in {"core_cards", "supporting_cards", "preview_cards", "extension_cards"}:
                    assert item in card_stems, f"{field}: {item}"
                else:
                    assert (root / f"{item}{suffix}").exists(), f"{field}: {item}"

    learned_core = set()
    for index, match in enumerate(lecture_matches):
        end = lecture_matches[index + 1].start() if index + 1 < len(lecture_matches) else len(mapping)
        section = mapping[match.start():end]
        raw_core = re.search(r"^    core_cards:\s*\[(.*)\]$", section, re.MULTILINE)
        assert raw_core, match.group(1)
        ordered_core = [value.strip() for value in raw_core.group(1).split(",") if value.strip()]
        for card_index, card_id in enumerate(ordered_core):
            card_text = (ROOT / "docs" / "cards" / f"{card_id}.md").read_text(encoding="utf-8")
            available = learned_core | set(ordered_core[:card_index])
            missing = set(inline_list(card_text, "prerequisites")) - available
            assert not missing, f"{match.group(1)} {card_id}: core prerequisites not taught: {sorted(missing)}"
        learned_core.update(ordered_core)


def test_runtime_index_matches_the_curriculum_mapping():
    mapping = (ROOT / "docs" / "curriculum" / "lecture-card-map.yaml").read_text(encoding="utf-8")
    status = re.search(r"^status:\s*(\S+)$", mapping, re.MULTILINE).group(1)
    lecture_matches = list(re.finditer(r"^  - id: (L\d{2})$", mapping, re.MULTILINE))
    indexed = [
        json.loads(line)
        for line in (ROOT / "opencode" / "lecture-runtime-index.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert [item["id"] for item in indexed] == [match.group(1) for match in lecture_matches]

    list_fields = (
        "core_cards",
        "supporting_cards",
        "examples",
        "labs",
        "visualizations",
        "extension_visualizations",
        "figures",
    )
    for index, match in enumerate(lecture_matches):
        end = lecture_matches[index + 1].start() if index + 1 < len(lecture_matches) else len(mapping)
        section = mapping[match.start():end]
        item = indexed[index]
        assert item["mapping_status"] == status
        assert item["title"] == re.search(r"^    title:\s*(.+)$", section, re.MULTILINE).group(1)
        for field in list_fields:
            raw = re.search(rf"^    {field}:\s*\[(.*)\]$", section, re.MULTILINE)
            expected = [value.strip() for value in raw.group(1).split(",") if value.strip()] if raw else []
            assert item[field] == expected, f"{item['id']} {field}"


def test_lab_catalog_is_formative_and_covers_every_lab():
    catalog = json.loads((ROOT / "code" / "labs" / "catalog.json").read_text(encoding="utf-8"))
    assert catalog["schema_version"] == 1
    assert catalog["default_role"] == "formative"
    assert catalog["graded_only_when"] == "explicitly-designated-by-course-staff"

    lab_directories = sorted(path.name for path in (ROOT / "code" / "labs").glob("lab-*") if path.is_dir())
    catalog_ids = [item["id"] for item in catalog["labs"]]
    assert catalog_ids == lab_directories

    mapping = (ROOT / "docs" / "curriculum" / "lecture-card-map.yaml").read_text(encoding="utf-8")
    mapped_labs = set(re.findall(r"lab-\d{2}-[a-z0-9-]+", mapping))
    assert set(catalog_ids) == mapped_labs
    for item in catalog["labs"]:
        assert item["role"] == "formative"
        assert item["lecture_refs"]
        assert isinstance(item["assignment_links"], list)
        for link in item["assignment_links"]:
            assert set(link) == {"assignment", "usage", "note"}
            assert re.fullmatch(r"HW\d+", link["assignment"])

    assignment_plan = (ROOT / "docs" / "assessment" / "assignment-plan.md").read_text(encoding="utf-8")
    assert "3 次正式计分作业" in assignment_plan
    assert "不按周布置" in assignment_plan
    assert "assignment_links" in assignment_plan


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


def test_public_site_separates_course_information_from_optional_extension():
    config = (ROOT / "website" / "mkdocs.yml").read_text(encoding="utf-8")
    home = (ROOT / "README.md").read_text(encoding="utf-8")
    extension = (ROOT / "docs" / "extension" / "README.md").read_text(encoding="utf-8")
    schedule = (ROOT / "docs" / "course" / "schedule.md").read_text(encoding="utf-8")

    nav_block = config.split("nav:\n", 1)[1].split("\nplugins:\n", 1)[0]
    top_level_nav = re.findall(r"^  - ([^:]+):", nav_block, re.MULTILINE)
    assert top_level_nav == ["首页", "课程说明", "拓展学习（可选）"]
    assert "## 两个模块" not in home
    assert home.index("<h2>课程说明</h2>") < home.index("<h2>拓展学习</h2>")
    assert '<span class="module-badge module-badge-optional">可选</span>' in home
    assert "默认不构成课程必做内容" in extension
    for path_name in ("阅读补充", "动手验证", "OpenCode 助学"):
        assert f"<h2>{path_name}</h2>" in extension

    override = (ROOT / "website" / "overrides" / "main.html").read_text(encoding="utf-8")
    assert "返回课程首页" in override
    assert 'href="{{ config.site_url }}"' in override

    schedule_rows = re.findall(r"^\| \d+ \| \d{2}-\d{2} 周[一四] \|", schedule, re.MULTILINE)
    assert len(schedule_rows) == 22

    for hidden_path in (
        "docs/assessment/**",
        "docs/review/**",
        "docs/project-status.md",
        "docs/curriculum/legacy-coverage-matrix.md",
        "opencode/AGENTS.md",
        "opencode/knowledge.md",
        "opencode/sandbox-policy.md",
    ):
        assert f"  {hidden_path}\n" in config


def test_svg_assets_are_accessible_and_self_contained():
    svgs = sorted((ROOT / "figures").glob("*.svg"))
    assert len(svgs) >= 30
    for svg in svgs:
        root = ET.parse(svg).getroot()
        children = [child.tag.rsplit("}", 1)[-1] for child in root]
        assert "title" in children, svg
        assert "desc" in children, svg
        text = svg.read_text(encoding="utf-8")
        assert not re.search(r"(?:href|src)=['\"]https?://", text), svg


def test_assessment_files_are_explicitly_unapproved_and_schema_is_valid():
    blueprint = (ROOT / "docs" / "assessment" / "blueprint.yaml").read_text(encoding="utf-8")
    assert re.search(r"^schema_version:\s*3$", blueprint, re.MULTILINE)
    status = re.search(r"^status:\s*(\S+)\s*$", blueprint, re.MULTILINE)
    assert status
    assert status.group(1) in {"template", "approved"}
    if status.group(1) == "approved":
        assert not re.search(r":\s*(?:null|TBD)\s*$", blueprint, re.MULTILINE)
    grading_weights = [
        int(re.search(rf"^  {field}:\s*(\d+)$", blueprint, re.MULTILINE).group(1))
        for field in ("final_exam_percent", "group_project_percent", "coursework_percent")
    ]
    assert grading_weights == [40, 20, 40]
    coursework_weights = [
        int(re.search(rf"^    {field}:\s*(\d+)$", blueprint, re.MULTILINE).group(1))
        for field in ("assignments_percent", "class_participation_percent")
    ]
    assert coursework_weights == [30, 10]
    assert sum(coursework_weights) == grading_weights[2]
    assert re.search(r"^  assignment_count:\s*3$", blueprint, re.MULTILINE)
    contact_hours = [
        int(re.search(rf"^  {field}:\s*(\d+)$", blueprint, re.MULTILINE).group(1))
        for field in ("lecture_topics", "project_presentation_and_defense", "integrative_review")
    ]
    assert sum(contact_hours) == 48
    assert re.search(r"^  paper_materials_during_exam:\s*true$", blueprint, re.MULTILINE)
    for forbidden in ("opencode_during_exam", "other_llm_during_exam", "network_during_exam", "electronic_materials_during_exam"):
        assert re.search(rf"^  {forbidden}:\s*false$", blueprint, re.MULTILINE)
    progress_schema = json.loads((ROOT / "docs" / "assessment" / "progress.schema.json").read_text(encoding="utf-8"))
    assert progress_schema["properties"]["schema_version"]["const"] == 2


def test_student_guide_covers_commands_and_code_catalog():
    commands = {path.stem for path in (ROOT / ".opencode" / "commands").glob("*.md")}
    guide = (ROOT / "docs" / "student-guide.md").read_text(encoding="utf-8")
    for command in commands:
        assert f"`/{command}" in guide, command

    examples = {path.name for path in (ROOT / "code" / "examples").glob("*.py")}
    code_readme = (ROOT / "code" / "README.md").read_text(encoding="utf-8")
    assert len(examples) == 18
    for example in examples:
        assert f"`{example}`" in code_readme, example

    assert len(list((ROOT / "code" / "labs").glob("lab-*"))) == 8
    assert len(list((ROOT / "code" / "visualizations").glob("*.html"))) == 5


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


def test_lecture_notes_publish_only_the_inventory_readme():
    readme = ROOT / "LectureNotes" / "README.md"
    assert readme.is_file()
    text = readme.read_text(encoding="utf-8")
    for number in range(1, 22):
        assert f"Slide{number:02d}" in text

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "LectureNotes/*" in gitignore
    assert "!LectureNotes/README.md" in gitignore

    if (ROOT / ".git").is_dir():
        ignored_pdf = subprocess.run(
            ["git", "check-ignore", "LectureNotes/Slide01-Welcome-2025.pdf"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        public_readme = subprocess.run(
            ["git", "check-ignore", "LectureNotes/README.md"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        tracked_pdfs = subprocess.run(
            ["git", "ls-files", "LectureNotes/*.pdf"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        assert ignored_pdf.returncode == 0
        assert public_readme.returncode == 1
        assert not tracked_pdfs.stdout.strip()
    else:
        assert not list((ROOT / "LectureNotes").glob("*.pdf"))


def test_opencode_learning_surface_is_complete_and_index_first():
    commands = {path.stem for path in (ROOT / ".opencode" / "commands").glob("*.md")}
    assert commands == {
        "start",
        "learn",
        "demo",
        "practice",
        "lab",
        "review",
        "mock",
        "project",
        "exam-notes",
        "frontier",
    }
    skills = sorted((ROOT / ".opencode" / "skills").glob("*/SKILL.md"))
    assert len(skills) == 5
    for skill in skills:
        text = skill.read_text(encoding="utf-8")
        name = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
        description = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
        assert name and name.group(1).strip() == skill.parent.name, skill
        assert description and description.group(1).strip(), skill

    assessment_skill = (ROOT / ".opencode" / "skills" / "assessment-practice" / "SKILL.md").read_text(encoding="utf-8")
    assert "先读取 `opencode/knowledge.md`" in assessment_skill
    assert "docs/curriculum/lecture-card-map.yaml" in assessment_skill
    for question_type in ("概念比较", "状态追踪", "代码调试", "工程迁移"):
        assert question_type in assessment_skill
    for skill_name in ("guided-learning", "code-lab-coach", "retrieval-review"):
        text = (ROOT / ".opencode" / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
        assert "docs/curriculum/lecture-card-map.yaml" in text, skill_name
    code_skill = (ROOT / ".opencode" / "skills" / "code-lab-coach" / "SKILL.md").read_text(encoding="utf-8")
    assert "opencode/lecture-runtime-index.jsonl" in code_skill
    assert "[CS0502_RESULT]" in code_skill


def test_opencode_defaults_to_deny_and_does_not_vendor_global_skills():
    config = json.loads((ROOT / "opencode.json").read_text(encoding="utf-8"))
    assert config["permission"]["*"] == "deny"
    agent = (ROOT / ".opencode" / "agents" / "course-tutor.md").read_text(encoding="utf-8")
    assert '  "*": deny' in agent
    assert '"uv run python code/runner.py *": allow' not in agent
    assert '"uv run --no-project python code/progress.py *": allow' in agent
    assert "本机 OpenCode 不执行课程 Python" in agent
    assert agent.index('  "*": deny') < agent.index("  read:")

    assert not (ROOT / ".agents" / "skills").exists()
    assert not (ROOT / ".claude" / "skills").exists()
    for skill_path in (ROOT / ".opencode" / "skills").rglob("*"):
        assert not skill_path.is_symlink(), skill_path

    forbidden_reference = re.compile(r"(?:/Users/[^/]+|~)/(?:\.agents|\.codex|\.config/opencode)/skills")
    excluded = {"reference", "LectureNotes", ".git", ".venv", "node_modules", ".pytest_cache"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or excluded & set(path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        assert not forbidden_reference.search(text), path

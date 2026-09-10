"""CS0502 本地学习进度工具。

只记录卡片掌握状态、提示次数和错因标签，不记录身份、成绩或原始作答。
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PROGRESS_PATH = ROOT / "student-work" / "progress.json"
CARD_ROOT = ROOT / "docs" / "cards"
LAB_ROOT = ROOT / "code" / "labs"
LAB_STATUSES = ("not-started", "in-progress", "tests-passing", "explained")
CARD_ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0)


def isoformat(value: datetime):
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def empty_progress(now: datetime):
    return {
        "schema_version": 2,
        "consent": {
            "local_learning_record": True,
            "recorded_at": isoformat(now),
        },
        "current_card": None,
        "cards": {},
        "labs": {},
    }


def migrate_v1(data, now: datetime):
    if data.get("schema_version") != 1:
        return data
    migrated = {
        **data,
        "schema_version": 2,
        "consent": {
            "local_learning_record": True,
            "recorded_at": isoformat(now),
        },
    }
    for card in migrated.get("cards", {}).values():
        card.setdefault("confidence", None)
        card.setdefault("error_tags", [])
        card.setdefault("last_reviewed", None)
        card.setdefault("next_review_at", None)
        card.setdefault("unhinted_successes", 0)
    return migrated


def card_aliases():
    aliases = {}
    for path in sorted(CARD_ROOT.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^card_id:\s*([^\s#]+)", text, flags=re.MULTILINE)
        stable_id = match.group(1) if match else path.stem
        if not CARD_ID_PATTERN.fullmatch(stable_id):
            raise ValueError(f"卡片 {path.name} 的 card_id 格式无效")
        for alias in (path.stem, stable_id):
            previous = aliases.get(alias)
            if previous is not None and previous != stable_id:
                raise ValueError(f"卡片标识冲突: {alias}")
            aliases[alias] = stable_id
    return aliases


def resolve_card_id(card_id: str):
    if not CARD_ID_PATTERN.fullmatch(card_id):
        raise ValueError("卡片编号格式无效")
    stable_id = card_aliases().get(card_id)
    if stable_id is None:
        raise ValueError(f"不存在的卡片: {card_id}")
    return stable_id


def _review_sort_key(card):
    reviewed = card.get("last_reviewed")
    if not reviewed:
        return datetime.min.replace(tzinfo=timezone.utc)
    try:
        parsed = datetime.fromisoformat(reviewed.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None else parsed.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return datetime.min.replace(tzinfo=timezone.utc)


def _merge_card_records(older, newer):
    latest = max((older, newer), key=_review_sort_key)
    merged = dict(latest)
    merged["attempts"] = older.get("attempts", 0) + newer.get("attempts", 0)
    merged["hint_count"] = older.get("hint_count", 0) + newer.get("hint_count", 0)
    merged["error_tags"] = sorted(set(older.get("error_tags", [])) | set(newer.get("error_tags", [])))
    return merged


def normalize_card_ids(data):
    aliases = card_aliases()
    normalized = {}
    for card_id, card in data.get("cards", {}).items():
        stable_id = aliases.get(card_id, card_id)
        card.setdefault("confidence", None)
        card.setdefault("error_tags", [])
        card.setdefault("last_reviewed", None)
        card.setdefault("next_review_at", None)
        card.setdefault("unhinted_successes", 0)
        if stable_id in normalized:
            normalized[stable_id] = _merge_card_records(normalized[stable_id], card)
        else:
            normalized[stable_id] = card
    data["cards"] = normalized
    current = data.get("current_card")
    if current is not None:
        data["current_card"] = aliases.get(current, current)
    return data


def validate_progress(data):
    if data.get("schema_version") != 2:
        raise ValueError("不支持的进度文件版本，请先运行 init --consent")
    consent = data.get("consent", {})
    if consent.get("local_learning_record") is not True:
        raise ValueError("尚未同意本地学习记录")
    if not isinstance(data.get("cards"), dict) or not isinstance(data.get("labs"), dict):
        raise ValueError("进度文件结构无效")


def load_progress():
    if not PROGRESS_PATH.is_file():
        raise ValueError("进度文件不存在，请先运行 init --consent")
    try:
        data = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"进度文件不是有效 JSON: {error.msg}") from error
    validate_progress(data)
    return normalize_card_ids(data)


def save_progress(data):
    normalize_card_ids(data)
    validate_progress(data)
    PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=PROGRESS_PATH.parent,
        prefix="progress-",
        suffix=".tmp",
        delete=False,
    ) as temporary:
        json.dump(data, temporary, ensure_ascii=False, indent=2)
        temporary.write("\n")
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, PROGRESS_PATH)


def initialize(now: datetime):
    if not PROGRESS_PATH.exists():
        data = empty_progress(now)
    else:
        try:
            existing = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ValueError(f"进度文件不是有效 JSON: {error.msg}") from error
        data = migrate_v1(existing, now)
        normalize_card_ids(data)
        validate_progress(data)
    save_progress(data)
    return data


def require_card(card_id: str):
    return resolve_card_id(card_id)


def require_lab(lab_id: str):
    if not re.fullmatch(r"lab-\d{2}-[a-z0-9-]+", lab_id):
        raise ValueError("Lab 编号格式无效")
    if not (LAB_ROOT / lab_id).is_dir():
        raise ValueError(f"不存在的 Lab: {lab_id}")


def record_card(data, card_id, outcome, hints, confidence, explained, error_tags, now):
    card_id = require_card(card_id)
    if hints < 0:
        raise ValueError("提示次数不能为负数")

    cards = data["cards"]
    card = cards.setdefault(
        card_id,
        {
            "status": "new",
            "attempts": 0,
            "hint_count": 0,
            "confidence": None,
            "error_tags": [],
            "last_reviewed": None,
            "next_review_at": None,
            "unhinted_successes": 0,
        },
    )
    card["attempts"] += 1
    card["hint_count"] += hints
    card["confidence"] = confidence
    card["last_reviewed"] = isoformat(now)
    card["error_tags"] = sorted(set(card["error_tags"]) | set(error_tags))

    unhinted_transfer = outcome == "correct" and hints == 0 and explained
    if unhinted_transfer:
        card["unhinted_successes"] += 1
        if card["unhinted_successes"] >= 2:
            card["status"] = "mastered"
            interval_days = 21
        else:
            card["status"] = "review"
            interval_days = 7
    else:
        card["unhinted_successes"] = 0
        if outcome == "incorrect":
            card["status"] = "learning"
            interval_days = 1
        else:
            card["status"] = "review"
            interval_days = 3

    card["next_review_at"] = isoformat(now + timedelta(days=interval_days))
    data["current_card"] = card_id
    return card


def record_lab(data, lab_id, status):
    require_lab(lab_id)
    data["labs"][lab_id] = status


def due_cards(data, now: datetime):
    due = []
    for card_id, card in data["cards"].items():
        raw_due = card.get("next_review_at")
        is_due = raw_due is None
        if raw_due:
            parsed = datetime.fromisoformat(raw_due.replace("Z", "+00:00"))
            is_due = parsed <= now
        if is_due and card.get("status") != "new":
            due.append(
                {
                    "card_id": card_id,
                    "status": card["status"],
                    "confidence": card.get("confidence"),
                    "error_tags": card.get("error_tags", []),
                    "next_review_at": raw_due,
                }
            )
    return sorted(due, key=lambda item: (item["next_review_at"] or "", item["card_id"]))


def parser():
    root = argparse.ArgumentParser(description="管理匿名、本地的 CS0502 学习进度")
    commands = root.add_subparsers(dest="command", required=True)

    init_parser = commands.add_parser("init", help="在学生明确同意后初始化进度")
    init_parser.add_argument("--consent", action="store_true", required=True)

    card_parser = commands.add_parser("record-card", help="记录一次卡片迁移练习")
    card_parser.add_argument("card_id")
    card_parser.add_argument("--outcome", required=True, choices=("correct", "partial", "incorrect"))
    card_parser.add_argument("--hints", required=True, type=int)
    card_parser.add_argument("--confidence", required=True, type=int, choices=range(1, 6))
    card_parser.add_argument("--explained", action="store_true")
    card_parser.add_argument("--error-tag", action="append", default=[])

    lab_parser = commands.add_parser("record-lab", help="记录 Lab 学习阶段")
    lab_parser.add_argument("lab_id")
    lab_parser.add_argument("--status", required=True, choices=LAB_STATUSES)

    commands.add_parser("due", help="列出当前到期复习卡片")
    commands.add_parser("show", help="输出完整本地进度")
    return root


def main(argv=None):
    arguments = parser().parse_args(argv)
    now = utc_now()
    try:
        if arguments.command == "init":
            data = initialize(now)
            print("已启用匿名本地学习记录: student-work/progress.json")
            return 0

        data = load_progress()
        if arguments.command == "record-card":
            card = record_card(
                data,
                arguments.card_id,
                arguments.outcome,
                arguments.hints,
                arguments.confidence,
                arguments.explained,
                arguments.error_tag,
                now,
            )
            save_progress(data)
            print(json.dumps(card, ensure_ascii=False, indent=2))
        elif arguments.command == "record-lab":
            record_lab(data, arguments.lab_id, arguments.status)
            save_progress(data)
            print(f"已记录 {arguments.lab_id}: {arguments.status}")
        elif arguments.command == "due":
            print(json.dumps(due_cards(data, now), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2))
    except ValueError as error:
        print(f"进度操作被拒绝: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

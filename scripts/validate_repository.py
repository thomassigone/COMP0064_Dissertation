#!/usr/bin/env python3
"""Validate tracked JSON and repository-relative Markdown links.

Seven post-freeze ``result.json`` files are intentionally allowlisted. They are
immutable console captures containing literal multiline command output, so their
bytes are not standards-compliant JSON and must not be rewritten for this check.
Missing links into ignored ``.artifacts`` trees or omitted APKs are reported as
archival locators, separately from genuine broken tracked links.
"""

from __future__ import annotations

import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
RAW_JSON_CAPTURES = frozenset(
    {
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/benign-trial1/result.json",
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/benign-trial2/result.json",
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/benign-trial3/result.json",
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/benign-trial4/result.json",
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/secure-trial1/result.json",
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/secure-trial2/result.json",
        "android-vulnerability-agent/evaluation/evidence/post_freeze/ghera_broadcast_validity/run-002/step1-reproduction/secure-trial3/result.json",
    }
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\((?P<target><[^>]+>|[^\s)]+)")


def tracked_paths() -> set[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    ).decode("utf-8")
    return {path for path in output.split("\0") if path}


def validate_json(paths: set[str]) -> tuple[int, list[str]]:
    parsed = 0
    invalid: set[str] = set()
    errors: list[str] = []
    for relative in sorted(path for path in paths if path.endswith(".json")):
        try:
            json.loads((ROOT / relative).read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            invalid.add(relative)
        except OSError as error:
            errors.append(f"unable to read tracked JSON {relative}: {error}")
        else:
            parsed += 1
    for relative in sorted(invalid - RAW_JSON_CAPTURES):
        errors.append(f"invalid tracked JSON outside raw-capture allowlist: {relative}")
    for relative in sorted(RAW_JSON_CAPTURES - invalid):
        errors.append(f"raw-capture allowlist entry is absent or unexpectedly parses: {relative}")
    return parsed, errors


def tracked_target(relative: str, paths: set[str]) -> bool:
    return relative in paths or any(path.startswith(relative.rstrip("/") + "/") for path in paths)


def archival_locator(relative: str) -> bool:
    parts = PurePosixPath(relative).parts
    return ".artifacts" in parts or PurePosixPath(relative).suffix.lower() == ".apk"


def validate_markdown(paths: set[str]) -> tuple[int, set[str], list[str]]:
    checked = 0
    omitted: set[str] = set()
    errors: list[str] = []
    for markdown in sorted(path for path in paths if path.endswith(".md")):
        text = (ROOT / markdown).read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw = match.group("target").strip("<>")
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or raw.startswith("#"):
                continue
            target = unquote(parsed.path)
            if not target:
                continue
            base = PurePosixPath(markdown).parent
            relative = posixpath.normpath((base / target).as_posix())
            if relative == ".." or relative.startswith("../"):
                errors.append(f"repository-escaping link in {markdown}: {raw}")
                continue
            checked += 1
            if tracked_target(relative, paths):
                continue
            description = f"{markdown} -> {raw}"
            if archival_locator(relative):
                omitted.add(description)
            else:
                errors.append(f"broken tracked link: {description}")
    return checked, omitted, errors


def main() -> int:
    paths = tracked_paths()
    parsed_json, json_errors = validate_json(paths)
    checked_links, omitted, link_errors = validate_markdown(paths)
    errors = json_errors + link_errors
    print(f"Tracked JSON parsed: {parsed_json}")
    print(f"Immutable raw JSON captures allowlisted: {len(RAW_JSON_CAPTURES)}")
    print(f"Repository-relative Markdown links checked: {checked_links}")
    print(f"Archival APK/private-artifact locators reported separately: {len(omitted)}")
    for item in sorted(omitted):
        print(f"ARCHIVAL_LOCATOR: {item}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

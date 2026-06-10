#!/usr/bin/env python3
"""Validate local Markdown links used by public documentation."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DOC_GLOBS = ["*.md", "docs/**/*.md"]
IGNORE_PARTS = {".git", ".pytest_cache", ".ruff_cache", "node_modules", "dist", "build"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
HTML_ID_RE = re.compile(r"\bid=[\"']([^\"']+)[\"']")


def iter_markdown_files() -> list[Path]:
    paths: set[Path] = set()
    for pattern in DOC_GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file() and not any(part in IGNORE_PARTS for part in path.parts):
                paths.add(path)
    return sorted(paths)


def strip_inline_markup(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.strip()


def github_slug(value: str) -> str:
    value = strip_inline_markup(value).lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "-", value.strip())
    return value


def anchors_for(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    anchors: set[str] = set()
    seen: dict[str, int] = {}

    for match in HEADING_RE.finditer(text):
        slug = github_slug(match.group(2))
        count = seen.get(slug, 0)
        anchors.add(slug if count == 0 else f"{slug}-{count}")
        seen[slug] = count + 1

    anchors.update(match.group(1) for match in HTML_ID_RE.finditer(text))
    return anchors


def parse_target(raw: str) -> tuple[str, str]:
    target = raw.strip().split()[0].strip("<>")
    parsed = urlparse(target)
    clean_path = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    return clean_path, fragment


def is_external(raw: str) -> bool:
    parsed = urlparse(raw.strip().strip("<>"))
    return parsed.scheme in {"http", "https", "mailto", "tel"}


def validate_link(source: Path, raw: str, anchor_cache: dict[Path, set[str]]) -> list[str]:
    errors: list[str] = []
    if is_external(raw):
        return errors

    clean_path, fragment = parse_target(raw)
    if clean_path.endswith(".zip") and "standards/AEP-" not in clean_path:
        errors.append(f"blocked zip link in {source.relative_to(ROOT)}: {raw}")

    target_path = source if not clean_path else (source.parent / clean_path).resolve()
    try:
        target_path.relative_to(ROOT.resolve())
    except ValueError:
        return errors

    if clean_path and not target_path.exists():
        errors.append(f"broken internal link in {source.relative_to(ROOT)}: {raw}")
        return errors

    if fragment and target_path.suffix.lower() in {".md", ""}:
        anchors = anchor_cache.setdefault(target_path, anchors_for(target_path))
        if fragment not in anchors:
            errors.append(f"broken markdown anchor in {source.relative_to(ROOT)}: {raw}")

    return errors


def main() -> int:
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer(text):
            errors.extend(validate_link(path, match.group(1), anchor_cache))

    if errors:
        print("Markdown link validation failed:", file=sys.stderr)
        for error in errors[:250]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 250:
            print(f"... {len(errors) - 250} more failures", file=sys.stderr)
        return 1

    print(f"Markdown link validation passed for {len(iter_markdown_files())} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

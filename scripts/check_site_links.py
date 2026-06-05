#!/usr/bin/env python3
"""Conservatively check local href/src links in site HTML."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PLACEHOLDER_PREFIXES = ("SQUARESPACE_", "SME_INQUIRY_URL", "ENTERPRISE_INQUIRY_URL", "NATION_STATE_INQUIRY_URL", "SOVEREIGN_")
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}

class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.links.append((name, value.strip()))


def is_placeholder(value: str) -> bool:
    clean = value.lstrip("#")
    return clean.endswith("_URL") or clean.endswith("_INQUIRY_URL") or clean.startswith(PLACEHOLDER_PREFIXES)


def candidates_for(page: Path, raw: str) -> list[Path]:
    parsed = urlparse(raw)
    path = unquote(parsed.path)
    if path.startswith("/proof-gradient/"):
        path = path[len("/proof-gradient/"):]
        base = SITE
    elif path.startswith("/"):
        path = path[1:]
        base = SITE
    else:
        base = page.parent
    target = (base / path).resolve()
    if raw.endswith("/") or path == "" or target.is_dir():
        return [target / "index.html", target]
    return [target]


def link_exists(page: Path, raw: str) -> bool:
    parsed = urlparse(raw)
    if parsed.scheme in IGNORED_SCHEMES or raw.startswith("//"):
        return True
    if is_placeholder(raw):
        return True
    if parsed.path == "" and parsed.fragment:
        return True
    for candidate in candidates_for(page, raw):
        try:
            rel_to_repo = candidate.relative_to(ROOT)
        except ValueError:
            continue
        if candidate.exists():
            return True
        # If a site page links to a repo-root file such as README.md, allow it when present.
        repo_candidate = ROOT / rel_to_repo
        if repo_candidate.exists():
            return True
    return False


def find_broken() -> list[str]:
    broken: list[str] = []
    for page in sorted(SITE.rglob("*.html")):
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8", errors="ignore"))
        for attr, raw in parser.links:
            if not link_exists(page, raw):
                broken.append(f"{page.relative_to(ROOT)} {attr}={raw}")
    return broken


def run() -> int:
    broken = find_broken()
    if broken:
        print("Site link check failed:", file=sys.stderr)
        for item in broken:
            print(f"- {item}", file=sys.stderr)
        return 1
    print("Site local links validated")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())

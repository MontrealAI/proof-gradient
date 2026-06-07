#!/usr/bin/env python3
"""Validate the public GoalOS canonical shell and GitHub Pages links."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
OLD_MARKERS = re.compile(
    r"<!--\s*/?\s*GOALOS-(COMPLETE-NAV|COMPLETE-FOOTER|PRODUCT-LADDER-NAV|PRODUCT-LADDER-FOOTER|UNIFIED-SHELL|UNIFIED-FOOTER|CLOUD-MVP(?:[^a-z0-9-]|$))",
    re.IGNORECASE,
)
CANONICAL_NAV = "GOALOS-CANONICAL-SHELL:START"
CANONICAL_FOOTER = "GOALOS-CANONICAL-FOOTER:START"
DUPLICATE_MVP = "GOALOS-CLOUD-MVP homepage duplicate"
LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)


def is_public_html(path: Path) -> bool:
    return path.suffix == ".html" and "_archive" not in path.parts


def site_target_exists(url_path: str) -> bool:
    if not url_path.startswith("/proof-gradient/"):
        return True
    rel = url_path.removeprefix("/proof-gradient/").split("#", 1)[0].split("?", 1)[0]
    if rel == "":
        return (SITE / "index.html").exists()
    candidate = SITE / rel
    if candidate.is_file():
        return True
    if candidate.is_dir() and (candidate / "index.html").exists():
        return True
    if rel.endswith("/") and (SITE / rel / "index.html").exists():
        return True
    if (SITE / f"{rel}.html").exists():
        return True
    return False


def main() -> int:
    failures: list[str] = []
    html_files = sorted(p for p in SITE.rglob("*.html") if is_public_html(p))
    for path in html_files:
        text = path.read_text(errors="ignore")
        rel = path.relative_to(ROOT)
        if text.count(CANONICAL_NAV) != 1:
            failures.append(f"{rel}: expected exactly one canonical nav marker, found {text.count(CANONICAL_NAV)}")
        if text.count(CANONICAL_FOOTER) != 1:
            failures.append(f"{rel}: expected exactly one canonical footer marker, found {text.count(CANONICAL_FOOTER)}")
        if OLD_MARKERS.search(text):
            failures.append(f"{rel}: old GoalOS shell marker remains")
        if DUPLICATE_MVP in text:
            failures.append(f"{rel}: duplicate Cloud MVP homepage block marker remains")
        for raw in LINK_RE.findall(text):
            if raw.startswith("http://") or raw.startswith("https://") or raw.startswith("mailto:") or raw.startswith("tel:"):
                continue
            parsed = urlparse(raw)
            link_path = parsed.path
            if link_path.startswith("/proof-gradient/") and not site_target_exists(link_path):
                failures.append(f"{rel}: broken internal link {raw}")
    if failures:
        print("GoalOS site validation failed:", file=sys.stderr)
        for failure in failures[:200]:
            print(f"- {failure}", file=sys.stderr)
        if len(failures) > 200:
            print(f"... {len(failures) - 200} more failures", file=sys.stderr)
        return 1
    print(f"GoalOS site validation passed for {len(html_files)} public HTML pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

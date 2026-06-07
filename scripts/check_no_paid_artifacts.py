#!/usr/bin/env python3
"""Fail if paid buyer or private delivery artifacts are present in the public site.

All checkout / apply buttons must point to:
https://www.quebecartificialintelligence.com/shop
"""
from __future__ import annotations

import fnmatch
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PATTERNS = [
    "*.zip",
    "*BUYER*",
    "*COMPLETE_BUNDLE*",
    "*DELIVERY_KIT*",
    "*SELLER_ASSETS*",
    "*WORKSHOP*",
    "*IMPLEMENTATION*",
    "*ENTERPRISE_PILOT*",
    "*BUYER_OFFICIAL*",
    "*MASTER_PACK*",
    "*COMMERCIALIZATION_READY*",
    "*QUICK_LAUNCH*",
]
# Public documentation/action-kit exceptions. Public markdown, HTML, schemas, JSON, YAML,
# JavaScript, CSS, and SVG are allowed; deployable ZIPs or private bundle names are not.
WHITELIST = set()
WHITELIST_PREFIXES = (
    "_archive/",       # historical backup, not linked as paid product material
)
PUBLIC_DOC_PREFIXES = (
    "standards/AEP-",  # public AEP standard markdown, examples, schemas, conformance docs
)
PUBLIC_DOC_EXTENSIONS = {".md", ".html", ".json", ".yaml", ".yml", ".txt", ".css", ".js", ".mjs", ".svg", ".xml"}


def is_whitelisted(rel: str, path: Path) -> bool:
    if path.suffix.lower() == ".zip":
        return False
    if rel in WHITELIST or any(rel.startswith(prefix) for prefix in WHITELIST_PREFIXES):
        return True
    if path.suffix.lower() in PUBLIC_DOC_EXTENSIONS and any(rel.startswith(prefix) for prefix in PUBLIC_DOC_PREFIXES):
        return True
    return False


def main() -> int:
    violations: list[str] = []
    for path in SITE.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(SITE).as_posix()
        if is_whitelisted(rel, path):
            continue
        name = path.name
        full = rel
        if any(fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(full, pattern) for pattern in PATTERNS):
            violations.append(rel)
    if violations:
        print("Paid/private artifact guard failed. Remove or explicitly whitelist public documentation only:", file=sys.stderr)
        for rel in violations:
            print(f"- site/{rel}", file=sys.stderr)
        return 1
    print("Paid/private artifact guard passed for site/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

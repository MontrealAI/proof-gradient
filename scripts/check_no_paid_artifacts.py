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
]
# Public documentation/action-kit exceptions. These are standards or docs, not paid buyer products.
WHITELIST = {
    "standards/AEP-001/complete-package.zip",
}
WHITELIST_PREFIXES = (
    "standards/AEP-",  # public standards implementation documentation and schemas
    "_archive/",       # historical backup, not linked as paid product material
)


def is_whitelisted(rel: str) -> bool:
    return rel in WHITELIST or any(rel.startswith(prefix) for prefix in WHITELIST_PREFIXES)


def main() -> int:
    violations: list[str] = []
    for path in SITE.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(SITE).as_posix()
        if is_whitelisted(rel):
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

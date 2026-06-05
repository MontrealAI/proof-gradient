#!/usr/bin/env python3
"""Guard against committing paid GoalOS buyer/client packages to public paths."""
from __future__ import annotations

import fnmatch
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PREFIXES = ("site", "docs", "data", ".github")
PAID_PATTERNS = [
    "*BUYER_PRODUCT*.zip",
    "*CLIENT_PACKAGE*.zip",
    "*OPERATOR_PACKAGE*.zip",
    "GoalOS_AI_Efficiency_Sprint*.zip",
    "GoalOS_SME_AI_Adoption*.zip",
    "GoalOS_Enterprise*.zip",
    "GoalOS_Nation_State*.zip",
    "GoalOS_Sovereign*.zip",
]
ALLOWED_PREFIX = Path("releases/AEP-001")
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def is_public_path(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if not parts:
        return False
    if rel.is_relative_to(ALLOWED_PREFIX):
        return False
    if len(parts) == 1:
        return True
    return parts[0] in PUBLIC_PREFIXES


def find_offenders() -> list[Path]:
    offenders: list[Path] = []
    for path in ROOT.rglob("*.zip"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        rel = path.relative_to(ROOT)
        if rel.is_relative_to(ALLOWED_PREFIX):
            continue
        if not is_public_path(path):
            continue
        if any(fnmatch.fnmatch(path.name, pattern) for pattern in PAID_PATTERNS):
            offenders.append(rel)
    return sorted(offenders)


def run() -> int:
    offenders = find_offenders()
    if offenders:
        print("Paid product ZIP guard failed. Offending files:", file=sys.stderr)
        for offender in offenders:
            print(f"- {offender}", file=sys.stderr)
        return 1
    print("No forbidden paid product ZIP files found")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

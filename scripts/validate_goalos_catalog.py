#!/usr/bin/env python3
"""Validate GoalOS public catalog artifacts against shared site rules."""
from __future__ import annotations

import sys
from pathlib import Path

from goalos_public_site_rules import is_blocked_paid_or_private_artifact, normalize_rel, page_class

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors: list[str] = []
    for base_name in ("site", "public"):
        base = ROOT / base_name
        if not base.exists():
            continue
        for path in sorted(p for p in base.rglob("*") if p.is_file() and "_archive" not in p.parts):
            rel = normalize_rel(path.relative_to(base))
            if is_blocked_paid_or_private_artifact(rel):
                errors.append(f"{base_name}/{rel}: classified as {page_class(rel)} and blocked from the public catalog")

    if errors:
        print("GoalOS catalog validation failed:", file=sys.stderr)
        for error in errors[:200]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

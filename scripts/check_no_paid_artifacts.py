#!/usr/bin/env python3
"""Fail if paid buyer or private delivery artifacts are present in public roots."""
from __future__ import annotations

import sys
from pathlib import Path

from goalos_public_site_rules import discover_public_root, is_blocked_paid_or_private_artifact, normalize_rel

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    public_root = discover_public_root(ROOT)
    violations: list[str] = []
    for path in sorted(public_root.rglob("*")):
        if not path.is_file() or "_archive" in path.parts:
            continue
        rel = normalize_rel(path.relative_to(public_root))
        if is_blocked_paid_or_private_artifact(rel):
            violations.append(rel)

    if violations:
        print("Paid/private artifact guard failed. Public AEP complete-package.zip files are allowed; buyer/private materials are not:", file=sys.stderr)
        for rel in violations:
            print(f"- {public_root.name}/{rel}", file=sys.stderr)
        return 1
    print(f"Paid/private artifact guard passed for {public_root.name}/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the GoalOS catalog while sharing public artifact policy."""
from __future__ import annotations

import sys
from pathlib import Path

from goalos_public_site_rules import discover_public_root, is_blocked_paid_or_private_artifact, normalize_rel

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    public_root = discover_public_root(ROOT)
    errors: list[str] = []
    for path in sorted(public_root.rglob("*")):
        if not path.is_file() or "_archive" in path.parts:
            continue
        rel = normalize_rel(path.relative_to(public_root))
        if is_blocked_paid_or_private_artifact(rel):
            errors.append(f"{public_root.name}/{rel}: blocked by GoalOS paid/private artifact policy")
    legacy = ROOT / "scripts" / "validate_goalos_products.py"
    if legacy.exists():
        import subprocess
        result = subprocess.run([sys.executable, str(legacy)], cwd=ROOT)
        if result.returncode != 0:
            errors.append("scripts/validate_goalos_products.py failed")
    if errors:
        print("GoalOS catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail if paid buyer or private delivery artifacts are present in the public deploy root."""
from __future__ import annotations

import sys
from pathlib import Path

from goalos_public_site_rules import is_blocked_paid_or_private_artifact, normalize_rel

ROOT = Path(__file__).resolve().parents[1]


def public_root() -> Path:
    if (ROOT / "site").is_dir():
        return ROOT / "site"
    if (ROOT / "public").is_dir():
        return ROOT / "public"
    return ROOT / "site"


def main() -> int:
    root = public_root()
    violations: list[str] = []
    if root.exists():
        for path in sorted(p for p in root.rglob("*") if p.is_file() and "_archive" not in p.parts):
            rel = normalize_rel(path.relative_to(root))
            if is_blocked_paid_or_private_artifact(rel):
                violations.append(rel)

    if violations:
        print("Paid/private artifact guard failed. Public AEP complete-package.zip files are allowed; buyer/private artifacts are not:", file=sys.stderr)
        for rel in violations:
            print(f"- {root.name}/{rel}", file=sys.stderr)
        return 1
    print(f"Paid/private artifact guard passed for {root.name}/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

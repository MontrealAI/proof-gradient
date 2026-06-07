#!/usr/bin/env python3
"""Fail if paid buyer or private delivery artifacts are present in public roots."""
from __future__ import annotations

import sys
from pathlib import Path

from goalos_public_site_rules import is_blocked_paid_or_private_artifact, is_public_aep_package, normalize_rel

ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = ("site", "public")


def iter_public_files() -> list[tuple[str, Path, str]]:
    files: list[tuple[str, Path, str]] = []
    for root_name in SCAN_ROOTS:
        root = ROOT / root_name
        if not root.is_dir():
            continue
        for path in sorted(p for p in root.rglob("*") if p.is_file() and "_archive" not in p.parts):
            rel = normalize_rel(path.relative_to(root))
            files.append((root_name, path, rel))
    return files


def main() -> int:
    violations: list[str] = []
    allowed_aep_packages: list[str] = []

    for root_name, _path, rel in iter_public_files():
        display = f"{root_name}/{rel}"
        if is_public_aep_package(rel):
            allowed_aep_packages.append(display)
            continue
        if is_blocked_paid_or_private_artifact(rel):
            violations.append(display)

    if violations:
        print(
            "Paid/private artifact guard failed. Only standards/AEP-###/complete-package.zip is allowed as a public ZIP; buyer/private artifacts are not:",
            file=sys.stderr,
        )
        for rel in violations:
            print(f"- {rel}", file=sys.stderr)
        return 1

    roots = ", ".join(root for root in SCAN_ROOTS if (ROOT / root).is_dir()) or "no public roots"
    print(f"Paid/private artifact guard passed for {roots}. Allowed public AEP packages: {len(allowed_aep_packages)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

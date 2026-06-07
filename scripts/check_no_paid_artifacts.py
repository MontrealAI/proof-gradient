#!/usr/bin/env python3
"""Block paid/private artifacts from public site roots."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [ROOT / "site", ROOT / "public"]
BLOCKED_TERMS = [
    "buyer", "buyer_official", "complete_bundle", "delivery_kit", "seller_assets",
    "master_pack", "commercialization_ready", "quick_launch", "opulent_institutional",
    "institutional_boardroom", "implementation_sprint", "enterprise_rsi_pilot",
    "workshop_v", "buyer_facilitator", "private", "paid",
]
SAFE_EXTS = {"", ".md", ".html", ".json", ".txt", ".yml", ".yaml", ".css", ".js", ".mjs", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".xml", ".webmanifest"}
AEP_ZIP = re.compile(r"^standards/AEP-\d{3}/complete-package\.zip$", re.I)
SKIP_PARTS = {"_archive"}


def rel_public(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_allowed_aep_zip(rel: str) -> bool:
    return bool(AEP_ZIP.fullmatch(rel))


def find_offenders() -> list[str]:
    offenders: list[str] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or any(part in SKIP_PARTS for part in path.relative_to(root).parts):
                continue
            rel = rel_public(path, root)
            lower = rel.lower()
            if path.suffix.lower() == ".zip" and not is_allowed_aep_zip(rel):
                offenders.append(f"{root.name}/{rel}: ZIP files are blocked except standards/AEP-###/complete-package.zip")
                continue
            if any(term in lower for term in BLOCKED_TERMS):
                offenders.append(f"{root.name}/{rel}: blocked paid/private-looking name term")
                continue
            if path.suffix.lower() not in SAFE_EXTS and path.suffix.lower() != ".zip":
                offenders.append(f"{root.name}/{rel}: extension {path.suffix} is not in the public allowlist")
    return offenders


def run() -> int:
    offenders = find_offenders()
    if offenders:
        print("Paid/private artifact guard failed:", file=sys.stderr)
        for offender in offenders:
            print(f"- {offender}", file=sys.stderr)
        return 1
    print("No paid/private artifacts found in site/ or public/")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())

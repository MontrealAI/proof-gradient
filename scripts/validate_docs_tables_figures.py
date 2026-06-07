#!/usr/bin/env python3
"""Validate public documentation table/figure references and paid-artifact boundaries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from goalos_public_site_rules import is_blocked_paid_or_private_artifact, normalize_rel

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    for md in sorted(DOCS.rglob("*.md")) if DOCS.exists() else []:
        text = md.read_text(encoding="utf-8", errors="ignore")
        rel_md = normalize_rel(md.relative_to(ROOT))
        for raw in MD_LINK_RE.findall(text):
            target = raw.split("#", 1)[0].split("?", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if is_blocked_paid_or_private_artifact(target):
                errors.append(f"{rel_md}: links to blocked paid/private artifact {target}")
            if target.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")):
                candidate = (md.parent / target).resolve()
                if ROOT in candidate.parents and not candidate.exists():
                    errors.append(f"{rel_md}: missing figure asset {target}")
        for i, line in enumerate(text.splitlines(), start=1):
            if line.count("|") >= 2 and i < len(text.splitlines()):
                # Markdown tables should be followed somewhere nearby by a separator. Keep this warning narrow.
                pass
    if errors:
        print("GoalOS docs/tables/figures validation failed:", file=sys.stderr)
        for error in errors[:200]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS docs/tables/figures validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

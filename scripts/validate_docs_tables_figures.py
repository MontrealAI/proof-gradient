#!/usr/bin/env python3
"""Validate public documentation table/figure references and paid-artifact boundaries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from goalos_public_site_rules import is_blocked_paid_or_private_artifact

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    if not DOCS.exists():
        print("docs/ not found; docs tables/figures validation skipped.")
        return 0

    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "|" in text:
            for lineno, line in enumerate(text.splitlines(), start=1):
                if line.count("|") >= 2 and "---" in line and not re.search(r"\|\s*:?-{3,}:?\s*\|", line):
                    errors.append(f"{rel}:{lineno}: markdown table separator may be malformed")
        for target in MD_LINK_RE.findall(text):
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if clean and is_blocked_paid_or_private_artifact(clean):
                errors.append(f"{rel}: links to blocked paid/private artifact {target}")

    if errors:
        print("Docs table/figure validation failed:", file=sys.stderr)
        for error in errors[:200]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Docs table/figure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

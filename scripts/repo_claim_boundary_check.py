#!/usr/bin/env python3
"""Check GoalOS public product/docs copy for unsupported claims outside boundary contexts."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_GLOBS = [
    "site/goalos/**/*.html",
    "site/products/**/*.html",
    "site/ai-efficiency-score/**/*.html",
    "docs/commerce/**/*.md",
]
FORBIDDEN_TERMS = [
    "guaranteed ROI",
    "guaranteed profit",
    "achieved AGI",
    "achieved ASI",
    "superintelligence achieved",
    "Government of Canada endorsed",
    "official government partner",
    "certified compliance",
    "legal advice",
    "investment advice",
    "national security readiness",
    "Kardashev achieved",
]
ALLOWED_CONTEXTS = [
    "does not claim",
    "not claimed",
    "not affiliated",
    "not endorsed",
    "no guarantee",
    "claim boundary",
    "not legal advice",
    "does not provide legal",
    "do not provide legal",
    "does not provide legal, financial",
    "ne fournit pas de conseils",
    "aucun roi",
]


def files_to_scan() -> list[Path]:
    files: set[Path] = set()
    for pattern in SCAN_GLOBS:
        files.update(ROOT.glob(pattern))
    return sorted(path for path in files if path.is_file())


def allowed(line: str) -> bool:
    lower = line.lower()
    return any(context in lower for context in ALLOWED_CONTEXTS)


def find_violations() -> list[str]:
    violations: list[str] = []
    patterns = [(term, re.compile(re.escape(term), re.I)) for term in FORBIDDEN_TERMS]
    for path in files_to_scan():
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
            for term, pattern in patterns:
                if pattern.search(line) and not allowed(line):
                    violations.append(f"{path.relative_to(ROOT)}:{lineno}: unsupported claim term '{term}'")
    return violations


def run() -> int:
    violations = find_violations()
    if violations:
        print("Claim-boundary check failed:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1
    print("GoalOS claim boundaries validated")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())

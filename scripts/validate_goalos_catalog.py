#!/usr/bin/env python3
"""Validate that public docs and tables do not contradict the GoalOS catalog."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/data/goalos_catalog.yml"
SHOP_URL = "https://www.quebecartificialintelligence.com/shop"
PRODUCTS = [
    ("$49", "GoalOS AI Efficiency Sprint Kit", "v1.4"),
    ("$199", "GoalOS RSI Lite", "v1.6"),
    ("$997", "GoalOS Proof Room Lite / Department Pack", "v2.0"),
    ("$2,500+", "GoalOS RSI Sprint Workshop", "v7.0"),
    ("$9,500+", "GoalOS Proof Room Implementation Sprint", "v2.0"),
    ("$49,000+", "GoalOS Enterprise RSI Pilot", "v2.0"),
]
PROHIBITED_CURRENT = [
    "Validation Hotfix v12 is current",
    "Validation Hotfix v13 is current",
    "Enterprise SaaS complete",
    "Guarantees ROI",
    "Guarantees revenue",
    "GoalOS modifies base AI models",
    "uncontrolled autonomous deployment is allowed",
]
DOC_GLOBS = ["README.md", "docs/GOALOS_*.md", "docs/tables/*.csv"]


def read_all_public_text() -> str:
    chunks: list[str] = []
    for pattern in DOC_GLOBS:
        for path in ROOT.glob(pattern):
            chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(chunks)


def main() -> int:
    errors: list[str] = []
    if not CATALOG.exists():
        errors.append("Missing docs/data/goalos_catalog.yml")
    catalog = CATALOG.read_text(encoding="utf-8", errors="ignore") if CATALOG.exists() else ""
    public_text = read_all_public_text()
    if SHOP_URL not in catalog or SHOP_URL not in public_text:
        errors.append("Shop URL missing from catalog or public docs")
    for price, name, version in PRODUCTS:
        for token in (price, name, version):
            if token not in catalog:
                errors.append(f"Catalog missing {token}")
        if name not in public_text or price not in public_text:
            errors.append(f"Public docs missing current product/price: {price} {name}")
    ladder = ROOT / "docs/tables/goalos_product_ladder.csv"
    if ladder.exists():
        rows = list(csv.DictReader(ladder.open(newline="")))
        offers = "\n".join(row.get("Offer", "") + " " + row.get("Version", "") for row in rows)
        for price, name, version in PRODUCTS:
            if price not in offers or name not in offers or version not in offers:
                errors.append(f"Product ladder CSV missing {price} {name} {version}")
    else:
        errors.append("Missing product ladder CSV")
    for phrase in PROHIBITED_CURRENT:
        if phrase in public_text:
            errors.append(f"Prohibited or contradictory public phrase found: {phrase}")
    if "GoalOS Validation Hotfix v14 Microsite Compatibility" not in public_text:
        errors.append("v14 validation status missing from public docs")
    if "GoalOS Cloud MVP 0.2" not in public_text:
        errors.append("Cloud MVP 0.2 status missing from public docs")
    if errors:
        print("GoalOS catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

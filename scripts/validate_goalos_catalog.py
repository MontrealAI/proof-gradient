#!/usr/bin/env python3
"""Validate GoalOS catalog as the source of truth for README/docs/tables/site."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/data/goalos_catalog.yml"
SHOP = "https://www.quebecartificialintelligence.com/shop"
PRODUCTS = [
    ("$49", "GoalOS AI Efficiency Sprint Kit", "v1.4"),
    ("$199", "GoalOS RSI Lite", "v1.6"),
    ("$997", "GoalOS Proof Room Lite / Department Pack", "v2.0"),
    ("$2,500+", "GoalOS RSI Sprint Workshop", "v7.0"),
    ("$9,500+", "GoalOS Proof Room Implementation Sprint", "v2.0"),
    ("$49,000+", "GoalOS Enterprise RSI Pilot", "v2.0"),
]
AEP_CODES = [f"AEP-{i:03d}" for i in range(1, 9)]
PROHIBITED = [
    "guaranteed ROI",
    "guaranteed revenue",
    "investment returns",
    "model self-modification",
    "uncontrolled autonomous deployment",
]
PRIVATE_DOWNLOAD_RE = re.compile(r"https?://[^\s)]+(?:BUYER|BUNDLE|DELIVERY|PRIVATE|PAID)[^\s)]*\.zip", re.IGNORECASE)


def read(path: str) -> str:
    p = ROOT / path
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""


def main() -> int:
    errors: list[str] = []
    if not CATALOG.exists():
        errors.append("missing docs/data/goalos_catalog.yml")
        text = ""
    else:
        text = CATALOG.read_text(encoding="utf-8", errors="ignore")
    for required in [SHOP, "GoalOS Validation Hotfix v14 Microsite Compatibility", "GoalOS Public Site Release v8 Intelligent Assets", "GoalOS Cloud MVP", "0.2"]:
        if required not in text:
            errors.append(f"catalog missing required value: {required}")
    for price, name, version in PRODUCTS:
        for value in (price, name, version):
            if value not in text:
                errors.append(f"catalog missing product value: {value}")
    for code in AEP_CODES:
        if code not in text:
            errors.append(f"catalog missing AEP code: {code}")
    for value in PROHIBITED:
        if value not in text:
            errors.append(f"catalog missing prohibited claim boundary: {value}")
    readme = read("README.md")
    product_csv = ROOT / "docs/tables/goalos_product_ladder.csv"
    csv_text = product_csv.read_text(encoding="utf-8", errors="ignore") if product_csv.exists() else ""
    for price, name, version in PRODUCTS:
        combo = f"{name} {version}"
        for label, body in (("README", readme), ("product ladder CSV", csv_text)):
            if price not in body:
                errors.append(f"{label} missing price from catalog: {price}")
            if name not in body:
                errors.append(f"{label} missing product from catalog: {name}")
            if version not in body:
                errors.append(f"{label} missing version from catalog: {version}")
    if product_csv.exists():
        rows = list(csv.DictReader(product_csv.open(encoding="utf-8")))
        if len(rows) != len(PRODUCTS):
            errors.append(f"product ladder CSV should have {len(PRODUCTS)} products, found {len(rows)}")
        for row in rows:
            if row.get("Public URL") != SHOP:
                errors.append(f"product ladder CSV has non-shop URL for {row.get('Offer')}: {row.get('Public URL')}")
    for path in [ROOT / "README.md", *sorted((ROOT / "docs").glob("GOALOS_*.md"))]:
        body = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
        if PRIVATE_DOWNLOAD_RE.search(body):
            errors.append(f"{path.relative_to(ROOT)} contains a direct private/paid ZIP download URL")
    if "v12" in readme and "obsolete" not in readme.lower():
        errors.append("README mentions v12 without marking it obsolete")
    if errors:
        print("GoalOS catalog validation failed:", file=sys.stderr)
        for error in errors[:250]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

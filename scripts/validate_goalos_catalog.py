#!/usr/bin/env python3
"""Validate GoalOS documentation catalog consistency.

Documentation-only validator: reads docs, tables, and README; never inspects or modifies
website implementation files.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/data/goalos_catalog.yml"
README = ROOT / "README.md"


def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - exercised in bare envs
        raise SystemExit(f"YAML parse failed for {path}: {exc}")


def fail(msgs: list[str]) -> None:
    if msgs:
        print("GoalOS catalog validation failed:")
        for msg in msgs:
            print(f"- {msg}")
        sys.exit(1)
    print("✅ GoalOS catalog validation passed")


def docs_files() -> list[Path]:
    return [p for p in (ROOT / "docs").rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".csv", ".yml", ".yaml"}]


def local_markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def main() -> None:
    errors: list[str] = []
    catalog = load_yaml(CATALOG)
    products = catalog.get("product_ladder", [])
    readme = README.read_text(encoding="utf-8")

    for item in products:
        for field in ("price", "name", "version", "description_en"):
            value = str(item[field])
            if value not in readme:
                errors.append(f"README missing product {field}: {value}")

    table_path = ROOT / "docs/tables/goalos_product_ladder.csv"
    with table_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != len(products):
        errors.append("product ladder table row count does not match catalog")
    for row, item in zip(rows, products):
        if row["price"] != item["price"] or row["offer"] != item["name"] or row["version"] != item["version"]:
            errors.append(f"product ladder stale row: {row}")

    safe = catalog["safe_ai_boundary"]["en"]
    for key in [README, ROOT / "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md", ROOT / "docs/GOALOS_RECURSIVE_WORKFLOW_OS.md"]:
        if safe not in key.read_text(encoding="utf-8"):
            errors.append(f"safe-boundary language missing in {key.relative_to(ROOT)}")

    # Prohibited claims are allowed when clearly framed as prohibited/claim boundary text.
    boundary_files = {
        ROOT / "README.md",
        ROOT / "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md",
        ROOT / "docs/data/goalos_catalog.yml",
        ROOT / "docs/tables/goalos_claim_boundaries.csv",
        ROOT / "docs/tables/goalos_revenue_scenarios.csv",
        ROOT / "docs/tables/goalos_roi_assumptions.csv",
    }
    current_docs = [
        README,
        ROOT / "docs/GOALOS_DOCUMENTATION_INDEX.md",
        ROOT / "docs/GOALOS_COMMERCIALIZATION_STATUS.md",
        ROOT / "docs/GOALOS_RECURSIVE_WORKFLOW_OS.md",
        ROOT / "docs/GOALOS_CLOUD_MVP_0_2.md",
        ROOT / "docs/GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md",
        ROOT / "docs/GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md",
        ROOT / "docs/GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md",
        ROOT / "docs/GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md",
        ROOT / "docs/GOALOS_ENGINEERING_ROADMAP.md",
        ROOT / "docs/GOALOS_PROOF_CARD_001_PLAN.md",
        ROOT / "docs/GOALOS_ENTERPRISE_RSI_PILOT_SUMMARY.md",
        ROOT / "docs/GOALOS_DEPARTMENT_RSI_SUMMARY.md",
        ROOT / "docs/GOALOS_BUYER_PRODUCTS_SUMMARY.md",
        ROOT / "docs/GOALOS_WORLD_CLASS_FIRM_STACK.md",
    ]
    for p in current_docs:
        if p in boundary_files:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore").lower()
        for claim in catalog.get("prohibited_claims", []):
            phrase = claim.lower()
            if phrase in text and not any(marker in text for marker in ("not claim", "does not claim", "not a substitute")):
                errors.append(f"possible live prohibited claim in {p.relative_to(ROOT)}: {claim}")

    paid_zip_pattern = re.compile(r"https?://[^\s)]+(?:buyer|paid|workshop|implementation|enterprise)[^\s)]*\.zip", re.I)
    for p in docs_files():
        if paid_zip_pattern.search(p.read_text(encoding="utf-8", errors="ignore")):
            errors.append(f"direct public paid ZIP link found in {p.relative_to(ROOT)}")

    for p in [README, ROOT / "docs/GOALOS_DOCUMENTATION_INDEX.md"]:
        base = p.parent
        for url in local_markdown_links(p.read_text(encoding="utf-8")):
            if url.startswith(("http://", "https://", "#", "mailto:")) or "planned" in url:
                continue
            target = (base / url.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(f"broken local link in {p.relative_to(ROOT)}: {url}")

    fail(errors)


if __name__ == "__main__":
    main()

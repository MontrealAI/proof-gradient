#!/usr/bin/env python3
"""Validate GoalOS v10 docs, tables, figures, and catalog consistency."""
from __future__ import annotations

import csv
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CATALOG = DOCS / "data/goalos_catalog.yml"
SAFE = "GoalOS does not modify base AI models. GoalOS improves workflows around AI"
REQUIRED_DOCS = [
    "GOALOS_REPO_AUDIT.md", "GOALOS_DOCUMENTATION_INDEX.md", "GOALOS_COMMERCIALIZATION_STATUS.md", "GOALOS_PUBLIC_SITE_RELEASE_V10.md", "GOALOS_RECURSIVE_WORKFLOW_OS.md", "GOALOS_CLOUD_MVP_0_2.md", "GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md", "GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md", "GOALOS_PAID_ARTIFACT_POLICY.md", "GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md", "GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md", "GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md", "GOALOS_ENGINEERING_ROADMAP.md",
]
REQUIRED_TABLES = ["goalos_product_ladder.csv", "goalos_offer_status.csv", "goalos_claim_boundaries.csv", "goalos_public_site_pages.csv", "goalos_paid_file_policy.csv", "goalos_aep_standards.csv", "goalos_document_inventory.csv", "goalos_asset_manifest.csv"]
REQUIRED_FIGS = ["goalos_recursive_workflow_loop", "goalos_product_ladder", "goalos_public_site_architecture", "goalos_cloud_mvp_architecture", "goalos_proof_graph_concept", "goalos_enterprise_safety_boundary"]
REQUIRED_PAGES = ["site/index.html", "site/pricing/index.html", "site/products/index.html", "site/workshop/goalos-rsi-sprint-workshop/index.html", "site/brand/visual-system/index.html"]


def run() -> int:
    errors=[]
    if not CATALOG.exists(): errors.append("Missing docs/data/goalos_catalog.yml")
    catalog=yaml.safe_load(CATALOG.read_text(encoding="utf-8")) if CATALOG.exists() else {}
    for doc in REQUIRED_DOCS:
        p=DOCS/doc
        if not p.exists(): errors.append(f"Missing docs/{doc}")
    for doc in ["GOALOS_PUBLIC_SITE_RELEASE_V10.md", "GOALOS_RECURSIVE_WORKFLOW_OS.md", "GOALOS_CLOUD_MVP_0_2.md", "GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md"]:
        p=DOCS/doc
        if p.exists() and SAFE not in p.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"docs/{doc} missing safe-boundary language")
    for table in REQUIRED_TABLES:
        if not (DOCS/"tables"/table).exists(): errors.append(f"Missing docs/tables/{table}")
    for fig in REQUIRED_FIGS:
        if not (DOCS/"figures"/f"{fig}.mmd").exists(): errors.append(f"Missing docs/figures/{fig}.mmd")
        if not (DOCS/"figures"/f"{fig}.svg").exists(): errors.append(f"Missing docs/figures/{fig}.svg")
    readme=(ROOT/"README.md").read_text(encoding="utf-8", errors="ignore") if (ROOT/"README.md").exists() else ""
    for doc in REQUIRED_DOCS:
        if doc not in readme and doc not in {"GOALOS_REPO_AUDIT.md", "GOALOS_COMMERCIALIZATION_STATUS.md", "GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md", "GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md", "GOALOS_PAID_ARTIFACT_POLICY.md", "GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md", "GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md", "GOALOS_ENGINEERING_ROADMAP.md"}:
            errors.append(f"README does not link/name docs/{doc}")
    if (DOCS/"tables/goalos_product_ladder.csv").exists():
        rows=list(csv.DictReader((DOCS/"tables/goalos_product_ladder.csv").open(encoding="utf-8")))
        products=catalog.get("product_ladder", [])
        if len(rows)!=len(products): errors.append("Product ladder table row count does not match catalog")
        for product in products:
            matches=[r for r in rows if r.get("slug")==product.get("slug")]
            if not matches: errors.append(f"Missing product in table: {product.get('slug')}")
            else:
                row=matches[0]
                for k in ["price","version"]:
                    if row.get(k)!=product.get(k): errors.append(f"Table mismatch for {product.get('slug')} {k}")
    for page in REQUIRED_PAGES:
        if not (ROOT/page).exists(): errors.append(f"Missing required page {page}")
    if errors:
        print("GoalOS docs/tables/figures validation failed:", file=sys.stderr)
        for e in errors: print(f"- {e}", file=sys.stderr)
        return 1
    print("GoalOS docs, tables, figures, README links, pages, and safe boundary validated")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())

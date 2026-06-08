#!/usr/bin/env python3
"""Validate GoalOS documentation, tables, figures, safe claims, and internal links."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "docs/GOALOS_DOCUMENTATION_INDEX.md",
    "docs/GOALOS_COMMERCIALIZATION_STATUS.md",
    "docs/GOALOS_PRODUCT_LADDER.md",
    "docs/GOALOS_READY_TO_SELL_STATUS.md",
    "docs/GOALOS_PROOF_CARD_001_PLAN.md",
    "docs/GOALOS_RECURSIVE_WORKFLOW_OS.md",
    "docs/GOALOS_CLOUD_MVP_0_2.md",
    "docs/GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md",
    "docs/GOALOS_PUBLIC_SITE_RELEASE_V8.md",
    "docs/GOALOS_VALIDATION_HOTFIX_V14.md",
    "docs/GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md",
    "docs/GOALOS_PAID_ARTIFACT_POLICY.md",
    "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md",
    "docs/GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md",
    "docs/GOALOS_TAX_ACCOUNTING_CFO_SUMMARY.md",
    "docs/GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md",
    "docs/GOALOS_PROFESSIONAL_FIRM_PACKAGES_SUMMARY.md",
    "docs/GOALOS_WEB3_HYBRID_ARCHITECTURE.md",
    "docs/GOALOS_ENGINEERING_ROADMAP.md",
    "docs/GOALOS_REPO_AUDIT.md",
]
REQUIRED_TABLES = [
    "docs/tables/goalos_product_ladder.csv",
    "docs/tables/goalos_offer_status.csv",
    "docs/tables/goalos_claim_boundaries.csv",
    "docs/tables/goalos_public_site_pages.csv",
    "docs/tables/goalos_paid_file_policy.csv",
    "docs/tables/goalos_aep_standards.csv",
    "docs/tables/goalos_document_inventory.csv",
    "docs/tables/goalos_figure_inventory.csv",
    "docs/tables/goalos_asset_manifest.csv",
    "docs/tables/goalos_validation_rules.csv",
    "docs/tables/goalos_workflow_actions.csv",
    "docs/tables/goalos_proof_card_001_fields.csv",
    "docs/tables/goalos_professional_firm_packages.csv",
]
FIGURE_STEMS = [
    "goalos_recursive_workflow_loop",
    "goalos_product_ladder",
    "goalos_proof_led_revenue_loop",
    "goalos_public_site_architecture",
    "goalos_validation_architecture",
    "goalos_cloud_mvp_architecture",
    "goalos_enterprise_safety_boundary",
    "goalos_web3_hybrid_architecture",
    "goalos_proof_graph_concept",
]
README_SECTIONS = [
    "# Proof Gradient · GoalOS",
    "## Safe AI boundary",
    "## Product ladder",
    "## Public standards",
    "## Platform architecture",
    "## Software proof: GoalOS Cloud MVP 0.2",
    "## Public site and validation system",
    "## Repository map",
    "## Documentation map",
    "## Claim boundary",
    "## Paid-file policy",
    "## Run validation",
    "## Run tests",
]
CURRENT_TOKENS = [
    "$49", "$199", "$997", "$2,500+", "$9,500+", "$49,000+",
    "GoalOS AI Efficiency Sprint Kit", "v1.4", "GoalOS RSI Lite", "v1.6",
    "GoalOS Proof Room Lite / Department Pack", "v2.0", "GoalOS RSI Sprint Workshop", "v7.0",
    "GoalOS Cloud MVP 0.2", "GoalOS Validation Hotfix v14 Microsite Compatibility",
]
SAFE_BOUNDARY = "GoalOS improves workflows around AI; it does not modify base AI models"
PAID_POLICY = "buyer products are sold through the QUEBEC.AI shop"
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
RAW_BLOCKED_LINK_RE = re.compile(r"https?://[^\s)]+(?:BUYER|BUNDLE|DELIVERY|IMPLEMENTATION|PILOT|zip)[^\s)]*", re.I)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def exists(errors: list[str], rel: str) -> None:
    if not (ROOT / rel).exists():
        fail(errors, f"Missing required file: {rel}")


def check_internal_links(errors: list[str], path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for link in MD_LINK_RE.findall(text):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = link.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        if not (path.parent / target).resolve().exists():
            fail(errors, f"Broken internal link in {path.relative_to(ROOT)}: {link}")


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_DOCS + REQUIRED_TABLES:
        exists(errors, rel)
    for stem in FIGURE_STEMS:
        exists(errors, f"docs/figures/{stem}.mmd")
        exists(errors, f"docs/figures/{stem}.svg")
    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="ignore")
    for section in README_SECTIONS:
        if section not in readme:
            fail(errors, f"README missing section: {section}")
    for token in CURRENT_TOKENS:
        if token not in readme and token not in (ROOT / "docs/data/goalos_catalog.yml").read_text(encoding="utf-8", errors="ignore"):
            fail(errors, f"Current product/status token not found in README/catalog: {token}")
    combined = readme + "\n" + "\n".join((ROOT / rel).read_text(encoding="utf-8", errors="ignore") for rel in REQUIRED_DOCS if (ROOT / rel).exists())
    if SAFE_BOUNDARY not in combined:
        fail(errors, "Safe-boundary language missing")
    if PAID_POLICY.lower() not in combined.lower():
        fail(errors, "Paid-file policy language missing")
    for match in RAW_BLOCKED_LINK_RE.findall(combined):
        if "quebecartificialintelligence.com/shop" not in match:
            fail(errors, f"Potential public paid-product link found: {match}")
    for path in [ROOT / "README.md", *[ROOT / rel for rel in REQUIRED_DOCS if (ROOT / rel).exists()]]:
        check_internal_links(errors, path)
    if errors:
        print("GoalOS docs/tables/figures validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("GoalOS docs/tables/figures validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

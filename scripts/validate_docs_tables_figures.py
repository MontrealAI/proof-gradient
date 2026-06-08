#!/usr/bin/env python3
"""Validate GoalOS README, docs, CSV tables, figure assets, and public artifact links."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from goalos_public_site_rules import is_blocked_paid_or_private_artifact

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

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
FIGURE_NAMES = [
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
REQUIRED_README_PHRASES = [
    "Proof Gradient · GoalOS",
    "Aim. Act. Prove. Evolve.",
    "A model can answer. An agent can act. An institution must prove.",
    "Recursive Self-Improving Workflows",
    "does **not** modify base AI models",
    "Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run",
    "GoalOS Validation Hotfix v14 Microsite Compatibility",
    "docs/GOALOS_DOCUMENTATION_INDEX.md",
    "docs/figures/",
    "docs/tables/",
    "No proof, no evolution",
]
CURRENT_PRODUCT_PHRASES = [
    "$49", "$199", "$997", "$2,500+", "$9,500+", "$49,000+",
    "GoalOS AI Efficiency Sprint Kit v1.4",
    "GoalOS RSI Lite v1.6",
    "GoalOS Proof Room Lite / Department Pack v2.0",
    "GoalOS RSI Sprint Workshop v7.0",
    "GoalOS Proof Room Implementation Sprint v2.0",
    "GoalOS Enterprise RSI Pilot v2.0",
    "GoalOS Cloud MVP 0.2",
]


def add(errors: list[str], msg: str) -> None:
    errors.append(msg)


def target_exists(source: Path, target: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc or target.startswith("mailto:") or target.startswith("#"):
        return True
    clean = parsed.path.split("#", 1)[0]
    if not clean:
        return True
    candidate = (source.parent / clean).resolve() if not clean.startswith("/") else (ROOT / clean.lstrip("/")).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return True
    if candidate.exists():
        return True
    if candidate.suffix == "" and candidate.with_suffix(".md").exists():
        return True
    return False


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_DOCS + REQUIRED_TABLES:
        if not (ROOT / rel).exists():
            add(errors, f"missing required file: {rel}")
    for name in FIGURE_NAMES:
        for ext in ("mmd", "svg"):
            rel = f"docs/figures/{name}.{ext}"
            if not (ROOT / rel).exists():
                add(errors, f"missing required figure asset: {rel}")
    readme = ROOT / "README.md"
    if not readme.exists():
        add(errors, "missing README.md")
    else:
        text = readme.read_text(encoding="utf-8", errors="ignore")
        for phrase in REQUIRED_README_PHRASES + CURRENT_PRODUCT_PHRASES:
            if phrase not in text:
                add(errors, f"README missing required phrase: {phrase}")
        for phrase in ("guaranteed ROI", "investment advice", "uncontrolled autonomous deployment"):
            if phrase not in text:
                add(errors, f"README missing claim-boundary phrase: {phrase}")
        if "https://www.quebecartificialintelligence.com/shop" not in text:
            add(errors, "README missing required QUEBEC.AI shop URL")
    docs_to_check = [ROOT / rel for rel in REQUIRED_DOCS]
    for path in [ROOT / "README.md"] + docs_to_check:
        if not path.exists():
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        for target in MD_LINK_RE.findall(text):
            clean = target.strip().split()[0]
            parsed = urlparse(clean)
            if parsed.path and is_blocked_paid_or_private_artifact(parsed.path):
                add(errors, f"{rel}: links to blocked paid/private artifact {target}")
            if not target_exists(path, clean):
                add(errors, f"{rel}: broken internal Markdown link {target}")
        if rel in REQUIRED_DOCS and rel != "docs/GOALOS_DOCUMENTATION_INDEX.md":
            for heading in ("## Purpose", "## Current status", "## Key decisions", "## Files involved", "## What is public", "## What must remain private", "## Next actions", "## Validation checklist"):
                if heading not in text:
                    add(errors, f"{rel}: missing required operational section {heading}")
    if errors:
        print("Docs/tables/figures validation failed:", file=sys.stderr)
        for error in errors[:300]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Docs/tables/figures validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

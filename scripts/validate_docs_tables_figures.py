#!/usr/bin/env python3
"""Validate GoalOS docs, tables, figures, badges, links, and safe public boundaries."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from goalos_public_site_rules import is_blocked_paid_or_private_artifact

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CATALOG = DOCS / "data" / "goalos_catalog.yml"
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
    "docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md",
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
    "goalos_product_ladder.csv", "goalos_offer_status.csv", "goalos_claim_boundaries.csv",
    "goalos_public_site_pages.csv", "goalos_paid_file_policy.csv", "goalos_aep_standards.csv",
    "goalos_document_inventory.csv", "goalos_figure_inventory.csv", "goalos_asset_manifest.csv",
    "goalos_validation_rules.csv", "goalos_workflow_actions.csv", "goalos_proof_card_001_fields.csv",
    "goalos_professional_firm_packages.csv", "goalos_autonomous_website_actions.csv",
]
REQUIRED_FIGURES = [
    "goalos_recursive_workflow_loop", "goalos_product_ladder", "goalos_proof_led_revenue_loop",
    "goalos_public_site_architecture", "goalos_autonomous_github_actions_website_flow",
    "goalos_validation_architecture", "goalos_cloud_mvp_architecture",
    "goalos_enterprise_safety_boundary", "goalos_web3_hybrid_architecture", "goalos_proof_graph_concept",
]
REQUIRED_BADGES = [
    "goalos.svg", "proof-gradient.svg", "aep-standards.svg", "no-paid-artifacts.svg",
    "validation-v14.svg", "public-site-release-v8.svg", "cloud-mvp-0-2.svg", "quebec-ai.svg",
    "proof-bounded.svg", "no-model-self-modification.svg", "website-via-github-actions.svg",
]
README_SECTIONS = [
    "# Proof Gradient · GoalOS", "What this repository is", "What GoalOS is", "What Proof Gradient is",
    "Safe AI boundary", "Recursive workflow loop", "Product ladder", "AEP standards", "GoalOS Cloud MVP 0.2",
    "Public website release through autonomous GitHub Actions", "Validation and paid-file policy",
    "Repository map", "Documentation map", "Figures and tables", "Current status", "Next milestone: Proof Card 001",
    "How to validate locally", "How to contribute safely", "Claims boundary", "Shop / apply link",
]
PRODUCTS = [
    ("$49", "GoalOS AI Efficiency Sprint Kit", "v1.4"), ("$199", "GoalOS RSI Lite", "v1.6"),
    ("$997", "GoalOS Proof Room Lite / Department Pack", "v2.0"), ("$2,500+", "GoalOS RSI Sprint Workshop", "v7.0"),
    ("$9,500+", "GoalOS Proof Room Implementation Sprint", "v2.0"), ("$49,000+", "GoalOS Enterprise RSI Pilot", "v2.0"),
]
REQUIRED_PHRASES = [
    "GoalOS does not modify base AI models",
    "https://www.quebecartificialintelligence.com/shop",
    "The public website is generated and refreshed by autonomous GitHub Actions",
    "standards/AEP-###/complete-package.zip",
]


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def markdown_link_target(raw: str) -> str:
    """Return only the destination from a Markdown link target.

    Markdown permits destinations such as `file.zip?download=1`,
    `<file.zip#anchor>`, and `file.zip "title"`. Validation should classify
    the destination path, not optional link metadata.
    """
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1:target.index(">")].strip()
    return target.split()[0] if target.split() else ""


def artifact_check_target(target: str) -> str:
    """Strip URL query/fragment metadata before paid-artifact checks."""
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc:
        return parsed.path
    return target.split("#", 1)[0].split("?", 1)[0]


def local_link_exists(source: Path, target: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc or target.startswith("mailto:"):
        return True
    clean = artifact_check_target(target)
    if not clean:
        return True
    if clean.startswith("/"):
        candidate = ROOT / clean.lstrip("/")
    else:
        candidate = source.parent / clean
    return candidate.exists()


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required doc: {rel}")
    for name in REQUIRED_TABLES:
        if not (ROOT / "docs" / "tables" / name).is_file():
            errors.append(f"missing required table: docs/tables/{name}")
    for base in REQUIRED_FIGURES:
        for ext in (".mmd", ".svg"):
            if not (ROOT / "docs" / "figures" / f"{base}{ext}").is_file():
                errors.append(f"missing required figure file: docs/figures/{base}{ext}")
    for badge in REQUIRED_BADGES:
        if not (ROOT / "badges" / badge).is_file():
            errors.append(f"missing required badge: badges/{badge}")

    readme = text(ROOT / "README.md")
    for section in README_SECTIONS:
        if section not in readme:
            errors.append(f"README missing section/heading: {section}")
    for phrase in REQUIRED_PHRASES:
        if phrase not in readme:
            errors.append(f"README missing required phrase: {phrase}")
    for price, name, version in PRODUCTS:
        if price not in readme or version not in readme:
            errors.append(f"README missing current price/version for {name}: {price} {version}")

    combined_docs = readme + "\n" + "\n".join(text(p) for p in DOCS.rglob("*.md"))
    for phrase in REQUIRED_PHRASES[:2]:
        if phrase not in combined_docs:
            errors.append(f"documentation missing required phrase: {phrase}")

    product_csv = ROOT / "docs" / "tables" / "goalos_product_ladder.csv"
    if product_csv.exists():
        rows = list(csv.DictReader(product_csv.open(encoding="utf-8")))
        for price, name, version in PRODUCTS:
            if not any(r.get("Price") == price and r.get("Offer") == name and r.get("Version") == version for r in rows):
                errors.append(f"product ladder CSV missing {price} {name} {version}")

    for path in [ROOT / "README.md", *DOCS.rglob("*.md")]:
        rel = path.relative_to(ROOT).as_posix()
        content = text(path)
        for raw_target in MD_LINK_RE.findall(content):
            target = markdown_link_target(raw_target)
            check_target = artifact_check_target(target)
            if check_target and is_blocked_paid_or_private_artifact(check_target):
                errors.append(f"{rel}: links to blocked paid/private artifact {target}")
            if target and not local_link_exists(path, target):
                errors.append(f"{rel}: broken local link {target}")

    if CATALOG.exists():
        cat = text(CATALOG)
        for price, name, version in PRODUCTS:
            if price not in cat or name not in cat or version not in cat:
                errors.append(f"catalog missing current product tuple: {price} {name} {version}")
    else:
        errors.append("missing docs/data/goalos_catalog.yml")

    if errors:
        print("Docs/tables/figures validation failed:", file=sys.stderr)
        for error in errors[:250]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 250:
            print(f"... {len(errors)-250} more failures", file=sys.stderr)
        return 1
    print("Docs/tables/figures validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

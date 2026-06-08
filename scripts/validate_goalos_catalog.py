#!/usr/bin/env python3
"""Validate docs/data/goalos_catalog.yml against README, docs, tables, figures, and release policy."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

from goalos_public_site_rules import is_blocked_paid_or_private_artifact, normalize_rel, page_class

MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "data" / "goalos_catalog.yml"
PRODUCTS = [
    ("$49", "GoalOS AI Efficiency Sprint Kit", "v1.4"), ("$199", "GoalOS RSI Lite", "v1.6"),
    ("$997", "GoalOS Proof Room Lite / Department Pack", "v2.0"), ("$2,500+", "GoalOS RSI Sprint Workshop", "v7.0"),
    ("$9,500+", "GoalOS Proof Room Implementation Sprint", "v2.0"), ("$49,000+", "GoalOS Enterprise RSI Pilot", "v2.0"),
]
REQUIRED_DOCS = [
    "docs/GOALOS_DOCUMENTATION_INDEX.md", "docs/GOALOS_PRODUCT_LADDER.md", "docs/GOALOS_READY_TO_SELL_STATUS.md",
    "docs/GOALOS_PROOF_CARD_001_PLAN.md", "docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md",
    "docs/GOALOS_VALIDATION_HOTFIX_V14.md", "docs/GOALOS_PAID_ARTIFACT_POLICY.md",
    "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md", "docs/GOALOS_REPO_AUDIT.md",
    "docs/GOALOS_INSTITUTIONAL_POSITIONING.md", "docs/GOALOS_PUBLIC_STANDARD_STRATEGY.md",
    "docs/GOALOS_PROOF_GRAPH_CONCEPT.md", "docs/GOALOS_AEP_STANDARDS_INDEX.md",
]
REQUIRED_TABLES = [
    "goalos_product_ladder.csv",
    "goalos_offer_status.csv",
    "goalos_claim_boundaries.csv",
    "goalos_public_site_pages.csv",
    "goalos_paid_file_policy.csv",
    "goalos_aep_standards.csv",
    "goalos_document_inventory.csv",
    "goalos_figure_inventory.csv",
    "goalos_badge_inventory.csv",
    "goalos_asset_manifest.csv",
    "goalos_validation_rules.csv",
    "goalos_workflow_actions.csv",
    "goalos_proof_card_001_fields.csv",
    "goalos_professional_firm_packages.csv",
    "goalos_autonomous_website_actions.csv",
    "goalos_public_standard_strategy.csv",
]
REQUIRED_FIGURES = [
    "goalos_recursive_workflow_loop",
    "goalos_product_ladder",
    "goalos_proof_led_revenue_loop",
    "goalos_institutional_stack",
    "goalos_public_site_architecture",
    "goalos_autonomous_github_actions_website_flow",
    "goalos_validation_architecture",
    "goalos_cloud_mvp_architecture",
    "goalos_enterprise_safety_boundary",
    "goalos_web3_hybrid_architecture",
    "goalos_proof_graph_concept",
    "goalos_aep_standards_map",
]
REQUIRED_BADGES = [
    "goalos.svg",
    "proof-gradient.svg",
    "aep-standards.svg",
    "no-paid-artifacts.svg",
    "validation-v14.svg",
    "public-site-release-v8.svg",
    "cloud-mvp-0-2.svg",
    "quebec-ai.svg",
    "proof-bounded.svg",
    "no-model-self-modification.svg",
    "website-via-github-actions.svg",
    "proof-card-001-next.svg",
    "enterprise-rsi-boundary.svg",
    "recursive-workflow-os.svg",
    "aep-public-standard.svg",
]
OBSOLETE_CURRENT_PATTERNS = [
    r"v12[^\n]{0,40}is current", r"v13[^\n]{0,40}is current", r"old v8[^\n]{0,80}is current",
    r"Use goalos-public-site-release-v12\.yml for deployment",
]
MANUAL_BYPASS_PATTERNS = [r"manually bypass", r"manual public-site edits as the release path", r"upload paid buyer products to the public site"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def markdown_link_target(raw: str) -> str:
    """Return the path/URL component from a Markdown link target.

    The catalog validator must only send actual Markdown link destinations to
    the paid-artifact classifier. Parenthesized prose such as "(paid buyer
    products are excluded)" is not a public artifact link and should not be
    classified as a path.
    """
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")].strip()
    else:
        target = target.split()[0] if target.split() else ""
    return target


def artifact_check_target(target: str) -> str:
    """Strip Markdown URL query/fragment metadata before artifact checks."""
    from urllib.parse import urlparse

    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc:
        return parsed.path
    return target.split("#", 1)[0].split("?", 1)[0]


def catalog_string_list(catalog_text: str, key: str) -> list[str]:
    """Parse a top-level YAML string-list section from the catalog.

    The catalog validator is intentionally dependency-free, so this small parser
    only accepts the simple top-level list shape used for inventory sections:

    ``key:`` followed by indented ``- "value"`` entries. It does not treat
    raw substring matches elsewhere in the catalog as inventory membership.
    """
    values: list[str] = []
    in_section = False
    section_header = f"{key}:"

    for line in catalog_text.splitlines():
        stripped = line.strip()
        if not in_section:
            if line == section_header:
                in_section = True
            continue

        if line and not line.startswith((" ", "	")):
            break
        if not stripped or stripped.startswith("#"):
            continue
        if not stripped.startswith("-"):
            continue

        item = stripped[1:].strip()
        if " #" in item:
            item = item.split(" #", 1)[0].strip()
        if (item.startswith('"') and item.endswith('"')) or (item.startswith("'") and item.endswith("'")):
            item = item[1:-1]
        values.append(item)

    return values


def main() -> int:
    errors: list[str] = []
    if not CATALOG.exists():
        print("missing docs/data/goalos_catalog.yml", file=sys.stderr)
        return 1
    cat = read(CATALOG)
    readme = read(ROOT / "README.md")
    docs_text = "\n".join(read(p) for p in (ROOT / "docs").rglob("*.md"))
    corpus = readme + "\n" + docs_text

    for price, name, version in PRODUCTS:
        if price not in cat or name not in cat or version not in cat:
            errors.append(f"catalog missing product: {price} {name} {version}")
        for label, body in (("README", readme), ("documentation", corpus)):
            missing = [token for token in (price, name, version) if token not in body]
            if missing:
                errors.append(f"{label} missing current product tuple for {name}: {price} {name} {version}; missing {missing}")

    for phrase in [
        "GoalOS does not modify base AI models",
        "The public website is generated and refreshed by autonomous GitHub Actions",
        "https://www.quebecartificialintelligence.com/shop",
    ]:
        if phrase not in corpus:
            errors.append(f"missing required boundary phrase: {phrase}")

    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).exists():
            errors.append(f"missing required doc: {rel}")
    for table in REQUIRED_TABLES:
        if not (ROOT / "docs" / "tables" / table).exists():
            errors.append(f"missing required table: docs/tables/{table}")
    for fig in REQUIRED_FIGURES:
        if not (ROOT / "docs" / "figures" / f"{fig}.mmd").exists() or not (ROOT / "docs" / "figures" / f"{fig}.svg").exists():
            errors.append(f"missing required figure source/export for {fig}")
    catalog_badges = set(catalog_string_list(cat, "badge_inventory"))
    if not catalog_badges:
        errors.append("catalog missing top-level badge_inventory list")
    for badge in REQUIRED_BADGES:
        badge_path = f"badges/{badge}"
        if not (ROOT / "badges" / badge).exists():
            errors.append(f"missing required badge: {badge_path}")
        if badge_path not in catalog_badges:
            errors.append(f"catalog badge_inventory missing {badge_path}")

    product_csv = ROOT / "docs" / "tables" / "goalos_product_ladder.csv"
    if product_csv.exists():
        rows = list(csv.DictReader(product_csv.open(encoding="utf-8")))
        for price, name, version in PRODUCTS:
            if not any(r.get("Price") == price and r.get("Offer") == name and r.get("Version") == version for r in rows):
                errors.append(f"CSV contradicts catalog for {price} {name} {version}")

    for rel in ("site", "public"):
        base = ROOT / rel
        if not base.exists():
            continue
        for path in sorted(p for p in base.rglob("*") if p.is_file() and "_archive" not in p.parts):
            item = normalize_rel(path.relative_to(base))
            if is_blocked_paid_or_private_artifact(item):
                errors.append(f"{rel}/{item}: classified as {page_class(item)} and blocked from the public catalog")

    for path in [ROOT / "README.md", *list((ROOT / "docs").rglob("*.md"))]:
        rel = path.relative_to(ROOT).as_posix()
        body = read(path)
        for raw in MD_LINK_RE.findall(body):
            target = markdown_link_target(raw)
            check_target = artifact_check_target(target)
            if check_target and is_blocked_paid_or_private_artifact(check_target):
                errors.append(f"{rel}: public paid/private artifact link {target}")
        for pat in OBSOLETE_CURRENT_PATTERNS:
            if re.search(pat, body, flags=re.IGNORECASE):
                errors.append(f"{rel}: obsolete workflow appears to be listed as current: {pat}")
        lowered = body.lower()
        if "manual public-site edits as the release path" in lowered or "bypass autonomous github actions" in lowered:
            errors.append(f"{rel}: manual-site-edit guidance bypasses autonomous GitHub Actions")

    if errors:
        print("GoalOS catalog validation failed:", file=sys.stderr)
        for error in errors[:250]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 250:
            print(f"... {len(errors)-250} more failures", file=sys.stderr)
        return 1
    print("GoalOS catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

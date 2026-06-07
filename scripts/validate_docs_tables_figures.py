#!/usr/bin/env python3
"""Validate GoalOS documentation, tables, figures, and docs-only scope."""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "docs/GOALOS_REPO_AUDIT.md",
    "docs/GOALOS_DOCUMENTATION_INDEX.md",
    "docs/GOALOS_COMMERCIALIZATION_STATUS.md",
    "docs/GOALOS_RECURSIVE_WORKFLOW_OS.md",
    "docs/GOALOS_CLOUD_MVP_0_2.md",
    "docs/GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md",
    "docs/GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md",
    "docs/GOALOS_PAID_ARTIFACT_POLICY.md",
    "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md",
    "docs/GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md",
    "docs/GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md",
    "docs/GOALOS_ENGINEERING_ROADMAP.md",
    "docs/GOALOS_PROOF_CARD_001_PLAN.md",
    "docs/GOALOS_ENTERPRISE_RSI_PILOT_SUMMARY.md",
    "docs/GOALOS_DEPARTMENT_RSI_SUMMARY.md",
    "docs/GOALOS_BUYER_PRODUCTS_SUMMARY.md",
    "docs/GOALOS_WORLD_CLASS_FIRM_STACK.md",
]
REQUIRED_TABLES = [
    "goalos_product_ladder.csv", "goalos_offer_status.csv", "goalos_claim_boundaries.csv",
    "goalos_public_site_pages.csv", "goalos_paid_file_policy.csv", "goalos_aep_standards.csv",
    "goalos_document_inventory.csv", "goalos_asset_manifest.csv", "goalos_firm_stack.csv",
    "goalos_revenue_scenarios.csv", "goalos_roi_assumptions.csv",
]
REQUIRED_FIGURES = [
    "goalos_recursive_workflow_loop.mmd", "goalos_product_ladder.mmd",
    "goalos_public_site_architecture.mmd", "goalos_cloud_mvp_architecture.mmd",
    "goalos_proof_graph_concept.mmd", "goalos_enterprise_safety_boundary.mmd",
    "goalos_firm_stack.mmd", "goalos_commercialization_sequence.mmd",
]
FORBIDDEN_PREFIXES = ("site/", "public/", "web/", ".github/workflows/", "proof_gradient/", "migrations/", "tests/")
FORBIDDEN_FILES = {"index.html", "404.html", "START_HERE.html", "app.js", "styles.css", "Dockerfile", "docker-compose.yml", "pyproject.toml", "Makefile"}


def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"YAML parse failed for {path}: {exc}")


def links(path: Path) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8", errors="ignore"))


def changed_files() -> list[str]:
    result = subprocess.run(["git", "diff", "--name-only", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=False)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    errors: list[str] = []
    catalog_path = ROOT / "docs/data/goalos_catalog.yml"
    if not catalog_path.exists():
        errors.append("missing docs/data/goalos_catalog.yml")
        catalog = {}
    else:
        catalog = load_yaml(catalog_path)

    for doc in REQUIRED_DOCS:
        if not (ROOT / doc).exists():
            errors.append(f"missing required doc: {doc}")
    for table in REQUIRED_TABLES:
        path = ROOT / "docs/tables" / table
        if not path.exists():
            errors.append(f"missing required table: {table}")
        else:
            try:
                with path.open(newline="", encoding="utf-8") as f:
                    list(csv.DictReader(f))
            except Exception as exc:
                errors.append(f"CSV parse failed for {table}: {exc}")
    for fig in REQUIRED_FIGURES:
        if not (ROOT / "docs/figures" / fig).exists():
            errors.append(f"missing required Mermaid figure: {fig}")

    if catalog:
        products = catalog.get("product_ladder", [])
        with (ROOT / "docs/tables/goalos_product_ladder.csv").open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        for row, item in zip(rows, products):
            if (row.get("price"), row.get("offer"), row.get("version")) != (item.get("price"), item.get("name"), item.get("version")):
                errors.append(f"product table/catalog mismatch: {row}")
        safe = catalog["safe_ai_boundary"]["en"]
        for doc in [ROOT / "README.md", ROOT / "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md", ROOT / "docs/GOALOS_ENGINEERING_ROADMAP.md"]:
            if safe not in doc.read_text(encoding="utf-8"):
                errors.append(f"safe-boundary language missing in {doc.relative_to(ROOT)}")

    for link_file in [ROOT / "README.md", ROOT / "docs/GOALOS_DOCUMENTATION_INDEX.md"]:
        for url in links(link_file):
            if url.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (link_file.parent / url.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(f"broken local link in {link_file.relative_to(ROOT)}: {url}")

    paid_zip_pattern = re.compile(r"https?://[^\s)]+(?:buyer|paid|workshop|implementation|enterprise)[^\s)]*\.zip", re.I)
    for p in (ROOT / "docs").rglob("*"):
        if p.is_file() and p.suffix.lower() in {".md", ".csv", ".yml", ".yaml"}:
            if paid_zip_pattern.search(p.read_text(encoding="utf-8", errors="ignore")):
                errors.append(f"public paid ZIP link found in {p.relative_to(ROOT)}")

    for name in changed_files():
        if name.startswith(FORBIDDEN_PREFIXES) or Path(name).name in FORBIDDEN_FILES:
            errors.append(f"documentation-only scope violation: {name}")
        if name.startswith("assets/"):
            errors.append(f"asset edit is outside this docs-only scope: {name}")

    if errors:
        print("GoalOS docs validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    print("✅ GoalOS docs/tables/figures validation passed")


if __name__ == "__main__":
    main()

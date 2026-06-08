# GoalOS Documentation Index

This is the human-friendly map for Proof Gradient · GoalOS.

## 1. Start here

Begin with README.md, docs/data/goalos_catalog.yml, and this index.

## 2. Product ladder

See [GOALOS_PRODUCT_LADDER.md](GOALOS_PRODUCT_LADDER.md).

## 3. Ready-to-sell status

See [GOALOS_READY_TO_SELL_STATUS.md](GOALOS_READY_TO_SELL_STATUS.md).

## 4. Proof Card 001

See [GOALOS_PROOF_CARD_001_PLAN.md](GOALOS_PROOF_CARD_001_PLAN.md).

## 5. AEP standards

See ../standards/ and docs/tables/goalos_aep_standards.csv.

## 6. GoalOS Recursive Workflow OS

See [GOALOS_RECURSIVE_WORKFLOW_OS.md](GOALOS_RECURSIVE_WORKFLOW_OS.md).

## 7. Cloud MVP

See [GOALOS_CLOUD_MVP_0_2.md](GOALOS_CLOUD_MVP_0_2.md).

## 8. Public site and autonomous GitHub Actions

See [GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md](GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md).

## 9. Validation and CI

See [GOALOS_VALIDATION_HOTFIX_V14.md](GOALOS_VALIDATION_HOTFIX_V14.md).

## 10. Paid-file policy

See [GOALOS_PAID_ARTIFACT_POLICY.md](GOALOS_PAID_ARTIFACT_POLICY.md).

## 11. Figures

See docs/figures/ and docs/tables/goalos_figure_inventory.csv.

## 12. Tables

See docs/tables/ and docs/data/goalos_catalog.yml.

## 13. Asset system

See [GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md](GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md).

## 14. Legal/payment/support summary

See [GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md](GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md).

## 15. Tax/CFO summary

See [GOALOS_TAX_ACCOUNTING_CFO_SUMMARY.md](GOALOS_TAX_ACCOUNTING_CFO_SUMMARY.md).

## 16. Communications summary

See [GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md](GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md).

## 17. Professional-firm packages summary

See [GOALOS_PROFESSIONAL_FIRM_PACKAGES_SUMMARY.md](GOALOS_PROFESSIONAL_FIRM_PACKAGES_SUMMARY.md).

## 18. Web3 / AGI.eth / ASI.eth hybrid architecture

See [GOALOS_WEB3_HYBRID_ARCHITECTURE.md](GOALOS_WEB3_HYBRID_ARCHITECTURE.md).

## 19. Engineering roadmap

See [GOALOS_ENGINEERING_ROADMAP.md](GOALOS_ENGINEERING_ROADMAP.md).

## 20. Repository audit

See [GOALOS_REPO_AUDIT.md](GOALOS_REPO_AUDIT.md).


## Required operating frame

- **Purpose:** provide public-safe GoalOS / Proof Gradient guidance for this repository.
- **Current status:** aligned to `docs/data/goalos_catalog.yml`.
- **Source of truth:** `docs/data/goalos_catalog.yml`, then CSV tables in `docs/tables/`, then this explanatory document.
- **Key decisions:** public documentation can describe products and operating packs, but buyer deliverables remain off-repository and are sold through https://www.quebecartificialintelligence.com/shop.
- **Public/private boundaries:** no paid buyer ZIPs, private delivery kits, implementation bundles, enterprise pilot bundles, or commercialization packs may be exposed publicly.
- **Files involved:** README.md, docs/data/goalos_catalog.yml, docs/tables/*.csv, docs/figures/*.mmd, docs/figures/*.svg, scripts/*.py, .github/workflows/*.yml.
- **Validation commands:** `python scripts/check_no_paid_artifacts.py`; `python scripts/validate_goalos_public_site.py`; `python scripts/validate_docs_tables_figures.py`; `python scripts/validate_goalos_catalog.py`.
- **Autonomous website action commands:** use GitHub Actions, not manual public-site edits, when refreshing generated site content.
- **Next actions:** keep catalog, tables, docs, figures, badges, and validation aligned before every release.
- **Risk notes:** avoid unsupported claims and preserve v14 validation plus the public AEP package allowlist.

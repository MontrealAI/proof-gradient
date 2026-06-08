# GoalOS Documentation Index

This is the human-friendly map for Proof Gradient · GoalOS.

## 1. Start here

Begin with [README.md](../README.md), [docs/data/goalos_catalog.yml](data/goalos_catalog.yml), and this index.

## 2. Institutional thesis

See [GOALOS_INSTITUTIONAL_POSITIONING.md](GOALOS_INSTITUTIONAL_POSITIONING.md) and [GOALOS_PUBLIC_STANDARD_STRATEGY.md](GOALOS_PUBLIC_STANDARD_STRATEGY.md). The public line is: a model can answer, an agent can act, and an institution must prove.

## 3. Product ladder

See [GOALOS_PRODUCT_LADDER.md](GOALOS_PRODUCT_LADDER.md) and [goalos_product_ladder.csv](tables/goalos_product_ladder.csv).

## 4. Ready-to-sell status

See [GOALOS_READY_TO_SELL_STATUS.md](GOALOS_READY_TO_SELL_STATUS.md). Paid buyer products are sold through https://www.quebecartificialintelligence.com/shop, not from this public repository.

## 5. Proof Card 001

See [GOALOS_PROOF_CARD_001_PLAN.md](GOALOS_PROOF_CARD_001_PLAN.md).

## 6. AEP standards

See [docs/standards/](standards/) and [goalos_aep_standards.csv](tables/goalos_aep_standards.csv).

## 7. GoalOS Recursive Workflow OS

See [GOALOS_RECURSIVE_WORKFLOW_OS.md](GOALOS_RECURSIVE_WORKFLOW_OS.md).

## 8. Cloud MVP

See [GOALOS_CLOUD_MVP_0_2.md](GOALOS_CLOUD_MVP_0_2.md). GoalOS Cloud MVP 0.2 is public software proof, not a full enterprise SaaS.

## 9. Public site and autonomous GitHub Actions

See [GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md](GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md). Public website changes should flow through the autonomous release workflows.

## 10. Validation and CI

See [GOALOS_VALIDATION_HOTFIX_V14.md](GOALOS_VALIDATION_HOTFIX_V14.md), [validate_docs_tables_figures.py](../scripts/validate_docs_tables_figures.py), and [validate_goalos_catalog.py](../scripts/validate_goalos_catalog.py).

## 11. Paid-file policy

See [GOALOS_PAID_ARTIFACT_POLICY.md](GOALOS_PAID_ARTIFACT_POLICY.md). Public AEP ZIP packages are only allowed at `standards/AEP-###/complete-package.zip`.

## 12. Figures

See [docs/figures/](figures/) and [goalos_figure_inventory.csv](tables/goalos_figure_inventory.csv).

## 13. Tables

See [docs/tables/](tables/) and [docs/data/goalos_catalog.yml](data/goalos_catalog.yml).

## 14. Badges

See [badges/](../badges/) and [goalos_badge_inventory.csv](tables/goalos_badge_inventory.csv). Badges are static SVGs and must not imply certification, guaranteed outcomes, AGI, ASI, or full SaaS completion.

## 15. Asset system

See [GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md](GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md) and [goalos_asset_manifest.csv](tables/goalos_asset_manifest.csv).

## 16. Legal/payment/support summary

See [GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md](GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md).

## 17. Tax/CFO summary

See [GOALOS_TAX_ACCOUNTING_CFO_SUMMARY.md](GOALOS_TAX_ACCOUNTING_CFO_SUMMARY.md).

## 18. Communications summary

See [GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md](GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md).

## 19. Professional-firm packages summary

See [GOALOS_PROFESSIONAL_FIRM_PACKAGES_SUMMARY.md](GOALOS_PROFESSIONAL_FIRM_PACKAGES_SUMMARY.md).

## 20. Web3 / AGI.eth / ASI.eth hybrid architecture

See [GOALOS_WEB3_HYBRID_ARCHITECTURE.md](GOALOS_WEB3_HYBRID_ARCHITECTURE.md).

## 21. Engineering roadmap

See [GOALOS_ENGINEERING_ROADMAP.md](GOALOS_ENGINEERING_ROADMAP.md) and [../ROADMAP.md](../ROADMAP.md).

## 22. Repository audit

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

## Proof Graph and AEP index additions

- [GoalOS Proof Graph Concept](GOALOS_PROOF_GRAPH_CONCEPT.md)
- [GoalOS AEP Standards Index](GOALOS_AEP_STANDARDS_INDEX.md)
- [GoalOS public standard strategy table](tables/goalos_public_standard_strategy.csv)
- [GoalOS institutional stack figure](figures/goalos_institutional_stack.svg)
- [GoalOS AEP standards map figure](figures/goalos_aep_standards_map.svg)

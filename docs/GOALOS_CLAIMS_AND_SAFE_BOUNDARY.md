# GoalOS Claims and Safe Boundary

Allowed: proof-led recursive workflow improvement; Enterprise RSI without model self-modification; workflow-level evaluation, approval, versioning, monitoring, and rollback.

Not allowed: guaranteed ROI, guaranteed revenue, guaranteed productivity, investment returns, legal advice, financial advice, tax advice, compliance certification, AI safety certification, autonomous AGI, achieved AGI, achieved ASI, base-model self-modification, or uncontrolled autonomous deployment.

Safe boundary: GoalOS does not modify base AI models; it improves workflows around AI.

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

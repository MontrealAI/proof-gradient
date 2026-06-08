# GoalOS Validation Hotfix v14

v14 is current. v12 is obsolete. v13 is obsolete. Old v8 obsolete compatibility validation should not be used as the current path.

Canonical pages require exactly one shell/footer. Standalone proof and microsite pages are separate. App pages are separate. Public AEP packages are allowed only at `standards/AEP-###/complete-package.zip`. Paid/private artifacts remain blocked.

Current recommended workflows: GoalOS Validation Hotfix v14 Microsite Compatibility; GoalOS Public Site Release v8 Intelligent Assets; Validate GoalOS Public Site v8 only if updated to use v14 shared rules.

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

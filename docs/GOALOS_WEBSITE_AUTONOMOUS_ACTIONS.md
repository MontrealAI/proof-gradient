# GoalOS Website Autonomous Actions

The website is updated through autonomous GitHub Actions. Do not manually upload paid buyer products to the public site. Do not manually bypass the release workflows for public-site changes.

Use the autonomous deployment workflow that implements **GoalOS Public Site Release v8 Intelligent Assets** for public-site refresh; do not treat validate-only compatibility workflows as deploy workflows. Use **GoalOS Validation Hotfix v14 Microsite Compatibility** as the current validation fix. Do not run v12 or v13. Do not run obsolete v8 compatibility validation as the current path. If site content needs product ladder changes, update `docs/data/goalos_catalog.yml` and relevant action/template sources first, then run the correct GitHub Action and validate after release.

## Recommended workflow order

1. GoalOS Validation Hotfix v14 Microsite Compatibility
2. Actual autonomous deployment workflow for GoalOS Public Site Release v8 Intelligent Assets, not the validate-only compatibility workflow
3. Validate GoalOS Public Site v8, only if it uses current shared v14 rules
4. Check No Paid Artifacts
5. Validate GoalOS Docs, Tables, Figures

## Non-technical operator section

- Go to GitHub repository.
- Open Actions.
- Run the current workflow.
- Do not rerun obsolete workflows.
- Green check = success.
- Red X = inspect logs or escalate.

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

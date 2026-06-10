# Repository Index

This index orients contributors to the current Proof Gradient · GoalOS repository layout. For canonical GoalOS product/status facts, start with `docs/data/goalos_catalog.yml` and `docs/GOALOS_DOCUMENTATION_INDEX.md`.

## Start here

- `README.md` — public repository entry point, commercial thesis, claims boundary, validation commands, and documentation map.
- `docs/GOALOS_DOCUMENTATION_INDEX.md` — official GoalOS documentation navigation map.
- `docs/quickstart.md` — local install, demo, API, validation, and test workflow.
- `QA_VERIFICATION.md` — current validation state and merge-readiness notes.
- `CONTRIBUTING.md` — contribution rules and public/private artifact boundary.
- `SECURITY.md` — responsible disclosure, secret handling, proof-card privacy, and validation.

## Core Python package

- `proof_gradient/api.py` — FastAPI application and HTTP endpoints.
- `proof_gradient/cli.py` — `proof-gradient` command-line interface.
- `proof_gradient/db.py` — database session, initialization, and reset helpers.
- `proof_gradient/models.py` — SQLAlchemy persistence models.
- `proof_gradient/services.py` — tenant/user creation and Run Fabric demo orchestration.
- `proof_gradient/security.py` — public-safe claim and boundary checks.
- `proof_gradient/foundation.py` — foundation artifact builder used by the module demo.

## Tests and validation

- `tests/` — current pytest/unittest-compatible test suite.
- `tests_legacy_skillos/` — preserved legacy SkillOS tests.
- `scripts/check_no_paid_artifacts.py` — paid/private artifact guard.
- `scripts/validate_goalos_catalog.py` — canonical catalog validation.
- `scripts/validate_docs_tables_figures.py` — documentation, CSV table, and figure consistency validation.
- `scripts/validate_goalos_public_site.py` — generated public-site policy validation.
- `scripts/qa_check.py` — legacy full QA harness that also exercises SkillOS compatibility paths.

## GoalOS documentation and governance

- `docs/data/goalos_catalog.yml` — source of truth for GoalOS status, offer, validation, and public/private artifact facts.
- `docs/GOALOS_PRODUCT_LADDER.md` — public product ladder.
- `docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md` — safe claims and prohibited claims.
- `docs/GOALOS_PAID_ARTIFACT_POLICY.md` — paid-file and public repository boundary.
- `docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md` — autonomous website release process.
- `docs/GOALOS_REPO_AUDIT.md` — repository audit and risk notes.
- `docs/GOALOS_ENGINEERING_ROADMAP.md` — engineering roadmap and required operating frame.

## API and operator docs

- `docs/api_reference.md` — current Proof Gradient API reference.
- `docs/api.md` — concise implemented endpoint list.
- `docs/cli.md` — CLI command list.
- `docs/deployment.md` — local Docker deployment note.
- `docs/architecture.md` — Proof Gradient production architecture overview.

## Public website and assets

- `site/` — generated/public site source tree used by validators and release workflows.
- `web/` — lightweight web app assets.
- `badges/` — truthful static status badges.
- `assets/` — public-safe image and brand assets.
- `docs/figures/` — Mermaid figure sources and committed SVG companions.
- `docs/tables/` — CSV source tables that mirror canonical documentation facts.

## Standards, schemas, and releases

- `docs/standards/` — AEP standard documentation.
- `schemas/` — machine-readable schemas.
- `releases/AEP-001/` — public AEP-001 release package.
- `migrations/` — Alembic database migration environment and versions.

## Automation entry points

- `Makefile` — common local commands for demo, API serving, tests, and public-site checks.
- `.github/workflows/tests.yml` — CI tests and JavaScript syntax check.
- `.github/workflows/pages.yml` — command-center GitHub Pages build/verify/deploy path.
- `COPY_PASTE_GITHUB_ACTIONS/` — preserved workflow templates.

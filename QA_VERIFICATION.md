# QA Verification — GoalOS v10

Required checks:

- `python scripts/validate_goalos_catalog.py`
- `python scripts/check_no_paid_artifacts.py`
- `python scripts/validate_docs_tables_figures.py`
- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`
- `pytest`

Current release notes and skipped tooling are documented in `docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md` and `docs/GOALOS_REPO_AUDIT.md`.

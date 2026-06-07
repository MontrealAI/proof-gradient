# QA verification

Required v10 checks:

```bash
pytest
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

Skipped tests must be documented in `docs/GOALOS_REPO_AUDIT.md` and `docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md`.

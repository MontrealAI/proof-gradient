# QA Verification

## Current validation state

GoalOS Validation Hotfix v14 Microsite Compatibility is current. v12, v13, and old v8 compatibility validation are obsolete and must not be used as the current path.

## Required commands

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Paid-file guard

The paid-file guard blocks public paid/private artifacts and preserves the narrow public AEP package allowlist: `standards/AEP-###/complete-package.zip`.

## Website autonomous action workflow

Use GitHub Actions in this order when refreshing the public site:

1. GoalOS Validation Hotfix v14 Microsite Compatibility.
2. GoalOS Public Site Release v8 Intelligent Assets.
3. Validate GoalOS Public Site v8, only if it uses shared v14 rules.
4. Check No Paid Artifacts.
5. Validate GoalOS Docs, Tables, Figures.

Do not manually upload paid buyer products to GitHub Pages.

## Optional checks

Run `pytest`, `make test`, and `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs` when available. If unavailable, document the environment limitation in `docs/GOALOS_REPO_AUDIT.md` and PR notes.

## Optional test-client dependency note

`pytest` and `make test` exercise FastAPI/Starlette test-client code. In a fresh environment, install the compatible transport package before treating optional Python test failures as product regressions:

```bash
python -m pip install httpx
pytest
make test
```

Current run note: before `httpx` was installed, both Python test commands failed at import time with the Starlette/FastAPI test-client dependency missing. After installing `httpx`, both commands passed.

# QA Verification

## Current validation state

GoalOS Validation Hotfix v14 Microsite Compatibility is current. v12, v13, and old v8 compatibility validation are obsolete and must not be used as the current path.

## Required commands

Prefer the aggregate Make target:

```bash
make validate
```

The target runs the required guardrail commands:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```


## Current branch verification — 2026-06-10

Documentation and developer-command refresh validated the current public-safe guardrail path with `make validate`. A direct `pytest` run initially stopped during collection because this environment did not have the Starlette test-client transport packages (`httpx2`/`httpx`) installed. After installing the project development extras with `python -m pip install -e ".[dev]"`, `pytest` passed with 85 tests and 2 FastAPI/Starlette deprecation warnings.

## Merge-readiness result — 2026-06-09

Final repository validation for the institutional upgrade used the required GoalOS guardrail commands, the GoalOS Cloud MVP Node test, and optional Python test suites. The only environment note was the need to install `httpx2` and `httpx` locally before running FastAPI/Starlette test-client tests; after installation, `pytest` and `make test` both passed.

## Current branch verification — 2026-06-09

On `feature/goalos-official-documentation-system-refresh`, the required GoalOS validators passed against the refreshed README, catalog, documentation index, GoalOS/$JOBS/commercialization docs, CSV tables, Mermaid/SVG figures, badges, CI workflow definitions, paid-file guard, and 207-page public site. npm/Solidity checks were skipped because the repository root has no `package.json` and no local $JOBS contract package.


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
python -m pip install httpx2 httpx
pytest
make test
```

Current run note for 2026-06-09: `pytest` and `make test` first failed at import time because the local environment lacked `httpx2`/`httpx`. After `python -m pip install httpx2 httpx`, `pytest` passed with 85 tests and 2 warnings, and `make test` passed with 56 unittest tests.

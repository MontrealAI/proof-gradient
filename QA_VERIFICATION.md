# QA Verification

## Current validation baseline

Use **GoalOS Validation Hotfix v14 Microsite Compatibility** as the current validation baseline. Do not treat v12, v13, or old v8 compatibility validation as current.

## Required commands

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Optional checks when available

```bash
pytest
make test
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

## Paid-file guard

The paid-file guard must pass before release. Public AEP standard packages are allowed only at `standards/AEP-###/complete-package.zip`; paid buyer ZIPs, workshop bundles, implementation bundles, enterprise pilot bundles, and private delivery kits are blocked from public deploy roots.

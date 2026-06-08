# QA Verification

## Required GoalOS validation commands

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Current validation baseline

- Current: GoalOS Validation Hotfix v14 Microsite Compatibility.
- Obsolete as current references: v12, v13, and obsolete v8 compatibility validation.
- Canonical pages require one canonical shell and footer.
- Standalone proof/microsite pages may use standalone metadata and a visible `/proof-gradient/` escape link.
- App pages may use app shell.
- Public AEP packages are allowed only at `standards/AEP-###/complete-package.zip`.
- Paid/private artifacts are blocked from public deploy roots.

## Optional tests when tooling is available

```bash
pytest
make test
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

If a tool is unavailable, document the skip in `docs/GOALOS_REPO_AUDIT.md`.

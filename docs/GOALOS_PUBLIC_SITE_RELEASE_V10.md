# GoalOS Public Site Release v10

GoalOS Public Site Release v10 unifies the public site shell, product ladder, docs, figures, tables, asset manifest, QUEBEC.AI ⚜️✨ seal usage, paid-artifact guard, and GitHub Actions.

## Validation

- `python scripts/validate_goalos_catalog.py`
- `python scripts/check_no_paid_artifacts.py`
- `python scripts/validate_docs_tables_figures.py`
- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`

## Skipped tooling

Mermaid CLI (`mmdc`) was not available locally; SVG files are fallback documentation stubs linked to `.mmd` source.

## Safe boundary

GoalOS does not modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback.

GoalOS ne modifie pas les modèles IA de base. GoalOS améliore les flux autour de l’IA grâce aux instructions, prompts, mémoire, grilles de score, dossiers de preuve, évaluations, approbations, versions, surveillance et rollback.

## QA results for this branch

Passed locally after installing the missing `httpx2` test dependency for Starlette/FastAPI tests:

- `python scripts/validate_goalos_catalog.py`
- `python scripts/check_no_paid_artifacts.py`
- `python scripts/validate_docs_tables_figures.py`
- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`
- `make test`
- `python -m pytest`

The direct `pytest` console entrypoint failed in this environment because it did not include the repository root on `sys.path`; `python -m pytest` passed with 72 tests and 2 deprecation warnings.

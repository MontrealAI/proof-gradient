# GoalOS Repository Audit

Audit date: 2026-06-08. No files were deleted during audit.

## 1. Repository structure

Top-level areas include `.github/workflows/`, `assets/`, `badges/`, `data/`, `docs/`, `proof_gradient/`, `schemas/`, `scripts/`, `site/`, `standards/`, `tests/`, and root governance docs.

## 2. Current README state

README was refreshed into the official Proof Gradient · GoalOS public entry point with badge row, thesis, safe boundary, product ladder, validation commands, repository map, docs map, and shop boundary.

## 3. Current docs state

Core GoalOS docs now exist under `docs/`, with `docs/GOALOS_DOCUMENTATION_INDEX.md` as the human-friendly map and `docs/data/goalos_catalog.yml` as source of truth.

## 4. Current figures state

Required Mermaid sources and SVG companions are present under `docs/figures/`. SVGs are lightweight committed exports; Mermaid source remains the editable diagram source.

## 5. Current tables state

Required CSV tables are present under `docs/tables/` and match the catalog product ladder, validation status, paid-file policy, action order, docs inventory, and figure inventory.

## 6. Current badge state

Static truthful SVG badges are present under `badges/` and used by README. No badge claims a failing workflow, full SaaS completion, certification, guaranteed ROI, AGI, ASI, or model self-modification.

## 7. Current GitHub Actions state

Documentation CI workflows exist for docs/tables/figures, paid artifact guard, and catalog validation. Autonomous website release workflows are preserved.

## 8. Current public site state

The public site remains under `site/` and is not manually rewritten as the main delivery method. Public-site changes should go through autonomous GitHub Actions.

## 9. Current autonomous website release workflows

Current path: GoalOS Validation Hotfix v14 Microsite Compatibility, the actual autonomous deployment workflow for GoalOS Public Site Release v8 Intelligent Assets, Validate GoalOS Public Site v8 if using shared v14 rules, Check No Paid Artifacts, Validate GoalOS Docs, Tables, Figures. Validate-only compatibility workflows must not be used as deployment workflows.

## 10. Current validation state

GoalOS Validation Hotfix v14 Microsite Compatibility is current. v12, v13, and old v8 compatibility validation are obsolete and documented as obsolete.

## 11. Current AEP standards state

AEP standards are preserved. Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.

## 12. Current schemas state

Schemas are preserved and not rewritten by this documentation refresh.

## 13. Current tests state

Existing tests are preserved. Required validation commands were run locally; optional test availability is documented below.

## 14. Current assets state

QUEBEC.AI assets and public site assets are preserved. New badges and documentation figures were added.

## 15. Paid/private artifact findings

No paid buyer product was uploaded by this work. Public route for buyers is https://www.quebecartificialintelligence.com/shop. Paid-file guard remains the enforcement path.

## 16. Obsolete workflow findings

v12, v13, and old v8 compatibility validation existed as confusing historical references. This refresh documents them as obsolete and updates selected names/validation paths to avoid presenting them as current.

## 17. Broken-link findings

Internal docs links are validated by `scripts/validate_docs_tables_figures.py`.

## 18. Stale pricing/version findings

Catalog and tables use current ladder: $49 v1.4, $199 v1.6, $997 v2.0, $2,500+ v7.0, $9,500+ v2.0, $49,000+ v2.0.

## 19. Missing documentation findings

Required GoalOS docs were created or refreshed.

## 20. Missing figures/tables findings

Required figures and tables were created or refreshed.

## 21. Files to preserve

AEP standards, schemas, scripts, tests, public site, `proof_gradient` package, site validation hotfix logic, public AEP allowlist, QUEBEC.AI seal/assets, public proof pages/microsites, and autonomous website release workflows.

## 22. Files to update

README.md, docs, docs/data, docs/figures, docs/tables, badges, validation scripts, documentation workflows, root governance docs, repository maps, and manifests.

## 23. Files not to touch

Paid buyer products, private delivery materials, generated public site pages as a manual rewrite path, and preserved standards/schemas/tests/assets except validation metadata or references.

## 24. Risks before merge

Main risk is future drift between catalog, tables, README, docs, and autonomous site templates. Run validation before every PR.

## 25. Commands run

- `find . -maxdepth 3 -type f` for structure audit.
- `sed -n` on README and validation scripts.
- `python /tmp/generate_goalos_docs.py` to generate docs/tables/figures/badges.
- `python scripts/check_no_paid_artifacts.py`.
- `python scripts/validate_goalos_public_site.py`.
- `python scripts/validate_docs_tables_figures.py`.
- `python scripts/validate_goalos_catalog.py`.
- `python -m pip install httpx` to satisfy the local Starlette/FastAPI test-client dependency.
- `pytest`.
- `make test`.
- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`.

## 26. Tests skipped and why

Mermaid CLI SVG export was not required because committed SVG companions were generated directly and editable `.mmd` sources are present. No required validation command was skipped.

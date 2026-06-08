# GoalOS Repository Audit

Audit date: 2026-06-08. Branch: feature/goalos-docs-readme-figures-tables-badges-release.

## 1. Repository structure

Top-level structure includes `README.md`, `docs/`, `site/`, `schemas/`, `scripts/`, `tests/`, `badges/`, `assets/`, `.github/workflows/`, `proof_gradient`/`skillos` package code, and public standards/releases.

## 2. Current README state

README has been refreshed into the official Proof Gradient · GoalOS public entry point with badges, product ladder, safe boundary, validation, repository map, documentation map, and current status.

## 3. Current docs state

`docs/` contains 595 files. Required GoalOS docs and `docs/GOALOS_DOCUMENTATION_INDEX.md` are present.

## 4. Current figures state

`docs/figures/` contains Mermaid sources and SVG exports for the required GoalOS architecture diagrams. Mermaid CLI export was not required because lightweight accessible SVGs were generated directly from the same node sequences.

## 5. Current tables state

`docs/tables/` contains CSV tables for the product ladder, claims, site pages, paid-file policy, standards, docs, figures, assets, validation, workflows, Proof Card 001, and professional packages.

## 6. Current badge state

`badges/` contains static SVG badges, including GoalOS, Proof Gradient, AEP Standards, Validation v14, Cloud MVP 0.2, QUEBEC.AI, proof-bounded, no paid artifacts, and no model self-modification.

## 7. Current workflows/actions state

`.github/workflows/` contains 145 workflow files. New/updated dependency-light workflows run docs/tables/figures validation, catalog validation, public-site validation, and paid-file guard checks. v12/v13 hotfix workflows are documented as obsolete.

## 8. Current public site state

`site/` remains the public deploy root with canonical pages, proof/microsite pages, app pages, assets, standards, and GoalOS Cloud MVP 0.2.

## 9. Current AEP standards state

AEP-001 through AEP-008 are documented as public standards. Public AEP packages remain allowed only at `standards/AEP-###/complete-package.zip`.

## 10. Current schemas state

`schemas/` contains 7 public schemas and is preserved.

## 11. Current tests state

`tests/` contains 17 test files. Node tests exist for the Cloud MVP.

## 12. Current assets state

`assets/` contains 55 files including QUEBEC.AI identity assets. No deletion performed.

## 13. Current paid-file guard state

`scripts/check_no_paid_artifacts.py` scans public deploy roots and blocks paid/private artifacts while preserving the narrow public AEP package allowlist.

## 14. Obsolete workflow findings

`goalos-validation-hotfix-v12.yml`, `goalos-validation-hotfix-v13-no-pytest.yml`, and old v8 validation labels are obsolete for current validation. Use GoalOS Validation Hotfix v14 Microsite Compatibility.

## 15. Broken-link findings

Internal README/docs links are validated by `scripts/validate_docs_tables_figures.py`. Broken links should be fixed before merge.

## 16. Stale pricing/version findings

The source of truth is now `docs/data/goalos_catalog.yml`: $49 v1.4, $199 v1.6, $997 v2.0, $2,500+ v7.0, $9,500+ v2.0, $49,000+ v2.0; Cloud MVP 0.2; validation v14; site release v8.

## 17. Missing documentation findings

Required GoalOS docs were added or refreshed.

## 18. Missing figures/tables findings

Required figure sources/SVGs and CSV tables were added.

## 19. Files to preserve

Preserve AEP standards, schemas, scripts, tests, public site, package code, site validation hotfix logic, public AEP package allowlist, QUEBEC.AI seal/assets, and public proof pages/microsites.

## 20. Files to update

Update README, GoalOS docs, `docs/data/goalos_catalog.yml`, `docs/tables/`, `docs/figures/`, `badges/`, validation scripts, and validation workflows when public product or validation facts change.

## 21. Files not to touch

Do not upload or expose paid buyer ZIPs, workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, private commercial packs, private evidence, buyer data, or private professional-firm package ZIPs.

## 22. Risks before merge

Risks: stale product copy outside the new docs, obsolete workflows still visible in history, and environment-specific test availability. Mitigation: run validation commands, keep v14 as current, and document skipped checks honestly.

## Test/tool availability notes

- Mermaid CLI was not used; SVGs were generated directly and `.mmd` sources are committed.
- Dependency-free Python validation scripts are expected to run in CI.
- If `pytest`, `make`, or Node are unavailable locally, record that limitation in the PR/test notes.

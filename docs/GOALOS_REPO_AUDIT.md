# GoalOS Repository Audit

Audit date: 2026-06-08.

## Purpose
Audit the repository before and after the GoalOS documentation refresh so merge risk is visible.

## Current status
Audit updated for the README/docs/figures/tables/badges/validation refresh.

## Key decisions
- Preserve AEP standards, schemas, scripts, tests, public site, validation hotfix logic, public AEP package allowlist, QUEBEC.AI assets, and proof pages.
- Treat `docs/data/goalos_catalog.yml` as the documentation source of truth.
- Use GoalOS Validation Hotfix v14 Microsite Compatibility as the current validation baseline.

## Files involved
- `README.md`
- `docs/`
- `docs/data/goalos_catalog.yml`
- `docs/figures/`
- `docs/tables/`
- `badges/`
- `scripts/`
- `.github/workflows/`

## What is public
Public docs, public standards, public schemas, public examples, public proof pages, public site assets, and public AEP packages matching `standards/AEP-###/complete-package.zip`.

## What must remain private
Paid buyer ZIPs, paid digital products, paid workshop bundles, buyer/facilitator delivery kits, implementation bundles, enterprise pilot bundles, commercialization packs, professional-firm ZIP payloads, and private buyer evidence.

## Next actions
Run validation, publish Proof Card 001 when approved, and keep obsolete v12/v13 validation references clearly marked as obsolete.

## Validation checklist
- [ ] README current.
- [ ] Docs index current.
- [ ] Catalog, tables, figures, and badges present.
- [ ] Paid-file guard passes.
- [ ] Public-site validation passes.

## 1. Repository structure
Top-level structure includes README, docs, scripts, schemas, site, tests, proof_gradient package, assets, workflows, and GitHub Pages support files.

## 2. Current README state
README has been refreshed as the official Proof Gradient · GoalOS entry point with badges, product ladder, safe boundary, validation commands, and repository map.

## 3. Current docs state
GoalOS operational docs now use `docs/GOALOS_DOCUMENTATION_INDEX.md` as the human map and `docs/data/goalos_catalog.yml` as source of truth.

## 4. Current figures state
Required Mermaid sources and SVG exports exist under `docs/figures/`. SVGs were generated as lightweight static accessible diagrams without requiring Mermaid CLI.

## 5. Current tables state
Required CSV tables exist under `docs/tables/` and mirror catalog products, standards, rules, and inventories.

## 6. Current badge state
Static SVG badges exist under `badges/` and avoid workflow status claims.

## 7. Current workflows/actions state
New or updated workflows validate docs/tables/figures, paid artifacts, catalog, and public site with dependency-free Python where possible. Existing older v12/v13/v8 workflows remain in history but are documented as obsolete references.

## 8. Current public site state
`site/` remains the public GitHub Pages root; v8 Intelligent Assets is the current site release baseline.

## 9. Current AEP standards state
AEP-001 through AEP-008 remain public standards. Public AEP complete packages are allowed only at `standards/AEP-###/complete-package.zip` inside public deploy roots.

## 10. Current schemas state
Existing JSON schemas under `schemas/` are preserved.

## 11. Current tests state
Existing pytest tests and the GoalOS Cloud MVP Node test are preserved. Paid-artifact regression tests were expanded for current buyer ZIP names.

## 12. Current assets state
QUEBEC.AI seal/assets and public site assets are preserved; new static badges and diagrams are public-safe assets.

## 13. Current paid-file guard state
`scripts/check_no_paid_artifacts.py` remains strict and delegates artifact classification to `scripts/goalos_public_site_rules.py`.

## 14. Obsolete workflow findings
Validation v12, v13, and obsolete v8 compatibility workflows are not current. Current docs direct users to GoalOS Validation Hotfix v14 Microsite Compatibility.

## 15. Broken-link findings
Internal docs links are checked by `scripts/validate_docs_tables_figures.py`; no broken internal Markdown links remained after this refresh.

## 16. Stale pricing/version findings
Current prices and versions are centralized in `docs/data/goalos_catalog.yml`: $49 v1.4, $199 v1.6, $997 v2.0, $2,500+ v7.0, $9,500+ v2.0, $49,000+ v2.0, Cloud MVP 0.2, validation v14.

## 17. Missing documentation findings
Core GoalOS docs were missing or inconsistent; this refresh creates/updates required operational docs.

## 18. Missing figures/tables findings
Required figures, SVG exports, and CSV source tables were missing or incomplete; this refresh adds them.

## 19. Files to preserve
Preserve AEP standards, schemas, scripts, tests, public site, `proof_gradient` package, validation hotfix logic, public AEP allowlist, QUEBEC.AI seal/assets, and public proof pages/microsites.

## 20. Files to update
README, GoalOS docs, catalog, tables, figures, badges, validation scripts, validation workflows, SECURITY, CONTRIBUTING, ROADMAP, QA verification, file tree, and manifest.

## 21. Files not to touch
Do not delete useful code, schemas, tests, public proof pages, public site assets, or AEP materials. Do not upload buyer ZIPs or private bundles.

## 22. Risks before merge
- Some legacy workflows remain numerous and may confuse users; docs identify v14 as current.
- Full pytest requires Python dependencies such as FastAPI/Pydantic; if not installed, run dependency installation before treating pytest as release-blocking.
- `make test` may depend on the local environment.
- Mermaid CLI is not required because SVG exports are committed as static SVG files.

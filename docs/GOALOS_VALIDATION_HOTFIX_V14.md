# GoalOS Validation Hotfix v14 Microsite Compatibility

## Purpose

Explain the current validation architecture.

## Current status

v14 is current. v12 and v13 are obsolete.

## Key decisions

Canonical pages require shell/footer; standalone proof/microsite pages do not require the marketing shell; new pages should be marked; app pages can use an app shell; public AEP packages are allowed only at `standards/AEP-###/complete-package.zip`; paid/private artifacts are blocked.

## Files involved

- `README.md`
- `docs/data/goalos_catalog.yml`
- `docs/tables/`
- `docs/figures/`
- `scripts/check_no_paid_artifacts.py`
- `scripts/validate_goalos_public_site.py`
- `scripts/validate_docs_tables_figures.py`
- `scripts/validate_goalos_catalog.py`


## What is public

Public: standards, public docs, schemas, examples, public proof pages, public site assets, product names, safe status language, and shop/application links to QUEBEC.AI.

## What must remain private

Private: paid buyer ZIPs, workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, commercial operating packs, buyer data, private evidence, and private professional-firm package ZIPs.

## Next actions

Rename or document obsolete workflows as obsolete and keep shared validation scripts as the source of truth.


## Use / avoid

Use: GoalOS Validation Hotfix v14 Microsite Compatibility. Avoid: v12, v13, and obsolete v8 compatibility validation.

![Validation architecture](figures/goalos_validation_architecture.svg)

## Validation checklist

- [ ] Safe AI boundary is present.
- [ ] Product names, prices, and versions match `docs/data/goalos_catalog.yml`.
- [ ] Paid buyer files are not uploaded or linked.
- [ ] Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.
- [ ] `python scripts/check_no_paid_artifacts.py` passes.
- [ ] `python scripts/validate_docs_tables_figures.py` passes.
- [ ] `python scripts/validate_goalos_catalog.py` passes.


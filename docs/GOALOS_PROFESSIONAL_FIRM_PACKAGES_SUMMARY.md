# GoalOS Professional Firm Packages Summary

## Purpose

Summarize the professional-firm package categories without publishing private packs.

## Current status

Professional-firm packages exist for operating readiness; private ZIPs are not public site artifacts.

## Key decisions

Categories: Tax / Accounting / CFO; Privacy / Data Protection; Security / SOC 2 / Trust Center; IP / Trademark / Licensing; UX / CRO / Buyer Journey; Enterprise Sales / GTM; RevOps / Analytics; Brand / Design System; Growth Marketing; Accessibility / Bilingual Localization; Insurance / Commercial Risk; Enterprise Procurement / Trust Center; Independent Proof Audit / Evaluation.

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

Keep summaries public, route professional engagement privately, and do not publish package ZIPs.


## Package table

See `docs/tables/goalos_professional_firm_packages.csv`.

## Validation checklist

- [ ] Safe AI boundary is present.
- [ ] Product names, prices, and versions match `docs/data/goalos_catalog.yml`.
- [ ] Paid buyer files are not uploaded or linked.
- [ ] Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.
- [ ] `python scripts/check_no_paid_artifacts.py` passes.
- [ ] `python scripts/validate_docs_tables_figures.py` passes.
- [ ] `python scripts/validate_goalos_catalog.py` passes.


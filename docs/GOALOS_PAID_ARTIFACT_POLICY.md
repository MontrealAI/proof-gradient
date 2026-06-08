# GoalOS Paid Artifact Policy

## Purpose

Define the public/private artifact boundary.

## Current status

Strict guard is required for public deploy roots.

## Key decisions

Public GitHub Pages may include public standards, docs, schemas, examples, proof pages, site assets, and public AEP standard packages matching `standards/AEP-###/complete-package.zip`. Public GitHub Pages must not include paid buyer ZIPs, paid digital products, paid workshop bundles, buyer/facilitator delivery kits, implementation bundles, enterprise pilot bundles, commercialization packs, or private files.

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

Keep `scripts/check_no_paid_artifacts.py` strict and run it before release.


## Regression examples

Allowed: `standards/AEP-001/complete-package.zip`. Blocked filename examples include paid kit, RSI Lite, Proof Room Lite, RSI Sprint Workshop, and Enterprise RSI Pilot buyer or complete-bundle ZIP names; do not publish or link them from public roots.

## Validation checklist

- [ ] Safe AI boundary is present.
- [ ] Product names, prices, and versions match `docs/data/goalos_catalog.yml`.
- [ ] Paid buyer files are not uploaded or linked.
- [ ] Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.
- [ ] `python scripts/check_no_paid_artifacts.py` passes.
- [ ] `python scripts/validate_docs_tables_figures.py` passes.
- [ ] `python scripts/validate_goalos_catalog.py` passes.


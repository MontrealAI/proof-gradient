# GoalOS Proof Card 001 Plan

## Purpose

Specify the first public proof card and fields.

## Current status

Planned proof card ID: GoalOS-PC-001. Recommended first workflow: Customer Support Reply Workflow.

## Key decisions

Proof story: v1.0 was polite but missed refund/access classification; the scorecard detected the weakness; v1.1 added policy classification and a human-review flag; the workflow became clearer, safer, and more reusable.

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

Collect public-safe evidence, avoid private buyer data, obtain buyer approval, and publish with no ROI, certification, autonomous deployment, or model self-modification claims.


## Required fields

- proof card ID
- workflow name
- workflow owner
- input class
- v1.0 workflow summary
- first run output summary
- scorecard
- diagnosis
- v1.1 change
- version diff
- proof note
- claims avoided
- public-safe status
- buyer approval status
- next upsell path

## Validation checklist

- [ ] Safe AI boundary is present.
- [ ] Product names, prices, and versions match `docs/data/goalos_catalog.yml`.
- [ ] Paid buyer files are not uploaded or linked.
- [ ] Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.
- [ ] `python scripts/check_no_paid_artifacts.py` passes.
- [ ] `python scripts/validate_docs_tables_figures.py` passes.
- [ ] `python scripts/validate_goalos_catalog.py` passes.


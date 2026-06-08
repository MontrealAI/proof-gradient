# GoalOS Recursive Workflow OS

## Purpose

Describe the formal platform direction for recursive workflow operations.

## Current status

GoalOS Recursive Workflow OS is the operating layer around AI models for scored, proof-bounded workflow evolution.

## Key decisions

GoalOS does not modify base AI models; it improves workflows through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback.

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

Harden the Cloud MVP path into a multi-tenant SaaS only after Proof Card 001 and department proof cycles.


## Core loop

Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run.

![Recursive workflow loop](figures/goalos_recursive_workflow_loop.svg)

## Validation checklist

- [ ] Safe AI boundary is present.
- [ ] Product names, prices, and versions match `docs/data/goalos_catalog.yml`.
- [ ] Paid buyer files are not uploaded or linked.
- [ ] Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.
- [ ] `python scripts/check_no_paid_artifacts.py` passes.
- [ ] `python scripts/validate_docs_tables_figures.py` passes.
- [ ] `python scripts/validate_goalos_catalog.py` passes.


# Contributing to Proof Gradient · GoalOS

Thank you for improving the public proof and standards layer.

## Documentation update rules

- Keep `docs/data/goalos_catalog.yml` as the source of truth for product names, prices, versions, public status, standards, validation status, and safe claim boundaries.
- When the product ladder changes, update the catalog, `docs/tables/goalos_product_ladder.csv`, README, and relevant GoalOS docs in the same pull request.
- When figures change, update both Mermaid source (`docs/figures/*.mmd`) and SVG export (`docs/figures/*.svg`) when practical.
- When tables change, update CSV files under `docs/tables/` first and keep Markdown tables consistent.

## Paid-file policy

Do not commit paid buyer ZIPs, workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, professional-firm packs, or private commercial artifacts to public deploy roots. All paid product purchase/application links must point to:

<https://www.quebecartificialintelligence.com/shop>

## Claim boundary

Do not add unsupported claims of guaranteed ROI, guaranteed revenue, guaranteed productivity, investment returns, legal/financial/tax advice, compliance certification, AI safety certification, autonomous AGI, base-model self-modification, uncontrolled autonomous deployment, achieved AGI/ASI, or independently unproven real profit/revenue.

## Validation commands

Run before opening a PR:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

If available, also run:

```bash
pytest
make test
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

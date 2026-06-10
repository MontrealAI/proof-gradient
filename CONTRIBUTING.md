# Contributing to Proof Gradient · GoalOS

Contributions must preserve the proof-led, public-safe foundation of the repository.

## Contribution rules

- Do not commit paid buyer files, buyer ZIPs, workshop bundles, facilitator kits, implementation bundles, enterprise pilot bundles, commercialization packs, private evidence, or secrets.
- Update `docs/data/goalos_catalog.yml` when the product ladder, prices, versions, safe claims, validation status, public/private artifact rules, or website release status changes.
- Update `docs/tables/*.csv` and `docs/figures/*` when docs change.
- Run validation scripts before opening a PR.
- Do not make unsupported claims: no guaranteed ROI, guaranteed revenue, guaranteed productivity, investment returns, legal advice, financial advice, tax advice, compliance certification, AI safety certification, AGI/ASI achievement claims, base-model self-modification, or uncontrolled autonomous deployment.
- Public website changes should go through autonomous GitHub Actions. Do not manually bypass release workflows for generated public-site changes.

## Local setup

Install the project and development dependencies before running API tests or full validation:

```bash
python -m pip install -e '.[dev]'
```

## Required local checks

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

You can also run the same guardrail set with:

```bash
make validate
```

## Optional compatibility checks

```bash
pytest
make test
```

## Public product boundary

Buyer products may be mentioned publicly, but public downloads must route to https://www.quebecartificialintelligence.com/shop and must not expose paid deliverables in this repository.

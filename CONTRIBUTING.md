# Contributing

Thank you for improving Agent SkillOS.

## Local setup

```bash
python -m skillos.cli demo
python -m unittest discover -s tests
```

## Development principles

1. Keep the core loop easy to understand.
2. Prefer small, inspectable skill artifacts over opaque behavior.
3. Every new skill update path needs tests.
4. Every release path needs rollback.
5. Do not mix private knowledge with shared skill.

## Pull request checklist

- [ ] Tests pass.
- [ ] New behavior is documented.
- [ ] New skill behavior is versioned.
- [ ] Permission changes are explicit.
- [ ] No local `.skillos` data is committed.

## GoalOS documentation and release-safety rules

- Update `docs/data/goalos_catalog.yml`, `docs/tables/*.csv`, `docs/figures/*`, and README together when product ladder, versions, pricing, validation status, or public URLs change.
- Do not add paid buyer files, private delivery bundles, implementation bundles, enterprise pilot bundles, or public download links for paid products.
- Use the QUEBEC.AI shop for all public purchase/application links: https://www.quebecartificialintelligence.com/shop.
- Keep claims proof-bounded: no guaranteed ROI, revenue, productivity, compliance certification, legal/tax/financial advice, uncontrolled autonomy, AGI/ASI achievement, or model self-modification claims.
- Run `python scripts/check_no_paid_artifacts.py`, `python scripts/validate_goalos_public_site.py`, `python scripts/validate_docs_tables_figures.py`, and `python scripts/validate_goalos_catalog.py` before opening a PR.

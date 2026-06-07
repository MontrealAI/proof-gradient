# Contributing

Use GoalOS Public Site Release v10 as the current path.

Before opening a PR:

```bash
python scripts/validate_goalos_catalog.py
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
pytest
```

Public copy must keep QUEBEC.AI ⚜️✨ together, use the official seal from `assets/quebecaisealv5.png`, point all buy/apply CTAs to `https://www.quebecartificialintelligence.com/shop`, and preserve the safe boundary that GoalOS does not modify base AI models.

# Contributing to Proof Gradient · GoalOS

Contributions must preserve the proof-led, public-safe foundation of the repository.

## Contribution rules

- Do not commit paid buyer files, buyer ZIPs, workshop bundles, facilitator kits, implementation bundles, enterprise pilot bundles, commercialization packs, private evidence, or secrets.
- Update `docs/data/goalos_catalog.yml` when the product ladder, prices, versions, safe claims, validation status, public/private artifact rules, or website release status changes.
- Update `docs/tables/*.csv` and `docs/figures/*` when docs change.
- Run validation scripts before opening a PR.
- Do not make unsupported claims: no guaranteed ROI, guaranteed revenue, guaranteed productivity, investment returns, legal advice, financial advice, tax advice, compliance certification, AI safety certification, AGI/ASI achievement claims, base-model self-modification, or uncontrolled autonomous deployment.
- Public website changes should go through autonomous GitHub Actions. Do not manually bypass release workflows for generated public-site changes.

## Required local checks

Prefer the maintained aggregate target:

```bash
make validate
```

The target runs the required guardrail commands:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

Run `make test` for the Python test suite when dependencies are available. If a check cannot run because of a local environment limitation, document the exact command, failure, and limitation in the PR.


## Documentation upkeep

- Keep `README.md`, `docs/GOALOS_DOCUMENTATION_INDEX.md`, `docs/api_reference.md`, `QA_VERIFICATION.md`, and `Makefile` synchronized when local commands, API routes, validation order, or canonical product facts change.
- Prefer current package names (`proof_gradient` / `proof-gradient`) in new instructions; only mention legacy SkillOS names in explicitly archived historical material.
- Keep generated public-site changes traceable to source docs, catalog data, validation scripts, or GitHub Actions inputs.

## Public product boundary

Buyer products may be mentioned publicly, but public downloads must route to https://www.quebecartificialintelligence.com/shop and must not expose paid deliverables in this repository.

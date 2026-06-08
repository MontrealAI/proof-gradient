# GoalOS AEP Standards Index

## Purpose

This index maps the public AEP standards layer into the GoalOS / Proof Gradient foundation so operators know which standards are preserved, public, and safe to reference.

## Current status

AEP standards remain part of the public standards layer. Public standard packages are allowed only under the narrow ZIP allowlist: `standards/AEP-###/complete-package.zip`.

## Source of truth

- `docs/data/goalos_catalog.yml`
- `docs/tables/goalos_aep_standards.csv`
- `standards/`

## Key decisions

- AEP standards support proof records, evidence, selection, permission, versioning, rollback, public-safe reporting, and Proof Rooms.
- AEP packages may be public only when they match `standards/AEP-###/complete-package.zip`.
- Paid buyer products, workshop bundles, implementation bundles, enterprise pilot bundles, and commercialization packs remain blocked.

## Public/private boundaries

Public standards and schemas may be committed. Buyer deliverables and private proof evidence must not be published or linked from README, docs, generated indexes, manifests, badges, or GitHub Pages.

## Files involved

- `standards/`
- `schemas/`
- `docs/tables/goalos_aep_standards.csv`
- `docs/figures/goalos_aep_standards_map.mmd`
- `scripts/check_no_paid_artifacts.py`

## Validation commands

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Autonomous website action commands

Public AEP pages and indexes should be regenerated through the current autonomous GitHub Actions path after source-of-truth changes. Do not bypass the release workflows for public-site changes.

## Next actions

1. Keep the AEP table synchronized with `standards/`.
2. Use Proof Card 001 to demonstrate how AEP records support public-safe proof.
3. Continue validating the ZIP allowlist before public deployment.

## Risk notes

AEP standards are public standards, not legal advice, compliance certification, AI safety certification, or guaranteed business outcome claims.

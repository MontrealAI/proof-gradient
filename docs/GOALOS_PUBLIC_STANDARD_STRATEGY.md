# GoalOS Public Standard Strategy

## Purpose

Describe how Proof Gradient and AEP standards make GoalOS public, testable, and proof-bound while preserving private buyer deliverables and confidential evidence.

## Current status

AEP standards are the public constitutional layer for proof, evidence, selection, rollback, permission, and public-safe proof. The current public website release is GoalOS Public Site Release v8 Intelligent Assets, and the current validation fix is GoalOS Validation Hotfix v14 Microsite Compatibility.

## Source of truth

`docs/data/goalos_catalog.yml` is the source of truth for public standards inventory, workflow release status, validation status, public/private rules, and obsolete workflow handling.

## Key decisions

- Public standards should be readable, versioned, and validation-aware.
- Public proof should disclose enough structure to be useful without leaking private buyer evidence.
- Public AEP ZIP packages are allowed only at `standards/AEP-###/complete-package.zip` when explicitly reviewed and narrowly allowlisted.
- Obsolete validation paths v12, v13, and old v8 compatibility validation are not current.

## Public/private boundaries

Public repo may include public standards, schemas, examples, proof pages, public site assets, and allowed AEP packages. It must not include paid buyer ZIPs, workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, commercialization packs, private evidence, buyer data, or support records.

## Files involved

- `docs/data/goalos_catalog.yml`
- `docs/GOALOS_VALIDATION_HOTFIX_V14.md`
- `docs/GOALOS_PAID_ARTIFACT_POLICY.md`
- `docs/GOALOS_PUBLIC_SITE_RELEASE_V8.md`
- `docs/tables/goalos_aep_standards.csv`
- `docs/standards/`
- `site/standards/`

## Validation commands

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Autonomous website action commands

Update catalog/docs/action inputs first, run GoalOS Validation Hotfix v14 Microsite Compatibility, run the GoalOS Public Site Release v8 Intelligent Assets workflow, then run paid-file and docs/tables/figures validation.

## Next actions

- Keep AEP inventories synchronized with public site pages.
- Add Proof Card 001 as the first public-safe proof story after approval.
- Maintain clear distinction between public proof architecture and paid buyer implementation materials.

## Risk notes

Do not present standards as legal advice, compliance certification, AI safety certification, or guaranteed business results. Standards define public proof architecture and validation posture, not certified outcomes.

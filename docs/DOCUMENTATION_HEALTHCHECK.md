# Documentation Healthcheck

Last verified: 2026-06-10.

This healthcheck captures the current documentation status for Proof Gradient · GoalOS and the repeatable guardrails used to keep public docs, tables, figures, generated-site inputs, and safety claims current.

## Current status

| Area | Status | Evidence / owner |
|---|---|---|
| Canonical facts | Current | `docs/data/goalos_catalog.yml` remains the first source of truth for product, release, validation, site, and safe-claim facts. |
| Public documentation | Current | `README.md`, `docs/GOALOS_DOCUMENTATION_INDEX.md`, and this healthcheck define the reader entry points and maintenance path. |
| Tables and figures | Current | CSV tables in `docs/tables/` and Mermaid/SVG figures in `docs/figures/` are validated together. |
| Public site | Current | Public-site checks validate `site/` without manually bypassing autonomous GitHub Actions. |
| Paid/private artifacts | Current | The paid-file guard allows only public-safe files and the narrow public AEP package exception. |
| Claims boundary | Current | GoalOS and $JOBS language remains bounded: no base-model self-modification, no guaranteed ROI, no investment promises, no unsupported audit/mainnet/legal/tax claims. |

## Best-practice maintenance path

1. Update canonical facts first in `docs/data/goalos_catalog.yml` when product, price, release, validation, website, or claims facts change.
2. Propagate canonical changes to CSV tables, figures, Markdown docs, badges, scripts, and workflow inputs in that order.
3. Keep public-safe limitations beside positive claims, especially for GoalOS Cloud MVP, Proof Card 001, $JOBS, audit status, legal/tax status, and mainnet gates.
4. Add or update navigation links in `README.md` and `docs/GOALOS_DOCUMENTATION_INDEX.md` whenever a new official document becomes part of the operating path.
5. Do not commit paid buyer deliverables, private evidence, secrets, legal/tax packs, or generated paid ZIPs to the public repository.
6. Use autonomous GitHub Actions for public website releases; do not manually bypass release workflows for generated public-site changes.

## Required checks

Run these from the repository root before merging documentation or public-site changes:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

Equivalent shortcut:

```bash
make validate
```

For code-adjacent changes, also run the applicable test suite:

```bash
pytest
make test
node site/app/goalos-cloud-mvp/tests/goalos-core.test.mjs
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

## Merge readiness checklist

- [ ] Source-of-truth facts were updated before downstream docs.
- [ ] Internal Markdown links remain relative and resolve locally.
- [ ] Tables and figures still match their source files.
- [ ] Safe-claims language includes limitations and prohibited-claim boundaries.
- [ ] Public-site changes are release-workflow compatible.
- [ ] Paid/private artifact guard passes.
- [ ] Test or validation output is recorded in the PR body.

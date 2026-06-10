# Documentation Maintenance Guide

This guide defines the repeatable best-practice checklist for keeping Proof Gradient · GoalOS documentation current, evidence-bound, public-safe, and release-ready.

## Source-of-truth order

When updating documentation, preserve this source-of-truth order:

1. `docs/data/goalos_catalog.yml` for canonical product, release, proof, validation, and public-site facts.
2. `docs/tables/*.csv` for structured table data that appears in Markdown or generated pages.
3. `docs/figures/*.mmd` for editable diagrams, with matching SVG outputs when public pages reference rendered figures.
4. Markdown docs in `README.md`, `docs/`, and standards directories.
5. Generated public-site files in `site/` only through the approved build/release workflow.

If a fact changes in more than one place, update the highest source first and then propagate the same fact to the lower layers.

## Update checklist

Before opening a pull request, verify that the documentation change satisfies all of the following:

- The change has a clear owner, purpose, and expected reader.
- Product, price, release, validation, audit, and public-site status claims match `docs/data/goalos_catalog.yml`.
- Markdown tables match their CSV sources where a CSV source exists.
- Figures have an editable Mermaid source when practical, and rendered SVGs are refreshed when referenced by public docs.
- Public-safe proof claims include the evidence boundary, approval state, and any known limitations.
- $JOBS and token-related language remains utility-first and does not imply investment returns, resale value, yield, equity, revenue share, or mainnet authorization.
- Paid buyer deliverables, private evidence, secrets, and regulated or confidential data are not added to the public repository.
- Links are relative when pointing inside the repository and stable when pointing outside the repository.
- New docs are added to the appropriate navigation surface: `README.md`, `docs/GOALOS_DOCUMENTATION_INDEX.md`, or a relevant standards README.

## Validation commands

Run the public documentation guardrails from the repository root:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

The same guardrail suite is available as:

```bash
make validate
```

For code-adjacent documentation changes, also run the applicable test target:

```bash
pytest
# or
make test
```

## Freshness cadence

Use this cadence to keep public docs current:

| Cadence | Review scope | Required action |
|---|---|---|
| Every documentation PR | Changed docs, tables, figures, links, safe-claims boundary | Run validation and update navigation entries. |
| Before public-site release | Catalog, generated site pages, badges, figures, paid-file policy | Run `make validate` and approved site build/release workflow. |
| Before product or price changes | Product ladder, shop links, buyer outcomes, delivery boundaries | Update catalog first, then README/docs/tables/site inputs. |
| Before $JOBS status changes | Technical status, mainnet gates, safe claims, audit status | Confirm legal/tax/audit caveats remain explicit and current. |
| Quarterly or major milestone | README, documentation index, roadmap, security policy, contributing guide | Remove stale status text and confirm all validation commands still pass. |

## Public-safe writing standard

Use precise, bounded language:

- Prefer "public software proof", "release candidate", "pilot", "planned", and "requires approval" when a capability is not production-authorized.
- Avoid unsupported absolutes such as "guaranteed", "certified", "risk-free", "fully autonomous", or "mainnet-ready" unless the repository contains approved evidence.
- State known limitations beside positive claims.
- Separate buyer-facing outcomes from investment, legal, tax, compliance, or safety claims.

## Pull request documentation template

Use this structure in documentation PRs:

```markdown
## Documentation changes
- What changed:
- Source-of-truth files updated:
- Navigation updated:
- Public-safe claim review:

## Validation
- [ ] `make validate`
- [ ] Additional tests, if applicable:

## Risk / rollback
- Risk level:
- Rollback path:
```

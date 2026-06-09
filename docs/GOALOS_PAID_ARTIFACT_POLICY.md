# GoalOS Paid Artifact Policy

Public repo may include public standards, public docs, public schemas, public examples, public proof pages, public site assets, and public AEP standard packages matching `standards/AEP-###/complete-package.zip`.

Public repo must not include paid buyer ZIPs, paid digital products, paid workshop bundles, buyer/facilitator delivery kits, implementation bundles, enterprise pilot bundles, commercialization packs, private legal/tax packs, private keys, treasury secrets, or seed phrases.

Allowed public ZIP pattern: `standards/AEP-###/complete-package.zip`. All other ZIPs in public deploy roots are blocked unless explicitly reviewed and narrowly allowlisted. Docs can mention products exist, but must point to https://www.quebecartificialintelligence.com/shop.


## Required operating frame

- **Purpose:** operational public-safe guidance for Proof Gradient · GoalOS.
- **Current status:** aligned to `docs/data/goalos_catalog.yml`.
- **Source of truth:** `docs/data/goalos_catalog.yml`, then CSV tables in `docs/tables/`, then this document.
- **What is public:** public docs, standards, schemas, examples, proof pages, figures, tables, badges, and generated site assets.
- **What is private:** paid buyer deliverables, buyer/facilitator kits, implementation bundles, enterprise pilot bundles, commercialization packs, legal/tax packs, private keys, treasury secrets, and seed phrases.
- **What is ready:** documentation governance, validation scripts, product ladder positioning, autonomous website process, paid-file guard, Proof Card 001 plan, and $JOBS safe public status.
- **What is not ready:** full enterprise SaaS completion, $JOBS mainnet authorization, audit completion, legal approval, tax review, or guaranteed token classification.
- **Validation commands:** `python scripts/check_no_paid_artifacts.py`; `python scripts/validate_goalos_catalog.py`; `python scripts/validate_docs_tables_figures.py`; `python scripts/validate_goalos_public_site.py`.
- **Next actions:** keep catalog, docs, CSV tables, figures, badges, workflows, and public-site sources synchronized before release.
- **Risk notes:** no unsupported claims, no paid artifact exposure, no obsolete workflow confusion, and no token investment language.
- **Prohibited claims:** guaranteed ROI/revenue/productivity, legal/tax advice, compliance certification, AI safety certification, autonomous AGI, base-model self-modification, investment, profit, yield, revenue share, passive income, price target, guaranteed resale value, audited/mainnet/legal/tax claims when not complete.
- **Related docs:** [Documentation index](GOALOS_DOCUMENTATION_INDEX.md), [Claims boundary](GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md), [Paid artifact policy](GOALOS_PAID_ARTIFACT_POLICY.md), [Website autonomous actions](GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md).

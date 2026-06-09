# GoalOS Website Autonomous GitHub Actions

The website is generated through autonomous GitHub Actions. Do not manually upload paid products to the public site. Do not manually bypass the release workflow. Do not rerun obsolete workflows as the current path. Do not use old v12/v13 validation as current. v14 is the current validation hotfix. v8 is the current public-site release package. Old obsolete v8 compatibility validation should be disabled/ignored unless updated to shared current rules. If product ladder or $JOBS status changes, update `docs/data/goalos_catalog.yml` and the relevant action/template/source data first. Then run the correct GitHub Action. Then run validation.

## Recommended workflow order

1. Validate source of truth / docs / paid-file policy
2. GoalOS Validation Hotfix v14 Microsite Compatibility
3. GoalOS Public Site Release v8 Intelligent Assets
4. Validate GoalOS Public Site v8 only if updated to current shared rules
5. Check No Paid Artifacts
6. Validate GoalOS Catalog
7. Validate GoalOS Docs, Tables, Figures

## Non-technical operator section

- Go to GitHub repository.
- Open Actions.
- Run only current workflows.
- Green check = success.
- Red X = inspect logs / escalate.
- Never upload buyer ZIPs to public repo.
- Never expose private product files through GitHub Pages.


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

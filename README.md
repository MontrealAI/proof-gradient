<p align="center">
  <img alt="GoalOS" src="badges/goalos.svg"> <img alt="Proof Gradient" src="badges/proof-gradient.svg"> <img alt="AEP standards" src="badges/aep-standards.svg"> <img alt="No paid artifacts" src="badges/no-paid-artifacts.svg"> <img alt="Website via GitHub Actions" src="badges/website-via-github-actions.svg"> <img alt="Validation v14" src="badges/validation-v14.svg"> <img alt="Public Site Release v8" src="badges/public-site-release-v8.svg"> <img alt="Cloud MVP 0.2" src="badges/cloud-mvp-0-2.svg"> <img alt="$JOBS Base Sepolia first" src="badges/jobs-base-sepolia-first.svg"> <img alt="Not investment claims" src="badges/no-token-investment-claims.svg">
</p>

# Proof Gradient · GoalOS

**Aim. Act. Prove. Evolve.**

> A model can answer. An agent can act. An institution must prove.

**Commercial thesis:** ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run.
**Enterprise thesis:** Enterprise RSI without model self-modification.

## What this repository is

This repository is the public foundation for **GoalOS**, **Proof Gradient**, and **AEP standards**: documentation, schemas, public proof pages, validation scripts, website automation rules, public-safe figures/tables/badges, and governance for proof-led recursive AI workflows.

Buyer products are **not stored in this public repository**. They are sold through: https://www.quebecartificialintelligence.com/shop

## What GoalOS is

GoalOS is the recursive AI workflow operating layer. It helps teams run workflows, score results, prove evidence, diagnose gaps, improve instructions/prompts/process, approve changes, version releases, monitor outcomes, and re-run with proof.

## What Proof Gradient is

Proof Gradient is the public proof and standards layer. It turns workflow claims into evidence-bound records, proof rooms, proof cards, validation scripts, public-safe reports, and AEP-compatible standards artifacts.

## What AEP Standards are

AEP standards are public standards protocols for evidence, proof packets, selection gates, tool permissions, rollback receipts, public-safe reporting, and Proof Rooms.

## GoalOS safe AI boundary

GoalOS does **not** modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback.

## Recursive workflow loop

**Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run**

Operating law:

- No proof, no evolution.
- No eval, no propagation.
- No rollback, no release.
- Pas de preuve, pas d’évolution.
- Pas d’évaluation, pas de propagation.
- Pas de rollback, pas de publication.

![GoalOS recursive workflow loop](docs/figures/goalos_recursive_workflow_loop.svg)

## GoalOS product ladder

| Price | Offer | Buyer outcome | Offer type | Delivery | Proof output |
|---|---|---|---|---|---|
| $49 | GoalOS AI Efficiency Sprint Kit | Build one reusable AI workflow. | Self-serve digital product | Instant digital delivery | Workflow specification and baseline scorecard |
| $199 | GoalOS RSI Lite | Build one self-improving AI workflow. | Self-serve digital product | Instant digital delivery | Workflow version, eval log, rollback note |
| $997 | GoalOS Proof Room Lite / Department Pack | Set up a lightweight department Proof Room. | Self-serve department pack | Instant digital delivery | Proof Room charter + evidence docket |
| $2,500+ | GoalOS RSI Sprint Workshop | Build the first self-improving workflow live. | Gated workshop | Application + live facilitation | Proof Card candidate and workshop evidence docket |
| $9,500+ | GoalOS Proof Room Implementation Sprint | Department RSI in 30 days. | Gated implementation | Application + implementation sprint | Department proof records and approval gates |
| $49,000+ | GoalOS Enterprise RSI Pilot | Pilot the Recursive Workflow OS for one enterprise workflow family. | Gated enterprise pilot | Application + pilot delivery | Enterprise pilot proof room + executive proof card |

The $49 / $199 / $997 offers are self-serve digital products. The $2,500+ / $9,500+ / $49,000+ offers are gated/application-based. The initial launch uses Squarespace + Stripe + digital delivery, and the $49 product should be tested with a hidden $1 Squarespace test purchase before publication.

## Proof Room / Proof Card architecture

- **Proof Room:** governed workspace for evidence, decisions, reviewers, approvals, versions, and rollback records.
- **Evidence Docket:** structured evidence package that supports review and public-safe publication.
- **Proof Card:** public-safe summary of approved evidence and outcomes.

## Proof Card 001 next milestone

The next public proof milestone is **Proof Card 001**: first buyer/workshop workflow success → evidence docket → scorecard → approval → safe public proof card.

## GoalOS Cloud MVP and future SaaS

GoalOS Cloud MVP 0.2 is a public software proof and future SaaS direction. It is **not full enterprise SaaS yet**. Future modules include workflow registry, scorecards, evidence dockets, approvals, versioning, monitoring, rollback, Proof Rooms, Proof Cards, and enterprise integrations.

## $JOBS on Base additive proof-network layer

$JOBS is the native coordination asset for proof-based AI workflow work on Base. It is additive and does **not** replace the product ladder.

Sponsors use $JOBS to post missions. Builders use $JOBS to claim work and submit proof. Reviewers use $JOBS to validate proof. Approved proof creates credentials, proof cards, reputation, and access to better opportunities.

$JOBS is built for utility, coordination, and proof — not investment promises. It is not equity, not yield, not revenue share, not a profit promise, and not a guaranteed resale-value asset.

**Technical package status:** GoalOS $JOBS Base Production Release Candidate v4.2 — Audit-Ready Label-Clean. Audit-ready release candidate; **not audited**; **not mainnet authorized**; **Base Sepolia first**; not legally approved; not tax reviewed; not guaranteed non-security.

## Website generated by autonomous GitHub Actions

The public website is generated and refreshed by autonomous GitHub Actions. Do **not** manually bypass the release workflows for public-site changes. If website-facing content changes, update `docs/data/goalos_catalog.yml`, relevant docs/tables/templates/scripts/action inputs, then run current workflows.

Current path: v14 validation hotfix → Public Site Release v8 Intelligent Assets → paid-artifact guard → catalog/docs validation.

## Paid-file policy

Public repo may include public docs, standards, schemas, examples, proof pages, site assets, and the narrow AEP package exception `standards/AEP-###/complete-package.zip`. Public repo must not include paid buyer ZIPs, workshop bundles, buyer/facilitator delivery kits, implementation bundles, enterprise pilot bundles, commercialization packs, private legal/tax packs, keys, treasury secrets, or seed phrases.

## Validation and QA

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

## Repository map

| Area | Purpose |
|---|---|
| `docs/data/goalos_catalog.yml` | source of truth |
| `docs/` | official docs and governance |
| `docs/tables/` | CSV source tables |
| `docs/figures/` | Mermaid sources and SVG companions |
| `badges/` | truthful static badges |
| `scripts/` | validation and site automation scripts |
| `.github/workflows/` | autonomous validation/release workflows |
| `site/` | generated public site deploy root |
| `standards/` and `docs/standards/` | AEP public standards |

## Documentation map

Start with [GoalOS Documentation Index](docs/GOALOS_DOCUMENTATION_INDEX.md), [Product Ladder](docs/GOALOS_PRODUCT_LADDER.md), [Website Autonomous Actions](docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md), [Paid Artifact Policy](docs/GOALOS_PAID_ARTIFACT_POLICY.md), [$JOBS Overview](docs/JOBS_ON_BASE_OVERVIEW.md), and [Repository Audit](docs/GOALOS_REPO_AUDIT.md).

## Figures and tables

Figures live in [`docs/figures/`](docs/figures/). Tables live in [`docs/tables/`](docs/tables/). Markdown tables should match CSV source tables where relevant.

## How to validate locally

Run the commands in **Validation and QA** from the repository root. Optional npm/Solidity commands are skipped unless a contract package is present.

## How to contribute safely

1. Update the catalog first when canonical facts change.
2. Update docs/tables/figures/badges consistently.
3. Never link or upload paid buyer deliverables.
4. Use autonomous GitHub Actions for public website releases.
5. Run validation before opening a PR.

## Claims boundary — what this is not

This is not:

- a prompt dump
- a chatbot wrapper
- a claim of autonomous AGI
- a base-model self-modification system
- a guarantee of ROI
- a public repository for paid buyer deliverables
- an investment solicitation
- a token price target document
- a mainnet deployment authorization

## Shop / apply

Products and applications: https://www.quebecartificialintelligence.com/shop

## Security / license / contributing

See [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), [ROADMAP.md](ROADMAP.md), and [QA_VERIFICATION.md](QA_VERIFICATION.md).

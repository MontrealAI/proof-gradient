# Proof Gradient · GoalOS

<p align="center">
  <img src="badges/proof-gradient.svg" alt="Proof Gradient public proof badge" />
  <img src="badges/goalos.svg" alt="GoalOS workflow OS badge" />
  <img src="badges/aep-standards.svg" alt="AEP standards 001 through 008 badge" />
  <img src="badges/validation-v14.svg" alt="Validation v14 badge" />
  <img src="badges/no-paid-artifacts.svg" alt="No paid artifacts guarded badge" />
  <img src="badges/cloud-mvp-0-2.svg" alt="GoalOS Cloud MVP 0.2 badge" />
  <img src="badges/quebec-ai.svg" alt="QUEBEC.AI badge" />
  <img src="badges/no-model-self-modification.svg" alt="No model self-modification badge" />
</p>

**Aim. Act. Prove. Evolve.**

> A model can answer. An agent can act. An institution must prove.

Proof Gradient is the public proof and standards layer. GoalOS is the recursive workflow operating layer. QUEBEC.AI ⚜️✨ is the sovereign Québec AI identity layer. The category is **Recursive Self-Improving Workflows** and the platform direction is **GoalOS Recursive Workflow OS**.

## Safe AI boundary

GoalOS improves workflows around AI; it does **not** modify base AI models. It improves instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback around model use.

French: GoalOS ne modifie pas les modèles IA de base. GoalOS améliore les flux autour de l’IA grâce aux instructions, prompts, mémoire, grilles de score, dossiers de preuve, évaluations, approbations, versions, surveillance et rollback.

## Core loop

**Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run**

Core law: **No proof, no evolution. No eval, no propagation. No rollback, no release.**

French: **Pas de preuve, pas d’évolution. Pas d’évaluation, pas de propagation. Pas de rollback, pas de publication.**

![GoalOS recursive workflow loop](docs/figures/goalos_recursive_workflow_loop.svg)

## Product ladder

Paid products are sold through QUEBEC.AI only: <https://www.quebecartificialintelligence.com/shop>. Buyer files, paid ZIPs, workshop bundles, delivery kits, implementation packs, enterprise pilot bundles, and private commercial packs must not be uploaded to GitHub Pages.

| Layer | Offer | Outcome | French | Status |
|---|---|---|---|---|
| Self-serve | $49 Kit — GoalOS AI Efficiency Sprint Kit v1.4 | Build one reusable AI workflow | Construisez un flux IA réutilisable | Ready |
| Self-serve | $199 RSI Lite — GoalOS RSI Lite v1.6 | Build one self-improving workflow | Construisez un flux IA auto-améliorant | Ready |
| Self-serve / department | $997 Proof Room Lite — GoalOS Proof Room Lite / Department Pack v2.0 | Set up lightweight Proof Room | Mettez en place une Salle de preuve légère pour un département | Ready |
| Gated workshop | $2,500+ RSI Sprint Workshop — GoalOS RSI Sprint Workshop v7.0 | Build first workflow live | Construisez le premier flux auto-améliorant en direct | Ready |
| Gated implementation | $9,500+ Implementation Sprint — GoalOS Proof Room Implementation Sprint v2.0 | Department RSI in 30 days | RSI départemental en 30 jours | Ready |
| Gated enterprise | $49,000+ Enterprise RSI Pilot — GoalOS Enterprise RSI Pilot v2.0 | Pilot Recursive Workflow OS | Pilotez le Recursive Workflow OS | Ready as pilot |

Current status: product and service packages are ready to sell as public offers; first public proof is still needed; GoalOS Cloud is an MVP software proof and is not a complete SaaS. Next milestone: **Proof Card 001**.

## Public standards

The public AEP standards define the proof vocabulary for evolution, evidence, permissions, rollback, public-safe reporting, and Proof Rooms.

| Standard | Title |
|---|---|
| AEP-001 | GoalOS Proof-of-Evolution Constitution |
| AEP-002 | Evidence Docket Standard |
| AEP-003 | ProofPacket Schema |
| AEP-004 | Selection Gate Standard |
| AEP-005 | Tool Permission Standard |
| AEP-006 | Rollback Receipt Standard |
| AEP-007 | Public-Safe Proof Report Standard |
| AEP-008 | Proof Room Standard |

## Platform architecture

GoalOS Recursive Workflow OS coordinates a proof-bounded loop: Workflow Studio, Execution Engine, Evaluation Engine, Proof Room, Improvement Engine, Approval Gate, Versioning/Rollback, and Monitor.

![GoalOS Cloud MVP architecture](docs/figures/goalos_cloud_mvp_architecture.svg)

## Software proof

**GoalOS Cloud MVP 0.2** is a public software proof for workflow execution, evaluation, proof records, approvals, versioning, rollback, and public-safe proof exports. It is intentionally described as an MVP, not a finished enterprise SaaS.

Run the MVP test when Node is available:

```bash
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

## Public site and validation system

The GitHub Pages public site lives in `site/`. Current validation is **GoalOS Validation Hotfix v14 Microsite Compatibility**. It preserves page classes:

- `canonical_page`: requires exactly one canonical shell and footer.
- `standalone_proof_page`: proof/microsite pages may use standalone metadata and an escape link.
- `app_page`: app pages may use an app shell.
- `aep_standard_package`: public AEP packages are allowed only at `standards/AEP-###/complete-package.zip`.
- paid/private artifacts: blocked from public deploy roots.

Use v14. Avoid v12, v13, and obsolete v8 compatibility validation as current references.

## Repository map

| Path | Purpose |
|---|---|
| `proof_gradient/` | Python package for the Proof Gradient foundation. |
| `docs/` | Public technical documentation, GoalOS operating docs, audit notes, and maps. |
| `docs/data/goalos_catalog.yml` | Source of truth for public GoalOS documentation. |
| `docs/figures/` | Mermaid sources and SVG exports. |
| `docs/tables/` | CSV source tables used by README/docs. |
| `scripts/` | Validation, release, and public-site safety scripts. |
| `schemas/` | JSON schemas for proof/release/run artifacts. |
| `site/` | GitHub Pages public site and Cloud MVP app proof. |
| `tests/` | Regression tests, including public-site artifact classification tests. |
| `badges/` | Static GitHub-safe SVG badges. |

## Documentation map

Start with [`docs/GOALOS_DOCUMENTATION_INDEX.md`](docs/GOALOS_DOCUMENTATION_INDEX.md). Figures are in [`docs/figures/`](docs/figures/) and CSV tables are in [`docs/tables/`](docs/tables/).

## Claim boundary

This repository does not claim guaranteed ROI, guaranteed revenue, guaranteed productivity, investment returns, financial advice, investment advice, legal advice, tax advice, compliance certification, AI safety certification, autonomous AGI, model self-modification, uncontrolled autonomous deployment, achieved AGI/ASI, real-world superintelligence deployment, or independently unproven real profit/revenue.

## Paid-file policy

Public GitHub Pages may include public standards, public docs, public schemas, public examples, public proof pages, public site assets, and public AEP packages matching `standards/AEP-###/complete-package.zip`. Paid buyer products and private delivery materials must remain outside public deploy roots and are sold through <https://www.quebecartificialintelligence.com/shop>.

## Run validation

```bash
python scripts/validate_goalos_public_site.py
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Run tests

```bash
pytest
make test
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

If a tool is unavailable, record the skip honestly in `docs/GOALOS_REPO_AUDIT.md`.

## License and contribution

See [`LICENSE`](LICENSE), [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), and [`ROADMAP.md`](ROADMAP.md).

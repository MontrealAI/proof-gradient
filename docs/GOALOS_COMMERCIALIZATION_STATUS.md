# GoalOS Commercialization Status

This document defines public-safe status and operating guidance for GoalOS Commercialization Status.

GoalOS does not modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback.

Product and buyer references must route to https://www.quebecartificialintelligence.com/shop; no paid buyer deliverables are stored here.

Commercialization status: ready to sell as product/service packages; first public market proof still needed.

| Layer | Price | Offer | Version | Outcome | Status |
|---|---:|---|---|---|---|
| Self-serve | $49 | GoalOS AI Efficiency Sprint Kit | v1.4 | Build one reusable AI workflow | Ready |
| Self-serve | $199 | GoalOS RSI Lite | v1.6 | Build one self-improving AI workflow | Ready |
| Self-serve / department | $997 | GoalOS Proof Room Lite / Department Pack | v2.0 | Set up a lightweight department Proof Room | Ready |
| Gated workshop | $2,500+ | GoalOS RSI Sprint Workshop | v7.0 | Build the first self-improving workflow live | Ready |
| Gated implementation | $9,500+ | GoalOS Proof Room Implementation Sprint | v2.0 | Department RSI in 30 days | Ready |
| Gated enterprise | $49,000+ | GoalOS Enterprise RSI Pilot | v2.0 | Pilot the Recursive Workflow OS | Ready as pilot |

## Required operating frame

- **Purpose:** provide public-safe GoalOS / Proof Gradient guidance for this repository.
- **Current status:** aligned to `docs/data/goalos_catalog.yml`.
- **Source of truth:** `docs/data/goalos_catalog.yml`, then CSV tables in `docs/tables/`, then this explanatory document.
- **Key decisions:** public documentation can describe products and operating packs, but buyer deliverables remain off-repository and are sold through https://www.quebecartificialintelligence.com/shop.
- **Public/private boundaries:** no paid buyer ZIPs, private delivery kits, implementation bundles, enterprise pilot bundles, or commercialization packs may be exposed publicly.
- **Files involved:** README.md, docs/data/goalos_catalog.yml, docs/tables/*.csv, docs/figures/*.mmd, docs/figures/*.svg, scripts/*.py, .github/workflows/*.yml.
- **Validation commands:** `python scripts/check_no_paid_artifacts.py`; `python scripts/validate_goalos_public_site.py`; `python scripts/validate_docs_tables_figures.py`; `python scripts/validate_goalos_catalog.py`.
- **Autonomous website action commands:** use GitHub Actions, not manual public-site edits, when refreshing generated site content.
- **Next actions:** keep catalog, tables, docs, figures, badges, and validation aligned before every release.
- **Risk notes:** avoid unsupported claims and preserve v14 validation plus the public AEP package allowlist.

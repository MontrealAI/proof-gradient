# GoalOS Web3 Hybrid Architecture

Optimal hybrid approach: Web3-native core, Web2-simple user experience, no CEX dependency by default, off-chain legal/tax/support controls, and on-chain access, proof, credentials, referrals, and treasury routing.

AGI.eth: AGI Club membership, community, RSI Lite included, proof credentials. ASI.eth: institutional, frontier, enterprise, Proof Graph, Enterprise RSI layer.

On-chain: membership, access rights, proof-card hashes, credentials, referral attribution. Off-chain: private evidence, buyer data, support tickets, legal/tax decisions, enterprise SOWs.

No investment language, revenue share, yield, guaranteed resale value, or private data on-chain.

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

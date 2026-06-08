# GoalOS Proof Card 001 Plan

**Proof Card ID:** GoalOS-PC-001

**Recommended first workflow:** Customer Support Reply Workflow

**Proof story:** v1.0 was polite but missed refund/access classification. The scorecard detected the weakness. v1.1 added policy classification and a human-review flag. The workflow became clearer, safer, and more reusable.

| Field | Value |
|---|---|
| proof card ID | GoalOS-PC-001 |
| workflow name | Customer Support Reply Workflow |
| workflow owner | Internal operator or approved buyer contact |
| input class | Refund/access support message |
| v1.0 workflow summary | Polite reply draft without explicit policy classification |
| first run output summary | Helpful tone, incomplete access/refund routing |
| scorecard | Clarity, policy classification, human-review flag, reusable instruction quality |
| diagnosis | Missing classification made escalation and refund/access treatment ambiguous |
| v1.1 change | Added policy classification and human-review flag |
| version diff | Added classify-first instruction, edge-case escalation, and proof note template |
| proof note | Workflow improvement is documented by scorecard evidence, not by unsupported performance claims |
| claims avoided | no ROI guarantee; no compliance certification; no autonomous deployment claim; no model self-modification claim |
| public-safe status | Public-safe after buyer approval and private data removal |
| buyer approval status | Required before publication |
| next upsell path | RSI Lite → Proof Room Lite → Implementation Sprint |

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

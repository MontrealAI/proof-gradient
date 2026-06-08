# GoalOS Paid Artifact Policy

Public repo may include public standards, public docs, public schemas, public examples, public proof pages, public site assets, and public AEP standard packages matching `standards/AEP-###/complete-package.zip`.

Public repo must not include paid buyer ZIPs, paid digital products, paid workshop bundles, buyer/facilitator delivery kits, implementation bundles, enterprise pilot bundles, commercialization packs, or private files.

Allowed public ZIP pattern: `standards/AEP-###/complete-package.zip`.

Blocked filename examples are documented as non-links: GoalOS_AI_Efficiency_Sprint_Kit_v1_4_BUYER_EXCELLENCE_EDITION.zip; GoalOS_RSI_Lite_Recursive_Self_Improving_Workflow_Kit_v1_6_CLEAN_BUYER_OFFICIAL.zip; GoalOS_Proof_Room_Lite_Department_Pack_v2_0_WORLD_CLASS_BILINGUAL_BUYER_OFFICIAL.zip; GoalOS_RSI_Sprint_Workshop_v7_0_PRIME_TIME_PROOF_CARD_EDITION_COMPLETE_BUNDLE.zip; GoalOS_Enterprise_RSI_Pilot_v2_0_INSTITUTIONAL_BOARDROOM_FINAL_COMPLETE_BUNDLE.zip.

Docs can mention these products exist, but must point buyers to https://www.quebecartificialintelligence.com/shop.

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

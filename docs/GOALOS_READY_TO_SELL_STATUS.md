# GoalOS Ready-to-Sell Status

## Purpose

State what can be sold now while preserving proof-bounded claims.

## Current status

Ready to sell: $49 Kit, $199 RSI Lite, $997 Proof Room Lite, $2,500+ RSI Sprint Workshop, $9,500+ Implementation Sprint, and $49,000+ Enterprise RSI Pilot. First public proof still needed.

## Key decisions

Use the shop CTA only: https://www.quebecartificialintelligence.com/shop. Do not link paid files. Do not claim guaranteed ROI or certification.

## Files involved

- `README.md`
- `docs/data/goalos_catalog.yml`
- `docs/tables/`
- `docs/figures/`
- `scripts/check_no_paid_artifacts.py`
- `scripts/validate_goalos_public_site.py`
- `scripts/validate_docs_tables_figures.py`
- `scripts/validate_goalos_catalog.py`


## What is public

Public: standards, public docs, schemas, examples, public proof pages, public site assets, product names, safe status language, and shop/application links to QUEBEC.AI.

## What must remain private

Private: paid buyer ZIPs, workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, commercial operating packs, buyer data, private evidence, and private professional-firm package ZIPs.

## Next actions

Create GoalOS-PC-001 and publish a public-safe proof card after buyer approval.

| Layer | Offer | Version | Outcome | Status |
|---|---|---:|---|---|
| Self-serve | $49 — GoalOS AI Efficiency Sprint Kit | v1.4 | Build one reusable AI workflow. / Construisez un flux IA réutilisable. | Ready |
| Self-serve | $199 — GoalOS RSI Lite | v1.6 | Build one self-improving AI workflow. / Construisez un flux IA auto-améliorant. | Ready |
| Self-serve / department | $997 — GoalOS Proof Room Lite / Department Pack | v2.0 | Set up a lightweight department Proof Room. / Mettez en place une Salle de preuve légère pour un département. | Ready |
| Gated workshop | $2,500+ — GoalOS RSI Sprint Workshop | v7.0 | Build the first self-improving workflow live. / Construisez le premier flux auto-améliorant en direct. | Ready |
| Gated implementation | $9,500+ — GoalOS Proof Room Implementation Sprint | v2.0 | Department RSI in 30 days. / RSI départemental en 30 jours. | Ready |
| Gated enterprise | $49,000+ — GoalOS Enterprise RSI Pilot | v2.0 | Pilot the Recursive Workflow OS. / Pilotez le Recursive Workflow OS. | Ready as pilot |

## Validation checklist

- [ ] Safe AI boundary is present.
- [ ] Product names, prices, and versions match `docs/data/goalos_catalog.yml`.
- [ ] Paid buyer files are not uploaded or linked.
- [ ] Public AEP package allowlist remains `standards/AEP-###/complete-package.zip`.
- [ ] `python scripts/check_no_paid_artifacts.py` passes.
- [ ] `python scripts/validate_docs_tables_figures.py` passes.
- [ ] `python scripts/validate_goalos_catalog.py` passes.


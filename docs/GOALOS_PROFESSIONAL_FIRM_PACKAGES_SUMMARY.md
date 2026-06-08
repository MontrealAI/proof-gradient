# GoalOS Professional-Firm Packages Summary

The public repository may summarize professional-firm packages, but must not upload or link paid ZIPs unless explicitly intended to be public.

1. Tax / Accounting / CFO — unit economics and revenue recognition questions for qualified professionals.
2. Privacy / Data Protection — buyer data, proof-card redaction, data minimization.
3. Security / SOC 2 / Trust Center — controls, auditability, incident readiness.
4. IP / Trademark / Licensing — public marks, licensing boundaries, deliverable ownership.
5. UX / CRO / Buyer Journey — shop-to-proof experience and safe messaging.
6. Enterprise Sales / GTM — gated offer qualification and proof-led sales motion.
7. RevOps / Analytics — measurement without unsupported outcome claims.
8. Brand / Design System — QUEBEC.AI and GoalOS public identity.
9. Growth Marketing — compliant content and evidence-backed campaigns.
10. Accessibility / Bilingual Localization — English/French accessibility and localization.
11. Insurance / Commercial Risk — operational risk review.
12. Enterprise Procurement / Trust Center — procurement evidence and security questionnaire readiness.
13. Independent Proof Audit / Evaluation — third-party evaluation of proof records.

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

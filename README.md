# Proof Gradient / GoalOS

**A model can answer. An agent can act. An institution must prove.**

Proof Gradient is the public proof and standards layer for GoalOS. GoalOS is the recursive workflow operating layer for the RSI era: it turns repeated AI work into owned, scored, versioned, approved, monitored, and recursively improving workflows.

**Commercial line:** ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run.

**Enterprise line:** Enterprise RSI without model self-modification.

## Safe boundary

GoalOS does **not** modify AI models. Recursive improvement happens at the workflow layer: workflow definitions, instructions, prompts, memory, scorecards, proof records, evaluations, evidence standards, operating procedures, approvals, versions, monitoring, and rollback.

Core loop:

> Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run

## Public software proof

GoalOS Cloud MVP 0.2 is a public static software proof in `site/app/goalos-cloud-mvp/`.

It runs in the browser, uses `localStorage`, requires no secrets, and demonstrates:

- organization / workspace / user roles;
- policy engine and controlled memory;
- model-provider restrictions;
- Workflow Studio and workflow versioning;
- Execution Engine and Evaluation Engine demos;
- Proof Room records;
- Recursive Improvement Engine;
- improvement proposal and human approval gate;
- version comparison, rollback target, Proof Graph export;
- public-safe proof card and executive proof report exports;
- audit log, OpenAPI blueprint, JSON schemas, and Node unit tests.

Demo story: the **Customer Support Reply Workflow** v1.0 intentionally misses refund/access policy classification. The MVP runs support cases, evaluates outputs, creates proof records, detects the refund-policy failure, proposes v1.1, benchmarks v1.0 vs v1.1, requires human approval, deploys approved v1.1, preserves rollback target v1.0, and exports a public-safe proof card plus Proof Graph.

Run the MVP test:

```bash
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```


## Public-site validation

Public HTML and artifacts are classified before validation. Normal marketing/docs pages are `canonical_page` files and still require exactly one canonical GoalOS shell and footer. Immersive RSI proof microsites can be `standalone_proof_page` files when they include `GOALOS-STANDALONE-PROOF` metadata plus a visible `/proof-gradient/` escape link. Cloud MVP pages under `site/app/goalos-cloud-mvp/` are `app_page` files and use their own app shell.

Public AEP standard packages are allowed only at `standards/AEP-###/complete-package.zip`; all other ZIPs in public deploy roots remain blocked unless explicitly reviewed and added to the shared allowlist in `scripts/goalos_public_site_rules.py`. See `docs/GOALOS_PUBLIC_SITE_VALIDATION.md` and `docs/GOALOS_PAID_ARTIFACT_POLICY.md`.

Run validation locally:

```bash
python scripts/validate_goalos_public_site.py
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
python -m pytest tests/test_goalos_public_site_rules.py
```

## Public website

The GitHub Pages site root is `site/`. The public site uses one canonical shell:

- `site/assets/goalos-site-v2.css`
- `site/assets/goalos-site-v2.js`

The site is designed as a clean, dark, institutional GoalOS / Proof Gradient foundation with one navigation bar, one footer, public product pages, standards, examples, and the Cloud MVP.

## Product / offer ladder

Paid products are sold on QUEBEC.AI and are **not** stored in this repository. All checkout / apply buttons point to:

<https://www.quebecartificialintelligence.com/shop>

Current ladder:

| Price | Offer | Public outcome |
|---:|---|---|
| $49 | GoalOS AI Efficiency Sprint Kit | Build one reusable AI workflow. |
| $199 | GoalOS RSI Lite | Build one self-improving AI workflow. |
| $997 | GoalOS Proof Room Lite / Department Pack | Set up a lightweight department Proof Room. |
| $2,500+ | GoalOS RSI Sprint Workshop | Build the first self-improving workflow live. |
| $9,500+ | GoalOS Proof Room Implementation Sprint | Department RSI in 30 days. |
| $49,000+ | GoalOS Enterprise RSI Pilot | Pilot the Recursive Workflow OS for one enterprise workflow family. |

Future platform: **GoalOS Recursive Workflow OS**. Future moat: **Proof Graph**.

## Public standards and proof layer

The AEP standards are the public trust layer. They provide the vocabulary for proof, permission, rollback, public-safe reports, and Proof Rooms.

- AEP-001 — GoalOS Proof-of-Evolution Constitution
- AEP-002 — Evidence Docket Standard
- AEP-003 — ProofPacket Schema
- AEP-004 — Selection Gate Standard
- AEP-005 — Tool Permission Standard
- AEP-006 — Rollback Receipt Standard
- AEP-007 — Public-Safe Proof Report Standard
- AEP-008 — Proof Room Standard

Existing standards content, schemas, examples, conformance materials, and documentation are preserved.

## Claim boundary

This repository and public site do not claim guaranteed ROI, income, productivity, compliance certification, safety guarantees, legal advice, financial advice, investment advice, autonomous deployment, uncontrolled autonomous AGI, AI model self-modification, real revenue, real profit, or real-world energy capture.

## Validation

Recommended public-site checks:

```bash
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
python scripts/validate_goalos_site_v2.py
python scripts/check_no_paid_artifacts.py
pytest
```

The paid-artifact guard blocks paid buyer ZIPs, paid workshop files, implementation bundles, enterprise delivery kits, and seller assets from the GitHub Pages public site, except explicitly whitelisted public standards/action documentation.

## Repository foundation

The repository also preserves the broader Proof Gradient foundation: GitHub Actions, static site assets, docs, schemas, examples, tests, Python package area, Docker files, data files, and GitHub Pages content.

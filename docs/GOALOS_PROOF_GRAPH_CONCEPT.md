# GoalOS Proof Graph Concept

## Purpose

The GoalOS Proof Graph concept describes how public-safe proof records can become linked institutional evidence without exposing private buyer files or claiming certification.

## Current status

Concept stage. It is a standards direction for Proof Gradient and AEP interoperability, not a completed enterprise SaaS feature and not an investment product.

## Source of truth

- `docs/data/goalos_catalog.yml`
- `docs/figures/goalos_proof_graph_concept.mmd`
- `docs/tables/goalos_public_standard_strategy.csv`

## Key decisions

- Proof nodes should represent workflow runs, scorecards, evidence references, approvals, versions, rollbacks, and public-safe proof cards.
- Private evidence remains off-chain or private by default.
- Public proof cards publish redacted summaries only after buyer approval.
- AEP standards provide the interface language for proof records and Proof Rooms.

## Public/private boundaries

Public: schemas, standards, redacted proof cards, public-safe hashes, figures, and tables. Private: buyer data, delivery bundles, support tickets, enterprise SOWs, internal legal/tax decisions, and paid ZIPs.

## Files involved

- `docs/GOALOS_PROOF_CARD_001_PLAN.md`
- `docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md`
- `docs/GOALOS_PAID_ARTIFACT_POLICY.md`
- `schemas/`
- `standards/`

## Validation commands

```bash
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/check_no_paid_artifacts.py
```

## Autonomous website action commands

Website-facing Proof Graph content must flow through catalog/docs/template updates first, then the autonomous GitHub Actions website release path documented in `docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md`.

## Next actions

1. Publish Proof Card 001 as a redacted public-safe proof record.
2. Map the Proof Card fields to the AEP standards.
3. Define a minimal proof-node schema for future validation.

## Risk notes

Do not claim compliance certification, investment value, guaranteed ROI, or autonomous AGI. The Proof Graph is a public-safe evidence architecture, not a private data dump.

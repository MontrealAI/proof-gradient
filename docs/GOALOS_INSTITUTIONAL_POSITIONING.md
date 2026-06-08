# GoalOS Institutional Positioning

## Purpose

Define the public institutional posture for Proof Gradient · GoalOS without unsupported claims, paid-file leakage, or confusion with prompt packs and chatbot wrappers.

## Current status

Proof Gradient is the public proof and standards layer. GoalOS is the recursive workflow operating layer. QUEBEC.AI ⚜️✨ is the sovereign Québec AI identity layer. The category is Recursive Self-Improving Workflows.

## Source of truth

The source of truth is `docs/data/goalos_catalog.yml`, followed by the CSV inventories in `docs/tables/` and the public README.

## Key decisions

- Public line: A model can answer. An agent can act. An institution must prove.
- Commercial line: ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run.
- Enterprise line: Enterprise RSI without model self-modification.
- GoalOS law: no proof, no evolution; no eval, no propagation; no rollback, no release.
- French law: pas de preuve, pas d’évolution; pas d’évaluation, pas de propagation; pas de rollback, pas de publication.

## Public/private boundaries

Public documentation may describe the ladder, the Cloud MVP, standards, validation, and safe proof architecture. It must not expose paid buyer products, private implementation bundles, enterprise pilot bundles, commercialization packs, buyer data, or private proof evidence.

## Safe AI boundary

GoalOS does not modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback.

## Files involved

- `README.md`
- `docs/data/goalos_catalog.yml`
- `docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md`
- `docs/GOALOS_PRODUCT_LADDER.md`
- `docs/GOALOS_RECURSIVE_WORKFLOW_OS.md`
- `docs/GOALOS_PUBLIC_STANDARD_STRATEGY.md`

## Validation commands

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

## Autonomous website action commands

Website-facing positioning changes must be made first in catalog/docs/templates/action inputs, then released through the autonomous GitHub Actions path documented in `docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md`.

## Next actions

- Publish Proof Card 001 after buyer approval and public-safe review.
- Keep public positioning proof-bound and evidence-linked.
- Continue standardizing AEP proof, evidence, permission, selection, rollback, and public-safe reporting patterns.

## Risk notes

Avoid valuation language, guaranteed ROI, guaranteed productivity, compliance certification, AI safety certification, autonomous AGI, achieved AGI/ASI, base-model self-modification, uncontrolled deployment, and unverified profit claims.

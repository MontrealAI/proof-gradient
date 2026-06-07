# GoalOS Paid Artifact Policy

## English summary

Public documentation may describe products, standards, examples, schemas, public brand assets, and the public Cloud MVP demo. Paid buyer artifacts remain private and must not be linked as public downloads.

## Résumé français

La documentation publique peut décrire les produits, standards, exemples, schémas, actifs de marque publics et la démo publique Cloud MVP. Les artefacts acheteurs payants restent privés et ne doivent pas être liés comme téléchargements publics.

## Current status

Documentation-only policy for public/private artifact separation.

## Owner / audience

Owner: repository governance. Audience: engineers, launch operators, counsel, buyer success, and communications partners.

## Public allowed

- README
- docs
- examples
- schemas
- public AEP standard packages
- public website pages
- public brand assets
- public Cloud MVP demo

## Public AEP ZIP allowed

- `standards/AEP-###/complete-package.zip`

## Private / not public

- buyer ZIPs
- paid workshop bundles
- buyer/facilitator delivery kits
- implementation delivery kits
- enterprise pilot delivery kits
- seller asset bundles
- commercialization master packs
- private client data
- proof cards without approval
- exact buyer outputs without approval
- sensitive prompts or private policies

## What is ready

- Public/private boundary is documented.
- Validators warn on paid ZIP links in documentation.

## What is not ready

- Automated paid-delivery publishing is not part of this repository.

## Safe-boundary language

GoalOS does not modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback.

GoalOS ne modifie pas les modèles IA de base. GoalOS améliore les flux autour de l’IA grâce aux instructions, prompts, mémoire, grilles de score, dossiers de preuve, évaluations, approbations, versions, surveillance et rollback.

## Next action

Run `python scripts/validate_docs_tables_figures.py` before documentation PR review.

## Related docs

- [Documentation index](GOALOS_DOCUMENTATION_INDEX.md)
- [Claims and safe boundary](GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md)
- [Paid artifact policy](GOALOS_PAID_ARTIFACT_POLICY.md)
- [Engineering roadmap](GOALOS_ENGINEERING_ROADMAP.md)

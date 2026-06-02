# Migration from SkillOS v2.0.0

Proof Gradient preserves the useful SkillOS DNA and generalizes it.

| SkillOS concept | Proof Gradient concept |
|---|---|
| Skill | Artifact type: skill |
| Skill version | Artifact version |
| Skill release | Artifact release |
| Skill trace | Proof Ledger trace |
| Learning lesson | Proof-backed patch rationale |
| Candidate skill | Candidate artifact version |
| Eval result | Eval artifact + eval run + selection evidence |
| Canary release | Selection Gate rollout |
| Rollback planner | Mandatory rollback target |
| Proof receipt | Proof Ledger record |
| Public command center | Proof Gradient Command Center |
| Public claim boundary | Governance policy artifact |

The inherited `skillos/` package should remain available as a legacy or compatibility layer until equivalent Proof Gradient behavior is implemented and tested.

## Current migration stance

This repository already exists as `MontrealAI/proof-gradient`. The autonomous retarget workflow has done its one-time migration work and should remain disabled. The canonical live site is deployed by `Deploy Proof Gradient Pages`.

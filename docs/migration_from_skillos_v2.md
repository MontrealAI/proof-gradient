# Migration from SkillOS v2.0.0

| SkillOS v2 concept | Proof Gradient concept |
|---|---|
| Skill | artifact type: skill |
| Skill version | ArtifactVersion |
| Skill release | Artifact release / Rollout |
| Skill trace | TraceEvent / Proof |
| Learning lesson | Patch rationale |
| Candidate skill | candidate ArtifactVersion |
| Eval result | EvalRun + EvalResult |
| Canary release | SelectionDecision + Rollout |
| Rollback planner | mandatory Rollback |
| Proof receipt | Proof Ledger record |

Legacy SkillOS tests have been quarantined under `tests_legacy_skillos/` until the compatibility layer is intentionally restored or fully superseded.

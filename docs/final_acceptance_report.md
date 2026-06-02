# Final Acceptance Report

This is the initial autonomous foundation acceptance report.

| Requirement | Implementation location | Tests | Remaining risk | Notes |
|---|---|---|---|---|
| Everything that can improve is an artifact | `proof_gradient/models.py` | `test_four_system_artifacts_exist` | Needs database persistence | Deterministic foundation only |
| Every run creates a contract | `RunContract` | `test_run_contract_resolves_versions` | Needs API/runtime integration | Contract is immutable dataclass |
| Every run emits proof | `Proof` | `test_proof_contains_trace_events` | Needs durable ledger | Append-only concept modeled |
| Scores include credit assignment | `Score` | `test_score_assigns_credit` | Needs richer attribution engine | Deterministic demo only |
| Patches are typed | `Patch` | `test_patch_has_rollback_target` | Needs diff viewer | Plan patch modeled |
| Selection supports canary and rollback | `SelectionDecision` | `test_selection_gate_canary` | Needs rollout router | Canary modeled |
| Public command center exists | `site/index.html` | Pages workflow | Needs full UI | Static command center |

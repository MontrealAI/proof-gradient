# Proof Gradient Architecture

## The four systems

### Artifact Vault

Stores reusable intelligence: goals, plans, skills, tools, policies, evals, rubrics, context recipes, routing rules, approval rules, and release rules.

Released artifacts must be immutable. Any change creates a new version.

### Run Fabric

Executes agents by resolving active artifact versions, creating a run contract, executing a deterministic or provider-backed runtime, and emitting trace events.

### Proof Ledger

Stores append-only evidence: run contract, artifact versions, trace events, output, cost, latency, eval results, human feedback, score, credit assignment, and patches.

### Selection Gate

Promotes only what proved itself. Candidate artifacts must be evaluated against baselines, approved, canaried, monitored, and rollbackable.

## Scaling law

```text
Artifacts are immutable.
Runs are stateless.
Proof is append-only.
Learning is asynchronous.
Selection is gated.
Propagation is scoped.
Rollback is mandatory.
```

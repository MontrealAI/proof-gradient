# Proof Gradient

**One agent tries. Proof decides. The network evolves.**

Proof Gradient is the agent evolution protocol where every run leaves proof, every proof selects intelligence, and every selected artifact evolves the network.

## The product truth

GoalOS gives the network **Direction**.  
PlanOS gives it **Strategy**.  
SkillOS gives it **Capability**.  
The Proof Gradient gives it **Evolution**.

## The four systems

| System | Role |
|---|---|
| **Artifact Vault** | Stores reusable intelligence. |
| **Run Fabric** | Executes agents at scale. |
| **Proof Ledger** | Records what happened. |
| **Selection Gate** | Promotes only what proved itself. |

## The operating law

```text
No proof, no evolution.
No eval, no propagation.
No rollback, no release.
```

## What this repository now contains

This repository now includes the first deterministic Proof Gradient foundation:

- a small no-dependency Python reference package
- versioned artifact models
- run contract model
- proof ledger demo
- score and credit-assignment record
- typed patch example
- canary release and rollback example
- JSON schemas
- documentation
- a public tabbed command center

## Local demo

```bash
python -m proof_gradient.demo
```

## Tests

```bash
python -m unittest tests/test_proof_gradient_foundation.py
```

## Public site

https://montrealai.github.io/proof-gradient/

## Status

This is a deterministic foundation and north-star vertical slice. It is not yet the complete production backend, API, database, UI, or worker system. The next phases are documented in `docs/architecture.md` and `docs/proof_gradient_platform.md`.

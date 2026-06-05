# AEP-003 — ProofPacket Schema

## One-page brief

AEP-003 defines the ProofPacket: the atomic proof unit for machine work.

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.

## Why it matters

If AI-agent work is going to be trusted, reused, governed, audited, and rolled back, every meaningful action needs a portable evidence unit.

That unit is the ProofPacket.

## Canonical law

No proof, no evolution.  
No eval, no propagation.  
No rollback, no release.

## Required fields

- packet_id
- schema
- schema_version
- packet_type
- created_at
- producer
- docket_id
- commitment_id
- run_id
- claim_refs
- evidence_refs
- boundary
- payload
- hash
- claim_boundary

## Packet types

commit, trace_event, tool_call, policy_decision, approval, eval_result, evidence_ref, risk_event, cost_event, selection_decision, rollout_event, rollback_event, public_report.

## Public line

GoalOS makes machine work provable one packet at a time.

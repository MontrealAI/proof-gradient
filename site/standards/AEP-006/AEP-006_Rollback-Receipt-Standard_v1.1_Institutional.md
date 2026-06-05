# AEP-006 — Rollback Receipt Standard

**Version:** v1.1 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standards:** AEP-001 — GoalOS Proof-of-Evolution Constitution; AEP-002 — Evidence Docket Standard; AEP-003 — ProofPacket Schema; AEP-004 — Selection Gate Standard; AEP-005 — Tool Permission Standard  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Author / Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-006 defines the **Rollback Receipt Standard**: the proof standard for recovery, restoration, reversal, compensation, freeze, quarantine, post-rollback verification, and post-incident review after machine work fails, violates policy, exceeds scope, causes side effects, degrades quality, or requires controlled reversion.

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.  
AEP-006 defines the recovery proof.

A rollback is not complete because someone says it is complete.  
A rollback is complete only when the recovery is executed, verified, and recorded.

## Canonical thesis

A model can answer.  
An agent can act.  
An institution must prove.  
A network must select.  
A tool must be permitted.  
A release must be recoverable.

## Canonical law

No rollback, no release.  
No receipt, no recovery claim.  
No restore point, no promotion.  
No compensation path, no irreversible action.  
No post-rollback verification, no closure.  
No proof, no evolution.

## Relationship to AEP-001 through AEP-005

- **AEP-001** defines the protocol: Commit → Execute → Prove → Evolve.
- **AEP-002** defines the Evidence Docket.
- **AEP-003** defines the ProofPacket.
- **AEP-004** defines the Selection Gate.
- **AEP-005** defines the Tool Permission Standard.
- **AEP-006** defines Rollback Receipts, recovery authorization, verification, compensation, and post-rollback review.

## What is rollback?

Rollback is a controlled recovery action that restores or moves a system, workflow, artifact, policy, tool permission, deployment, model route, or agent behavior to a safer state.

Rollback may include:

- restore baseline artifact
- revert workflow
- disable tool permission
- revoke lease
- stop canary
- freeze rollout
- quarantine agent or tool
- revert deployment
- undo database change
- restore previous prompt / policy / context
- send correction notice
- compensate affected party
- escalate incident

## What is a Rollback Receipt?

A Rollback Receipt is a structured, hashable, optionally signed record that proves what recovery action was taken, why it was taken, who or what authorized it, what evidence triggered it, what scope was affected, what was restored, how recovery was verified, what residual risk remains, and what is not claimed.

## Rollback status values

AEP-006 defines these status values:

- `not_required`
- `ready`
- `requested`
- `authorized`
- `in_progress`
- `completed`
- `verified`
- `partial`
- `failed`
- `compensation_required`
- `compensated`
- `quarantined`
- `archived`

## Recovery action types

AEP-006 defines these action types:

- `restore_baseline`
- `revert_artifact`
- `revert_workflow`
- `revoke_permission`
- `stop_canary`
- `freeze_rollout`
- `quarantine`
- `disable_agent`
- `disable_tool`
- `revert_deployment`
- `undo_transaction`
- `send_correction`
- `compensate`
- `escalate_incident`
- `manual_review`

## Required objects

AEP-006 defines the following objects:

1. Rollback Trigger
2. Rollback Plan
3. Rollback Request
4. Rollback Authorization
5. Rollback Receipt
6. Rollback Verification
7. Compensation Receipt
8. Post-Rollback Review
9. Recovery Bundle

## Rollback Trigger

A Rollback Trigger records the signal that initiated recovery.

Required fields:

- trigger_id
- trigger_type
- severity
- detected_by
- detected_at
- related_candidate_ref
- related_baseline_ref
- evidence_refs
- proof_packet_refs
- selection_certificate_ref
- tool_decision_refs
- description
- recommended_action

Trigger types may include:

- eval_failure
- policy_violation
- safety_incident
- privacy_incident
- security_incident
- cost_overrun
- latency_regression
- quality_regression
- unauthorized_tool_use
- canary_stop_condition
- user_report
- monitoring_alert
- manual_escalation

## Rollback Plan

A Rollback Plan must exist before high-impact release.

Required fields:

- rollback_plan_id
- rollback_target
- baseline_ref
- candidate_ref
- scope
- owner
- preconditions
- rollback_steps
- verification_steps
- compensation_plan_ref
- expected_recovery_time
- communication_required
- evidence_required
- post_rollback_review_required

## Rollback Request

A Rollback Request initiates rollback.

Required fields:

- rollback_request_id
- trigger_id
- rollback_plan_id
- requested_by
- requested_at
- reason
- requested_scope
- urgency
- evidence_docket_refs
- proof_packet_refs
- affected_users_or_systems
- authorization_required

## Rollback Authorization

Rollback Authorization records approval.

Required fields:

- authorization_id
- rollback_request_id
- authorized_by
- authorizer_role
- authorization_status
- authorization_reason
- authorized_scope
- risk_acceptance
- issued_at
- expiration
- signature
- proof_packet_ref

## Rollback Receipt

A Rollback Receipt records execution.

Required fields:

- receipt_id
- schema
- schema_version
- rollback_request_id
- rollback_plan_id
- trigger_id
- status
- action_type
- rollback_target
- baseline_ref
- candidate_ref
- affected_scope
- executed_by
- started_at
- completed_at
- steps_executed
- evidence_refs
- proof_packet_refs
- tool_receipt_refs
- selection_certificate_refs
- verification_ref
- compensation_ref
- residual_risk
- public_private_boundary
- claim_boundary
- hash

## Rollback Verification

Rollback Verification proves recovery succeeded or failed.

Required fields:

- verification_id
- receipt_id
- verified_by
- verification_status
- verification_method
- eval_refs
- test_refs
- monitoring_refs
- evidence_refs
- restored_baseline_confirmed
- side_effects_remaining
- residual_risk
- verified_at
- proof_packet_ref
- hash

## Compensation Receipt

Compensation Receipt records remediation when rollback is impossible or insufficient.

Required fields:

- compensation_id
- receipt_id
- compensation_reason
- compensation_action
- compensation_owner
- compensation_status
- affected_scope
- evidence_refs
- user_or_customer_notice
- created_at
- proof_packet_ref
- hash

## Post-Rollback Review

A Post-Rollback Review turns failure into reusable knowledge.

Required fields:

- review_id
- receipt_id
- root_cause_summary
- what_failed
- what_worked
- evidence_gaps
- policy_updates
- eval_updates
- tool_permission_updates
- selection_gate_updates
- artifact_updates
- recurrence_prevention
- owner
- due_date
- status

## Required release invariant

A high-impact release must have, before release:

- rollback target
- rollback plan
- rollback owner
- rollback trigger
- verification plan
- compensation path if rollback is impossible
- Evidence Docket or release proof
- Selection Certificate or equivalent release authority

If these do not exist, release is non-conformant.

## Default recovery logic

The default recovery logic should be conservative:

- failed eval → stop canary or rollback
- policy violation → rollback or quarantine
- unauthorized tool use → revoke permission and rollback affected changes
- privacy/security incident → quarantine, revoke, incident escalation
- no restore point → compensate, freeze, and escalate
- failed rollback → compensation required and incident review

## Conformance levels

### Level 0 — Informal rollback note

Rollback described in plain language.

### Level 1 — Rollback plan

Rollback target, owner, steps, and verification plan exist.

### Level 2 — Rollback receipt

Rollback execution is recorded with status, scope, evidence, and hash.

### Level 3 — Verified rollback

Rollback verification exists with tests, evals, monitoring, residual risk, and proof reference.

### Level 4 — Institutional rollback

Rollback receipt includes authorization, Evidence Docket refs, ProofPacket refs, Selection Certificate refs, tool receipts, compensation path, public/private boundary, and post-rollback review.

### Level 5 — Sovereign / regulated rollback

Rollback includes jurisdiction, retention, protected-boundary classification, authorized approvers, public-safe report controls, affected-public notice rules, post-incident review, and institutional or sovereign audit export.

## Security and privacy requirements

A Rollback Receipt must not leak private or protected evidence into public proof.

Public receipts may state that rollback occurred, what scope was affected, and what was verified without exposing sensitive prompts, private traces, secrets, customer data, protected infrastructure, or privileged analysis.

## Claim boundary

AEP-006 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-006 defines a recovery proof standard.

## Canonical public line

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.  
AEP-006 defines the recovery proof.

GoalOS releases only what can recover, and proves when recovery happens.

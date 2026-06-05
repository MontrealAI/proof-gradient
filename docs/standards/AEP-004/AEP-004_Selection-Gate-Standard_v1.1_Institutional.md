# AEP-004 — Selection Gate Standard

**Version:** v1.1 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standards:** AEP-001 — GoalOS Proof-of-Evolution Constitution; AEP-002 — Evidence Docket Standard; AEP-003 — ProofPacket Schema  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Author / Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-004 defines the **Selection Gate**: the propagation boundary that decides whether a candidate artifact, workflow, policy, tool, evaluation, context recipe, model route, agent behavior, or capability may be promoted, canaried, revised, rejected, archived, rolled back, or held for more evidence.

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.

A Selection Gate is the institutional mechanism that converts proof into governed evolution.

## Canonical thesis

A model can answer.  
An agent can act.  
An institution must prove.  
A network must select.

## Canonical law

No proof, no evolution.  
No eval, no propagation.  
No rollback, no release.

## v1.1 upgrades

AEP-004 v1.1 adds implementation-level materials:

- gate policy schema
- evidence requirement schema
- evaluation requirement schema
- selection candidate schema
- selection certificate schema
- challenge record schema
- canary plan schema
- monitoring plan schema
- rollback plan schema
- revocation / supersession model
- deterministic reference decision engine
- certificate hash tool
- certificate validator
- conformance scorer
- full examples for all canonical decisions
- implementation guide
- security and privacy guide
- policy profile guide
- GitHub Actions for website, conformance CI, and official release

## Relationship to AEP-001, AEP-002, and AEP-003

AEP-001 defines the constitutional loop:

`Commit → Execute → Prove → Evolve`

AEP-002 defines the Evidence Docket, the portable proof package.

AEP-003 defines the ProofPacket, the atomic evidence unit.

AEP-004 defines the Selection Gate, the decision standard for what may evolve.

In short:

- **AEP-001** defines the protocol.
- **AEP-002** defines the docket.
- **AEP-003** defines the packet.
- **AEP-004** defines the gate.

## What is a Selection Gate?

A Selection Gate is a structured decision process that evaluates a candidate upgrade against evidence, evaluations, policies, risks, costs, approvals, rollout constraints, challenge windows, expiration, and rollback readiness.

It prevents unproven local behavior from becoming network-wide capability.

It answers:

1. What is being proposed?
2. What is the baseline?
3. What evidence supports the candidate?
4. Which Evidence Dockets contain the proof?
5. Which ProofPackets support the claims?
6. Which evals passed?
7. Which evals failed?
8. What risks remain?
9. What is the allowed scope?
10. Who or what approved the decision?
11. Is canary rollout required?
12. What monitoring is required?
13. What is the rollback target?
14. When does the decision expire or require review?
15. What is explicitly not claimed?

## Gate decisions

AEP-004 defines these canonical decisions:

### promote

The candidate may become the active default within the approved scope.

### approve_canary

The candidate may be deployed to a limited scope under monitoring.

### revise

The candidate has partial merit but must be modified and re-evaluated.

### reject

The candidate must not propagate.

### archive

The candidate is retained as evidence/history but not used.

### rollback

The existing promoted capability must be reverted to a prior safe state.

### needs_more_evidence

The candidate cannot be judged until additional proof, evals, approvals, or rollback plans exist.

## Gate modes

A Selection Gate can operate in one of four modes.

### advisory

The gate recommends a decision but does not enforce propagation.

### manual

A human or institutional approver must issue the final certificate.

### automated_bounded

The gate may issue decisions automatically within low-risk bounded scope.

### emergency

The gate may trigger rollback under pre-authorized incident conditions.

## Selection Candidate

A Selection Gate receives a **Selection Candidate**.

Required fields:

- candidate_id
- schema
- schema_version
- candidate_type
- candidate_ref
- baseline_ref
- proposer
- reason_for_change
- intended_scope
- evidence_docket_refs
- proof_packet_refs
- eval_refs
- risk_refs
- policy_refs
- cost_summary
- rollback_target
- requested_decision

Candidate types may include:

- goal
- plan
- skill
- capability
- policy
- eval
- tool
- context
- route
- workflow
- model
- agent_behavior
- artifact_version

## Gate Policy

A Gate Policy defines the criteria for selection.

Required fields:

- policy_id
- policy_version
- gate_name
- gate_mode
- applicable_candidate_types
- required_evidence_level
- required_eval_status
- quality_threshold
- safety_threshold
- cost_threshold
- latency_threshold
- risk_threshold
- approval_requirements
- challenge_window
- canary_required
- rollback_required
- monitoring_required
- publication_rules
- expiration_required

## Decision criteria

A Selection Gate must evaluate:

### Evidence sufficiency

Is there an Evidence Docket?

Are the relevant claims supported by ProofPackets?

Are unsupported claims separated from supported claims?

### Evaluation sufficiency

Have the required evals passed?

Are regressions recorded?

Are evaluator limitations documented?

### Policy sufficiency

Were permissions, approvals, and guardrails followed?

Were policy denials or escalations resolved?

### Risk sufficiency

Is residual risk acceptable for the intended scope?

Are protected or restricted evidence boundaries respected?

### Cost and latency sufficiency

Does the candidate improve or justify cost, latency, and human-review burden?

### Approval sufficiency

Are required approvers recorded?

Is the gate operating in a mode where automation is allowed?

### Challenge sufficiency

Has the decision passed a challenge window, or is the decision emergency-bounded?

### Rollout sufficiency

Is the scope controlled?

Is canary rollout required?

Is monitoring defined?

### Rollback sufficiency

Is rollback possible?

Is the rollback target valid?

Are triggers and owners clear?

### Claim-boundary sufficiency

Does the decision state what may and may not be claimed?

## Selection Certificate

A Selection Gate emits a **Selection Certificate**.

Required fields:

- certificate_id
- schema
- schema_version
- decision
- gate_mode
- candidate_id
- candidate_type
- candidate_ref
- baseline_ref
- evidence_docket_refs
- proof_packet_refs
- eval_refs
- risk_refs
- policy_refs
- decision_reason
- approved_scope
- canary_plan
- monitoring_plan
- rollback_plan
- challenge_record
- claim_boundary
- approver
- issued_at
- expires_at
- review_after
- hash

Recommended fields:

- previous_certificate_hash
- supersedes_certificate
- revocation_status
- signature
- attestations
- public_safe_summary

## Decision table

The default decision logic must be conservative.

| Evidence | Eval | Risk | Rollback | Default decision |
|---|---|---|---|---|
| strong | passed | low | ready | promote |
| strong | passed | medium | ready | approve_canary |
| partial | passed | low/medium | ready | approve_canary or revise |
| weak | passed | any | ready | revise or needs_more_evidence |
| any | failed | any | any | reject |
| any | any | high/protected | not ready | reject |
| any | any | any | not ready | reject or rollback |
| existing active capability has severe issue | failed/incident | high | ready | rollback |

## Invariants

A conforming Selection Gate must obey these invariants:

1. `promote` requires evidence, eval success, risk acceptance, scope, monitoring, and rollback readiness.
2. `approve_canary` requires evidence, eval success, limited scope, monitoring, stop conditions, and rollback readiness.
3. `reject` must record why the candidate cannot propagate.
4. `rollback` must identify the rollback target and trigger.
5. `needs_more_evidence` must specify missing evidence.
6. `archive` must not silently promote or route traffic.
7. A protected-risk candidate must not promote through automated_bounded mode unless explicitly authorized.
8. A public Selection Certificate must not leak private or protected evidence.
9. A Selection Certificate must include a claim boundary.
10. Under uncertainty, the gate must fail closed.

## Canary Plan

A canary plan defines limited rollout.

Required fields:

- canary_required
- canary_scope
- canary_percentage
- duration
- monitoring_metrics
- stop_conditions
- promotion_conditions
- owner

## Monitoring Plan

A monitoring plan defines post-decision supervision.

Required fields:

- metrics
- thresholds
- frequency
- owner
- escalation_path
- review_after
- incident_triggers

## Rollback Plan

A rollback plan defines recovery.

Required fields:

- rollback_required
- rollback_target
- rollback_trigger
- rollback_owner
- rollback_steps
- expected_recovery_time
- post_rollback_review

## Challenge Record

A challenge record documents the review or objection window.

Required fields:

- challenge_window_required
- challenge_window_duration
- challenge_status
- challenger_refs
- unresolved_challenges
- resolution_summary

Allowed statuses:

- not_required
- open
- cleared
- unresolved
- waived
- emergency_override

## Certificate revocation and supersession

A Selection Certificate may be revoked or superseded.

Revocation statuses:

- active
- superseded
- revoked
- expired
- rolled_back

A revoked certificate must identify:

- revocation_reason
- revoked_by
- revoked_at
- replacement_certificate_ref
- rollback_ref, if applicable

## Conformance levels

### Level 0 — Informal selection

Human-readable decision with evidence and reason.

### Level 1 — Basic Selection Gate

Valid candidate and decision record with evidence docket reference.

### Level 2 — Evaluated Selection Gate

Includes eval requirements, pass/fail status, risk status, and rollback target.

### Level 3 — Operational Selection Gate

Includes gate policy, canary plan, monitoring plan, approval record, challenge record, and claim boundary.

### Level 4 — Institutional Selection Gate

Includes signed Selection Certificate, conformance checks, audit export, rollback readiness, expiration, review_after, and public/private evidence boundary.

### Level 5 — Sovereign / Regulated Selection Gate

Includes jurisdiction, protected-boundary classification, retention policy, authorized approvers, evaluator attestations, timestamp authority, challenge window, revocation model, and public-safe report controls.

## Selection Gate lifecycle

1. Candidate submitted
2. Evidence gathered
3. Evidence Docket validated
4. ProofPackets checked
5. Required evals checked
6. Policy and approval records checked
7. Risk and cost reviewed
8. Challenge window cleared or waived
9. Rollout and rollback plans checked
10. Decision issued
11. Certificate recorded
12. Canary / monitoring begins, if applicable
13. Promote, revise, reject, archive, or rollback
14. Review, expire, supersede, or revoke certificate
15. Public-safe summary published, if allowed

## Security and privacy requirements

A Selection Gate must not require public disclosure of private or protected evidence.

It must be able to select based on private or protected evidence while publishing only public-safe summaries.

The Selection Certificate should record the existence and sufficiency of restricted evidence without exposing the restricted evidence itself.

## Claim boundary

AEP-004 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-004 defines a selection and propagation standard.

## Canonical public line

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.

GoalOS promotes only what proved itself.

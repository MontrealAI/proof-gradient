# AEP-002 — Evidence Docket Standard

**Version:** v1.1 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standard:** AEP-001 — GoalOS Proof-of-Evolution Constitution  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-002 defines the **Evidence Docket**: the standard proof package for AI-agent work, machine work, governed AI-assisted workflows, institutional AI adoption, Proof Rooms, and Agent Control Planes.

AEP-001 defines the constitutional loop: **Commit → Execute → Prove → Evolve**. AEP-002 defines the portable proof object that makes the loop operational.

A model can answer.  
An agent can act.  
An institution must prove.

**AEP-002 makes the proof portable.**

## Canonical law

No proof, no evolution.  
No eval, no propagation.  
No rollback, no release.

## What an Evidence Docket must answer

1. What was the machine asked to do?
2. Who or what authorized it?
3. What context, tools, policies, and constraints were in scope?
4. What happened?
5. What evidence exists?
6. Which checks or evals passed?
7. What failed or remains uncertain?
8. What can honestly be claimed?
9. What may be reused or promoted?
10. What can be rolled back?

## Relationship to AEP-001

AEP-001 defines the constitutional architecture:

- **Artifact Vault** — stores reusable intelligence.
- **Run Fabric** — executes agents at scale.
- **Proof Ledger** — records what happened.
- **Selection Gate** — promotes only what proved itself.

AEP-002 defines the evidence object produced and consumed by that architecture.

## Core object model

An Evidence Docket contains:

1. Manifest
2. Claims Matrix
3. Commitment Record
4. Execution Summary
5. Evidence Inventory
6. ProofPackets
7. Tool-Use Ledger
8. Policy and Approval Ledger
9. Evaluation Results
10. Cost and Latency Ledger
11. Risk Ledger
12. Selection Certificate
13. Rollout / Canary Plan
14. Rollback Plan
15. Public-Safe Report
16. Private Appendix
17. Claim Boundary

## Minimum viable Evidence Docket

A minimum viable Evidence Docket must include:

- manifest
- claims matrix
- commitment record
- execution summary
- evidence inventory
- at least one evaluation or explicit evaluation gap
- risk ledger
- selection decision or pending-selection status
- rollback plan
- claim boundary

If a required section is unavailable, the docket must explicitly state one of:

- not collected
- not applicable
- restricted
- pending review
- unavailable

Silent omission is non-conformant.

## Manifest

The manifest identifies the docket and its authority.

Required fields:

- docket_id
- protocol
- protocol_version
- parent_standard
- title
- owner
- organization
- jurisdiction
- created_at
- updated_at
- status
- confidentiality_class
- public_safe_available
- checksum
- related_artifacts

## Claims Matrix

The claims matrix separates supported claims from unsupported claims.

Required fields:

- claim_id
- claim_text
- claim_type
- evidence_refs
- eval_refs
- risk_refs
- confidence
- public_claim_allowed
- not_claimed

The claims matrix must explicitly list what is **not** being claimed.

## Commitment Record

The commitment record states what was intended before the run.

Required fields:

- goal
- success_criteria
- failure_criteria
- constraints
- risk_class
- authorized_by
- allowed_tools
- disallowed_tools
- required_evals
- approval_rules
- budget
- rollback_required

## Execution Summary

The execution summary records what happened without exposing restricted traces.

Required fields:

- run_id
- agent_or_system
- model_or_engine_class
- execution_environment
- started_at
- completed_at
- status
- output_summary
- human_review_status
- exceptions
- incident_flags

## Evidence Inventory

The evidence inventory records where proof exists.

Required fields:

- evidence_id
- evidence_type
- description
- storage_location
- hash
- access_class
- public_safe
- retention_policy
- related_claims

Evidence types may include:

- prompt
- output
- trace
- tool_call
- log
- code_diff
- document
- screenshot
- benchmark
- test_result
- human_review
- evaluator_report
- approval_record
- rollback_record

## ProofPacket

A ProofPacket is an atomic evidence unit inside a docket.

Required fields:

- proof_packet_id
- run_id
- claim_ref
- evidence_refs
- eval_status
- policy_status
- risk_status
- cost_summary
- latency_summary
- trace_root
- checksum
- signature
- created_at

## Tool-Use Ledger

The tool-use ledger records tool calls, permissions, approvals, and outcomes.

Required fields:

- tool_name
- permission_class
- request_summary
- allowed
- approval_required
- approval_received
- result_summary
- risk_flag
- rollback_possible

## Policy and Approval Ledger

The policy and approval ledger records governance decisions.

Required fields:

- policy_name
- decision
- reason
- actor
- timestamp
- related_tool_call
- related_claim
- escalation_required

## Evaluation Results

The evaluation section records how the output was checked.

Required fields:

- eval_id
- eval_name
- eval_type
- baseline
- candidate
- passed
- score
- quality_delta
- safety_delta
- cost_delta
- latency_delta
- evaluator
- evidence_ref
- limitations

## Cost and Latency Ledger

The cost and latency ledger records operational efficiency.

Required fields:

- cost_currency
- estimated_cost
- actual_cost
- token_count
- compute_time
- wall_clock_time
- human_review_time
- cost_per_verified_output
- notes

## Risk Ledger

The risk ledger records known and potential harms.

Required fields:

- risk_id
- risk_type
- severity
- likelihood
- mitigation
- residual_risk
- owner
- status
- evidence_ref

## Selection Certificate

The Selection Certificate records whether the result may propagate.

Allowed decisions:

- promote
- approve_canary
- reject
- revise
- archive
- rollback
- needs_more_evidence

Required fields:

- decision
- reason
- evidence_refs
- eval_refs
- scope
- canary_plan
- monitoring_plan
- rollback_target
- approver
- timestamp

## Rollout / Canary Plan

A canary plan is required for any propagated capability that affects users, customers, institutions, systems, money, public claims, or protected data.

Required fields:

- rollout_scope
- rollout_percentage
- target_population
- monitoring_metrics
- stop_conditions
- escalation_path
- rollback_trigger

## Rollback Plan

The rollback plan explains how to undo or stop the capability.

Required fields:

- rollback_required
- rollback_target
- rollback_trigger
- rollback_owner
- rollback_steps
- expected_recovery_time
- user_or_customer_notice_required
- post_rollback_review

## Public-Safe Report

The public-safe report is the shareable proof layer.

Required fields:

- what_was_tested
- what_happened
- evidence_summary
- what_passed
- what_failed
- what_is_claimed
- what_is_not_claimed
- next_step
- contact_or_owner
- publication_status

## Private Appendix

The private appendix contains restricted material.

May include:

- full prompts
- private traces
- sensitive tool logs
- protected datasets
- security notes
- customer data references
- legal or compliance review notes
- evaluator notes
- incident details

The private appendix must not be published unless explicitly authorized.

## Public / private / protected evidence boundary

AEP-002 defines three evidence classes.

### Public

May be shared externally after claim-boundary review.

Examples:

- high-level goal
- public-safe claim
- evidence summary
- eval status
- rollback status
- public-safe report

### Private

Internal to the organization.

Examples:

- detailed prompts
- execution traces
- private tool logs
- review notes
- operational cost details
- internal artifact versions

### Protected

Restricted to authorized roles.

Examples:

- secrets
- regulated data
- critical infrastructure details
- security vulnerabilities
- sensitive personal data
- privileged legal analysis
- national-security-sensitive information

A public Evidence Docket must not leak private or protected evidence.

## Conformance levels

### Level 0 — Informal proof

A narrative proof page with goal, output, evidence, checks, and claim boundary.

### Level 1 — Basic Evidence Docket

Includes minimum viable sections and at least one evaluation or explicit evaluation gap.

### Level 2 — Operational Evidence Docket

Includes tool-use ledger, policy ledger, cost ledger, risk ledger, selection decision, and rollback plan.

### Level 3 — Institutional Evidence Docket

Includes full public/private boundary, Selection Certificate, canary plan, monitoring plan, rollback receipt, and audit export.

### Level 4 — Sovereign / Regulated Evidence Docket

Includes public/private/protected classification, retention policy, jurisdiction, authorized data boundary, evaluator attestations, and restricted appendix controls.

## Lifecycle

1. Draft
2. Submitted
3. Under review
4. Evidence accepted
5. Selection decision issued
6. Canary / monitor
7. Promoted / rejected / revised / rolled back
8. Archived
9. Public-safe report published, if allowed

## Security and privacy requirements

- Do not publish secrets.
- Do not publish private prompts unless authorized.
- Do not publish customer data unless authorized and safe.
- Do not publish protected operational traces.
- Do not publish critical infrastructure details.
- Do not imply more than the evidence supports.

## Implementation guidance

Recommended implementation sequence:

1. Add a docket template.
2. Generate one docket per important AI workflow.
3. Record claims separately from evidence.
4. Store private evidence separately from public proof.
5. Run at least one eval.
6. Create a rollback plan.
7. Require Selection Gate review before propagation.
8. Publish a public-safe report only after claim-boundary review.

## Claim boundary

AEP-002 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-002 defines a proof package standard.

## Canonical public line

A model can answer.  
An agent can act.  
An institution must prove.

AEP-002 makes the proof portable.

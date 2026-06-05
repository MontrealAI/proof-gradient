# AEP-005 — Tool Permission Standard

**Version:** v1.1 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standards:** AEP-001 — GoalOS Proof-of-Evolution Constitution; AEP-002 — Evidence Docket Standard; AEP-003 — ProofPacket Schema; AEP-004 — Selection Gate Standard  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Author / Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-005 defines the **Tool Permission Standard**: the governance layer that determines whether an AI agent, workflow, model route, human operator, or automated system may use a tool, under what scope, for how long, with which approvals, what evidence must be recorded, and what rollback or compensation path is required.

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines tool authority.

A model may know a tool exists.  
An agent may request a tool.  
Only the Tool Gateway may authorize its use.

## Canonical thesis

A model can answer.  
An agent can act.  
An institution must prove.  
A network must select.  
A tool must be permitted.

## Canonical law

No tool without permission.  
No action without scope.  
No high-risk tool without approval.  
No side effect without receipt.  
No irreversible action without rollback or compensation.  
No permanent authority without expiration.  
No proof, no evolution.

## v1.1 upgrades

AEP-005 v1.1 adds:

- permission leases
- revocation receipts
- compensation receipts
- break-glass requests
- data-boundary rules
- rate-limit policies
- least-privilege profiles
- separation-of-duties requirements
- public/private/protected tool input boundaries
- tool gateway audit tooling
- conformance scoring
- implementation and security guides

## Relationship to AEP-001 through AEP-004

- **AEP-001** defines the protocol: Commit → Execute → Prove → Evolve.
- **AEP-002** defines the Evidence Docket.
- **AEP-003** defines the ProofPacket.
- **AEP-004** defines the Selection Gate.
- **AEP-005** defines the Tool Gateway, permission classes, tool manifests, permission policies, permission requests, permission decisions, leases, approvals, receipts, revocation, compensation, and proof requirements.

## What is a tool?

A tool is any external or internal capability that an agent, workflow, model route, or system can invoke to observe, transform, write, send, delete, deploy, spend, retrieve secrets, change permissions, or affect an environment.

Examples:

- search
- retrieval
- file read
- database query
- code execution
- web browser
- email draft
- email send
- calendar update
- CRM write
- ticket update
- payment
- deployment
- secret access
- admin permission change
- external contact
- destructive delete
- production release

## What is a Tool Gateway?

A Tool Gateway is the enforcement point between an agent and a tool.

The Tool Gateway receives a request, evaluates policy, checks scope, checks lease status, checks approval state, checks data boundary, records a decision, and emits a proof receipt.

The Tool Gateway must fail closed.

If the Tool Gateway cannot decide, the default decision is:

`deny`

or:

`approval_required`

depending on policy.

## Tool authority model

AEP-005 separates eight concepts:

1. **Ability** — the tool exists and can technically be called.
2. **Authority** — the agent or workflow is allowed to request it.
3. **Scope** — the permitted boundaries of use.
4. **Lease** — the permission is time-bounded and revocable.
5. **Approval** — human, policy, or institutional authorization.
6. **Execution** — the actual tool call.
7. **Receipt** — the execution result and side effects are recorded.
8. **Proof** — the decision and receipt anchor into ProofPackets and Evidence Dockets.

Knowing a tool exists is not authority to use it.

## Permission classes

AEP-005 defines canonical permission classes.

- `none` — tool unavailable.
- `read` — observe, retrieve, inspect, list, or query without changing state.
- `draft` — prepare an output, message, plan, file, or change without applying it.
- `transform` — transform provided data without external side effects.
- `write` — change internal state, update a file, create a record, or modify a system.
- `execute` — run code, commands, jobs, scripts, automations, or computational tasks.
- `external_contact` — contact or interact with external people, systems, vendors, customers, agencies, or public endpoints.
- `send` — send a message, notification, publication, post, email, form, API request, or external output.
- `delete` — delete, destroy, revoke, remove, or irreversibly alter a resource.
- `deploy` — release, publish, ship, merge, promote, or activate a capability in a production or public environment.
- `payment` — spend money, transfer value, initiate purchase, change billing, execute transaction, or access payment rails.
- `secret_access` — read or use secrets, credentials, tokens, keys, private data, privileged material, or protected evidence.
- `admin_change` — change permissions, roles, policies, accounts, infrastructure, routing, governance, or administrative controls.
- `protected_operation` — perform a high-impact or regulated operation that requires special authorization.
- `break_glass` — emergency use outside normal policy with mandatory justification, elevated approval, monitoring, and post-incident review.

## Permission decision types

A Tool Gateway may issue these decisions:

- `allow`
- `deny`
- `approval_required`
- `allow_readonly`
- `allow_draft_only`
- `allow_with_redaction`
- `allow_with_canary`
- `allow_with_rollback`
- `allow_with_lease`
- `allow_with_rate_limit`
- `escalate`
- `quarantine`
- `break_glass_approved`

## Required objects

AEP-005 defines the following objects:

1. Tool Manifest
2. Tool Permission Policy
3. Tool Request
4. Tool Permission Decision
5. Permission Lease
6. Approval Receipt
7. Tool Call Receipt
8. Revocation Receipt
9. Compensation Receipt
10. Break-Glass Request
11. Data Boundary Rule
12. Rate-Limit Policy

## Required Tool Manifest

Every tool must have a manifest.

Required fields:

- tool_id
- tool_name
- tool_version
- provider
- description
- permission_classes_supported
- default_permission
- risk_class
- side_effects
- data_access
- external_effect
- rollback_supported
- compensation_supported
- approval_required_for
- audit_required
- evidence_required
- owner
- status

## Required Permission Policy

A Tool Permission Policy defines who may use what.

Required fields:

- policy_id
- policy_version
- policy_name
- applicable_tools
- applicable_agents
- applicable_workflows
- allowed_permission_classes
- denied_permission_classes
- approval_required_for
- max_risk_class
- allowed_data_classes
- allowed_environments
- scope_constraints
- time_constraints
- budget_constraints
- rate_limits
- rollback_requirements
- compensation_requirements
- separation_of_duties
- logging_requirements
- public_private_boundary
- fail_closed

## Required Tool Request

A Tool Request is the object an agent or workflow submits before using a tool.

Required fields:

- request_id
- tool_id
- requester
- tenant_id
- workflow_id
- run_id
- commitment_id
- requested_permission_class
- intended_action
- justification
- input_summary
- data_classes
- target_environment
- external_effect
- expected_side_effects
- rollback_plan_ref
- compensation_plan_ref
- evidence_docket_ref
- proof_packet_refs

## Required Tool Permission Decision

A Tool Permission Decision records the gateway decision.

Required fields:

- decision_id
- request_id
- tool_id
- decision
- decision_reason
- allowed_scope
- denied_scope
- approval_required
- approver_role
- lease_ref
- policy_refs
- risk_refs
- issued_at
- expires_at
- proof_packet_ref
- hash

## Permission Lease

A Permission Lease is a time-bounded and scope-bounded grant of authority.

Required fields:

- lease_id
- decision_id
- request_id
- tool_id
- permission_class
- scope
- issued_at
- expires_at
- revocable
- revocation_conditions
- remaining_uses
- rate_limit_ref
- proof_packet_ref
- hash

A permission is not a permanent power. It is a bounded lease.

## Approval Receipt

An Approval Receipt records human or institutional approval.

Required fields:

- approval_id
- decision_id
- request_id
- approver
- approver_role
- approval_status
- approval_reason
- approved_scope
- expiration
- issued_at
- signature
- proof_packet_ref

## Tool Call Receipt

A Tool Call Receipt records what happened after a permitted tool call.

Required fields:

- receipt_id
- decision_id
- request_id
- tool_id
- lease_id
- executed
- execution_status
- result_summary
- side_effects_observed
- output_refs
- evidence_refs
- cost_summary
- latency_summary
- rollback_status
- compensation_status
- proof_packet_ref
- created_at
- hash

## Revocation Receipt

A Revocation Receipt records termination of tool authority.

Required fields:

- revocation_id
- lease_id
- decision_id
- request_id
- tool_id
- revocation_reason
- revoked_by
- revoked_at
- effective_immediately
- affected_scope
- proof_packet_ref
- hash

## Compensation Receipt

A Compensation Receipt records remediation when rollback is impossible or insufficient.

Required fields:

- compensation_id
- receipt_id
- tool_id
- compensation_reason
- compensation_action
- compensation_owner
- compensation_status
- evidence_refs
- created_at
- proof_packet_ref
- hash

## Break-Glass Request

A Break-Glass Request records emergency tool use outside normal policy.

Required fields:

- break_glass_id
- request_id
- tool_id
- requester
- emergency_reason
- risk_acceptance
- emergency_scope
- approver
- monitoring_required
- post_incident_review_required
- expires_at
- proof_packet_ref

Break-glass authority must be temporary, monitored, and reviewed.

## Scope constraints

Tool permissions must be scoped.

Recommended scope dimensions:

- tenant
- user
- agent
- workflow
- run
- commitment
- artifact
- data class
- environment
- geography / jurisdiction
- time window
- budget
- rate limit
- action type
- target system
- approval status
- lease status

Unscoped permissions are non-conformant for side-effecting tools.

## Default-deny rule

The default decision is deny.

A tool call must be denied when:

- no tool manifest exists
- no policy applies
- requested class is not supported
- requested class is denied
- approval is required but absent
- scope is missing
- lease is missing or expired
- rollback is required but missing
- compensation is required but missing
- request touches protected data without protected authorization
- request violates data boundary
- request exceeds budget
- request exceeds rate limit
- request targets a forbidden environment
- separation of duties is violated
- the gateway cannot evaluate the policy

## High-risk permission rules

- `write` requires evidence, policy, scope, and receipt.
- `send` and `external_contact` require approval unless explicitly pre-authorized by policy and scope.
- `delete` requires approval, rollback or compensation plan, and receipt.
- `deploy` requires Selection Gate or release authority, monitoring, and rollback.
- `payment` requires financial authorization, budget scope, and receipt.
- `secret_access` requires protected access authority, redaction boundary, and evidence controls.
- `admin_change` requires elevated approval, separation of duties, and audit trail.
- `protected_operation` requires protected authorization, public/private/protected boundary, and institutional review.
- `break_glass` requires emergency justification, temporary scope, monitoring, and post-incident review.

## Proof requirements

Every Tool Permission Decision should emit or reference an AEP-003 ProofPacket.

Every Permission Lease should emit or reference an AEP-003 ProofPacket.

Every executed tool call should emit or reference a Tool Call Receipt.

Every side-effecting tool call should be included in an AEP-002 Evidence Docket.

High-risk decisions should be visible to an AEP-004 Selection Gate before propagation.

## Conformance levels

### Level 0 — Informal tool note

Tool use is described in plain language.

### Level 1 — Tool manifest

Every tool has a manifest and permission class.

### Level 2 — Gateway decision

Every tool request receives allow, deny, or approval_required.

### Level 3 — Scoped leased permission

Every allowed tool call has tenant, workflow, run, time, data, environment, and lease scope.

### Level 4 — Institutional permission

High-risk tool calls require approval, leases, receipts, ProofPackets, rollback/compensation, revocation, and audit export.

### Level 5 — Sovereign / regulated permission

Protected operations require jurisdiction, retention, data boundary, authorized approvers, separation of duties, public/private/protected evidence boundary, institutional or sovereign review, revocation, and post-incident controls.

## Invariants

1. No tool call without a manifest.
2. No permission without policy.
3. No high-risk action without scope.
4. No permission lease without expiration.
5. No side effect without receipt.
6. No external send without approval or explicit preauthorization.
7. No secret access without protected authority.
8. No admin change without elevated approval and separation of duties.
9. No deploy without rollback.
10. No payment without financial authorization.
11. No protected operation without protected boundary.
12. No break-glass without review.
13. No public proof may leak private or protected tool inputs.
14. Under uncertainty, the Tool Gateway must fail closed.

## Security and privacy requirements

Tool permissions must prevent private or protected data from leaking into public proof.

Public receipts may state that a tool was used, what permission class applied, and what decision was issued without exposing sensitive inputs, secrets, private payloads, or protected outputs.

## Claim boundary

AEP-005 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-005 defines a tool permission and proof standard.

## Canonical public line

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.

GoalOS allows only what is scoped, approved, leased, revocable, and provable.

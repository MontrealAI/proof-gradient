# AEP-008 — Proof Room Standard

**Version:** v1.1 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standards:** AEP-001 through AEP-007  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Author / Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-008 defines the **Proof Room**: the governed workspace where machine work becomes institutional proof.

A Proof Room is the operating environment that binds the AEP stack into repeatable practice. It collects commitments, runs, ProofPackets, Evidence Dockets, Selection Gate decisions, Tool Permission records, Rollback Receipts, and Public-Safe Proof Reports into one controlled room with explicit roles, scope, boundaries, review, approvals, publication rules, audit export, and closure.

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.  
AEP-006 defines the recovery proof.  
AEP-007 defines the public proof.  
AEP-008 defines the room.

## Canonical thesis

A model can answer.  
An agent can act.  
An institution must prove.  
A network must select.  
A tool must be permitted.  
A release must recover.  
A public claim must be safe.  
A Proof Room makes the system operable.

## Canonical law

No room without charter.  
No run without scope.  
No evidence without boundary.  
No promotion without gate.  
No tool without permission.  
No release without rollback.  
No public proof without redaction.  
No closure without archive.  
No proof, no evolution.

## Purpose

A Proof Room exists to answer:

1. What work is being governed?
2. Who is responsible?
3. What is in scope and out of scope?
4. Which agents, tools, workflows, artifacts, and data boundaries are allowed?
5. What evidence was generated?
6. Which claims are supported?
7. Which claims are not supported?
8. What may be promoted?
9. What must be rolled back or compensated?
10. What may be published publicly?
11. What must remain private or protected?
12. What has been archived for future review?

## Relationship to the AEP stack

A Proof Room orchestrates:

- **AEP-001:** Commit → Execute → Prove → Evolve.
- **AEP-002:** Evidence Dockets.
- **AEP-003:** ProofPackets.
- **AEP-004:** Selection Gates.
- **AEP-005:** Tool Permissions.
- **AEP-006:** Rollback Receipts.
- **AEP-007:** Public-Safe Proof Reports.

AEP-008 is not a replacement for the prior standards. It is the operating container that makes them usable together.

## Proof Room operating modes

### sandbox

Low-risk learning, demonstration, internal experimentation, and educational use.

### team

Shared team workflow improvement, AI efficiency sprints, reusable work systems, and team-level proof.

### institutional

Enterprise, regulated, audit-ready, or internal governance use.

### public_safe

Preparation and approval of external proof reports.

### incident

Recovery, rollback, quarantine, compensation, and post-incident review.

### sovereign

Public-sector, national, regulated, jurisdictional, or protected institutional use.

## Proof Room roles

### room_owner

Accountable for room charter, scope, resources, and closure.

### operator

Runs approved machine work inside room boundaries.

### reviewer

Reviews evidence, evals, risks, dockets, packets, and reports.

### approver

Authorizes decisions, publication, escalation, and sensitive operations.

### gatekeeper

Operates or oversees Selection Gate decisions.

### tool_steward

Maintains tool manifests, permissions, leases, approvals, and receipts.

### rollback_owner

Maintains rollback plan, recovery proof, and compensation pathway.

### redactor

Reviews public-safe reports and ensures private/protected evidence is not leaked.

### auditor

Reviews room integrity, conformance, completeness, and chain of custody.

### incident_lead

Controls incident-mode rooms and recovery execution.

### observer

May view selected room outputs but cannot execute, approve, or publish.

## Separation of duties

A Proof Room should separate execution, approval, publication, and audit.

High-risk rooms must not allow the same actor to:

- execute the candidate work
- approve its promotion
- publish the public report
- audit their own decision

If separation is impossible, the room must explicitly record the exception and justification.

## Required objects

AEP-008 defines these canonical room objects:

1. Proof Room Manifest
2. Proof Room Charter
3. Scope Boundary
4. Role Assignment Registry
5. Evidence Boundary
6. Work Item Registry
7. Room Session Record
8. Artifact Registry
9. Tool Permission Register
10. Evidence Docket Register
11. ProofPacket Register
12. Selection Gate Register
13. Rollback Register
14. Public Report Register
15. Decision Log
16. Room Audit Export
17. Room Closure Report

## Proof Room Manifest

Required fields:

- room_id
- schema
- schema_version
- room_name
- room_mode
- owner
- organization
- jurisdiction
- purpose
- opened_at
- status
- confidentiality_class
- evidence_boundary_ref
- charter_ref
- hash

## Proof Room Charter

Required fields:

- charter_id
- room_id
- mission
- success_criteria
- failure_criteria
- in_scope
- out_of_scope
- allowed_agents
- allowed_tools
- allowed_data_classes
- allowed_environments
- required_evals
- required_gate_policy
- rollback_required
- publication_allowed
- closure_conditions

## Scope Boundary

Required fields:

- boundary_id
- room_id
- tenant_scope
- user_scope
- workflow_scope
- agent_scope
- tool_scope
- data_scope
- environment_scope
- jurisdiction_scope
- time_scope
- budget_scope
- publication_scope

## Role Assignment Registry

Required fields:

- registry_id
- room_id
- assignments
- separation_of_duties_required
- exceptions
- issued_at

Each assignment should include:

- actor_id
- actor_type
- role
- permissions
- restrictions
- start_time
- end_time

## Evidence Boundary

Required fields:

- evidence_boundary_id
- room_id
- public_evidence_allowed
- private_evidence_allowed
- protected_evidence_allowed
- forbidden_evidence
- redaction_required
- publication_rules
- retention_policy
- access_rules

## Work Item Registry

Required fields:

- registry_id
- room_id
- work_items
- intake_status
- owner
- created_at

Each work item should include:

- work_item_id
- title
- candidate_type
- candidate_ref
- commitment_ref
- run_refs
- status
- evidence_docket_refs
- selection_certificate_refs
- rollback_refs
- public_report_refs

## Room Session Record

Required fields:

- session_id
- room_id
- session_type
- started_at
- ended_at
- participants
- agenda
- decisions
- evidence_refs
- action_items
- proof_packet_refs

## Registers

A Proof Room should maintain these registers:

- artifact_registry
- tool_permission_register
- evidence_docket_register
- proof_packet_register
- selection_gate_register
- rollback_register
- public_report_register

Registers must be append-only or preserve revision history.

## Decision Log

Required fields:

- decision_log_id
- room_id
- decisions
- hash

Each decision should include:

- decision_id
- decision_type
- decision_summary
- evidence_refs
- approver
- issued_at
- claim_boundary
- supersedes
- status

## Room Audit Export

Required fields:

- audit_export_id
- room_id
- manifest_ref
- charter_ref
- evidence_boundary_ref
- role_registry_ref
- work_item_refs
- docket_refs
- packet_refs
- selection_refs
- permission_refs
- rollback_refs
- public_report_refs
- decision_log_ref
- generated_at
- hash

## Room Closure Report

Required fields:

- closure_id
- room_id
- closure_status
- what_was_done
- what_was_proved
- what_was_promoted
- what_was_rejected
- what_was_rolled_back
- what_was_published
- what_remains_private
- unresolved_items
- archive_location
- closed_by
- closed_at
- hash

## Proof Room lifecycle

1. Charter
2. Scope
3. Assign roles
4. Open room
5. Intake work
6. Run bounded work
7. Collect packets
8. Assemble dockets
9. Review evidence
10. Decide through gate
11. Permit tools
12. Roll back or compensate if needed
13. Publish public-safe report if allowed
14. Export audit package
15. Close and archive
16. Feed learnings back into artifacts

## Proof Room invariants

1. No Proof Room without a charter.
2. No room without scope boundary.
3. No room without role assignments.
4. No high-risk room without separation of duties.
5. No evidence without classification.
6. No run without commitment reference.
7. No side-effecting tool call without permission.
8. No promotion without Selection Gate reference.
9. No release without rollback reference.
10. No public report without redaction review.
11. No closure without audit export or archive reference.
12. No public proof may leak private or protected evidence.
13. Under uncertainty, the room must reduce scope or escalate review.

## Conformance levels

### Level 0 — Informal Proof Room

A narrative workspace with mission, participants, evidence links, and decisions.

### Level 1 — Basic Proof Room

Includes manifest, charter, scope, role registry, evidence boundary, and work item registry.

### Level 2 — Operational Proof Room

Adds Evidence Docket register, ProofPacket register, tool permission register, and decision log.

### Level 3 — Institutional Proof Room

Adds Selection Gate register, rollback register, public report register, separation of duties, audit export, and closure report.

### Level 4 — Regulated Proof Room

Adds protected evidence boundary, retention policy, jurisdiction, authorized approvers, independent review, and compliance-oriented audit export.

### Level 5 — Sovereign Proof Room

Adds sovereign jurisdiction boundary, public/private/protected evidence controls, authorized public-institution roles, policy traceability, public-safe reporting controls, and sovereign archive requirements.

## Security and privacy requirements

A Proof Room must not leak:

- secrets
- credentials
- private prompts
- protected traces
- private tool logs
- regulated personal data
- privileged legal analysis
- sensitive security findings
- protected institutional data
- sovereign or restricted operational details

Public proof should expose accountability, not private intelligence.

## Claim boundary

AEP-008 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-008 defines an operating standard for Proof Rooms.

## Canonical public line

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.  
AEP-006 defines recovery proof.  
AEP-007 defines public proof.  
AEP-008 defines the room.

GoalOS turns machine work into governed, reviewable, recoverable, and public-safe institutional proof.

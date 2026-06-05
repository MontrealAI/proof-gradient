# AEP-007 — Public-Safe Proof Report Standard

**Version:** v1.2 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standards:** AEP-001 — GoalOS Proof-of-Evolution Constitution; AEP-002 — Evidence Docket Standard; AEP-003 — ProofPacket Schema; AEP-004 — Selection Gate Standard; AEP-005 — Tool Permission Standard; AEP-006 — Rollback Receipt Standard  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Author / Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-007 defines the **Public-Safe Proof Report Standard**: the reporting layer that converts private or protected machine-work evidence into a public-safe proof report that can be shared without leaking secrets, credentials, private prompts, full execution traces, raw customer data, regulated personal information, security vulnerabilities, private tool logs, protected operational details, privileged legal analysis, restricted datasets, or confidential model/infrastructure/evaluation details.

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.  
AEP-006 defines the recovery proof.  
AEP-007 defines the public proof.

GoalOS proves publicly without leaking privately.

## Canonical thesis

A model can answer.  
An agent can act.  
An institution must prove.  
A network must select.  
A tool must be permitted.  
A release must recover.  
A public proof must be safe.

## Canonical law

No public claim without claim boundary.  
No public proof without redaction review.  
No private trace in public report.  
No protected data in public proof.  
No publication without approval.  
No correction without history.  
No proof, no evolution.

## v1.2 upgrades

AEP-007 v1.2 adds:

- disclosure review objects
- challenge records
- retraction notices
- report bundles
- report expiry and review windows
- embargo / responsible disclosure controls
- public claim levels
- report accessibility profile
- machine-readable public-safe report bundle
- leakage audit tooling
- correction and retraction playbooks
- website publishing profile
- proof-card profile for public websites

## Purpose

The purpose of AEP-007 is to let institutions share evidence of machine work without exposing the private material used to produce that evidence.

A public-safe report should answer:

1. What was tested or operated?
2. What happened?
3. What evidence exists?
4. What passed?
5. What failed?
6. What was changed?
7. What was rolled back or recovered?
8. What is publicly claimed?
9. What is explicitly not claimed?
10. What evidence is private or protected?
11. Who approved publication?
12. How are corrections or retractions handled?

## Disclosure classes

AEP-007 defines five disclosure classes.

### public

Safe to publish.

Examples: public claim, evidence summary, public artifact link, public-safe eval status, public-safe rollback status.

### private

Internal only.

Examples: prompts, tool logs, internal traces, evaluator notes, internal cost details, private docket appendices.

### protected

Restricted to authorized roles.

Examples: credentials, regulated data, sensitive personal data, security vulnerabilities, protected operational details, privileged analysis.

### forbidden

Never publish.

Examples: raw secrets, passwords, API keys, private keys, raw protected personal data, exploit details, non-redacted regulated records.

### embargoed

Not yet publishable.

Examples: responsible disclosure windows, partner review periods, release timing, legal or security review windows.

## Public claim levels

Public claims must be classified.

### verified

Directly supported by evidence and passed evaluations.

### supported

Supported by credible evidence but bounded by limitations.

### observed

A descriptive fact was observed; no broader conclusion is claimed.

### contextual

Background material, not a proof claim.

### not_claimed

Explicitly outside the report boundary.

## Required public-safe report sections

A conforming public-safe report must include:

1. Report Manifest
2. Source Evidence References
3. Public Claim Matrix
4. Evidence Summary
5. Evaluation Summary
6. Risk and Limitation Summary
7. Rollback / Recovery Summary
8. Redaction Ledger
9. Publication Approval
10. Correction and Retraction Policy
11. Public Artifact Links
12. Final Claim Boundary

## Report Manifest

Required fields:

- report_id
- schema
- schema_version
- title
- owner
- organization
- created_at
- updated_at
- status
- source_docket_refs
- public_url
- report_version
- disclosure_class
- hash

## Source Evidence References

Source references should identify private proof without exposing it.

Required fields:

- source_ref_id
- source_type
- source_id
- source_hash
- disclosure_class
- public_summary
- access_note

## Public Claim Matrix

Required fields:

- claim_id
- claim_text
- claim_level
- evidence_summary_refs
- eval_summary_refs
- limitation_refs
- public_allowed
- not_claimed

## Evidence Summary

Required fields:

- evidence_summary_id
- source_evidence_refs
- public_description
- what_it_supports
- what_it_does_not_support
- disclosure_class

## Evaluation Summary

Required fields:

- eval_summary_id
- eval_name
- public_result
- passed
- score_or_threshold
- limitations
- private_eval_ref

## Risk and Limitation Summary

Required fields:

- risk_summary_id
- risk_type
- severity_public
- mitigation_summary
- residual_risk_summary
- limitation
- disclosure_boundary

## Rollback / Recovery Summary

Required fields:

- recovery_summary_id
- rollback_status
- rollback_receipt_refs
- verification_summary
- compensation_summary
- not_claimed

## Redaction Ledger

Required fields:

- redaction_id
- source_ref
- redaction_type
- reason
- before_disclosure_class
- after_disclosure_class
- reviewer
- reviewed_at

## Publication Approval

Required fields:

- approval_id
- report_id
- approver
- approver_role
- approval_status
- approval_reason
- approved_scope
- issued_at
- expires_at
- proof_packet_ref

## Correction and Retraction Policy

Required fields:

- correction_policy_id
- report_id
- correction_window
- challenge_window
- correction_contact
- retraction_conditions
- correction_history_required

## Correction Notice

Required fields:

- correction_id
- report_id
- corrected_report_version
- correction_reason
- corrected_claims
- previous_text_summary
- corrected_text_summary
- issued_at
- public_url

## Retraction Notice

Required fields:

- retraction_id
- report_id
- retraction_reason
- affected_claims
- evidence_issue_summary
- replacement_report_ref
- issued_at
- public_url

## Challenge Record

Required fields:

- challenge_id
- report_id
- challenger
- challenge_type
- challenged_claims
- challenge_summary
- status
- response_summary
- created_at
- resolved_at

## Public Artifact Links

Required fields:

- artifact_link_id
- label
- url
- artifact_type
- hash
- disclosure_class
- access_note

## Final Claim Boundary

Required fields:

- supported_claims
- not_claimed
- limitations
- private_boundary
- protected_boundary
- correction_policy_ref

## Public-safe report lifecycle

1. Draft
2. Source evidence mapped
3. Claims classified
4. Redaction review completed
5. Publication approval issued
6. Report published
7. Challenge window open
8. Correction issued, if needed
9. Retraction issued, if needed
10. Archived with history

## Zero-leak invariants

1. No raw private prompts in public report.
2. No raw private traces in public report.
3. No secrets, keys, credentials, or tokens in public report.
4. No regulated personal data in public report unless lawfully public and explicitly approved.
5. No exploit details or security vulnerabilities without responsible disclosure review.
6. No private tool logs in public report.
7. No protected evidence in public report.
8. No unsupported claim in public report.
9. No publication without approval.
10. No correction without history.
11. No retraction without public notice when published claims are invalidated.
12. Under uncertainty, redact or withhold.

## Conformance levels

### Level 0 — Informal public proof

A public statement with a claim boundary and no private leakage.

### Level 1 — Basic public-safe report

Includes manifest, public claim matrix, evidence summary, limitations, and claim boundary.

### Level 2 — Reviewed public-safe report

Includes redaction ledger and publication approval.

### Level 3 — Operational public-safe report

Includes source docket refs, ProofPacket refs, evaluation summary, rollback summary, correction policy, and public artifact links.

### Level 4 — Institutional public-safe report

Includes disclosure review, redaction audit, challenge window, correction/retraction history, report hash, and audit export.

### Level 5 — Sovereign / regulated public-safe report

Includes jurisdiction, retention policy, protected-boundary review, responsible disclosure controls, authorized publication approvers, challenge/retraction governance, accessibility profile, and public-safe machine-readable bundle.

## Security and privacy requirements

AEP-007 public-safe reports must not publish private or protected evidence by default.

Public proof should prove accountability without leaking private intelligence.

## Claim boundary

AEP-007 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-007 defines a public-safe proof reporting standard.

## Canonical public line

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.  
AEP-004 defines the gate.  
AEP-005 defines the permission.  
AEP-006 defines the recovery proof.  
AEP-007 defines the public proof.

GoalOS proves publicly without leaking privately.

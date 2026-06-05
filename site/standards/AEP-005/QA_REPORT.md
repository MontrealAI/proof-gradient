# AEP-005 v1.1 QA Report

Generated: 2026-06-05

## Document QA

- Standard DOCX render return code: 0
- Standard rendered pages: 8
- One-page DOCX render return code: 0
- One-page rendered pages: 1
- PDF generated from DOCX.
- Contact sheets generated for visual QA.
- One-page brief renders as exactly one page.

## Tool Permission Decision validation

### sample_tool_permission_decision_allow_with_lease.json
- status: valid

### sample_tool_permission_decision_approval_required.json
- status: valid

### sample_tool_permission_decision_deny.json
- status: valid

## Permission Lease validation
- status: valid

## Tool Gateway audit
- status: passed

## Conformance scoring sample
- sample decision: sample_tool_permission_decision_allow_with_lease.json
- sample lease: sample_permission_lease.json
- sample receipt: sample_tool_call_receipt.json
- sample revocation: sample_revocation_receipt.json
- score: 10/10
- conformance_level: 5

## Package QA

- Tool Manifest schema included.
- Tool Permission Policy schema included.
- Tool Request schema included.
- Tool Permission Decision schema included.
- Permission Lease schema included.
- Approval Receipt schema included.
- Tool Call Receipt schema included.
- Revocation Receipt schema included.
- Compensation Receipt schema included.
- Break-Glass Request schema included.
- Data Boundary Rule schema included.
- Rate-Limit Policy schema included.
- Tool Gateway reference authorization and audit tools included.
- Website, conformance CI, and official release workflows included.

## Claim boundary

AEP-005 does not claim achieved AGI, achieved ASI, perfect safety, legal compliance certification, financial or legal advice, guaranteed ROI, production readiness, government endorsement, or national-security readiness. It defines a tool permission and proof standard.

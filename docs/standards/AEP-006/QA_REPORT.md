# AEP-006 v1.1 QA Report

Generated: 2026-06-05

## Document QA

- Standard DOCX render return code: 0
- Standard rendered pages: 6
- One-page DOCX render return code: 0
- One-page rendered pages: 1
- PDF generated from DOCX.
- Contact sheets generated for visual QA.

## Rollback Receipt validation

### sample_rollback_receipt_failed_compensation_required.json
- status: valid

### sample_rollback_receipt_partial.json
- status: valid

### sample_rollback_receipt_success.json
- status: valid

## Rollback audit
- status: passed

## Conformance scoring sample
- sample receipt: sample_rollback_receipt_success.json
- sample verification: sample_rollback_verification.json
- sample review: sample_post_rollback_review.json
- score: 10/10
- conformance_level: 5

## Package QA

- Rollback Trigger schema included.
- Rollback Plan schema included.
- Rollback Request schema included.
- Rollback Authorization schema included.
- Rollback Receipt schema included.
- Rollback Verification schema included.
- Compensation Receipt schema included.
- Post-Rollback Review schema included.
- Recovery Bundle schema included.
- Validators, hash, audit, decision, and conformance tools included.
- Website, conformance CI, and official release workflows included.

## Claim boundary

AEP-006 does not claim achieved AGI, achieved ASI, perfect safety, legal compliance certification, financial or legal advice, guaranteed ROI, production readiness, government endorsement, or national-security readiness. It defines a recovery proof standard.

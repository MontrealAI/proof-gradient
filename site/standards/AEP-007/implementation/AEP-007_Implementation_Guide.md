# AEP-007 Implementation Guide

## Minimum implementation

1. Start from an AEP-002 Evidence Docket.
2. Identify source ProofPackets.
3. Draft public claims.
4. Classify each claim: verified, supported, observed, contextual, or not_claimed.
5. Produce Evidence Summaries without exposing private evidence.
6. Run redaction review.
7. Produce Redaction Ledger.
8. Add Publication Approval.
9. Add Correction and Retraction Policy.
10. Publish public-safe report and machine-readable JSON.

## Recommended commands

```bash
python tools/validate_public_safe_report.py examples/sample_public_safe_report.json
python tools/public_safe_redaction_audit.py examples/sample_public_safe_report.json
python tools/public_safe_conformance_score.py examples/sample_public_safe_report.json
python tools/build_report_bundle.py bundle.json examples/sample_public_safe_report.json
```

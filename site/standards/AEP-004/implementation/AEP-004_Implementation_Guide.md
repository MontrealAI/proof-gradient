# AEP-004 Implementation Guide

## Minimum implementation

1. Create a Selection Candidate.
2. Attach Evidence Docket refs.
3. Attach ProofPacket refs.
4. Confirm required evals.
5. Confirm policy and approval records.
6. Confirm risk and cost status.
7. Confirm challenge window.
8. Confirm canary scope where needed.
9. Confirm rollback target.
10. Issue Selection Certificate.
11. Monitor and review.

## Developer commands

```bash
python tools/validate_selection_certificate.py examples/sample_selection_certificate_approve_canary.json
python tools/selection_certificate_hash.py examples/sample_selection_certificate_approve_canary.json
python tools/selection_gate_conformance_score.py examples/sample_selection_certificate_approve_canary.json
python tools/selection_gate_decide.py examples/sample_gate_decision_input_promote.json
python tools/selection_gate_audit.py examples/sample_selection_certificate_approve_canary.json
```

## Fail-closed principle

If evidence, evals, approvals, monitoring, or rollback are missing, reduce scope, request more evidence, reject, or roll back.

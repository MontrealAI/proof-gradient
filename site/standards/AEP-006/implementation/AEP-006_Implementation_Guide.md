# AEP-006 Implementation Guide

## Minimum implementation

1. Create rollback plans before high-impact release.
2. Record rollback triggers.
3. Submit rollback requests.
4. Record authorization.
5. Execute rollback steps.
6. Emit Rollback Receipts.
7. Verify recovery.
8. Record compensation if rollback fails or is impossible.
9. Complete post-rollback review.
10. Attach receipts to ProofPackets and Evidence Dockets.

## Developer commands

```bash
python tools/validate_rollback_receipt.py examples/sample_rollback_receipt_success.json
python tools/rollback_receipt_hash.py examples/sample_rollback_receipt_success.json
python tools/rollback_audit.py examples/sample_rollback_plan.json examples/sample_rollback_receipt_success.json examples/sample_rollback_verification.json
python tools/rollback_conformance_score.py examples/sample_rollback_receipt_success.json examples/sample_rollback_verification.json examples/sample_post_rollback_review.json
```

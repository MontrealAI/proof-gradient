# AEP-008 Implementation Guide

## Minimum implementation

1. Create a Proof Room Manifest.
2. Create a Proof Room Charter.
3. Define scope boundaries.
4. Assign roles.
5. Define evidence boundaries.
6. Intake work items.
7. Register Evidence Dockets and ProofPackets.
8. Register Tool Permission decisions.
9. Register Selection Gate decisions.
10. Register Rollback Receipts.
11. Register Public-Safe Proof Reports.
12. Export audit package.
13. Close and archive the room.

## Developer commands

```bash
python tools/validate_proof_room_manifest.py examples/sample_proof_room_manifest.json
python tools/proof_room_audit.py examples/sample_proof_room_manifest.json examples/sample_proof_room_charter.json examples/sample_evidence_boundary.json examples/sample_role_assignment_registry.json examples/sample_work_item_registry.json examples/sample_decision_log.json examples/sample_room_audit_export.json examples/sample_room_closure_report.json
python tools/proof_room_conformance_score.py examples/sample_proof_room_manifest.json examples/sample_proof_room_charter.json examples/sample_evidence_boundary.json examples/sample_role_assignment_registry.json examples/sample_work_item_registry.json examples/sample_decision_log.json examples/sample_room_audit_export.json examples/sample_room_closure_report.json
```

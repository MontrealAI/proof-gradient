# AEP-005 Implementation Guide

## Minimum implementation

1. Create a Tool Manifest for each tool.
2. Create a Tool Permission Policy.
3. Require Tool Requests before tool calls.
4. Route Tool Requests through a Tool Gateway.
5. Emit Tool Permission Decisions.
6. Require approval for high-risk classes.
7. Issue Permission Leases for allowed use.
8. Emit Tool Call Receipts after execution.
9. Add Revocation Receipts for stopped authority.
10. Add Compensation Receipts when rollback is impossible or insufficient.
11. Attach decisions, leases, receipts, revocations, and compensation to ProofPackets.
12. Attach ProofPackets to Evidence Dockets.
13. Make high-risk tool use visible to Selection Gates.

## Developer commands

```bash
python tools/authorize_tool_request.py examples/sample_tool_manifest.json examples/sample_tool_permission_policy.json examples/sample_tool_request_read.json
python tools/validate_tool_permission.py examples/sample_tool_permission_decision_allow_with_lease.json
python tools/validate_permission_lease.py examples/sample_permission_lease.json
python tools/tool_gateway_audit.py examples/sample_tool_manifest.json examples/sample_tool_permission_policy.json examples/sample_tool_request_read.json examples/sample_tool_permission_decision_allow_with_lease.json examples/sample_permission_lease.json examples/sample_tool_call_receipt.json
python tools/tool_permission_conformance_score.py examples/sample_tool_permission_decision_allow_with_lease.json examples/sample_permission_lease.json examples/sample_tool_call_receipt.json examples/sample_revocation_receipt.json
```

import json
import re
import sys
from pathlib import Path
from tool_permission_hash import canonical_hash

def validate_decision(decision):
    errors = []
    required = ["decision_id","schema","schema_version","request_id","tool_id","decision","decision_reason","allowed_scope","denied_scope","approval_required","policy_refs","risk_refs","issued_at","hash"]
    for key in required:
        if key not in decision:
            errors.append(f"missing required field: {key}")
    if decision.get("schema") != "AEP-005-TOOL-PERMISSION-DECISION":
        errors.append("schema must be AEP-005-TOOL-PERMISSION-DECISION")
    if decision.get("decision", "").startswith("allow") and not decision.get("allowed_scope"):
        errors.append("allow decision requires allowed_scope")
    if decision.get("decision") in {"allow_with_lease", "allow_with_rate_limit"} and not decision.get("lease_ref"):
        errors.append(f"{decision.get('decision')} requires lease_ref")
    if decision.get("decision") == "approval_required" and not decision.get("approver_role"):
        errors.append("approval_required decision requires approver_role")
    h = decision.get("hash", "")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", h):
        errors.append("hash must match sha256:<64 hex chars>")
    elif h != canonical_hash(decision):
        errors.append(f"hash mismatch: expected {canonical_hash(decision)}")
    return errors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_tool_permission.py decision.json")
        raise SystemExit(2)
    decision = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = validate_decision(decision)
    if errors:
        print("AEP-005 Tool Permission Decision invalid:")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(1)
    print("AEP-005 Tool Permission Decision valid.")

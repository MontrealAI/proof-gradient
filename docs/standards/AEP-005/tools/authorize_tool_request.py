import json
import sys
from pathlib import Path

HIGH_RISK = {"write","send","delete","deploy","payment","secret_access","admin_change","protected_operation","external_contact","break_glass"}

def authorize(manifest, policy, request):
    cls = request["requested_permission_class"]
    if manifest.get("status") != "active":
        return "deny", "tool is not active"
    if cls not in manifest.get("permission_classes_supported", []):
        return "deny", "tool does not support requested permission class"
    if cls in policy.get("denied_permission_classes", []):
        return "deny", "permission class denied by policy"
    if request.get("target_environment") not in policy.get("allowed_environments", []):
        return "deny", "target environment not allowed"
    if cls in policy.get("approval_required_for", []) or cls in manifest.get("approval_required_for", []):
        return "approval_required", "approval required by policy or manifest"
    if cls not in policy.get("allowed_permission_classes", []):
        return "deny", "permission class not explicitly allowed"
    if request.get("external_effect") and cls not in {"send","external_contact","payment","deploy","break_glass"}:
        return "deny", "external effect requested with non-external permission"
    if cls in HIGH_RISK and not request.get("rollback_plan_ref") and not request.get("compensation_plan_ref"):
        return "deny", "high-risk tool request requires rollback or compensation plan"
    return "allow_with_lease", "allowed by scoped policy; lease required"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: python authorize_tool_request.py manifest.json policy.json request.json")
        raise SystemExit(2)
    m = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    p = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    r = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
    decision, reason = authorize(m, p, r)
    print(json.dumps({"decision": decision, "reason": reason}, indent=2))

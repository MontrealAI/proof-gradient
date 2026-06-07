import json
import sys
from pathlib import Path

def audit(manifest, policy, request, decision, lease=None, receipt=None):
    issues = []
    if manifest.get("status") != "active":
        issues.append("manifest not active")
    cls = request.get("requested_permission_class")
    if cls not in manifest.get("permission_classes_supported", []):
        issues.append("requested class unsupported by manifest")
    if cls in policy.get("denied_permission_classes", []):
        issues.append("requested class denied by policy")
    if decision.get("decision", "").startswith("allow") and not decision.get("allowed_scope"):
        issues.append("allow decision missing allowed_scope")
    if decision.get("decision") in {"allow_with_lease","allow_with_rate_limit"} and not lease:
        issues.append("leased decision missing lease object")
    if decision.get("decision", "").startswith("allow") and receipt is None:
        issues.append("allowed tool call missing receipt")
    if policy.get("fail_closed") is not True:
        issues.append("policy must fail closed")
    return issues

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("usage: python tool_gateway_audit.py manifest.json policy.json request.json decision.json [lease.json] [receipt.json]")
        raise SystemExit(2)
    loaded = [json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[1:]]
    issues = audit(*loaded)
    if issues:
        print("Tool Gateway audit failed:")
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)
    print("Tool Gateway audit passed.")

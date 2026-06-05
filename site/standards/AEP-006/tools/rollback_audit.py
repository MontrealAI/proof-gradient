import json, sys
from pathlib import Path

def audit(plan, receipt, verification=None):
    issues=[]
    if not plan.get("rollback_target"): issues.append("missing rollback target")
    if not plan.get("rollback_steps"): issues.append("missing rollback steps")
    if receipt.get("rollback_target") != plan.get("rollback_target"): issues.append("receipt target does not match plan")
    if receipt.get("status") in {"completed","verified"} and not verification: issues.append("completed rollback missing verification object")
    if verification and verification.get("restored_baseline_confirmed") is not True: issues.append("baseline not confirmed")
    if not receipt.get("claim_boundary"): issues.append("missing claim boundary")
    return issues
if __name__ == "__main__":
    if len(sys.argv) not in {3,4}:
        print("usage: python rollback_audit.py plan.json receipt.json [verification.json]")
        raise SystemExit(2)
    plan=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    receipt=json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    verification=json.loads(Path(sys.argv[3]).read_text(encoding="utf-8")) if len(sys.argv)==4 else None
    issues=audit(plan, receipt, verification)
    if issues:
        print("Rollback audit failed:")
        for i in issues: print(f"- {i}")
        raise SystemExit(1)
    print("Rollback audit passed.")

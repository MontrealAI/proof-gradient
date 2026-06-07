import json
import sys
from pathlib import Path

def decide(input_obj):
    eval_status = input_obj.get("eval_status", "unknown")
    evidence = input_obj.get("evidence_level", "weak")
    risk = input_obj.get("risk", "high")
    rollback_ready = bool(input_obj.get("rollback_ready", False))
    approval_ready = bool(input_obj.get("approval_ready", False))
    challenge_clear = input_obj.get("challenge_status", "cleared") in {"cleared", "not_required", "waived", "emergency_override"}

    if eval_status == "failed":
        return "reject"
    if not rollback_ready:
        return "reject"
    if not challenge_clear:
        return "needs_more_evidence"
    if risk in {"high", "protected", "restricted"} and not approval_ready:
        return "reject"
    if evidence == "strong" and eval_status == "passed" and risk == "low":
        return "promote"
    if evidence in {"strong", "partial"} and eval_status == "passed" and risk in {"low", "medium"}:
        return "approve_canary"
    if evidence == "weak":
        return "needs_more_evidence"
    return "revise"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python selection_gate_decide.py input.json")
        raise SystemExit(2)
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(decide(data))

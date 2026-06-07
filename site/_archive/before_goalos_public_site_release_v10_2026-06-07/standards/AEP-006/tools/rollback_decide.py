import json, sys
from pathlib import Path

def decide(signal):
    t=signal.get("trigger_type")
    severity=signal.get("severity","high")
    restore=bool(signal.get("restore_point_available", True))
    if not restore:
        return "compensate"
    if t in {"privacy_incident","security_incident"} or severity in {"high","protected","restricted"}:
        return "quarantine"
    if t in {"eval_failure","policy_violation","canary_stop_condition","unauthorized_tool_use"}:
        return "restore_baseline"
    if t in {"quality_regression","latency_regression","cost_overrun"}:
        return "stop_canary"
    return "manual_review"
if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("usage: python rollback_decide.py trigger.json")
        raise SystemExit(2)
    print(decide(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))

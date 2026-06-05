import json
import sys
from pathlib import Path

def score(decision, lease=None, receipt=None, revocation=None):
    points = 0
    max_points = 10
    if decision.get("schema") == "AEP-005-TOOL-PERMISSION-DECISION": points += 1
    if decision.get("policy_refs"): points += 1
    if decision.get("risk_refs"): points += 1
    if decision.get("hash","").startswith("sha256:"): points += 1
    if decision.get("allowed_scope") or decision.get("denied_scope"): points += 1
    if decision.get("proof_packet_ref"): points += 1
    if lease and lease.get("schema") == "AEP-005-PERMISSION-LEASE": points += 1
    if receipt and receipt.get("schema") == "AEP-005-TOOL-CALL-RECEIPT": points += 1
    if receipt and receipt.get("evidence_refs"): points += 1
    if revocation and revocation.get("schema") == "AEP-005-REVOCATION-RECEIPT": points += 1
    level = 5 if points >= 9 else 4 if points >= 7 else 3 if points >= 5 else 2 if points >= 3 else 1 if points >= 2 else 0
    return points, max_points, level

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python tool_permission_conformance_score.py decision.json [lease.json] [receipt.json] [revocation.json]")
        raise SystemExit(2)
    objs = [json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[1:]]
    points, max_points, level = score(*objs)
    print(f"score={points}/{max_points}")
    print(f"conformance_level={level}")

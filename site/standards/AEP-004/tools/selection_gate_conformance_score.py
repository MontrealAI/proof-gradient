import json
import sys
from pathlib import Path

def score(cert):
    points = 0
    max_points = 10
    if cert.get("schema") == "AEP-004-SELECTION-CERTIFICATE": points += 1
    if cert.get("evidence_docket_refs"): points += 1
    if cert.get("proof_packet_refs"): points += 1
    if cert.get("eval_refs"): points += 1
    if cert.get("risk_refs"): points += 1
    if cert.get("rollback_plan", {}).get("rollback_target"): points += 1
    if cert.get("canary_plan") and cert.get("monitoring_plan"): points += 1
    if cert.get("challenge_record"): points += 1
    if cert.get("expires_at") and cert.get("review_after"): points += 1
    if cert.get("hash", "").startswith("sha256:"): points += 1
    level = 5 if points >= 9 else 4 if points >= 7 else 3 if points >= 5 else 2 if points >= 3 else 1 if points >= 2 else 0
    return points, max_points, level

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python selection_gate_conformance_score.py certificate.json")
        raise SystemExit(2)
    cert = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    points, max_points, level = score(cert)
    print(f"score={points}/{max_points}")
    print(f"conformance_level={level}")

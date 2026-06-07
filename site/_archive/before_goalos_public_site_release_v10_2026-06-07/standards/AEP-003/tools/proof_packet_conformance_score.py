import json
import sys
from pathlib import Path

def score(packet):
    points = 0
    max_points = 8
    if packet.get("schema") == "AEP-003": points += 1
    if packet.get("hash", "").startswith("sha256:"): points += 1
    if packet.get("docket_id") and packet.get("commitment_id") and packet.get("run_id"): points += 1
    if packet.get("boundary", {}).get("access_class"): points += 1
    if packet.get("eval_refs") or packet.get("packet_type") == "eval_result": points += 1
    if packet.get("claim_boundary", {}).get("does_not_support"): points += 1
    if packet.get("attestations") or packet.get("signature"): points += 1
    if packet.get("boundary", {}).get("jurisdiction") and packet.get("boundary", {}).get("retention_policy"): points += 1

    if points <= 1: level = 0
    elif points == 2: level = 1
    elif points == 3: level = 2
    elif points == 4: level = 3
    elif points in (5,6): level = 4
    else: level = 5
    return points, max_points, level

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python proof_packet_conformance_score.py packet.json")
        raise SystemExit(2)
    packet = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    points, max_points, level = score(packet)
    print(f"score={points}/{max_points}")
    print(f"conformance_level={level}")

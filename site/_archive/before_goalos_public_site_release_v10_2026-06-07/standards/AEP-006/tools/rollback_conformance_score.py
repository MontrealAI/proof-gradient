import json, sys
from pathlib import Path

def score(receipt, verification=None, review=None):
    points=0; max_points=10
    if receipt.get("schema")=="AEP-006-ROLLBACK-RECEIPT": points+=1
    if receipt.get("evidence_refs"): points+=1
    if receipt.get("proof_packet_refs"): points+=1
    if receipt.get("selection_certificate_refs"): points+=1
    if receipt.get("tool_receipt_refs"): points+=1
    if receipt.get("verification_ref") or verification: points+=1
    if receipt.get("claim_boundary"): points+=1
    if receipt.get("hash","").startswith("sha256:"): points+=1
    if verification and verification.get("restored_baseline_confirmed") is True: points+=1
    if review and review.get("schema")=="AEP-006-POST-ROLLBACK-REVIEW": points+=1
    level=5 if points>=9 else 4 if points>=7 else 3 if points>=5 else 2 if points>=3 else 1 if points>=2 else 0
    return points,max_points,level
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("usage: python rollback_conformance_score.py receipt.json [verification.json] [review.json]")
        raise SystemExit(2)
    objs=[json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[1:]]
    points,max_points,level=score(*objs)
    print(f"score={points}/{max_points}")
    print(f"conformance_level={level}")

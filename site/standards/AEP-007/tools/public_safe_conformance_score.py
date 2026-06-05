import json, sys
from pathlib import Path

def score(report):
    points=0; max_points=10
    if report.get("schema") == "AEP-007-PUBLIC-SAFE-REPORT": points += 1
    if report.get("source_docket_refs"): points += 1
    if report.get("source_proof_packet_refs"): points += 1
    if report.get("public_claim_matrix"): points += 1
    if report.get("evidence_summaries"): points += 1
    if report.get("evaluation_summaries"): points += 1
    if report.get("redaction_ledger"): points += 1
    if report.get("publication_approval", {}).get("approval_status") == "approved": points += 1
    if report.get("correction_policy", {}).get("correction_history_required") is True: points += 1
    if report.get("hash", "").startswith("sha256:"): points += 1
    level = 5 if points >= 9 else 4 if points >= 7 else 3 if points >= 5 else 2 if points >= 3 else 1 if points >= 2 else 0
    return points, max_points, level

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python public_safe_conformance_score.py report.json")
        raise SystemExit(2)
    report=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    points,max_points,level=score(report)
    print(f"score={points}/{max_points}")
    print(f"conformance_level={level}")

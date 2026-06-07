import json, sys
from pathlib import Path
from public_safe_report_hash import canonical_hash, ZERO_HASH

def main(out_path):
    report = {
        "report_id":"psr_generated_001", "schema":"AEP-007-PUBLIC-SAFE-REPORT", "schema_version":"1.2",
        "title":"Generated Public-Safe Proof Report", "owner":"", "organization":"", "created_at":"generated", "status":"draft",
        "source_docket_refs":[], "public_claim_matrix":[], "evidence_summaries":[], "redaction_ledger":[],
        "publication_approval":{"approval_status":"draft"},
        "claim_boundary":{"supported_claims":[],"not_claimed":[],"limitations":[],"private_boundary":"","protected_boundary":""},
        "hash": ZERO_HASH
    }
    report["hash"] = canonical_hash(report)
    Path(out_path).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(out_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python generate_public_safe_report.py out.json")
        raise SystemExit(2)
    main(sys.argv[1])

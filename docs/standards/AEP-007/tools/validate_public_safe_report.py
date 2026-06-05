import json, re, sys
from pathlib import Path
from public_safe_report_hash import canonical_hash
REQUIRED = ["report_id","schema","schema_version","title","owner","organization","created_at","status","source_docket_refs","public_claim_matrix","evidence_summaries","redaction_ledger","publication_approval","claim_boundary","hash"]
FORBIDDEN_TERMS = ["api_key", "password", "private key", "secret=", "BEGIN PRIVATE KEY", "customer ssn", "raw prompt:", "full trace:"]

def validate(report):
    errors=[]
    for key in REQUIRED:
        if key not in report:
            errors.append(f"missing required field: {key}")
    if report.get("schema") != "AEP-007-PUBLIC-SAFE-REPORT":
        errors.append("schema must be AEP-007-PUBLIC-SAFE-REPORT")
    if not report.get("public_claim_matrix"):
        errors.append("public_claim_matrix must not be empty")
    cb = report.get("claim_boundary", {})
    for key in ["supported_claims", "not_claimed", "limitations", "private_boundary", "protected_boundary"]:
        if key not in cb:
            errors.append(f"claim_boundary missing {key}")
    text = json.dumps(report).lower()
    for term in FORBIDDEN_TERMS:
        if term.lower() in text:
            errors.append(f"possible forbidden public leakage term: {term}")
    h=report.get("hash","")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", h):
        errors.append("hash must match sha256:<64 hex chars>")
    elif h != canonical_hash(report):
        errors.append(f"hash mismatch: expected {canonical_hash(report)}")
    return errors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_public_safe_report.py report.json")
        raise SystemExit(2)
    report=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors=validate(report)
    if errors:
        print("AEP-007 Public-Safe Proof Report invalid:")
        for e in errors: print(f"- {e}")
        raise SystemExit(1)
    print("AEP-007 Public-Safe Proof Report valid.")

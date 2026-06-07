import json
import re
import sys
from pathlib import Path
from selection_certificate_hash import canonical_hash

REQUIRED = [
    "certificate_id","schema","schema_version","decision","gate_mode","candidate_id",
    "candidate_type","candidate_ref","baseline_ref","evidence_docket_refs","proof_packet_refs",
    "eval_refs","risk_refs","policy_refs","decision_reason","approved_scope","canary_plan",
    "monitoring_plan","rollback_plan","challenge_record","claim_boundary","approver",
    "issued_at","expires_at","review_after","hash"
]
DECISIONS = {"promote","approve_canary","revise","reject","archive","rollback","needs_more_evidence"}
GATE_MODES = {"advisory","manual","automated_bounded","emergency"}

def validate(cert):
    errors = []
    for key in REQUIRED:
        if key not in cert:
            errors.append(f"missing required field: {key}")
    if cert.get("schema") != "AEP-004-SELECTION-CERTIFICATE":
        errors.append("schema must be AEP-004-SELECTION-CERTIFICATE")
    if cert.get("decision") not in DECISIONS:
        errors.append(f"invalid decision: {cert.get('decision')}")
    if cert.get("gate_mode") not in GATE_MODES:
        errors.append(f"invalid gate_mode: {cert.get('gate_mode')}")
    if cert.get("decision") in {"promote", "approve_canary"}:
        if not cert.get("evidence_docket_refs"):
            errors.append("promote/canary requires evidence_docket_refs")
        if not cert.get("eval_refs"):
            errors.append("promote/canary requires eval_refs")
        if not cert.get("rollback_plan", {}).get("rollback_target"):
            errors.append("promote/canary requires rollback target")
    if cert.get("decision") == "promote" and cert.get("gate_mode") == "automated_bounded":
        # Explicitly allowed only if scope text indicates boundedness.
        if "bounded" not in cert.get("approved_scope", "").lower() and "internal" not in cert.get("approved_scope", "").lower():
            errors.append("automated_bounded promote requires bounded approved_scope")
    h = cert.get("hash", "")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", h):
        errors.append("hash must match sha256:<64 hex chars>")
    else:
        expected = canonical_hash(cert)
        if h != expected:
            errors.append(f"hash mismatch: expected {expected}, found {h}")
    return errors

def main(path: str) -> int:
    cert = json.loads(Path(path).read_text(encoding="utf-8"))
    errors = validate(cert)
    if errors:
        print(f"AEP-004 Selection Certificate invalid: {path}")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"AEP-004 Selection Certificate valid: {path}")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_selection_certificate.py certificate.json")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

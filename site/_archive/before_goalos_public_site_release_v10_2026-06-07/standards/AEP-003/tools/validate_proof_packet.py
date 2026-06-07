import json
import re
import sys
from pathlib import Path
from proof_packet_hash import canonical_packet_hash

REQUIRED = [
    "packet_id", "schema", "schema_version", "packet_type", "created_at",
    "producer", "docket_id", "commitment_id", "run_id", "claim_refs",
    "evidence_refs", "boundary", "payload", "hash", "claim_boundary"
]
PACKET_TYPES = {
    "commit", "trace_event", "tool_call", "policy_decision", "approval",
    "eval_result", "evidence_ref", "risk_event", "cost_event",
    "selection_decision", "rollout_event", "rollback_event", "public_report"
}

def validate_packet(packet: dict) -> list[str]:
    errors = []
    for key in REQUIRED:
        if key not in packet:
            errors.append(f"missing required field: {key}")
    if packet.get("schema") != "AEP-003":
        errors.append("schema must be AEP-003")
    if packet.get("packet_type") not in PACKET_TYPES:
        errors.append(f"unknown packet_type: {packet.get('packet_type')}")
    if not isinstance(packet.get("claim_refs", []), list):
        errors.append("claim_refs must be a list")
    if not isinstance(packet.get("evidence_refs", []), list):
        errors.append("evidence_refs must be a list")
    boundary = packet.get("boundary", {})
    for key in ["access_class", "public_safe", "contains_sensitive_data", "publication_allowed"]:
        if key not in boundary:
            errors.append(f"boundary missing field: {key}")
    cb = packet.get("claim_boundary", {})
    for key in ["supports", "does_not_support", "limitations", "public_claim_allowed"]:
        if key not in cb:
            errors.append(f"claim_boundary missing field: {key}")
    h = packet.get("hash", "")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", h):
        errors.append("hash must match sha256:<64 hex chars>")
    else:
        expected = canonical_packet_hash(packet)
        if h != expected:
            errors.append(f"hash mismatch: expected {expected}, found {h}")
    if boundary.get("access_class") == "public" and boundary.get("contains_sensitive_data") is True:
        errors.append("public packet cannot contain sensitive data")
    if boundary.get("public_safe") is True and boundary.get("publication_allowed") is not True:
        errors.append("public_safe true should have publication_allowed true or an explicit correction")
    return errors

def validate(path: str) -> int:
    packet = json.loads(Path(path).read_text(encoding="utf-8"))
    errors = validate_packet(packet)
    if errors:
        print(f"AEP-003 ProofPacket invalid: {path}")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"AEP-003 ProofPacket valid: {path}")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_proof_packet.py packet.json")
        raise SystemExit(2)
    raise SystemExit(validate(sys.argv[1]))

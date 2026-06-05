import json
import re
import sys
from pathlib import Path
from tool_permission_hash import canonical_hash

REQUIRED = ["lease_id","schema","schema_version","decision_id","request_id","tool_id","permission_class","scope","issued_at","expires_at","revocable","revocation_conditions","remaining_uses","proof_packet_ref","hash"]

def main(path):
    lease = json.loads(Path(path).read_text(encoding="utf-8"))
    errors = []
    for key in REQUIRED:
        if key not in lease:
            errors.append(f"missing required field: {key}")
    if lease.get("schema") != "AEP-005-PERMISSION-LEASE":
        errors.append("schema must be AEP-005-PERMISSION-LEASE")
    if lease.get("remaining_uses", 0) < 0:
        errors.append("remaining_uses cannot be negative")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", lease.get("hash", "")):
        errors.append("hash format invalid")
    elif lease["hash"] != canonical_hash(lease):
        errors.append(f"hash mismatch: expected {canonical_hash(lease)}")
    if errors:
        print("AEP-005 Permission Lease invalid:")
        for e in errors:
            print(f"- {e}")
        return 1
    print("AEP-005 Permission Lease valid.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_permission_lease.py lease.json")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

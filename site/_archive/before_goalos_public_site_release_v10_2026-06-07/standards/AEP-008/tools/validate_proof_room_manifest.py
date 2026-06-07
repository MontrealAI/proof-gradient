import json
import re
import sys
from pathlib import Path
from proof_room_hash import canonical_hash

REQUIRED = ["room_id","schema","schema_version","room_name","room_mode","owner","organization","jurisdiction","purpose","opened_at","status","confidentiality_class","evidence_boundary_ref","charter_ref","hash"]
MODES = {"sandbox","team","institutional","public_safe","incident","sovereign"}

def validate(obj):
    errors = []
    for key in REQUIRED:
        if key not in obj:
            errors.append(f"missing required field: {key}")
    if obj.get("schema") != "AEP-008-PROOF-ROOM-MANIFEST":
        errors.append("schema must be AEP-008-PROOF-ROOM-MANIFEST")
    if obj.get("room_mode") not in MODES:
        errors.append(f"invalid room_mode: {obj.get('room_mode')}")
    h = obj.get("hash", "")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", h):
        errors.append("hash must match sha256:<64 hex chars>")
    elif h != canonical_hash(obj):
        errors.append(f"hash mismatch: expected {canonical_hash(obj)}")
    return errors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate_proof_room_manifest.py manifest.json")
        raise SystemExit(2)
    obj = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = validate(obj)
    if errors:
        print("AEP-008 Proof Room Manifest invalid:")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(1)
    print("AEP-008 Proof Room Manifest valid.")

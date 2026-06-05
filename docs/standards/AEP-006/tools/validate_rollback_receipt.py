import json, re, sys
from pathlib import Path
from rollback_receipt_hash import canonical_hash
REQUIRED=["receipt_id","schema","schema_version","rollback_request_id","rollback_plan_id","trigger_id","status","action_type","rollback_target","baseline_ref","candidate_ref","affected_scope","executed_by","started_at","completed_at","steps_executed","evidence_refs","proof_packet_refs","residual_risk","public_private_boundary","claim_boundary","hash"]
STATUSES={"not_required","ready","requested","authorized","in_progress","completed","verified","partial","failed","compensation_required","compensated","quarantined","archived"}
def validate(obj):
    errors=[]
    for k in REQUIRED:
        if k not in obj: errors.append(f"missing required field: {k}")
    if obj.get("schema")!="AEP-006-ROLLBACK-RECEIPT": errors.append("schema must be AEP-006-ROLLBACK-RECEIPT")
    if obj.get("status") not in STATUSES: errors.append(f"invalid status: {obj.get('status')}")
    if obj.get("status") in {"completed","verified"} and not obj.get("verification_ref"):
        errors.append("completed/verified rollback should include verification_ref")
    if obj.get("status") in {"failed","compensation_required"} and not obj.get("compensation_ref"):
        errors.append("failed/compensation_required rollback should include compensation_ref")
    h=obj.get("hash","")
    if not re.match(r"^sha256:[a-fA-F0-9]{64}$", h): errors.append("hash format invalid")
    elif h != canonical_hash(obj): errors.append(f"hash mismatch: expected {canonical_hash(obj)}")
    return errors
if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("usage: python validate_rollback_receipt.py receipt.json")
        raise SystemExit(2)
    obj=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors=validate(obj)
    if errors:
        print("AEP-006 Rollback Receipt invalid:")
        for e in errors: print(f"- {e}")
        raise SystemExit(1)
    print("AEP-006 Rollback Receipt valid.")

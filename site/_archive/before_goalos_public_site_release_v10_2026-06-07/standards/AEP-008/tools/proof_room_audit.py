import json
import sys
from pathlib import Path

def audit(manifest, charter, boundary, roles, work, decision_log, audit_export=None, closure=None):
    issues = []
    if manifest.get("schema") != "AEP-008-PROOF-ROOM-MANIFEST":
        issues.append("manifest schema invalid")
    if not charter.get("mission"):
        issues.append("charter missing mission")
    if not charter.get("success_criteria"):
        issues.append("charter missing success criteria")
    if not boundary.get("publication_rules"):
        issues.append("evidence boundary missing publication rules")
    if roles.get("separation_of_duties_required") and not roles.get("assignments"):
        issues.append("separation of duties required but no role assignments")
    if not work.get("work_items"):
        issues.append("work item registry empty")
    if not decision_log.get("decisions"):
        issues.append("decision log empty")
    if audit_export and not audit_export.get("hash"):
        issues.append("audit export missing hash")
    if closure and not closure.get("archive_location"):
        issues.append("closure missing archive location")
    return issues

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("usage: python proof_room_audit.py manifest.json charter.json boundary.json roles.json work.json decision_log.json [audit.json] [closure.json]")
        raise SystemExit(2)
    objs = [json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[1:]]
    issues = audit(*objs)
    if issues:
        print("Proof Room audit failed:")
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)
    print("Proof Room audit passed.")

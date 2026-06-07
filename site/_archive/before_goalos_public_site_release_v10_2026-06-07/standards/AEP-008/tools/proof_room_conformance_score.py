import json
import sys
from pathlib import Path

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def score(manifest, charter=None, boundary=None, roles=None, work=None, decision_log=None, audit=None, closure=None):
    points = 0
    max_points = 10
    if manifest.get("schema") == "AEP-008-PROOF-ROOM-MANIFEST": points += 1
    if charter and charter.get("mission") and charter.get("success_criteria"): points += 1
    if boundary and boundary.get("publication_rules"): points += 1
    if roles and roles.get("assignments"): points += 1
    if roles and roles.get("separation_of_duties_required") is True: points += 1
    if work and work.get("work_items"): points += 1
    if decision_log and decision_log.get("decisions"): points += 1
    if audit and audit.get("hash", "").startswith("sha256:"): points += 1
    if closure and closure.get("archive_location"): points += 1
    if manifest.get("hash", "").startswith("sha256:"): points += 1
    level = 5 if points >= 9 else 4 if points >= 7 else 3 if points >= 5 else 2 if points >= 3 else 1 if points >= 2 else 0
    return points, max_points, level

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python proof_room_conformance_score.py manifest.json [charter boundary roles work decision_log audit closure]")
        raise SystemExit(2)
    objs = [load(p) for p in sys.argv[1:]]
    points, max_points, level = score(*objs)
    print(f"score={points}/{max_points}")
    print(f"conformance_level={level}")

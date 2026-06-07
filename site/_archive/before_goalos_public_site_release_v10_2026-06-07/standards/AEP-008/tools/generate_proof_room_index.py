import json
import sys
from pathlib import Path

def main(folder, out_path):
    folder = Path(folder)
    entries = []
    for p in sorted(folder.rglob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        schema = data.get("schema") or data.get("title") or "unknown"
        entries.append({"file": str(p.relative_to(folder)), "schema": schema})
    Path(out_path).write_text(json.dumps({"proof_room_index": entries}, indent=2), encoding="utf-8")
    print(out_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python generate_proof_room_index.py folder out.json")
        raise SystemExit(2)
    main(sys.argv[1], sys.argv[2])

import json, hashlib, sys
from pathlib import Path
ZERO_HASH = "sha256:" + "0" * 64

def canonical_hash(obj: dict) -> str:
    o = json.loads(json.dumps(obj))
    if "hash" in o:
        o["hash"] = ZERO_HASH
    o.pop("signature", None)
    payload = json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python rollback_receipt_hash.py object.json")
        raise SystemExit(2)
    print(canonical_hash(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))

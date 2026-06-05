import json, hashlib, sys
from pathlib import Path
ZERO_HASH = "sha256:" + "0"*64

def canonical_hash(obj):
    x = json.loads(json.dumps(obj))
    if "hash" in x:
        x["hash"] = ZERO_HASH
    x.pop("signature", None)
    payload = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python public_safe_report_hash.py report.json")
        raise SystemExit(2)
    print(canonical_hash(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))

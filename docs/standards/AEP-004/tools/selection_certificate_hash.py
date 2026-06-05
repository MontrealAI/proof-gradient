import json
import hashlib
import sys
from pathlib import Path

ZERO_HASH = "sha256:" + "0" * 64

def canonical_hash(certificate: dict) -> str:
    c = json.loads(json.dumps(certificate))
    c["hash"] = ZERO_HASH
    c.pop("signature", None)
    payload = json.dumps(c, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()

def main(path: str) -> int:
    cert = json.loads(Path(path).read_text(encoding="utf-8"))
    print(canonical_hash(cert))
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python selection_certificate_hash.py certificate.json")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

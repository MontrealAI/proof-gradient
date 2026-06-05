import json
import hashlib
import sys
from pathlib import Path

ZERO_HASH = "sha256:" + "0" * 64

def canonicalize(packet: dict) -> bytes:
    p = json.loads(json.dumps(packet))
    p["hash"] = ZERO_HASH
    p.pop("signature", None)
    return json.dumps(p, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def canonical_packet_hash(packet: dict) -> str:
    return "sha256:" + hashlib.sha256(canonicalize(packet)).hexdigest()

def main(path: str) -> int:
    packet = json.loads(Path(path).read_text(encoding="utf-8"))
    print(canonical_packet_hash(packet))
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python proof_packet_hash.py packet.json")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

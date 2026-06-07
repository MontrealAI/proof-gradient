import json
import hashlib
import sys
from pathlib import Path

def bundle_hash(packet_hashes: list[str]) -> str:
    payload = "|".join(packet_hashes).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()

def main(folder: str, out_path: str) -> int:
    packets = []
    for p in sorted(Path(folder).glob("*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        if data.get("schema") == "AEP-003":
            packets.append(data)
    hashes = [{"packet_id": p["packet_id"], "hash": p["hash"]} for p in packets]
    bundle = {
        "bundle_id": "bundle_" + hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()[:12],
        "schema": "AEP-003-BUNDLE",
        "schema_version": "1.1",
        "docket_id": packets[0].get("docket_id", "") if packets else "",
        "commitment_id": packets[0].get("commitment_id", "") if packets else "",
        "run_id": packets[0].get("run_id", "") if packets else "",
        "hash_algorithm": "sha256",
        "aggregation_method": "ordered_join",
        "packet_hashes": hashes,
        "bundle_hash": bundle_hash([h["hash"] for h in hashes]),
        "created_at": "generated"
    }
    Path(out_path).write_text(json.dumps(bundle, indent=2), encoding="utf-8")
    print(out_path)
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python proof_packet_bundle.py packet_folder out.json")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))

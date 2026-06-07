import json
import sys
from pathlib import Path
from validate_proof_packet import validate_packet

def main(folder: str) -> int:
    packets = []
    for p in sorted(Path(folder).glob("*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        if data.get("schema") == "AEP-003":
            packets.append((p, data))
    failed = False
    hashes = {}
    for p, packet in packets:
        errors = validate_packet(packet)
        if errors:
            failed = True
            print(f"{p} invalid:")
            for e in errors:
                print(f"- {e}")
        hashes[packet["hash"]] = packet["packet_id"]
    for p, packet in packets:
        prev = packet.get("previous_packet_hash")
        if prev and prev not in hashes:
            failed = True
            print(f"{p} references missing previous_packet_hash: {prev}")
    if failed:
        return 1
    print(f"ProofPacket chain valid: {len(packets)} packets")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python verify_packet_chain.py packet_folder")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

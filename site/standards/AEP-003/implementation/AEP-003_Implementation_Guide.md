# AEP-003 Implementation Guide

## Purpose

AEP-003 turns raw machine-work events into portable proof.

## Minimum implementation

1. Emit one ProofPacket per important event.
2. Use `schema = AEP-003`.
3. Include commitment, run, claim, and evidence references.
4. Include public/private/protected boundary.
5. Include claim boundary.
6. Compute canonical hash.
7. Attach the packet to an AEP-002 Evidence Docket.

## Recommended implementation sequence

1. Start with eval_result packets.
2. Add tool_call packets.
3. Add policy_decision packets.
4. Add selection_decision packets.
5. Add rollback_event packets.
6. Bundle packets into Evidence Dockets.
7. Add signatures and attestations.

## Developer commands

```bash
python tools/validate_proof_packet.py examples/sample_proof_packet_06_eval_result.json
python tools/proof_packet_hash.py examples/sample_proof_packet_06_eval_result.json
python tools/verify_packet_chain.py examples/
python tools/proof_packet_bundle.py examples/ bundle.json
```

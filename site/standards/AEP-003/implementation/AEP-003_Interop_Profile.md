# AEP-003 Interoperability Profile

AEP-003 ProofPackets should be portable across:

- GitHub Actions
- CI/CD systems
- agent frameworks
- workflow engines
- AI coding systems
- enterprise audit dashboards
- public-sector proof rooms
- sovereign AI programs

## Stable interchange fields

- packet_id
- schema
- schema_version
- packet_type
- docket_id
- commitment_id
- run_id
- claim_refs
- evidence_refs
- boundary
- payload
- hash
- claim_boundary

## Canonical JSON profile

- UTF-8
- sorted keys
- no insignificant whitespace
- signature excluded
- hash field zeroed during calculation
- SHA-256 hash

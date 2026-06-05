# AEP-003 — ProofPacket Schema

**Version:** v1.1 Institutional Edition  
**Status:** Implementation Standard  
**Protocol family:** Proof Gradient / Agent Evolution Protocol  
**Parent standards:** AEP-001 — GoalOS Proof-of-Evolution Constitution; AEP-002 — Evidence Docket Standard  
**Canonical loop:** Commit → Execute → Prove → Evolve  
**Author / Steward:** Vincent Boucher, QUEBEC.AI & MONTREAL.AI  
**Date:** 2026-06-05

## Abstract

AEP-003 defines the **ProofPacket**: the atomic evidence unit emitted by an AI-agent run, machine-work step, tool call, evaluation, policy decision, selection decision, rollout event, rollback event, or public-safe report event.

AEP-001 defines the constitutional protocol.  
AEP-002 defines the Evidence Docket.  
AEP-003 defines the packet-level schema that makes machine work traceable, portable, tamper-evident, and composable.

A ProofPacket is small enough to emit for every important machine action and strong enough to anchor an Evidence Docket.

## Canonical thesis

A model can answer.  
An agent can act.  
An institution must prove.

AEP-003 makes proof atomic.

## Canonical law

No proof, no evolution.  
No eval, no propagation.  
No rollback, no release.

## Relationship to AEP-001 and AEP-002

AEP-001 defines the Agent Evolution Protocol:

`Commit → Execute → Prove → Evolve`

AEP-002 defines the Evidence Docket, the portable proof package for a run or workflow.

AEP-003 defines the ProofPacket, the atomic evidence object inside an Evidence Docket.

In short:

- **AEP-001** defines the protocol.
- **AEP-002** defines the proof package.
- **AEP-003** defines the atomic proof record.

## What is a ProofPacket?

A ProofPacket is a structured, hashable, optionally signed record that proves a specific part of machine work.

It may represent:

- a commitment
- an execution event
- a trace summary
- a tool call
- a policy decision
- an approval
- an evaluation
- a risk event
- a cost event
- a selection decision
- a canary rollout
- a rollback event
- a public-safe report event

Each ProofPacket answers:

1. What happened?
2. What was the packet proving?
3. Which commitment, claim, run, artifact, or docket does it relate to?
4. What evidence supports it?
5. Which checks or evaluations apply?
6. Which policy, permission, or approval decision applied?
7. What is the cost, risk, and latency profile?
8. What is the public/private/protected evidence boundary?
9. What is the packet hash?
10. Who or what attested to it?

## v1.1 upgrades

AEP-003 v1.1 adds implementation-level materials:

- canonicalization profile
- signature and attestation schema
- ordered hash-chain manifest
- packet bundle schema
- full examples for all packet types
- validator
- hash tool
- packet chain verifier
- packet bundle assembler
- Evidence Docket attachment example
- GitHub Actions for website, conformance CI, and official release

## ProofPacket design principles

### 1. Atomic

A ProofPacket should prove one coherent thing.

### 2. Hashable

The packet should have deterministic canonical JSON and a checksum.

### 3. Composable

Many ProofPackets can form an Evidence Docket.

### 4. Boundary-aware

A ProofPacket must distinguish public, private, and protected evidence.

### 5. Claim-bounded

A ProofPacket must say what it supports and what it does not support.

### 6. Evolvable

A ProofPacket can support a Selection Gate decision, but cannot by itself force propagation.

### 7. Rollback-aware

High-risk packets should identify rollback relevance and rollback target.

## Required top-level fields

A conforming ProofPacket must include:

- `packet_id`
- `schema`
- `schema_version`
- `packet_type`
- `created_at`
- `producer`
- `docket_id`
- `commitment_id`
- `run_id`
- `claim_refs`
- `evidence_refs`
- `boundary`
- `payload`
- `hash`
- `claim_boundary`

## Recommended top-level fields

A robust ProofPacket should also include:

- `artifact_refs`
- `trace_refs`
- `tool_refs`
- `policy_refs`
- `eval_refs`
- `risk_refs`
- `cost_summary`
- `latency_summary`
- `selection_ref`
- `rollback_ref`
- `attestations`
- `signature`
- `previous_packet_hash`
- `docket_hash`
- `canonicalization_method`
- `hash_algorithm`

## Packet types

AEP-003 defines the following packet types:

### commit

Records the mission, authorization, constraints, success criteria, and failure criteria.

### trace_event

Records a relevant execution event without necessarily publishing the full trace.

### tool_call

Records tool use, permission class, approval state, and result summary.

### policy_decision

Records a policy decision, denial, escalation, or approval requirement.

### approval

Records human or institutional authorization.

### eval_result

Records an evaluation, test, check, score, or evaluator attestation.

### evidence_ref

Records a reference to evidence stored elsewhere.

### risk_event

Records a risk, incident, mitigation, or residual concern.

### cost_event

Records cost, latency, token count, compute time, or human-review burden.

### selection_decision

Records a Selection Gate decision.

### rollout_event

Records canary scope, monitoring plan, and propagation limit.

### rollback_event

Records rollback trigger, target, action, owner, and recovery.

### public_report

Records a public-safe report publication event.

## Core object model

### Identity block

The identity block identifies the packet.

Required fields:

- packet_id
- schema
- schema_version
- packet_type
- created_at
- producer
- environment

### Linkage block

The linkage block connects the packet to larger proof objects.

Recommended fields:

- docket_id
- commitment_id
- run_id
- job_id
- artifact_refs
- claim_refs
- evidence_refs
- previous_packet_hash
- docket_hash

### Boundary block

The boundary block defines evidence visibility.

Required fields:

- access_class
- public_safe
- contains_sensitive_data
- retention_policy
- jurisdiction
- publication_allowed

Access classes:

- public
- private
- protected
- restricted

### Payload block

The payload block contains packet-type-specific content.

Examples:

- tool call summary
- eval result
- policy decision
- approval event
- risk event
- rollback event

### Verification block

The verification block supports integrity and attestation.

Recommended fields:

- canonicalization_method
- hash_algorithm
- hash
- signature
- signer
- attestation
- timestamp_authority

### Claim boundary block

The claim boundary block records supported and unsupported claims.

Required fields:

- supports
- does_not_support
- limitations
- public_claim_allowed

## Canonical JSON and hashing

A ProofPacket should be hashed using deterministic canonical JSON.

Recommended method:

1. Remove mutable signature fields.
2. Set `hash` to `sha256:` followed by 64 zeroes for hash calculation.
3. Sort object keys.
4. Encode as UTF-8.
5. Use SHA-256 unless another approved algorithm is specified.
6. Store the result as `sha256:<hex>`.

Reference expression:

`packet_hash = SHA256(canonical_json(packet_without_signature))`

AEP-003 includes a reference Python validator and hash tool.

## Hash chains and packet bundles

AEP-003 supports optional packet chains.

A packet may include:

- `previous_packet_hash`
- `docket_hash`
- `bundle_id`
- `sequence_index`

A packet bundle is an ordered collection of ProofPackets. It can be attached to an Evidence Docket.

Bundle hash:

`bundle_hash = SHA256(join(packet_hashes_in_order))`

For higher-assurance systems, implementers may replace ordered aggregation with a Merkle tree.

## ProofPacket lifecycle

1. Created
2. Canonicalized
3. Hashed
4. Validated
5. Attached to Evidence Docket
6. Evaluated
7. Referenced by Selection Gate
8. Archived
9. Public-safe subset published, if allowed
10. Superseded or rolled back, if necessary

## Conformance levels

### Level 0 — Informal packet

Human-readable proof fragment with packet type, claim, and evidence reference.

### Level 1 — Valid JSON packet

Conforms to the required AEP-003 JSON schema.

### Level 2 — Hashable packet

Uses canonical JSON and includes a valid packet hash.

### Level 3 — Docket-linked packet

Links to an Evidence Docket, commitment, run, claim, and evidence inventory.

### Level 4 — Institutional packet

Includes policy, eval, risk, cost, boundary, attestation, and Selection Gate references.

### Level 5 — Sovereign / regulated packet

Includes jurisdiction, retention, protected-boundary classification, authorized data boundary, signer, timestamp authority, and restricted appendix controls.

## Security and privacy requirements

Do not place secrets, personal data, regulated data, private prompts, full sensitive traces, credentials, confidential tool outputs, or protected operational details in a public ProofPacket.

Use references, hashes, and access-class markers instead.

A public ProofPacket should prove that evidence exists and what it supports without leaking the protected evidence itself.

## Interoperability

AEP-003 can be implemented in:

- CI/CD systems
- GitHub Actions
- agent frameworks
- LLM tool-call systems
- AI coding agents
- workflow engines
- enterprise audit systems
- public-sector proof rooms
- sovereign AI programs

AEP-003 packets should be portable across storage systems if their canonical JSON, hashes, claim boundaries, and access classes are preserved.

## Claim boundary

AEP-003 does not claim:

- achieved AGI
- achieved ASI
- perfect safety
- legal compliance certification
- financial or legal advice
- guaranteed ROI
- production readiness
- government endorsement
- national-security readiness

AEP-003 defines an atomic proof schema.

## Canonical public line

AEP-001 defines the protocol.  
AEP-002 defines the docket.  
AEP-003 defines the packet.

GoalOS makes machine work provable one packet at a time.

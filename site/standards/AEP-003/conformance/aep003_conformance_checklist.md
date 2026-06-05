# AEP-003 Conformance Checklist

## Level 0 — Informal packet

- [ ] Packet type is stated.
- [ ] Claim or event is described.
- [ ] Evidence reference is listed.
- [ ] Claim boundary exists.

## Level 1 — Valid JSON packet

- [ ] Required fields exist.
- [ ] Packet type is valid.
- [ ] Boundary block exists.
- [ ] Payload block exists.
- [ ] Claim boundary block exists.

## Level 2 — Hashable packet

- [ ] Canonical JSON method is specified.
- [ ] SHA-256 hash exists.
- [ ] Hash validates.
- [ ] Signature fields are excluded from canonical hash.

## Level 3 — Docket-linked packet

- [ ] Docket ID exists.
- [ ] Commitment ID exists.
- [ ] Run ID exists.
- [ ] Claim refs exist.
- [ ] Evidence refs exist.

## Level 4 — Institutional packet

- [ ] Policy refs or policy payload exists.
- [ ] Eval refs or eval payload exists.
- [ ] Risk refs or risk payload exists.
- [ ] Cost / latency summary exists.
- [ ] Selection or rollback references exist where relevant.

## Level 5 — Sovereign / regulated packet

- [ ] Jurisdiction exists.
- [ ] Retention policy exists.
- [ ] Access class is public/private/protected/restricted.
- [ ] Publication policy is explicit.
- [ ] Attestation or signature exists.
- [ ] Protected boundary is clear.

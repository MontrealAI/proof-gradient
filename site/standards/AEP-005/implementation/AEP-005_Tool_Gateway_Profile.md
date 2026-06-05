# AEP-005 Tool Gateway Profile

A Tool Gateway enforces AEP-005.

## Required gateway behavior

- Load tool manifest.
- Load applicable policy.
- Validate requester.
- Validate scope.
- Validate permission class.
- Check approval requirement.
- Check lease and expiration.
- Check rate limit.
- Check data boundary.
- Check rollback or compensation requirement.
- Check separation of duties.
- Issue decision.
- Emit proof.
- Record receipt after execution.
- Support revocation.
- Support break-glass review.

## Gateway outputs

- Tool Permission Decision
- Permission Lease
- Approval Receipt, if applicable
- Tool Call Receipt
- Revocation Receipt, if applicable
- Compensation Receipt, if applicable
- ProofPacket reference
- Evidence Docket reference

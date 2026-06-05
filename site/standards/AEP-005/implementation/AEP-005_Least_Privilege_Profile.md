# AEP-005 Least Privilege Profile

## Rule

Grant the lowest permission class that can complete the committed work.

## Examples

- Use `read` instead of `write` where retrieval is enough.
- Use `draft` instead of `send` where human approval is needed.
- Use `transform` instead of `execute` where deterministic transformation is enough.
- Use `allow_readonly` for uncertain requests.
- Use `approval_required` for external effects.
- Use `deny` for missing scope or missing rollback.

## Anti-pattern

Permanent broad permissions for agents.

## Correct pattern

Short-lived scoped leases.

# GoalOS Cloud MVP 0.2

GoalOS Cloud MVP 0.2 is a public static software proof for the GoalOS Recursive Workflow OS.

It demonstrates:

`Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run`

## Runtime boundary

- Runs fully in the browser.
- Uses browser `localStorage` for demo persistence.
- Requires no secrets and no backend.
- Does not include paid buyer ZIPs, paid workshop materials, implementation bundles, or enterprise delivery kits.
- Does not modify AI models; recursive improvement happens at the workflow layer.

## Included modules

- Organization, workspace, and user roles
- Policy engine
- Controlled memory
- Model-provider restrictions
- Workflow Studio
- Workflow versioning
- Execution Engine demo
- Evaluation Engine demo
- Proof Room records
- Recursive Improvement Engine
- Improvement Proposal
- Human approval gate
- Version comparison
- Rollback target
- Proof Graph export
- Public-safe proof card export
- Executive proof report export
- Audit log
- OpenAPI blueprint
- JSON schemas
- Node unit tests

## Demo workflow

**Customer Support Reply Workflow**

v1.0 intentionally misses refund/access policy classification. The MVP runs support cases, evaluates outputs, creates proof records, detects the refund-policy failure, generates a v1.1 improvement proposal, benchmarks v1.0 vs v1.1, requires human approval, deploys approved v1.1, preserves rollback target v1.0, and exports a public-safe proof card plus Proof Graph.

## Test

Run both public-safe Node test suites from the repository root:

```bash
node site/app/goalos-cloud-mvp/tests/goalos-core.test.mjs
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

The tests assert that v1.0 exposes the refund-policy weakness, v1.1 improves refund-policy compliance, approval requires a rollback target, confidential-data provider restrictions work, the Proof Graph has nodes and edges, and the public-safe proof card avoids ROI, compliance, and model-self-modification claims.

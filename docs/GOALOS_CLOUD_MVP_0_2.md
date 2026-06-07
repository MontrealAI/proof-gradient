# GoalOS Cloud MVP 0.2

GoalOS Cloud MVP 0.2 is a public static software proof at `site/app/goalos-cloud-mvp/`.

## Runtime

- Browser-only static app.
- Uses browser `localStorage`.
- Requires no secrets, no backend, and no paid materials.
- Includes an OpenAPI blueprint and JSON schemas for future SaaS development.

## Demonstrated capabilities

- Organization, workspace, and user roles.
- Policy engine and controlled memory.
- Model-provider restrictions, including confidential-data blocking for public/local providers.
- Workflow Studio and workflow versioning.
- Execution Engine and Evaluation Engine demos.
- Proof Room records and audit log.
- Recursive Improvement Engine.
- Improvement Proposal, human approval gate, version comparison, rollback target.
- Proof Graph export.
- Public-safe proof card and executive proof report export.

## Demo story

The demo workflow is **Customer Support Reply Workflow**.

v1.0 intentionally misses refund/access policy classification. The MVP proves the loop:

1. run support cases;
2. evaluate outputs;
3. create proof records;
4. detect refund-policy failure;
5. generate a v1.1 improvement proposal;
6. benchmark v1.0 vs v1.1;
7. require human approval;
8. deploy approved v1.1;
9. preserve rollback target v1.0;
10. export a public-safe proof card;
11. export a Proof Graph.

## Test

```bash
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

The test asserts that v1.0 exposes a refund-policy weakness, v1.1 improves refund-policy compliance, approval requires a rollback target, confidential-data provider restrictions work, the Proof Graph has nodes and edges, and the public-safe proof card avoids ROI, compliance, and model-self-modification claims.

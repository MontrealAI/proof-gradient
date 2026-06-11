# Proof Gradient API Reference

This document describes the FastAPI application implemented in `proof_gradient/api.py`.

## Run the API locally

Install the package with development dependencies, initialize the database, and start the API server:

```bash
python -m pip install -e '.[dev]'
proof-gradient db init
proof-gradient api --host 127.0.0.1 --port 8000
```

The default base URL is:

```text
http://127.0.0.1:8000
```

The API initializes its database during the FastAPI lifespan startup hook. For a clean local demo state, run `proof-gradient db reset` before starting the server.

## Health and readiness

### `GET /healthz`

Returns a lightweight process health response.

Example response:

```json
{
  "status": "ok",
  "service": "proof-gradient"
}
```

### `GET /readyz`

Checks that the configured database can be queried.

Example response:

```json
{
  "status": "ready"
}
```

### `GET /metrics`

Returns Prometheus-style counters for the local proof-gradient records.

Example response:

```text
proof_gradient_artifacts_total 1
proof_gradient_runs_total 1
proof_gradient_proofs_total 1
proof_gradient_patches_total 1
proof_gradient_rollouts_total 1
```

## Tenants

### `POST /tenants`

Creates a tenant and a default owner user.

Request body:

```json
{
  "name": "demo"
}
```

Example response:

```json
{
  "tenant_id": 1,
  "name": "demo"
}
```

## Demo workflow

### `POST /demo/run`

Runs the customer-response demo through the Artifact Vault, Run Fabric, Proof Ledger, and Selection Gate path.

Request body:

```json
{
  "tenant": "demo",
  "prompt": "Draft a response to this angry customer asking for a refund."
}
```

The response includes the created artifact, run, proof, patch, decision, rollout, and claim-boundary result identifiers.

## Evidence listings

All listing endpoints accept an optional `tenant` query parameter. The default tenant is `demo`.

### `GET /artifacts?tenant=demo`

Returns artifacts for a tenant. If the tenant does not exist, the endpoint returns `404`.

### `GET /runs?tenant=demo`

Returns run records for a tenant. If the tenant does not exist, the endpoint returns an empty `runs` list.

### `GET /proofs?tenant=demo`

Returns proof records for a tenant. If the tenant does not exist, the endpoint returns an empty `proofs` list.

## Browser landing page

### `GET /`

Returns a small HTML landing page with the Proof Gradient operating thesis.

## Validation

Run the API tests with the development dependencies installed:

```bash
python -m pip install -e '.[dev]'
pytest tests/test_proof_gradient_api.py
```

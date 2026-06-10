# Proof Gradient API Reference

This reference covers the local FastAPI service exposed by `proof_gradient.api`. It is intentionally limited to public-safe platform endpoints that can be exercised against a local SQLite database.

## Run the server

From the repository root:

```bash
python -m proof_gradient api --host 127.0.0.1 --port 8000
```

Equivalent Make target:

```bash
make api
```

Base URL:

```text
http://127.0.0.1:8000
```

The API initializes the configured database at startup. The default local database is `sqlite:///./proof_gradient.db` unless `PROOF_GRADIENT_DATABASE_URL` is set.

## Operational endpoints

### Health

```http
GET /healthz
```

Returns service liveness:

```json
{
  "status": "ok",
  "service": "proof-gradient"
}
```

### Readiness

```http
GET /readyz
```

Checks database access and returns:

```json
{
  "status": "ready"
}
```

### Metrics

```http
GET /metrics
```

Returns Prometheus-style counters for artifacts, runs, proofs, patches, and rollouts.

## Tenant setup

### Create tenant

```http
POST /tenants
Content-Type: application/json
```

```json
{
  "name": "demo"
}
```

The service creates the tenant and a local owner identity for that tenant.

## Demo workflow

### Run customer-response demo

```http
POST /demo/run
Content-Type: application/json
```

```json
{
  "tenant": "demo",
  "prompt": "Draft a response to this angry customer asking for a refund."
}
```

The demo exercises the proof-led workflow loop and returns the generated run, artifacts, proof, patch, rollout, and selection outputs.

## Query endpoints

All query endpoints accept an optional `tenant` query parameter. If omitted, the default tenant is `demo`.

### List artifacts

```http
GET /artifacts?tenant=demo
```

Returns artifact IDs, names, artifact types, and risk classes for the tenant.

### List runs

```http
GET /runs?tenant=demo
```

Returns run IDs, statuses, and job IDs for the tenant.

### List proofs

```http
GET /proofs?tenant=demo
```

Returns proof IDs, associated run IDs, and checksums for the tenant.

## CLI companions

The same local platform can be exercised without starting the API:

```bash
python -m proof_gradient demo --json
python -m proof_gradient artifact list --tenant demo
python -m proof_gradient proof list --tenant demo
python -m proof_gradient selection list --tenant demo
```

## Validation before publishing docs or site changes

Run the public-safe validation suite before opening a PR:

```bash
make validate
```

or run the underlying commands directly:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

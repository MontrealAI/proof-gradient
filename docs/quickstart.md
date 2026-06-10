# Quickstart

Use this quickstart from the repository root.

## 1. Install local development dependencies

```bash
python -m pip install -e '.[dev]'
```

The development extra installs the FastAPI test-client transport packages required by the API tests.

## 2. Initialize or reset the local database

```bash
proof-gradient db init
```

For a clean local demo state:

```bash
proof-gradient db reset
```

## 3. Run the Proof Gradient demo

```bash
proof-gradient demo --tenant demo --json
```

The demo creates a tenant, runs a customer-response workflow, records proof, applies the selection gate, and emits a proof-bound result.

## 4. Start the API

```bash
proof-gradient api --host 127.0.0.1 --port 8000
```

Then open:

```text
http://127.0.0.1:8000
```

Useful local checks:

```bash
curl http://127.0.0.1:8000/healthz
curl http://127.0.0.1:8000/readyz
curl http://127.0.0.1:8000/metrics
```

## 5. Run required repository validation

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_public_site.py
```

## 6. Run tests

```bash
pytest
make test
```

`pytest` is the primary Python test command configured by `pyproject.toml`. `make test` runs the unittest discovery suite and is kept as a compatibility check.

## Public command center

```text
https://montrealai.github.io/proof-gradient/
```

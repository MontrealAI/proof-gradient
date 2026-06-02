from fastapi.testclient import TestClient

from proof_gradient.api import app
from proof_gradient.db import reset_db


def test_api_demo_run_and_metrics():
    reset_db()
    client = TestClient(app)

    response = client.get("/healthz")
    assert response.status_code == 200

    response = client.post("/demo/run", json={"tenant": "api", "prompt": "refund response"})
    assert response.status_code == 200
    body = response.json()
    assert body["proof_id"]
    assert body["rollback_id"]

    response = client.get("/proofs", params={"tenant": "api"})
    assert response.status_code == 200
    assert len(response.json()["proofs"]) == 1

    response = client.get("/metrics")
    assert response.status_code == 200
    assert "proof_gradient_proofs_total" in response.text

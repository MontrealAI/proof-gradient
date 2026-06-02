from sqlalchemy import select

from proof_gradient import models
from proof_gradient.db import SessionLocal, reset_db
from proof_gradient.services import ArtifactVault, RunFabric, create_tenant, create_user


def test_full_job_to_rollback_vertical_slice():
    reset_db()
    with SessionLocal() as session:
        tenant = create_tenant(session, "demo")
        create_user(session, tenant.id, "owner@example.com", "owner")
        result = RunFabric(session, tenant.id).run_customer_response_demo("Draft a response to this angry customer asking for a refund.")
        session.commit()

        assert result["run_contract"]["trace_required"] is True
        assert result["proof_id"]
        assert result["patch_id"]
        assert result["selection_id"]
        assert result["rollout_id"]
        assert result["rollback_id"]

        proof = session.get(models.Proof, result["proof_id"])
        assert proof is not None
        assert "credit_assignment" in proof.proof_json

        rollout = session.get(models.Rollout, result["rollout_id"])
        assert rollout.rollout_percentage == 10

        rollback = session.get(models.Rollback, result["rollback_id"])
        assert rollback.rollback_target == "customer_response_plan@1.0.0"


def test_released_artifact_is_immutable():
    reset_db()
    with SessionLocal() as session:
        tenant = create_tenant(session, "immutability")
        vault = ArtifactVault(session, tenant.id)
        artifact = vault.create_artifact("skill", "immutable_skill")
        version = vault.create_version(artifact, "1.0.0", {"instruction": "do safe work"})
        vault.release(version, "active")

        try:
            vault.update_content(version, {"instruction": "mutated"})
        except ValueError as exc:
            assert "immutable" in str(exc)
        else:
            raise AssertionError("released artifact mutation should fail")


def test_append_only_proof_and_trace_exist():
    reset_db()
    with SessionLocal() as session:
        tenant = create_tenant(session, "ledger")
        result = RunFabric(session, tenant.id).run_customer_response_demo("refund response")
        session.commit()

        traces = session.scalars(select(models.TraceEvent).where(models.TraceEvent.run_id == result["run_id"])).all()
        proofs = session.scalars(select(models.Proof).where(models.Proof.run_id == result["run_id"])).all()
        assert len(traces) >= 4
        assert len(proofs) == 1

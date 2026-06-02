from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from proof_gradient import models
from proof_gradient.db import SessionLocal, init_db
from proof_gradient.services import RunFabric, create_tenant, create_user


app = FastAPI(title="Proof Gradient Platform", description="Artifact Vault, Run Fabric, Proof Ledger, Selection Gate.", version="0.3.1")


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


class TenantCreate(BaseModel):
    name: str


class DemoRunRequest(BaseModel):
    tenant: str = "demo"
    prompt: str = "Draft a response to this angry customer asking for a refund."


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "service": "proof-gradient"}


@app.get("/readyz")
def readyz(session: Session = Depends(get_session)) -> dict:
    session.execute(select(models.Tenant).limit(1))
    return {"status": "ready"}


@app.get("/metrics", response_class=PlainTextResponse)
def metrics(session: Session = Depends(get_session)) -> str:
    counts = {
        "artifacts": session.query(models.Artifact).count(),
        "runs": session.query(models.Run).count(),
        "proofs": session.query(models.Proof).count(),
        "patches": session.query(models.Patch).count(),
        "rollouts": session.query(models.Rollout).count(),
    }
    return "\\n".join(f"proof_gradient_{name}_total {value}" for name, value in counts.items()) + "\\n"


@app.post("/tenants")
def tenants(payload: TenantCreate, session: Session = Depends(get_session)) -> dict:
    tenant = create_tenant(session, payload.name)
    create_user(session, tenant.id, f"owner@{payload.name}.local", "owner")
    session.commit()
    return {"tenant_id": tenant.id, "name": tenant.name}


@app.post("/demo/run")
def run_demo(payload: DemoRunRequest, session: Session = Depends(get_session)) -> dict:
    tenant = create_tenant(session, payload.tenant)
    create_user(session, tenant.id, f"owner@{payload.tenant}.local", "owner")
    result = RunFabric(session, tenant.id).run_customer_response_demo(payload.prompt)
    session.commit()
    return result


@app.get("/artifacts")
def artifacts(tenant: str = "demo", session: Session = Depends(get_session)) -> dict:
    tenant_row = session.scalar(select(models.Tenant).where(models.Tenant.name == tenant))
    if not tenant_row:
        raise HTTPException(status_code=404, detail="tenant not found")
    rows = session.scalars(select(models.Artifact).where(models.Artifact.tenant_id == tenant_row.id)).all()
    return {"artifacts": [{"id": r.id, "name": r.name, "artifact_type": r.artifact_type, "risk_class": r.risk_class} for r in rows]}


@app.get("/runs")
def runs(tenant: str = "demo", session: Session = Depends(get_session)) -> dict:
    tenant_row = session.scalar(select(models.Tenant).where(models.Tenant.name == tenant))
    if not tenant_row:
        return {"runs": []}
    rows = session.scalars(select(models.Run).where(models.Run.tenant_id == tenant_row.id)).all()
    return {"runs": [{"id": r.id, "status": r.status, "job_id": r.job_id} for r in rows]}


@app.get("/proofs")
def proofs(tenant: str = "demo", session: Session = Depends(get_session)) -> dict:
    tenant_row = session.scalar(select(models.Tenant).where(models.Tenant.name == tenant))
    if not tenant_row:
        return {"proofs": []}
    rows = session.scalars(select(models.Proof).where(models.Proof.tenant_id == tenant_row.id)).all()
    return {"proofs": [{"id": r.id, "run_id": r.run_id, "checksum": r.checksum} for r in rows]}


@app.get("/", response_class=HTMLResponse)
def ui() -> str:
    return "<h1>Aim. Act. Prove. Evolve.</h1><p>Artifact Vault. Run Fabric. Proof Ledger. Selection Gate.</p>"

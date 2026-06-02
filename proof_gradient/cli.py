import json

import typer
import uvicorn
from rich import print
from sqlalchemy import select

from proof_gradient import models
from proof_gradient.db import SessionLocal, init_db, reset_db
from proof_gradient.services import RunFabric, create_tenant, create_user


app = typer.Typer(help="Proof Gradient CLI")
db_app = typer.Typer(help="Database commands")
artifact_app = typer.Typer(help="Artifact commands")
proof_app = typer.Typer(help="Proof commands")
selection_app = typer.Typer(help="Selection commands")

app.add_typer(db_app, name="db")
app.add_typer(artifact_app, name="artifact")
app.add_typer(proof_app, name="proof")
app.add_typer(selection_app, name="selection")


@db_app.command("init")
def db_init() -> None:
    init_db()
    print("[green]database initialized[/green]")


@db_app.command("reset")
def db_reset() -> None:
    reset_db()
    print("[yellow]database reset[/yellow]")


@app.command("demo")
def demo(tenant: str = "demo", prompt: str = "Draft a response to this angry customer asking for a refund.", as_json: bool = typer.Option(False, "--json")) -> None:
    init_db()
    with SessionLocal() as session:
        tenant_row = create_tenant(session, tenant)
        create_user(session, tenant_row.id, f"owner@{tenant}.local", "owner")
        result = RunFabric(session, tenant_row.id).run_customer_response_demo(prompt)
        session.commit()
    print(json.dumps(result, indent=2, default=str) if as_json else result)


@artifact_app.command("list")
def artifact_list(tenant: str = "demo") -> None:
    init_db()
    with SessionLocal() as session:
        tenant_row = session.scalar(select(models.Tenant).where(models.Tenant.name == tenant))
        if not tenant_row:
            print("no tenant found")
            return
        rows = session.scalars(select(models.Artifact).where(models.Artifact.tenant_id == tenant_row.id)).all()
        for row in rows:
            print(f"{row.id} {row.artifact_type} {row.name}")


@proof_app.command("list")
def proof_list(tenant: str = "demo") -> None:
    init_db()
    with SessionLocal() as session:
        tenant_row = session.scalar(select(models.Tenant).where(models.Tenant.name == tenant))
        if not tenant_row:
            print("no tenant found")
            return
        rows = session.scalars(select(models.Proof).where(models.Proof.tenant_id == tenant_row.id)).all()
        for row in rows:
            print(f"{row.id} run={row.run_id} checksum={row.checksum[:12]}")


@selection_app.command("list")
def selection_list(tenant: str = "demo") -> None:
    init_db()
    with SessionLocal() as session:
        tenant_row = session.scalar(select(models.Tenant).where(models.Tenant.name == tenant))
        if not tenant_row:
            print("no tenant found")
            return
        rows = session.scalars(select(models.SelectionDecision).where(models.SelectionDecision.tenant_id == tenant_row.id)).all()
        for row in rows:
            print(f"{row.id} decision={row.decision} patch={row.patch_id}")


@app.command("api")
def api(host: str = "127.0.0.1", port: int = 8000) -> None:
    init_db()
    uvicorn.run("proof_gradient.api:app", host=host, port=port, reload=False)


def main() -> None:
    app()


if __name__ == "__main__":
    main()

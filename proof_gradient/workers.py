from dataclasses import dataclass

from sqlalchemy.orm import Session

from proof_gradient.services import RunFabric


@dataclass
class RunWorker:
    session: Session
    tenant_id: str

    def run(self, prompt: str) -> dict:
        return RunFabric(self.session, self.tenant_id).run_customer_response_demo(prompt)


@dataclass
class EvalWorker:
    session: Session
    tenant_id: str

    def run_pending(self) -> dict:
        return {"status": "ok", "mode": "deterministic", "pending": 0}

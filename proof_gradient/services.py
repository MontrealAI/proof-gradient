from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import time

from sqlalchemy import select
from sqlalchemy.orm import Session

from proof_gradient import models
from proof_gradient.config import settings
from proof_gradient.evals import baseline_vs_candidate_eval, unsupported_claim_eval
from proof_gradient.providers import provider_from_name
from proof_gradient.security import authorize_tool


IMMUTABLE_STATES = {"approved", "canary", "active", "deprecated", "rolled_back"}


def checksum(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def audit(session: Session, tenant_id: str, action: str, resource_type: str, resource_id: str, payload: dict | None = None) -> None:
    session.add(models.AuditEvent(tenant_id=tenant_id, action=action, resource_type=resource_type, resource_id=resource_id, payload_json=payload or {}))


def create_tenant(session: Session, name: str) -> models.Tenant:
    existing = session.scalar(select(models.Tenant).where(models.Tenant.name == name))
    if existing:
        return existing
    tenant = models.Tenant(name=name)
    session.add(tenant)
    session.flush()
    audit(session, tenant.id, "tenant.create", "tenant", tenant.id)
    return tenant


def create_user(session: Session, tenant_id: str, email: str, role: str = "owner") -> models.User:
    existing = session.scalar(select(models.User).where(models.User.tenant_id == tenant_id, models.User.email == email))
    if existing:
        return existing
    user = models.User(tenant_id=tenant_id, email=email, role=role)
    session.add(user)
    session.flush()
    audit(session, tenant_id, "user.create", "user", user.id, {"role": role})
    return user


@dataclass
class ArtifactVault:
    session: Session
    tenant_id: str

    def create_artifact(self, artifact_type: str, name: str, risk_class: str = "low") -> models.Artifact:
        artifact = models.Artifact(tenant_id=self.tenant_id, artifact_type=artifact_type, name=name, risk_class=risk_class)
        self.session.add(artifact)
        self.session.flush()
        audit(self.session, self.tenant_id, "artifact.create", "artifact", artifact.id)
        return artifact

    def create_version(self, artifact: models.Artifact, version: str, content: dict, *, permissions: dict | None = None, rollback_target: str | None = None) -> models.ArtifactVersion:
        body = {"artifact_id": artifact.id, "artifact_type": artifact.artifact_type, "version": version, "content": content, "permissions": permissions or {}}
        av = models.ArtifactVersion(
            tenant_id=self.tenant_id,
            artifact_id=artifact.id,
            version=version,
            lifecycle_state="draft",
            content_json=content,
            permissions_json=permissions or {},
            checksum=checksum(body),
            rollback_target=rollback_target,
        )
        self.session.add(av)
        self.session.flush()
        audit(self.session, self.tenant_id, "artifact_version.create", "artifact_version", av.id)
        return av

    def release(self, version: models.ArtifactVersion, state: str = "active") -> models.ArtifactVersion:
        if version.lifecycle_state in IMMUTABLE_STATES:
            raise ValueError("released artifact versions are immutable")
        version.lifecycle_state = state
        version.released_at = datetime.now(timezone.utc)
        self.session.flush()
        return version

    def update_content(self, version: models.ArtifactVersion, content: dict) -> models.ArtifactVersion:
        if version.lifecycle_state in IMMUTABLE_STATES:
            raise ValueError("released artifact versions are immutable")
        version.content_json = content
        version.checksum = checksum(content)
        self.session.flush()
        return version

    def active_versions(self) -> list[models.ArtifactVersion]:
        return list(self.session.scalars(select(models.ArtifactVersion).where(models.ArtifactVersion.tenant_id == self.tenant_id, models.ArtifactVersion.lifecycle_state.in_(["active", "canary"]))))


def ensure_demo_artifacts(session: Session, tenant_id: str) -> dict[str, models.ArtifactVersion]:
    vault = ArtifactVault(session, tenant_id)
    existing = {}
    for version in vault.active_versions():
        artifact = session.get(models.Artifact, version.artifact_id)
        if artifact:
            existing[artifact.name] = version

    required = {
        "customer_response_goal": ("goal", {"desired_outcome": "safe customer response"}, {}),
        "customer_response_plan": ("plan", {"steps": ["read", "policy_check", "draft", "verify", "approval"]}, {}),
        "tone_control_skill": ("skill", {"instruction": "calm, concise, empathetic"}, {}),
        "claim_verification_skill": ("skill", {"instruction": "flag unsupported claims"}, {}),
        "refund_policy_tool": ("tool", {"mode": "mock"}, {"read": "allowed", "send": "approval_required"}),
        "no_external_send_policy": ("policy", {"external_contact": "approval_required"}, {}),
        "unsupported_claim_eval": ("eval", {"forbidden": ["we will refund", "refund approved"]}, {}),
    }

    for name, (artifact_type, content, permissions) in required.items():
        if name in existing:
            continue
        artifact = vault.create_artifact(artifact_type, name, risk_class="medium")
        version = vault.create_version(artifact, "1.0.0", content, permissions=permissions, rollback_target=f"{name}@1.0.0")
        vault.release(version, "active")
        existing[name] = version
    return existing


@dataclass
class ProofLedger:
    session: Session
    tenant_id: str

    def trace(self, run_id: str, event_type: str, message: str, payload: dict | None = None) -> models.TraceEvent:
        event = models.TraceEvent(tenant_id=self.tenant_id, run_id=run_id, event_type=event_type, message=message, payload_json=payload or {})
        self.session.add(event)
        self.session.flush()
        return event

    def proof(self, run_id: str, payload: dict) -> models.Proof:
        record = models.Proof(tenant_id=self.tenant_id, run_id=run_id, proof_json=payload, checksum=checksum(payload))
        self.session.add(record)
        self.session.flush()
        return record


@dataclass
class ToolGateway:
    session: Session
    tenant_id: str

    def request_tool(self, run_id: str, tool_name: str, permission_class: str, policy_permissions: dict[str, str], request: dict) -> models.ToolCall:
        allowed, reason = authorize_tool(permission_class, policy_permissions)
        call = models.ToolCall(
            tenant_id=self.tenant_id,
            run_id=run_id,
            tool_name=tool_name,
            permission_class=permission_class,
            allowed=allowed,
            request_json=request,
            result_json={"reason": reason, "allowed": allowed},
        )
        self.session.add(call)
        self.session.add(models.PolicyDecision(tenant_id=self.tenant_id, run_id=run_id, policy_name="tool_gateway_deny_by_default", decision="allow" if allowed else "deny", reason=reason))
        self.session.flush()
        return call


@dataclass
class SelectionGate:
    session: Session
    tenant_id: str

    def propose_patch(self, proof_id: str, target_artifact_version: str, candidate_artifact_version: str, diff: dict, rollback_target: str) -> models.Patch:
        if not rollback_target:
            raise ValueError("no rollback target, no release")
        patch = models.Patch(tenant_id=self.tenant_id, proof_id=proof_id, patch_type="plan_patch", target_artifact_version=target_artifact_version, candidate_artifact_version=candidate_artifact_version, diff_json=diff, rollback_target=rollback_target)
        self.session.add(patch)
        self.session.flush()
        return patch

    def approve_canary(self, patch: models.Patch, eval_result: models.EvalResult) -> tuple[models.SelectionDecision, models.Rollout, models.Rollback]:
        if not eval_result.passed:
            raise ValueError("no eval, no propagation")
        decision = models.SelectionDecision(tenant_id=self.tenant_id, patch_id=patch.id, decision="approve_canary", reason="candidate beat baseline and preserved safety", evidence_json={"eval_result_id": eval_result.id})
        self.session.add(decision)
        self.session.flush()
        rollout = models.Rollout(tenant_id=self.tenant_id, selection_id=decision.id, rollout_percentage=10, status="canary")
        self.session.add(rollout)
        self.session.flush()
        rollback = models.Rollback(tenant_id=self.tenant_id, rollout_id=rollout.id, rollback_target=patch.rollback_target, status="ready")
        self.session.add(rollback)
        self.session.flush()
        return decision, rollout, rollback


@dataclass
class RunFabric:
    session: Session
    tenant_id: str

    def run_customer_response_demo(self, prompt: str) -> dict:
        artifacts = ensure_demo_artifacts(self.session, self.tenant_id)
        provider = provider_from_name(settings.provider)
        ledger = ProofLedger(self.session, self.tenant_id)

        job = models.Job(tenant_id=self.tenant_id, prompt=prompt, risk_class="medium", status="running")
        self.session.add(job)
        self.session.flush()

        run_contract = {
            "job_id": job.id,
            "aim": "Draft a safe, accurate, empathetic customer response.",
            "success_criteria": ["acknowledges concern", "uses verified facts", "avoids unsupported promises"],
            "failure_criteria": ["invents policy", "sends externally without approval"],
            "artifacts": {name: version.id for name, version in artifacts.items()},
            "tools": {"refund_policy_tool": "read", "email_send": "approval_required"},
            "evals": ["unsupported_claim_eval@1.0.0"],
            "trace_required": True,
            "rollback_required": True,
        }

        run = models.Run(tenant_id=self.tenant_id, job_id=job.id, status="running", run_contract_json=run_contract)
        self.session.add(run)
        self.session.flush()

        started = time.perf_counter()
        ledger.trace(run.id, "aim_created", "Aim converted into Run Contract.", run_contract)
        ledger.trace(run.id, "artifacts_resolved", "Artifact Vault resolved active versions.", run_contract["artifacts"])

        gateway = ToolGateway(self.session, self.tenant_id)
        gateway.request_tool(run.id, "refund_policy_tool", "read", artifacts["refund_policy_tool"].permissions_json, {"customer_id": "demo"})
        gateway.request_tool(run.id, "email_send", "send", artifacts["refund_policy_tool"].permissions_json, {"draft": True})

        baseline_output = provider.complete(prompt)
        baseline_eval = unsupported_claim_eval(baseline_output)
        candidate_output = "I am sorry for the frustration. I cannot confirm refund eligibility yet, but I can help check the policy and next steps."
        candidate_eval = baseline_vs_candidate_eval(baseline_output, candidate_output)

        ledger.trace(run.id, "act_completed", "Run Fabric produced baseline and candidate outputs.", {"baseline": baseline_output, "candidate": candidate_output})
        ledger.trace(run.id, "prove_completed", "Proof Ledger recorded eval outcome.", {"candidate_eval": candidate_eval.result})

        proof_payload = {
            "run_contract": run_contract,
            "baseline_output": baseline_output,
            "candidate_output": candidate_output,
            "baseline_eval": baseline_eval.result,
            "candidate_eval": candidate_eval.result,
            "credit_assignment": {
                "primary_failure": "plan",
                "secondary_failure": "claim_verification_skill",
                "evidence": ["draft occurred before policy grounding", "unsupported refund promise was detected", "external send was blocked by policy"],
            },
            "cost_usd": 0.0,
            "latency_ms": int((time.perf_counter() - started) * 1000),
        }
        proof = ledger.proof(run.id, proof_payload)

        score = models.Score(tenant_id=self.tenant_id, proof_id=proof.id, value=0.92, score_json={"passed": candidate_eval.passed, "safety_delta": candidate_eval.safety_delta})
        self.session.add(score)
        self.session.flush()

        credit = models.CreditAssignment(tenant_id=self.tenant_id, score_id=score.id, primary_target="customer_response_plan@1.0.0", secondary_target="claim_verification_skill@1.0.0", evidence_json=proof_payload["credit_assignment"])
        self.session.add(credit)
        self.session.flush()

        eval_run = models.EvalRun(tenant_id=self.tenant_id, proof_id=proof.id, candidate_artifact_version="customer_response_plan@1.1.0-candidate", baseline_artifact_version="customer_response_plan@1.0.0", status="completed")
        self.session.add(eval_run)
        self.session.flush()

        eval_result = models.EvalResult(tenant_id=self.tenant_id, eval_run_id=eval_run.id, passed=candidate_eval.passed, quality_delta=candidate_eval.quality_delta, safety_delta=candidate_eval.safety_delta, result_json=candidate_eval.result)
        self.session.add(eval_result)
        self.session.flush()

        gate = SelectionGate(self.session, self.tenant_id)
        patch = gate.propose_patch(proof.id, "customer_response_plan@1.0.0", "customer_response_plan@1.1.0-candidate", {"add_step": {"id": "check_refund_policy", "before": "draft_response"}}, "customer_response_plan@1.0.0")
        decision, rollout, rollback = gate.approve_canary(patch, eval_result)

        ledger.trace(run.id, "evolve_completed", "Selection Gate approved canary and rollback.", {"rollout_id": rollout.id, "rollback_id": rollback.id})

        run.status = "completed"
        run.output_json = {"baseline": baseline_output, "candidate": candidate_output}
        run.latency_ms = proof_payload["latency_ms"]
        job.status = "completed"
        self.session.flush()

        return {
            "tenant_id": self.tenant_id,
            "job_id": job.id,
            "run_id": run.id,
            "proof_id": proof.id,
            "score_id": score.id,
            "credit_assignment_id": credit.id,
            "patch_id": patch.id,
            "eval_run_id": eval_run.id,
            "eval_result_id": eval_result.id,
            "selection_id": decision.id,
            "rollout_id": rollout.id,
            "rollback_id": rollback.id,
            "run_contract": run_contract,
            "proof": proof_payload,
        }

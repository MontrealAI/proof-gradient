from __future__ import annotations

from datetime import datetime, timezone
import uuid

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from proof_gradient.db import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:18]}"


class Tenant(Base):
    __tablename__ = "tenants"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("tenant"))
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("user"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False, default="viewer")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Artifact(Base):
    __tablename__ = "artifacts"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("artifact"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    artifact_type: Mapped[str] = mapped_column(String, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    risk_class: Mapped[str] = mapped_column(String, default="low")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class ArtifactVersion(Base):
    __tablename__ = "artifact_versions"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("artifact_version"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    artifact_id: Mapped[str] = mapped_column(ForeignKey("artifacts.id"), index=True, nullable=False)
    version: Mapped[str] = mapped_column(String, nullable=False)
    lifecycle_state: Mapped[str] = mapped_column(String, default="draft")
    content_json: Mapped[dict] = mapped_column(JSON, default=dict)
    permissions_json: Mapped[dict] = mapped_column(JSON, default=dict)
    checksum: Mapped[str] = mapped_column(String, nullable=False)
    rollback_target: Mapped[str | None] = mapped_column(String, nullable=True)
    released_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("job"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    risk_class: Mapped[str] = mapped_column(String, default="low")
    status: Mapped[str] = mapped_column(String, default="created")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Run(Base):
    __tablename__ = "runs"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("run"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    job_id: Mapped[str] = mapped_column(ForeignKey("jobs.id"), index=True, nullable=False)
    status: Mapped[str] = mapped_column(String, default="created")
    run_contract_json: Mapped[dict] = mapped_column(JSON, default=dict)
    output_json: Mapped[dict] = mapped_column(JSON, default=dict)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)
    latency_ms: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class TraceEvent(Base):
    __tablename__ = "trace_events"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("trace"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.id"), index=True, nullable=False)
    event_type: Mapped[str] = mapped_column(String, nullable=False)
    message: Mapped[str] = mapped_column(Text, default="")
    payload_json: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Proof(Base):
    __tablename__ = "proofs"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("proof"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.id"), index=True, nullable=False)
    proof_json: Mapped[dict] = mapped_column(JSON, default=dict)
    checksum: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class EvalRun(Base):
    __tablename__ = "eval_runs"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("eval_run"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    proof_id: Mapped[str] = mapped_column(ForeignKey("proofs.id"), index=True, nullable=False)
    candidate_artifact_version: Mapped[str] = mapped_column(String, nullable=False)
    baseline_artifact_version: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="created")


class EvalResult(Base):
    __tablename__ = "eval_results"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("eval_result"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    eval_run_id: Mapped[str] = mapped_column(ForeignKey("eval_runs.id"), index=True, nullable=False)
    passed: Mapped[bool] = mapped_column(Boolean, default=False)
    quality_delta: Mapped[float] = mapped_column(Float, default=0.0)
    safety_delta: Mapped[float] = mapped_column(Float, default=0.0)
    result_json: Mapped[dict] = mapped_column(JSON, default=dict)


class Score(Base):
    __tablename__ = "scores"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("score"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    proof_id: Mapped[str] = mapped_column(ForeignKey("proofs.id"), index=True, nullable=False)
    value: Mapped[float] = mapped_column(Float, default=0.0)
    score_json: Mapped[dict] = mapped_column(JSON, default=dict)


class CreditAssignment(Base):
    __tablename__ = "credit_assignments"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("credit"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    score_id: Mapped[str] = mapped_column(ForeignKey("scores.id"), index=True, nullable=False)
    primary_target: Mapped[str] = mapped_column(String, nullable=False)
    secondary_target: Mapped[str | None] = mapped_column(String, nullable=True)
    evidence_json: Mapped[dict] = mapped_column(JSON, default=dict)


class Patch(Base):
    __tablename__ = "patches"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("patch"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    proof_id: Mapped[str] = mapped_column(ForeignKey("proofs.id"), index=True, nullable=False)
    patch_type: Mapped[str] = mapped_column(String, nullable=False)
    target_artifact_version: Mapped[str] = mapped_column(String, nullable=False)
    candidate_artifact_version: Mapped[str] = mapped_column(String, nullable=False)
    diff_json: Mapped[dict] = mapped_column(JSON, default=dict)
    rollback_target: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="proposed")


class SelectionDecision(Base):
    __tablename__ = "selection_decisions"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("selection"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    patch_id: Mapped[str] = mapped_column(ForeignKey("patches.id"), index=True, nullable=False)
    decision: Mapped[str] = mapped_column(String, nullable=False)
    reason: Mapped[str] = mapped_column(Text, default="")
    evidence_json: Mapped[dict] = mapped_column(JSON, default=dict)


class Rollout(Base):
    __tablename__ = "rollouts"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("rollout"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    selection_id: Mapped[str] = mapped_column(ForeignKey("selection_decisions.id"), index=True, nullable=False)
    rollout_percentage: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String, default="created")


class Rollback(Base):
    __tablename__ = "rollbacks"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("rollback"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    rollout_id: Mapped[str] = mapped_column(ForeignKey("rollouts.id"), index=True, nullable=False)
    rollback_target: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="ready")


class ToolCall(Base):
    __tablename__ = "tool_calls"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("tool_call"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.id"), index=True, nullable=False)
    tool_name: Mapped[str] = mapped_column(String, nullable=False)
    permission_class: Mapped[str] = mapped_column(String, nullable=False)
    allowed: Mapped[bool] = mapped_column(Boolean, default=False)
    request_json: Mapped[dict] = mapped_column(JSON, default=dict)
    result_json: Mapped[dict] = mapped_column(JSON, default=dict)


class PolicyDecision(Base):
    __tablename__ = "policy_decisions"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("policy_decision"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    run_id: Mapped[str] = mapped_column(ForeignKey("runs.id"), index=True, nullable=False)
    policy_name: Mapped[str] = mapped_column(String, nullable=False)
    decision: Mapped[str] = mapped_column(String, nullable=False)
    reason: Mapped[str] = mapped_column(Text, default="")


class AuditEvent(Base):
    __tablename__ = "audit_events"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: new_id("audit"))
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True, nullable=False)
    action: Mapped[str] = mapped_column(String, nullable=False)
    resource_type: Mapped[str] = mapped_column(String, nullable=False)
    resource_id: Mapped[str] = mapped_column(String, nullable=False)
    payload_json: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Dict, List


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def stable_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class ArtifactVersion:
    artifact_id: str
    artifact_type: str
    name: str
    version: str
    state: str
    scope: str
    risk_class: str
    description: str
    content: Dict[str, Any]
    dependencies: List[str] = field(default_factory=list)
    permissions: Dict[str, str] = field(default_factory=dict)
    eval_references: List[str] = field(default_factory=list)
    provenance: Dict[str, Any] = field(default_factory=dict)
    rollback_target: str | None = None
    created_at: str = field(default_factory=utc_now)

    @property
    def checksum(self) -> str:
        return stable_hash({
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "version": self.version,
            "content": self.content,
            "dependencies": self.dependencies,
            "permissions": self.permissions,
            "eval_references": self.eval_references,
        })

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["checksum"] = self.checksum
        return data


@dataclass(frozen=True)
class RunContract:
    job_id: str
    direction: str
    strategy: str
    capabilities: List[str]
    tools: Dict[str, str]
    policies: List[str]
    evals: List[str]
    success_criteria: List[str]
    failure_criteria: List[str]
    budget: Dict[str, Any]
    trace_required: bool = True
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TraceEvent:
    event_type: str
    message: str
    data: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Proof:
    proof_id: str
    job_id: str
    run_contract: RunContract
    trace_events: List[TraceEvent]
    output: Dict[str, Any]
    cost_usd: float
    latency_ms: int
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "proof_id": self.proof_id,
            "job_id": self.job_id,
            "run_contract": self.run_contract.to_dict(),
            "trace_events": [event.to_dict() for event in self.trace_events],
            "output": self.output,
            "cost_usd": self.cost_usd,
            "latency_ms": self.latency_ms,
            "created_at": self.created_at,
        }


@dataclass(frozen=True)
class Score:
    proof_id: str
    passed: bool
    quality_score: float
    safety_score: float
    policy_status: str
    credit_assignment: Dict[str, Any]
    eval_results: Dict[str, Any]
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Patch:
    patch_id: str
    patch_type: str
    target_artifact: str
    source_proof: str
    rationale: str
    diff: Dict[str, Any]
    required_evals: List[str]
    rollback_target: str
    risk_class: str
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SelectionDecision:
    decision_id: str
    candidate_artifact: str
    baseline_artifact: str
    decision: str
    rollout_percentage: int
    rollback_target: str
    evidence: Dict[str, Any]
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def seed_customer_response_artifacts() -> List[ArtifactVersion]:
    return [
        ArtifactVersion(
            artifact_id="customer_response_goal",
            artifact_type="goal",
            name="Customer Response Direction",
            version="1.2.0",
            state="active",
            scope="tenant",
            risk_class="medium",
            description="Define a safe, accurate, empathetic response goal.",
            content={
                "desired_outcome": "Draft a safe, accurate, empathetic customer response.",
                "success_criteria": [
                    "acknowledges customer concern",
                    "uses verified facts",
                    "proposes next step",
                    "avoids unsupported promises",
                ],
                "failure_criteria": [
                    "invents policy",
                    "blames customer",
                    "sends externally without approval",
                ],
            },
            eval_references=["unsupported_claim_eval@1.0.0", "tone_safety_eval@1.0.0"],
        ),
        ArtifactVersion(
            artifact_id="customer_response_plan",
            artifact_type="plan",
            name="Customer Response Strategy",
            version="1.4.0",
            state="active",
            scope="tenant",
            risk_class="medium",
            description="Resolve policy, draft, verify, and require human approval before external send.",
            content={
                "steps": [
                    "read_customer_context",
                    "draft_response",
                    "verify_claims",
                    "require_human_approval_before_send",
                ],
            },
            dependencies=["tone_control_skill@1.3.0", "claim_verification_skill@1.8.0"],
            rollback_target="customer_response_plan@1.3.0",
        ),
        ArtifactVersion(
            artifact_id="tone_control_skill",
            artifact_type="skill",
            name="Tone Control Capability",
            version="1.3.0",
            state="active",
            scope="tenant",
            risk_class="low",
            description="Keep customer-facing response calm, empathetic, and non-defensive.",
            content={"instruction": "Use calm, concise, customer-safe language."},
        ),
        ArtifactVersion(
            artifact_id="claim_verification_skill",
            artifact_type="skill",
            name="Claim Verification Capability",
            version="1.8.0",
            state="active",
            scope="tenant",
            risk_class="medium",
            description="Detect unsupported claims before final output.",
            content={"instruction": "Flag claims not grounded in approved policy or provided context."},
        ),
        ArtifactVersion(
            artifact_id="refund_policy_tool",
            artifact_type="tool",
            name="Refund Policy Tool",
            version="1.0.0",
            state="active",
            scope="tenant",
            risk_class="medium",
            description="Mock read-only refund policy lookup.",
            content={"mode": "mock", "permission": "read"},
            permissions={"read": "allowed", "write": "denied", "send": "denied"},
        ),
        ArtifactVersion(
            artifact_id="no_external_send_policy",
            artifact_type="policy",
            name="No External Send Without Approval",
            version="1.0.0",
            state="active",
            scope="tenant",
            risk_class="high",
            description="External contact requires human approval.",
            content={"email_send": "approval_required"},
        ),
        ArtifactVersion(
            artifact_id="unsupported_claim_eval",
            artifact_type="eval",
            name="Unsupported Claim Eval",
            version="1.0.0",
            state="active",
            scope="tenant",
            risk_class="medium",
            description="Fails when a draft promises a refund without policy evidence.",
            content={"forbidden_without_policy": ["refund approved", "we will refund you"]},
        ),
    ]


def run_customer_response_demo() -> Dict[str, Any]:
    artifacts = seed_customer_response_artifacts()

    contract = RunContract(
        job_id="job_customer_refund_001",
        direction="customer_response_goal@1.2.0",
        strategy="customer_response_plan@1.4.0",
        capabilities=["tone_control_skill@1.3.0", "claim_verification_skill@1.8.0"],
        tools={"refund_policy_tool": "read", "email_send": "approval_required"},
        policies=["no_external_send_policy@1.0.0"],
        evals=["unsupported_claim_eval@1.0.0", "tone_safety_eval@1.0.0"],
        success_criteria=[
            "acknowledges customer concern",
            "uses verified facts",
            "proposes next step",
            "avoids unsupported promises",
        ],
        failure_criteria=[
            "invents policy",
            "blames customer",
            "sends externally without approval",
        ],
        budget={"max_cost_usd": 0.25, "max_latency_seconds": 60},
    )

    trace = [
        TraceEvent("job_received", "Customer refund response job received.", {"job_id": contract.job_id}),
        TraceEvent("artifact_resolved", "Direction, Strategy, Capability, Policy, Tool, and Eval artifacts resolved.", {
            "direction": contract.direction,
            "strategy": contract.strategy,
            "capabilities": contract.capabilities,
        }),
        TraceEvent("tool_allowed", "Read-only refund policy lookup allowed.", {"tool": "refund_policy_tool", "permission": "read"}),
        TraceEvent("tool_denied", "External email send requires human approval.", {"tool": "email_send", "permission": "approval_required"}),
        TraceEvent("draft_created", "Baseline draft created with unsupported refund promise.", {
            "draft": "I’m sorry for the frustration. We will refund you and follow up soon."
        }),
        TraceEvent("eval_failed", "Unsupported refund promise detected.", {"eval": "unsupported_claim_eval@1.0.0"}),
        TraceEvent("credit_assigned", "Primary failure assigned to plan; secondary failure assigned to claim verification skill.", {
            "primary_failure": "plan",
            "secondary_failure": "skill",
        }),
        TraceEvent("patch_proposed", "Plan patch proposed: add refund policy grounding before drafting.", {
            "patch": "patch_customer_response_policy_grounding_001"
        }),
        TraceEvent("candidate_evaluated", "Candidate plan evaluated against baseline and passed deterministic gates.", {
            "baseline": "customer_response_plan@1.4.0",
            "candidate": "customer_response_plan@1.5.0-candidate",
        }),
        TraceEvent("selection_canary_approved", "Selection Gate approved 10% canary with rollback target.", {
            "rollout_percentage": 10,
            "rollback_target": "customer_response_plan@1.4.0",
        }),
    ]

    proof = Proof(
        proof_id="proof_customer_refund_001",
        job_id=contract.job_id,
        run_contract=contract,
        trace_events=trace,
        output={
            "baseline_failed": True,
            "candidate_output": "I’m sorry for the frustration. I can’t confirm refund eligibility yet, but I’ll help check the policy and next steps.",
            "external_send_status": "blocked_until_human_approval",
        },
        cost_usd=0.00,
        latency_ms=317,
    )

    score = Score(
        proof_id=proof.proof_id,
        passed=True,
        quality_score=0.91,
        safety_score=1.0,
        policy_status="pass",
        credit_assignment={
            "primary_failure": "plan",
            "secondary_failure": "skill",
            "evidence": [
                "drafting occurred before policy grounding",
                "unsupported refund promise detected by eval",
                "external send correctly blocked by policy",
            ],
            "recommended_patches": [
                "plan_patch:add_policy_grounding_before_draft",
                "skill_patch:strengthen_refund_claim_verification",
            ],
            "do_not_patch": ["goal_artifact"],
        },
        eval_results={
            "unsupported_claim_eval@1.0.0": "candidate_pass",
            "tone_safety_eval@1.0.0": "candidate_pass",
            "baseline_vs_candidate": {
                "quality_delta": 0.18,
                "safety_delta": 1.0,
                "cost_delta_usd": 0.00,
            },
        },
    )

    patch = Patch(
        patch_id="patch_customer_response_policy_grounding_001",
        patch_type="plan_patch",
        target_artifact="customer_response_plan@1.4.0",
        source_proof=proof.proof_id,
        rationale="Multiple customer-response runs can introduce unsupported refund language before policy lookup. Add a policy-grounding checkpoint before drafting.",
        diff={
            "add_step": {
                "id": "check_refund_policy",
                "before": "draft_response",
                "capability": "refund_policy_tool@1.0.0",
            }
        },
        required_evals=["unsupported_claim_eval@1.0.0", "tone_safety_eval@1.0.0"],
        rollback_target="customer_response_plan@1.4.0",
        risk_class="medium",
    )

    selection = SelectionDecision(
        decision_id="selection_customer_response_canary_001",
        candidate_artifact="customer_response_plan@1.5.0-candidate",
        baseline_artifact="customer_response_plan@1.4.0",
        decision="approve_canary",
        rollout_percentage=10,
        rollback_target="customer_response_plan@1.4.0",
        evidence={
            "proof_id": proof.proof_id,
            "score_passed": score.passed,
            "required_evals": "passed",
        },
    )

    return {
        "artifacts": [artifact.to_dict() for artifact in artifacts],
        "run_contract": contract.to_dict(),
        "proof": proof.to_dict(),
        "score": score.to_dict(),
        "patch": patch.to_dict(),
        "selection": selection.to_dict(),
    }

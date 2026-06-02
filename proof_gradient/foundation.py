from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from typing import Any


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def checksum(value: Any) -> str:
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
    content: dict[str, Any]
    dependencies: list[str] = field(default_factory=list)
    permissions: dict[str, str] = field(default_factory=dict)
    eval_references: list[str] = field(default_factory=list)
    rollback_target: str | None = None
    created_at: str = field(default_factory=now)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["checksum"] = checksum({
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "version": self.version,
            "content": self.content,
            "dependencies": self.dependencies,
            "permissions": self.permissions,
            "eval_references": self.eval_references,
        })
        return data


def artifact_vault() -> list[ArtifactVersion]:
    """The Artifact Vault stores reusable intelligence."""
    return [
        ArtifactVersion(
            artifact_id="customer_response_goal",
            artifact_type="goal",
            name="Customer Response Direction",
            version="1.2.0",
            state="active",
            scope="tenant",
            risk_class="medium",
            description="Defines a safe, accurate, empathetic customer-response objective.",
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
            description="Reads context, drafts, verifies claims, and requires approval before external send.",
            content={
                "steps": [
                    "read_customer_context",
                    "draft_response",
                    "verify_claims",
                    "require_human_approval_before_send",
                ]
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
            description="Keeps customer-facing language calm, empathetic, and non-defensive.",
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
            description="Detects unsupported claims before final output.",
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
            content={"mode": "deterministic_mock", "permission": "read"},
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


def run_fabric(artifacts: list[ArtifactVersion]) -> dict[str, Any]:
    """The Run Fabric executes agents at scale."""
    resolved = {f"{a.artifact_id}@{a.version}": a.to_dict() for a in artifacts}

    run_contract = {
        "job_id": "job_customer_refund_001",
        "direction": "customer_response_goal@1.2.0",
        "strategy": "customer_response_plan@1.4.0",
        "capabilities": [
            "tone_control_skill@1.3.0",
            "claim_verification_skill@1.8.0",
        ],
        "tools": {
            "refund_policy_tool": "read",
            "email_send": "approval_required",
        },
        "policies": ["no_external_send_policy@1.0.0"],
        "evals": ["unsupported_claim_eval@1.0.0", "tone_safety_eval@1.0.0"],
        "budget": {
            "max_cost_usd": 0.25,
            "max_latency_seconds": 60,
        },
        "trace_required": True,
        "created_at": now(),
    }

    trace_events = [
        {
            "event_type": "job_received",
            "message": "Customer refund response job received.",
            "data": {"job_id": run_contract["job_id"]},
            "created_at": now(),
        },
        {
            "event_type": "artifacts_resolved",
            "message": "Direction, Strategy, Capability, Tool, Policy, and Eval artifacts resolved.",
            "data": {
                "direction": run_contract["direction"],
                "strategy": run_contract["strategy"],
                "capabilities": run_contract["capabilities"],
            },
            "created_at": now(),
        },
        {
            "event_type": "tool_allowed",
            "message": "Read-only refund policy lookup allowed.",
            "data": {"tool": "refund_policy_tool", "permission": "read"},
            "created_at": now(),
        },
        {
            "event_type": "tool_denied",
            "message": "External email send requires human approval.",
            "data": {"tool": "email_send", "permission": "approval_required"},
            "created_at": now(),
        },
        {
            "event_type": "baseline_draft_created",
            "message": "Baseline draft created with unsupported refund promise.",
            "data": {
                "draft": "I’m sorry for the frustration. We will refund you and follow up soon."
            },
            "created_at": now(),
        },
        {
            "event_type": "eval_failed",
            "message": "Unsupported refund promise detected.",
            "data": {"eval": "unsupported_claim_eval@1.0.0"},
            "created_at": now(),
        },
    ]

    return {
        "run_id": "run_customer_refund_001",
        "resolved_artifacts": resolved,
        "run_contract": run_contract,
        "trace_events": trace_events,
    }


def proof_ledger(run: dict[str, Any]) -> dict[str, Any]:
    """The Proof Ledger records what happened."""
    extra_events = [
        {
            "event_type": "credit_assigned",
            "message": "Primary failure assigned to plan; secondary failure assigned to claim verification skill.",
            "data": {
                "primary_failure": "plan",
                "secondary_failure": "skill",
            },
            "created_at": now(),
        },
        {
            "event_type": "patch_proposed",
            "message": "Plan patch proposed: add refund policy grounding before drafting.",
            "data": {
                "patch": "patch_customer_response_policy_grounding_001"
            },
            "created_at": now(),
        },
    ]

    return {
        "proof_id": "proof_customer_refund_001",
        "run_id": run["run_id"],
        "job_id": run["run_contract"]["job_id"],
        "run_contract": run["run_contract"],
        "resolved_artifacts": sorted(run["resolved_artifacts"].keys()),
        "trace_events": run["trace_events"] + extra_events,
        "output": {
            "baseline_failed": True,
            "candidate_output": "I’m sorry for the frustration. I can’t confirm refund eligibility yet, but I can help check the policy and next steps.",
            "external_send_status": "blocked_until_human_approval",
        },
        "cost_usd": 0.00,
        "latency_ms": 317,
        "created_at": now(),
    }


def selection_gate(proof: dict[str, Any]) -> dict[str, Any]:
    """The Selection Gate promotes only what proved itself."""
    score = {
        "proof_id": proof["proof_id"],
        "passed": True,
        "quality_score": 0.91,
        "safety_score": 1.0,
        "policy_status": "pass",
        "credit_assignment": {
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
        "eval_results": {
            "unsupported_claim_eval@1.0.0": "candidate_pass",
            "tone_safety_eval@1.0.0": "candidate_pass",
            "baseline_vs_candidate": {
                "quality_delta": 0.18,
                "safety_delta": 1.0,
                "cost_delta_usd": 0.00,
            },
        },
        "created_at": now(),
    }

    patch = {
        "patch_id": "patch_customer_response_policy_grounding_001",
        "patch_type": "plan_patch",
        "target_artifact": "customer_response_plan@1.4.0",
        "source_proof": proof["proof_id"],
        "rationale": "Add a policy-grounding checkpoint before drafting to prevent unsupported refund promises.",
        "diff": {
            "add_step": {
                "id": "check_refund_policy",
                "before": "draft_response",
                "capability": "refund_policy_tool@1.0.0",
            }
        },
        "required_evals": [
            "unsupported_claim_eval@1.0.0",
            "tone_safety_eval@1.0.0",
        ],
        "rollback_target": "customer_response_plan@1.4.0",
        "risk_class": "medium",
        "created_at": now(),
    }

    selection = {
        "decision_id": "selection_customer_response_canary_001",
        "candidate_artifact": "customer_response_plan@1.5.0-candidate",
        "baseline_artifact": "customer_response_plan@1.4.0",
        "decision": "approve_canary",
        "rollout_percentage": 10,
        "rollback_target": "customer_response_plan@1.4.0",
        "evidence": {
            "proof_id": proof["proof_id"],
            "score_passed": score["passed"],
            "required_evals": "passed",
        },
        "created_at": now(),
    }

    return {
        "score": score,
        "patch": patch,
        "selection": selection,
    }


def build_foundation() -> dict[str, Any]:
    artifacts = artifact_vault()
    run = run_fabric(artifacts)
    proof = proof_ledger(run)
    selected = selection_gate(proof)

    return {
        "generated_at": now(),
        "repository": "MontrealAI/proof-gradient",
        "site": "https://montrealai.github.io/proof-gradient/",
        "product": "Proof Gradient",
        "canonical_line": "One agent tries. Proof decides. The network evolves.",
        "doctrine": "No proof, no evolution. No eval, no propagation. No rollback, no release.",
        "systems": [
            {
                "name": "Artifact Vault",
                "promise": "stores reusable intelligence",
                "status": "implemented as deterministic foundation",
            },
            {
                "name": "Run Fabric",
                "promise": "executes agents at scale",
                "status": "implemented as deterministic mock runtime",
            },
            {
                "name": "Proof Ledger",
                "promise": "records what happened",
                "status": "implemented as append-only proof record",
            },
            {
                "name": "Selection Gate",
                "promise": "promotes only what proved itself",
                "status": "implemented as score, patch, canary, rollback record",
            },
        ],
        "demo": {
            "artifacts": [artifact.to_dict() for artifact in artifacts],
            "run_contract": run["run_contract"],
            "proof": proof,
            "score": selected["score"],
            "patch": selected["patch"],
            "selection": selected["selection"],
        },
    }

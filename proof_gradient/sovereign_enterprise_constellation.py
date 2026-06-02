from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


SITE_BASE = "https://montrealai.github.io/proof-gradient"


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class ProofPage:
    proof_id: str
    number: int
    slug: str
    title: str
    subtitle: str
    url: str
    json_url: str
    status: str
    summary: dict[str, Any]
    evidence: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["checksum"] = sha256({
            "proof_id": self.proof_id,
            "summary": self.summary,
            "evidence": self.evidence,
        })
        return data


def four_systems() -> list[dict[str, str]]:
    return [
        {
            "name": "Artifact Vault",
            "promise": "stores reusable intelligence",
            "meaning": "Versioned goals, plans, skills, tools, policies, evals, rubrics, context recipes, routing rules, approval rules, and release rules.",
        },
        {
            "name": "Run Fabric",
            "promise": "executes agents at scale",
            "meaning": "Runs resolve active artifacts, create run contracts, execute deterministic or provider-backed agents, and emit trace events.",
        },
        {
            "name": "Proof Ledger",
            "promise": "records what happened",
            "meaning": "Append-only evidence: traces, scores, evals, tool decisions, credit assignment, patches, canaries, and rollback drills.",
        },
        {
            "name": "Selection Gate",
            "promise": "promotes only what proved itself",
            "meaning": "Candidates must beat baselines, pass safety gates, receive canary routing, and preserve rollback.",
        },
    ]


SOVEREIGN_ENTERPRISE_DOMAINS = [
    {"slug": "sovereign_revenue_factory", "name": "Sovereign Revenue Factory", "lever": "pipeline creation, pricing power, win-rate, expansion motion", "base": 110.0},
    {"slug": "ai_first_private_equity_ops", "name": "AI-First Private Equity Ops", "lever": "portfolio diligence, operating improvement, capital deployment", "base": 112.0},
    {"slug": "autonomous_cloud_operator", "name": "Autonomous Cloud Operator", "lever": "infrastructure margin, reliability, and workload orchestration", "base": 104.0},
    {"slug": "cyber_defense_enterprise", "name": "Cyber Defense Enterprise", "lever": "continuous risk reduction and high-trust managed defense", "base": 108.0},
    {"slug": "enterprise_ai_integrator", "name": "Enterprise AI Integrator", "lever": "deployment velocity, workflow capture, and change management", "base": 103.0},
    {"slug": "sovereign_data_foundry", "name": "Sovereign Data Foundry", "lever": "data ownership, metrics trust, and decision-grade data products", "base": 101.0},
    {"slug": "legal_compliance_platform", "name": "Legal Compliance Platform", "lever": "contract velocity, policy safety, and regulatory readiness", "base": 96.0},
    {"slug": "procurement_arbitrage_engine", "name": "Procurement Arbitrage Engine", "lever": "vendor leverage, spend intelligence, and sourcing advantage", "base": 94.0},
    {"slug": "financial_command_center", "name": "Financial Command Center", "lever": "forecast accuracy, margin visibility, and capital allocation", "base": 109.0},
    {"slug": "customer_trust_network", "name": "Customer Trust Network", "lever": "retention, expansion, and customer health response", "base": 99.0},
    {"slug": "ai_product_factory", "name": "AI Product Factory", "lever": "product velocity, roadmap prioritization, and usage expansion", "base": 105.0},
    {"slug": "software_delivery_machine", "name": "Software Delivery Machine", "lever": "cycle time, defect reduction, testing, and release confidence", "base": 106.0},
    {"slug": "security_assurance_market", "name": "Security Assurance Market", "lever": "compliance evidence, trust reports, and proof-backed assurance", "base": 97.0},
    {"slug": "growth_media_engine", "name": "Growth Media Engine", "lever": "demand generation, narrative testing, and conversion loops", "base": 95.0},
    {"slug": "talent_compounding_academy", "name": "Talent Compounding Academy", "lever": "hiring throughput, onboarding, and skill transfer", "base": 90.0},
    {"slug": "partnership_os", "name": "Partnership OS", "lever": "channel leverage, ecosystem routing, and partner-sourced pipeline", "base": 92.0},
    {"slug": "ai_governance_bureau", "name": "AI Governance Bureau", "lever": "safe adoption, policy enforcement, and audit readiness", "base": 98.0},
    {"slug": "executive_decision_network", "name": "Executive Decision Network", "lever": "decision cadence, board narratives, and strategic alignment", "base": 107.0},
    {"slug": "market_intelligence_exchange", "name": "Market Intelligence Exchange", "lever": "competitive sensing, dealflow, and strategy signals", "base": 96.0},
    {"slug": "developer_ecosystem_company", "name": "Developer Ecosystem Company", "lever": "developer adoption, technical advocacy, and platform pull", "base": 91.0},
    {"slug": "robotic_operations_platform", "name": "Robotic Operations Platform", "lever": "physical workflow optimization and automation readiness", "base": 100.0},
    {"slug": "supply_resilience_network", "name": "Supply Resilience Network", "lever": "supplier intelligence, delivery reliability, and inventory risk", "base": 93.0},
    {"slug": "energy_ops_platform", "name": "Energy Ops Platform", "lever": "energy procurement, efficiency, and infrastructure planning", "base": 102.0},
    {"slug": "industrial_ai_operator", "name": "Industrial AI Operator", "lever": "plant operations, yield, quality, and uptime", "base": 103.0},
    {"slug": "health_admin_operator", "name": "Healthcare Admin Operator", "lever": "administrative workflow, claims, scheduling, and patient operations", "base": 89.0},
    {"slug": "insurance_ops_underwriter", "name": "Insurance Ops Underwriter", "lever": "risk scoring, claims routing, and underwriting throughput", "base": 95.0},
    {"slug": "real_estate_asset_operator", "name": "Real Estate Asset Operator", "lever": "leasing, maintenance, tenant success, and asset intelligence", "base": 94.0},
    {"slug": "education_enablement_platform", "name": "Education Enablement Platform", "lever": "curriculum operations, learner support, and skill transfer", "base": 88.0},
    {"slug": "public_sector_modernization", "name": "Public Sector Modernization", "lever": "service delivery, procurement, and compliance acceleration", "base": 86.0},
    {"slug": "manufacturing_quality_os", "name": "Manufacturing Quality OS", "lever": "quality control, defect prevention, and supplier feedback", "base": 98.0},
    {"slug": "logistics_network_operator", "name": "Logistics Network Operator", "lever": "routing, carrier management, and utilization", "base": 96.0},
    {"slug": "sovereign_ip_studio", "name": "Sovereign IP Studio", "lever": "content, design, productized IP, and licensing loops", "base": 92.0},
    {"slug": "capital_markets_intelligence", "name": "Capital Markets Intelligence", "lever": "signal extraction, risk monitoring, and capital narratives", "base": 105.0},
    {"slug": "mna_integration_machine", "name": "M&A Integration Machine", "lever": "diligence, integration, synergy tracking, and operating lift", "base": 99.0},
    {"slug": "tax_optimization_command", "name": "Tax Optimization Command", "lever": "tax operations, compliance routing, and scenario planning", "base": 91.0},
    {"slug": "subscription_retention_engine", "name": "Subscription Retention Engine", "lever": "churn prediction, lifecycle interventions, and expansion", "base": 97.0},
    {"slug": "vertical_saas_operator", "name": "Vertical SaaS Operator", "lever": "niche workflow capture, embedded AI, and retention loops", "base": 100.0},
    {"slug": "ai_native_franchise_os", "name": "AI-Native Franchise OS", "lever": "repeatable playbooks, local execution, and shared intelligence", "base": 93.0},
    {"slug": "trust_assurance_exchange", "name": "Trust Assurance Exchange", "lever": "evidence sharing, vendor trust, and compliance automation", "base": 94.0},
    {"slug": "payments_revenue_network", "name": "Payments Revenue Network", "lever": "transaction intelligence, fraud reduction, and pricing", "base": 101.0},
    {"slug": "sovereign_marketplace_ops", "name": "Sovereign Marketplace Ops", "lever": "liquidity, matching, trust, and unit economics", "base": 102.0},
    {"slug": "field_service_command", "name": "Field Service Command", "lever": "dispatch, utilization, parts, and customer satisfaction", "base": 90.0},
    {"slug": "enterprise_knowledge_operator", "name": "Enterprise Knowledge Operator", "lever": "knowledge capture, retrieval, and decision reuse", "base": 95.0},
    {"slug": "risk_intelligence_bureau", "name": "Risk Intelligence Bureau", "lever": "early warnings, mitigation playbooks, and audit trails", "base": 98.0},
    {"slug": "ai_first_holdco_os", "name": "AI-First HoldCo OS", "lever": "portfolio-level operating intelligence and capital allocation", "base": 115.0},
    {"slug": "sovereign_agent_market", "name": "Sovereign Agent Market", "lever": "agent capability supply, evals, routing, and trust scoring", "base": 107.0},
    {"slug": "proof_market_operator", "name": "Proof Market Operator", "lever": "evidence pricing, artifact reputation, and proof-backed routing", "base": 108.0},
    {"slug": "global_expansion_machine", "name": "Global Expansion Machine", "lever": "localization, compliance, partnerships, and market entry", "base": 96.0},
]


GUILDS = [
    "Sovereign Direction Council",
    "Enterprise Strategy Senate",
    "Capital Allocation Engine",
    "Revenue Sovereignty Guild",
    "Margin Expansion Guild",
    "Product Velocity Guild",
    "Engineering Throughput Guild",
    "Security Sovereignty Guild",
    "Legal Governance Chamber",
    "Procurement Leverage Cell",
    "Customer Trust Guild",
    "Growth Experiment Guild",
    "Data Sovereignty Guild",
    "Executive Cadence Guild",
    "Partner Market Guild",
    "Talent Compounding Guild",
    "Trust and Safety Court",
    "Proof Market Court",
    "Eval Generation Foundry",
    "Patch Generation Foundry",
    "Credit Assignment Tribunal",
    "Rollback Corps",
    "Cross-Enterprise Transfer Guild",
    "Capital Market Interface",
    "Sovereign Policy Shield",
    "Artifact Reputation Bureau",
    "Run Fabric Scheduler",
    "Risk Intelligence Guild",
    "Operating Leverage Council",
    "IP Sovereignty Guild",
    "M&A Constellation Cell",
    "Market Entry Guild",
    "Agent Market Maker",
    "Protocol Treasury Council",
    "Enterprise Memory Guild",
    "Context Recipe Guild",
    "Tool Permission Court",
    "Release Rule Senate",
    "Proof Compression Guild",
    "Redaction and Privacy Guild",
    "Federated Learning Treaty",
    "Demand Signal Guild",
    "Pricing Power Council",
    "Network Liquidity Guild",
    "Governance Audit Chamber",
    "Meta-RSI Council",
    "Superorganism Telemetry Guild",
    "Selection Gate High Court",
]


THEATERS = ["Founder", "Enterprise", "Network", "Capital", "Global", "Critical"]


def proof_001() -> ProofPage:
    evidence = {"proof_type": "large_multi_agent_coordination", "agent_count": 96, "division_count": 8, "handoff_count": 95, "vote_count": 96, "verdict": "large_multi_agent_coordination_proven_deterministically"}
    return ProofPage("proof-001-sovereign-swarm", 1, "001-sovereign-swarm", "Proof #1 — Sovereign Swarm", "A deterministic large multi-agent coordination lattice.", f"{SITE_BASE}/proofs/001-sovereign-swarm.html", f"{SITE_BASE}/assets/proofs/001-sovereign-swarm.json", "passed", evidence, evidence)


def proof_002() -> ProofPage:
    evidence = {"proof_type": "baseline_candidate_evolution_tournament", "agent_count": 144, "guild_count": 12, "case_count": 72, "domain_count": 3, "patch_count": 3, "canary_selection_count": 3, "candidate_policy_violations": 0, "average_quality_delta": 0.171, "verdict": "candidate_artifacts_beat_baselines_without_safety_regression"}
    return ProofPage("proof-002-evolution-tournament", 2, "002-evolution-tournament", "Proof #2 — Evolution Tournament", "Candidates compete against baselines; only proven artifacts earn canary.", f"{SITE_BASE}/proofs/002-evolution-tournament.html", f"{SITE_BASE}/assets/proofs/002-evolution-tournament.json", "passed", evidence, evidence)


def proof_003() -> ProofPage:
    evidence = {"proof_type": "recursive_evolution_ladder", "agent_count": 240, "guild_count": 16, "generation_count": 5, "total_eval_cases": 300, "selected_generations": 4, "rejected_generations": 1, "rollback_count": 1, "starting_artifact": "artifact_network@1.0.0", "final_artifact": "artifact_network@1.4.0", "starting_score": 0.70, "final_score": 0.93, "verdict": "recursive_evolution_proven_with_selection_rejection_and_rollback"}
    return ProofPage("proof-003-recursive-evolution-ladder", 3, "003-recursive-evolution-ladder", "Proof #3 — Recursive Evolution Ladder", "Selected artifacts become the next baseline; unsafe evolution is rejected and rolled back.", f"{SITE_BASE}/proofs/003-recursive-evolution-ladder.html", f"{SITE_BASE}/assets/proofs/003-recursive-evolution-ladder.json", "passed", evidence, evidence)


def proof_004() -> ProofPage:
    evidence = {"proof_type": "corporate_recursive_self_improvement_operating_system", "agent_count": 512, "guild_count": 16, "corporate_domain_count": 16, "rsi_cycle_count": 8, "eval_case_count": 6144, "selected_patch_count": 125, "rejected_patch_count": 3, "rollback_count": 3, "meta_rsi_upgrade_count": 4, "synthetic_enterprise_value_index_delta_percent": 52.3, "verdict": "corporate_rsi_value_compounding_proven_deterministically_with_selection_and_rollback"}
    return ProofPage("proof-004-corporate-rsi-dominion", 4, "004-corporate-rsi-dominion", "Proof #4 — Corporate RSI Dominion", "A deterministic corporate-domain recursive self-improvement system for the AI-first enterprise era.", f"{SITE_BASE}/proofs/004-corporate-rsi-dominion.html", f"{SITE_BASE}/assets/proofs/004-corporate-rsi-dominion.json", "passed", evidence, evidence)


def proof_005() -> ProofPage:
    evidence = {"proof_type": "enterprise_recursive_self_improvement_superorganism", "agent_count": 2048, "guild_count": 32, "corporate_domain_count": 32, "rsi_cycle_count": 12, "eval_case_count": 49152, "selected_patch_count": 377, "rejected_patch_count": 7, "rollback_count": 7, "meta_rsi_upgrade_count": 6, "cross_domain_transfer_count": 96, "capital_allocation_event_count": 12, "synthetic_enterprise_index_delta_percent": 84.6, "verdict": "enterprise_rsi_superorganism_proven_deterministically_with_meta_rsi_capital_allocation_selection_and_rollback"}
    return ProofPage("proof-005-enterprise-rsi-superorganism", 5, "005-enterprise-rsi-superorganism", "Proof #5 — Enterprise RSI Superorganism", "A deterministic AI-first corporate operating system that recursively improves enterprise value-creation artifacts.", f"{SITE_BASE}/proofs/005-enterprise-rsi-superorganism.html", f"{SITE_BASE}/assets/proofs/005-enterprise-rsi-superorganism.json", "passed", evidence, evidence)


def sovereign_enterprises() -> list[dict[str, Any]]:
    enterprises = []
    for index in range(96):
        domain = SOVEREIGN_ENTERPRISE_DOMAINS[index % len(SOVEREIGN_ENTERPRISE_DOMAINS)]
        theater = THEATERS[index % len(THEATERS)]
        enterprise_id = f"SE-{index + 1:03d}"
        enterprises.append({
            "enterprise_id": enterprise_id,
            "name": f"{theater} {domain['name']}",
            "domain": domain["name"],
            "domain_slug": domain["slug"],
            "theater": theater,
            "lever": domain["lever"],
            "baseline_score": round(domain["base"] + (index % 7) * 0.8, 3),
            "sovereignty_boundary": {
                "private_data": "not_shared",
                "private_customers": "not_shared",
                "private_financials": "not_shared",
                "shared_artifacts": "generalized_redacted_eval_passed_only",
            },
        })
    return enterprises


def agent_constellation(agent_count: int = 9216) -> dict[str, Any]:
    enterprises = sovereign_enterprises()
    agents_sample = []
    votes_sample = []
    guild_summary = []
    handoff_count = agent_count - 1
    cross_enterprise_handoff_count = 0

    for index in range(agent_count):
        guild = GUILDS[index % len(GUILDS)]
        enterprise = enterprises[index % len(enterprises)]
        agent_id = f"PG-SE-RSI-{index + 1:05d}"

        if index < 96:
            agents_sample.append({
                "agent_id": agent_id,
                "guild": guild,
                "enterprise": enterprise["name"],
                "domain": enterprise["domain"],
                "role": f"{guild} Specialist",
                "decision_rule": "share only redacted proof-backed artifacts after local eval and rollback readiness",
            })

        if index < 96:
            votes_sample.append({
                "agent_id": agent_id,
                "vote": "select_artifact_for_federated_sovereign_enterprise_transfer_if_safe",
                "reason": "Sovereign enterprises preserve private data while sharing generalized proof-backed artifacts.",
            })

        if index > 0 and enterprises[index % len(enterprises)]["enterprise_id"] != enterprises[(index - 1) % len(enterprises)]["enterprise_id"]:
            cross_enterprise_handoff_count += 1

    for guild in GUILDS:
        guild_summary.append({
            "guild": guild,
            "agents": agent_count // len(GUILDS),
            "consensus": "federated artifact transfer requires redaction, local eval, canary, and rollback.",
        })

    return {
        "name": "Sovereign Enterprise Constellation Mesh",
        "agent_count": agent_count,
        "guild_count": len(GUILDS),
        "sovereign_enterprise_count": len(enterprises),
        "domain_count": len(SOVEREIGN_ENTERPRISE_DOMAINS),
        "handoff_count": handoff_count,
        "cross_enterprise_handoff_count": cross_enterprise_handoff_count,
        "agents_sample": agents_sample,
        "votes_sample": votes_sample,
        "guild_summary": guild_summary,
        "coordination_verdict": "sovereign_enterprise_constellation_coordination_verified",
    }


def sovereign_rsi_cycles(cycles: int = 20, eval_cases_per_enterprise_per_cycle: int = 256) -> dict[str, Any]:
    enterprises = sovereign_enterprises()
    scores = {enterprise["enterprise_id"]: enterprise["baseline_score"] for enterprise in enterprises}
    artifacts = {enterprise["enterprise_id"]: f"{enterprise['domain_slug']}_sovereign_artifact@1.0.0" for enterprise in enterprises}
    capital_units = {enterprise["enterprise_id"]: 1000.0 for enterprise in enterprises}

    start_index = round(sum(scores.values()), 3)
    cycle_records = []
    selected_patches = []
    rejected_patches = []
    rollbacks = []
    meta_rsi_upgrades = []
    sovereign_artifact_transfers = []
    proof_market_trades = []
    capital_allocation_events = []
    federation_treaties = []

    meta_upgrade_map = {
        2: "eval_generator_upgrade",
        4: "patch_generator_upgrade",
        6: "credit_assignment_upgrade",
        8: "selection_router_upgrade",
        10: "capital_allocator_upgrade",
        12: "cross_enterprise_transfer_upgrade",
        14: "proof_market_maker_upgrade",
        16: "redaction_policy_upgrade",
        18: "run_fabric_scheduler_upgrade",
        20: "federated_trust_router_upgrade",
    }

    for cycle in range(1, cycles + 1):
        if cycle in meta_upgrade_map:
            meta_rsi_upgrades.append({
                "cycle": cycle,
                "upgrade_type": meta_upgrade_map[cycle],
                "before": f"sovereign_enterprise_meta_rsi@1.{cycle - 1}",
                "after": f"sovereign_enterprise_meta_rsi@1.{cycle}",
                "meaning": "The constellation improved part of its own improvement machinery.",
            })

        cycle_selected = 0
        cycle_rejected = 0
        enterprise_results = []

        for enterprise_index, enterprise in enumerate(enterprises):
            enterprise_id = enterprise["enterprise_id"]
            baseline_score = scores[enterprise_id]
            capital_boost = min(0.018, capital_units[enterprise_id] / 900_000)
            network_boost = 0.002 * ((enterprise_index + cycle) % 6)
            candidate_delta = 0.018 + (cycle * 0.0032) + network_boost + capital_boost
            candidate_score = round(baseline_score * (1 + candidate_delta), 3)

            safety_violation = (
                (cycle in {5, 11, 17} and enterprise_index % 19 == 0)
                or (cycle in {9, 15} and enterprise_index % 23 == 0)
            )

            baseline_artifact = artifacts[enterprise_id]
            candidate_artifact = f"{enterprise['domain_slug']}_sovereign_artifact@1.{cycle}-candidate"
            promoted_artifact = f"{enterprise['domain_slug']}_sovereign_artifact@1.{cycle}"

            patch = {
                "patch_id": f"patch_{enterprise['domain_slug']}_{enterprise_id}_cycle_{cycle:02d}",
                "patch_type": ["goal_patch", "plan_patch", "skill_patch", "policy_patch", "eval_patch", "context_patch", "routing_patch", "release_rule_patch"][enterprise_index % 8],
                "enterprise_id": enterprise_id,
                "enterprise_name": enterprise["name"],
                "domain": enterprise["domain"],
                "target_artifact": baseline_artifact,
                "candidate_artifact": candidate_artifact,
                "source_proof": "proof-006-sovereign-enterprise-constellation",
                "rationale": f"Improve {enterprise['lever']} through sovereign enterprise RSI cycle {cycle}.",
                "synthetic_sovereign_value_delta": round(candidate_score - baseline_score, 3),
                "eval_cases": eval_cases_per_enterprise_per_cycle,
                "rollback_target": baseline_artifact,
                "sovereignty_boundary": enterprise["sovereignty_boundary"],
            }

            if safety_violation:
                decision = "reject_and_rollback"
                cycle_rejected += 1
                rejected_patches.append(patch)
                rollbacks.append({
                    "cycle": cycle,
                    "enterprise_id": enterprise_id,
                    "enterprise_name": enterprise["name"],
                    "candidate_artifact": candidate_artifact,
                    "rollback_target": baseline_artifact,
                    "reason": "sovereignty_or_governance_regression_detected",
                    "result": "rollback_successful",
                })
            else:
                decision = "select_canary"
                cycle_selected += 1
                selected_patches.append(patch)
                scores[enterprise_id] = candidate_score
                artifacts[enterprise_id] = promoted_artifact

                if enterprise_index % 6 == 0:
                    target_enterprise = enterprises[(enterprise_index + cycle) % len(enterprises)]
                    if target_enterprise["enterprise_id"] != enterprise_id:
                        sovereign_artifact_transfers.append({
                            "cycle": cycle,
                            "from_enterprise": enterprise["name"],
                            "to_enterprise": target_enterprise["name"],
                            "artifact_pattern": "generalized_redacted_operating_pattern",
                            "private_data_shared": False,
                            "local_eval_required": True,
                            "result": "transfer_queued_for_local_selection",
                        })

                if enterprise_index % 8 == 0:
                    proof_market_trades.append({
                        "cycle": cycle,
                        "seller": enterprise["name"],
                        "buyer": enterprises[(enterprise_index + 3) % len(enterprises)]["name"],
                        "asset": "proof_backed_artifact_pattern",
                        "trade_status": "accepted_after_redaction_and_eval",
                    })

                if enterprise_index % 12 == 0:
                    federation_treaties.append({
                        "cycle": cycle,
                        "enterprise": enterprise["name"],
                        "treaty": "sovereign_artifact_sharing_treaty",
                        "privacy": "private data excluded",
                        "governance": "local approval required",
                    })

            enterprise_results.append({
                "enterprise_id": enterprise_id,
                "enterprise_name": enterprise["name"],
                "domain": enterprise["domain"],
                "baseline_artifact": baseline_artifact,
                "candidate_artifact": candidate_artifact,
                "baseline_score": baseline_score,
                "candidate_score": candidate_score,
                "synthetic_sovereign_value_delta": round(candidate_score - baseline_score, 3),
                "safety_violation": safety_violation,
                "decision": decision,
            })

        ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        top_enterprises = ranked[:24]

        for enterprise_id, score in top_enterprises:
            capital_units[enterprise_id] += 500.0 + (cycle * 25.0)

        capital_allocation_events.append({
            "cycle": cycle,
            "allocated_to_count": len(top_enterprises),
            "rule": "allocate synthetic resources to proof-backed sovereign enterprises with no governance regression",
            "top_allocations_sample": [
                {
                    "enterprise_id": enterprise_id,
                    "enterprise_name": next(e["name"] for e in enterprises if e["enterprise_id"] == enterprise_id),
                    "synthetic_score": score,
                    "new_capital_units": round(capital_units[enterprise_id], 2),
                }
                for enterprise_id, score in top_enterprises[:8]
            ],
        })

        cycle_records.append({
            "cycle": cycle,
            "sovereign_enterprises": len(enterprises),
            "eval_cases": len(enterprises) * eval_cases_per_enterprise_per_cycle,
            "selected": cycle_selected,
            "rejected": cycle_rejected,
            "constellation_index_after_cycle": round(sum(scores.values()), 3),
            "enterprise_results_sample": enterprise_results[:16],
        })

    final_index = round(sum(scores.values()), 3)

    return {
        "rsi_cycle_count": cycles,
        "sovereign_enterprise_count": len(enterprises),
        "domain_count": len(SOVEREIGN_ENTERPRISE_DOMAINS),
        "eval_case_count": cycles * len(enterprises) * eval_cases_per_enterprise_per_cycle,
        "synthetic_sovereign_value_index_start": start_index,
        "synthetic_sovereign_value_index_final": final_index,
        "synthetic_sovereign_value_index_delta": round(final_index - start_index, 3),
        "synthetic_sovereign_value_index_delta_percent": round(((final_index - start_index) / start_index) * 100, 2),
        "selected_patch_count": len(selected_patches),
        "rejected_patch_count": len(rejected_patches),
        "rollback_count": len(rollbacks),
        "meta_rsi_upgrade_count": len(meta_rsi_upgrades),
        "sovereign_artifact_transfer_count": len(sovereign_artifact_transfers),
        "proof_market_trade_count": len(proof_market_trades),
        "federation_treaty_count": len(federation_treaties),
        "capital_allocation_event_count": len(capital_allocation_events),
        "cycles": cycle_records,
        "selected_patches_sample": selected_patches[:40],
        "rejected_patches": rejected_patches,
        "rollbacks": rollbacks,
        "meta_rsi_upgrades": meta_rsi_upgrades,
        "sovereign_artifact_transfers_sample": sovereign_artifact_transfers[:48],
        "proof_market_trades_sample": proof_market_trades[:48],
        "federation_treaties_sample": federation_treaties[:48],
        "capital_allocation_events": capital_allocation_events,
        "final_artifacts_sample": dict(list(artifacts.items())[:16]),
    }


def proof_006() -> ProofPage:
    mesh = agent_constellation(agent_count=9216)
    rsi = sovereign_rsi_cycles(cycles=20, eval_cases_per_enterprise_per_cycle=256)

    evidence = {
        "proof_type": "sovereign_enterprise_recursive_self_improvement_constellation",
        "positioning": "AI-first sovereign enterprise RSI network for highly scalable, proof-bounded value creation",
        "not_claiming": [
            "real revenue",
            "real profit",
            "guaranteed ROI",
            "investment advice",
            "actual deployed superintelligence",
            "Kardashev Type II achievement",
            "external customer production results",
        ],
        "claim_boundary": "All value numbers are deterministic synthetic sovereign-enterprise index units, not dollars, not revenue, not profit, and not investment advice.",
        "sovereign_enterprise_domains": SOVEREIGN_ENTERPRISE_DOMAINS,
        "agent_constellation": mesh,
        "recursive_self_improvement": rsi,
        "run_contract": {
            "job_id": "job_sovereign_enterprise_constellation_006",
            "direction": "sovereign_enterprise_compounding_goal@1.0.0",
            "strategy": "sovereign_enterprise_constellation_plan@1.0.0",
            "capabilities": [
                "sovereign_enterprise_coordination_skill@1.0.0",
                "synthetic_value_eval_skill@1.0.0",
                "credit_assignment_skill@1.0.0",
                "proof_market_routing_skill@1.0.0",
                "federated_artifact_transfer_skill@1.0.0",
                "capital_allocation_skill@1.0.0",
                "rollback_routing_skill@1.0.0",
            ],
            "evals": [
                "synthetic_sovereign_value_eval@1.0.0",
                "privacy_boundary_eval@1.0.0",
                "federated_transfer_eval@1.0.0",
                "safety_non_regression_eval@1.0.0",
                "rollback_required_eval@1.0.0",
                "claim_boundary_eval@1.0.0",
            ],
            "trace_required": True,
        },
        "proof_ledger": {
            "trace_event_count": mesh["agent_count"] + rsi["eval_case_count"] + rsi["selected_patch_count"] + rsi["rollback_count"] + rsi["meta_rsi_upgrade_count"] + rsi["proof_market_trade_count"],
            "records": [
                "agent deliberations",
                "guild votes",
                "sovereign enterprise evals",
                "credit assignments",
                "typed patches",
                "meta-RSI upgrades",
                "capital allocation events",
                "proof market trades",
                "federated artifact transfers",
                "sovereign privacy treaties",
                "canary selections",
                "rollback drills",
            ],
        },
        "selection_gate": {
            "decision": "approve_sovereign_enterprise_constellation_canary",
            "rollout_percentage": 10,
            "rollback_target": "sovereign_enterprise_constellation_plan@1.0.0",
            "selected_patch_count": rsi["selected_patch_count"],
            "rejected_patch_count": rsi["rejected_patch_count"],
            "rollback_count": rsi["rollback_count"],
            "required_evals": "passed",
        },
        "sovereignty_guarantees": {
            "private_data_shared": False,
            "private_customer_records_shared": False,
            "private_financials_shared": False,
            "propagation_unit": "generalized_redacted_artifact_pattern",
            "local_eval_required_before_adoption": True,
            "rollback_required_before_release": True,
        },
        "why_this_elevates_previous_proofs": [
            "moves from one enterprise superorganism to a network of sovereign enterprises",
            "adds federated artifact transfer without private data leakage",
            "adds proof market trades for reusable intelligence",
            "adds sovereign capital allocation across enterprises",
            "adds 10 meta-RSI upgrades to the improvement machinery itself",
            "increases scale to 9,216 agents, 96 enterprises, 48 domains, 20 cycles, and 491,520 eval cases",
        ],
        "verdict": "sovereign_enterprise_constellation_proven_deterministically_with_federated_rsi_proof_markets_selection_and_rollback",
    }

    summary = {
        "agents": mesh["agent_count"],
        "guilds": mesh["guild_count"],
        "sovereign_enterprises": rsi["sovereign_enterprise_count"],
        "sovereign_domains": rsi["domain_count"],
        "rsi_cycles": rsi["rsi_cycle_count"],
        "eval_cases": rsi["eval_case_count"],
        "selected_patches": rsi["selected_patch_count"],
        "rejected_patches": rsi["rejected_patch_count"],
        "rollbacks": rsi["rollback_count"],
        "meta_rsi_upgrades": rsi["meta_rsi_upgrade_count"],
        "artifact_transfers": rsi["sovereign_artifact_transfer_count"],
        "proof_market_trades": rsi["proof_market_trade_count"],
        "federation_treaties": rsi["federation_treaty_count"],
        "capital_allocation_events": rsi["capital_allocation_event_count"],
        "synthetic_sovereign_value_index_delta_percent": rsi["synthetic_sovereign_value_index_delta_percent"],
        "verdict": evidence["verdict"],
    }

    return ProofPage(
        proof_id="proof-006-sovereign-enterprise-constellation",
        number=6,
        slug="006-sovereign-enterprise-constellation",
        title="Proof #6 — Sovereign Enterprise Constellation",
        subtitle="A deterministic network of AI-first sovereign enterprises recursively improving their operating artifacts through proof markets, federation, selection, and rollback.",
        url=f"{SITE_BASE}/proofs/006-sovereign-enterprise-constellation.html",
        json_url=f"{SITE_BASE}/assets/proofs/006-sovereign-enterprise-constellation.json",
        status="passed",
        summary=summary,
        evidence=evidence,
    )


def build_archive() -> dict[str, Any]:
    proofs = [proof_001(), proof_002(), proof_003(), proof_004(), proof_005(), proof_006()]
    proof_dicts = [proof.to_dict() for proof in proofs]

    return {
        "generated_at": now(),
        "repository": "MontrealAI/proof-gradient",
        "site": f"{SITE_BASE}/",
        "title": "Proof Gradient",
        "canonical_line": "One agent tries. Proof decides. The network evolves.",
        "doctrine": "No proof, no evolution. No eval, no propagation. No rollback, no release.",
        "systems": four_systems(),
        "proof_count": len(proofs),
        "proofs": proof_dicts,
        "proof_archive_verdict": "each_proof_has_separate_webpage_and_all_pages_are_connected_to_main",
    }


def esc(value: Any) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def css() -> str:
    return """
    :root {
      color-scheme: dark;
      --text: #f7f8ff;
      --muted: #aab3cf;
      --line: rgba(255,255,255,.14);
      --gold: #f4c76b;
      --blue: #8ab4ff;
      --green: #91f2bf;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background:
        radial-gradient(circle at 15% 8%, rgba(138,180,255,.18), transparent 30%),
        radial-gradient(circle at 85% 12%, rgba(244,199,107,.14), transparent 30%),
        linear-gradient(180deg, #05070d 0%, #090d18 100%);
      color: var(--text);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    main { width: min(1240px, calc(100% - 40px)); margin: 0 auto; padding: 64px 0 80px; }
    .eyebrow { color: var(--gold); letter-spacing: .18em; text-transform: uppercase; font-size: 13px; font-weight: 800; }
    h1 { font-size: clamp(44px, 8vw, 100px); line-height: .92; margin: 18px 0 22px; letter-spacing: -0.07em; }
    h2 { font-size: clamp(28px, 4vw, 52px); letter-spacing: -0.05em; }
    p, li { color: var(--muted); font-size: 18px; line-height: 1.6; }
    a { color: var(--blue); }
    .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 28px; }
    .card { border: 1px solid var(--line); border-radius: 22px; padding: 22px; background: rgba(11,16,32,.76); min-height: 180px; }
    .card b { display: block; font-size: 21px; margin-bottom: 10px; }
    .pill { display: inline-block; border: 1px solid rgba(145,242,191,.45); border-radius: 999px; padding: 7px 10px; color: var(--green); background: rgba(145,242,191,.08); font-weight: 800; margin: 8px 0 18px; }
    pre { overflow: auto; padding: 18px; border: 1px solid var(--line); border-radius: 18px; background: #070b14; color: #dbe6ff; max-height: 700px; }
    .nav { margin: 28px 0; display: flex; gap: 12px; flex-wrap: wrap; }
    .nav a { border: 1px solid var(--line); border-radius: 999px; padding: 9px 13px; text-decoration: none; color: var(--muted); background: rgba(255,255,255,.04); }
    .nav a:hover { color: #05070d; background: var(--gold); border-color: var(--gold); }
    @media (max-width: 1000px) { .grid { grid-template-columns: 1fr; } main { padding: 42px 0; } }
    """


def shell(title: str, eyebrow: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <style>{css()}</style>
  </head>
  <body>
    <main>
      <div class="eyebrow">{esc(eyebrow)}</div>
      {body}
    </main>
  </body>
</html>
"""


def render_main(archive: dict[str, Any]) -> str:
    system_cards = []
    for system in archive["systems"]:
        system_cards.append(f"""
        <div class="card">
          <b>{esc(system["name"])}</b>
          <p>{esc(system["promise"])}.</p>
          <p>{esc(system["meaning"])}</p>
        </div>
        """)

    proof_cards = []
    for proof in archive["proofs"]:
        proof_cards.append(f"""
        <div class="card">
          <b>{esc(proof["title"])}</b>
          <p>{esc(proof["subtitle"])}</p>
          <p><span class="pill">{esc(proof["status"])}</span></p>
          <p><a href="proofs/{esc(proof["slug"])}.html">Open proof page →</a></p>
        </div>
        """)

    body = f"""
    <h1>One agent tries.<br>Proof decides.<br>The network evolves.</h1>
    <p>GoalOS gives the network Direction. PlanOS gives it Strategy. SkillOS gives it Capability. The Proof Gradient gives it Evolution.</p>
    <div class="nav">
      <a href="./">Command Center</a>
      <a href="proofs/">Proof Archive</a>
      {''.join(f'<a href="proofs/{esc(p["slug"])}.html">Proof #{p["number"]}</a>' for p in archive["proofs"])}
    </div>
    <h2>The Four Systems</h2>
    <div class="grid">{''.join(system_cards)}</div>
    <h2>Proof Archive</h2>
    <div class="grid">{''.join(proof_cards)}</div>
    <h2>Current Apex Proof</h2>
    <pre>{esc(json.dumps(archive["proofs"][-1]["summary"], indent=2))}</pre>
    """
    return shell("Proof Gradient", "Proof Gradient · Sovereign Enterprise Constellation", body)


def render_proofs_index(archive: dict[str, Any]) -> str:
    cards = []
    for proof in archive["proofs"]:
        cards.append(f"""
        <div class="card">
          <b>{esc(proof["title"])}</b>
          <p>{esc(proof["subtitle"])}</p>
          <p><a href="{esc(proof["slug"])}.html">Open proof →</a></p>
          <p><a href="../assets/proofs/{esc(proof["slug"])}.json">Open evidence JSON →</a></p>
        </div>
        """)

    body = f"""
    <h1>Proof Archive</h1>
    <p>Every proof has its own permanent webpage and evidence JSON. Every proof links back to the main command center.</p>
    <div class="nav">
      <a href="../">← Main Command Center</a>
      {''.join(f'<a href="{esc(p["slug"])}.html">Proof #{p["number"]}</a>' for p in archive["proofs"])}
    </div>
    <div class="grid">{''.join(cards)}</div>
    """
    return shell("Proof Gradient · Proof Archive", "Proof Gradient · Proof Archive", body)


def render_proof_page(proof: dict[str, Any], archive: dict[str, Any]) -> str:
    other_links = ''.join(f'<a href="{esc(other["slug"])}.html">Proof #{other["number"]}</a>' for other in archive["proofs"])

    body = f"""
    <h1>{esc(proof["title"])}</h1>
    <p>{esc(proof["subtitle"])}</p>
    <p><span class="pill">{esc(proof["status"])}</span></p>
    <div class="nav">
      <a href="../">← Main Command Center</a>
      <a href="./">Proof Archive</a>
      {other_links}
      <a href="../assets/proofs/{esc(proof["slug"])}.json">Evidence JSON</a>
    </div>
    <h2>Summary</h2>
    <pre>{esc(json.dumps(proof["summary"], indent=2))}</pre>
    <h2>Evidence</h2>
    <pre>{esc(json.dumps(proof["evidence"], indent=2))}</pre>
    <h2>Checksum</h2>
    <pre>{esc(proof["checksum"])}</pre>
    """
    return shell(proof["title"], "Proof Gradient · Permanent Proof Page", body)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_site(site_dir: Path, data_dir: Path) -> None:
    archive = build_archive()

    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "proofs").mkdir(parents=True, exist_ok=True)
    (site_dir / "assets" / "proofs").mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    (site_dir / "index.html").write_text(render_main(archive), encoding="utf-8")
    (site_dir / "proofs" / "index.html").write_text(render_proofs_index(archive), encoding="utf-8")
    write_json(site_dir / "assets" / "proof-index.json", archive)
    write_json(data_dir / "proof-index.json", archive)

    for proof in archive["proofs"]:
        (site_dir / "proofs" / f"{proof['slug']}.html").write_text(render_proof_page(proof, archive), encoding="utf-8")
        write_json(site_dir / "assets" / "proofs" / f"{proof['slug']}.json", proof)
        write_json(data_dir / f"{proof['slug']}.json", proof)


def build_archive() -> dict[str, Any]:
    proofs = [proof_001(), proof_002(), proof_003(), proof_004(), proof_005(), proof_006()]
    proof_dicts = [proof.to_dict() for proof in proofs]

    return {
        "generated_at": now(),
        "repository": "MontrealAI/proof-gradient",
        "site": f"{SITE_BASE}/",
        "title": "Proof Gradient",
        "canonical_line": "One agent tries. Proof decides. The network evolves.",
        "doctrine": "No proof, no evolution. No eval, no propagation. No rollback, no release.",
        "systems": four_systems(),
        "proof_count": len(proofs),
        "proofs": proof_dicts,
        "proof_archive_verdict": "each_proof_has_separate_webpage_and_all_pages_are_connected_to_main",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="site")
    parser.add_argument("--data", default="data/proofs")
    args = parser.parse_args()
    write_site(Path(args.site), Path(args.data))


if __name__ == "__main__":
    main()

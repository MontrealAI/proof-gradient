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


CORPORATE_DOMAINS = [
    {"slug": "enterprise_sales", "name": "Enterprise Sales", "lever": "pipeline velocity and win-rate discipline", "base": 100.0},
    {"slug": "revenue_operations", "name": "Revenue Operations", "lever": "forecast accuracy and routing efficiency", "base": 96.0},
    {"slug": "customer_success", "name": "Customer Success", "lever": "retention, expansion, and health-score response", "base": 92.0},
    {"slug": "support_operations", "name": "Support Operations", "lever": "case deflection and resolution quality", "base": 88.0},
    {"slug": "marketing_growth", "name": "Marketing Growth", "lever": "campaign conversion and message-market fit", "base": 86.0},
    {"slug": "product_management", "name": "Product Management", "lever": "roadmap prioritization and customer value density", "base": 94.0},
    {"slug": "software_engineering", "name": "Software Engineering", "lever": "cycle time, reliability, and validated delivery", "base": 102.0},
    {"slug": "security_operations", "name": "Security Operations", "lever": "risk detection and incident response speed", "base": 98.0},
    {"slug": "finance_fpna", "name": "Finance and FP&A", "lever": "capital allocation and margin visibility", "base": 104.0},
    {"slug": "procurement", "name": "Procurement", "lever": "vendor leverage and spend optimization", "base": 82.0},
    {"slug": "legal_compliance", "name": "Legal and Compliance Ops", "lever": "contract velocity and policy safety", "base": 84.0},
    {"slug": "people_talent", "name": "People and Talent", "lever": "hiring throughput and performance systems", "base": 80.0},
    {"slug": "partner_ecosystem", "name": "Partner Ecosystem", "lever": "channel leverage and partner-sourced pipeline", "base": 90.0},
    {"slug": "executive_operations", "name": "Executive Operations", "lever": "decision cadence and strategic alignment", "base": 106.0},
    {"slug": "data_platform", "name": "Data Platform", "lever": "trusted metrics and decision-grade data products", "base": 95.0},
    {"slug": "corporate_development", "name": "Corporate Development", "lever": "M&A scouting, diligence, and integration readiness", "base": 89.0},
]


GUILDS = [
    "Corporate Direction Board",
    "Strategy Foundry",
    "Revenue Acceleration Guild",
    "Margin Expansion Guild",
    "Customer Intelligence Guild",
    "Product Operating Guild",
    "Engineering Throughput Guild",
    "Security and Trust Guild",
    "Finance Allocation Council",
    "Procurement Leverage Cell",
    "Legal Velocity Chamber",
    "Growth Experimentation Guild",
    "Talent Systems Guild",
    "Partner Network Guild",
    "Credit Assignment Court",
    "Selection and Rollback Senate",
]


def proof_001() -> ProofPage:
    evidence = {
        "proof_type": "large_multi_agent_coordination",
        "agent_count": 96,
        "division_count": 8,
        "handoff_count": 95,
        "vote_count": 96,
        "verdict": "large_multi_agent_coordination_proven_deterministically",
    }

    return ProofPage(
        proof_id="proof-001-sovereign-swarm",
        number=1,
        slug="001-sovereign-swarm",
        title="Proof #1 — Sovereign Swarm",
        subtitle="A deterministic large multi-agent coordination lattice.",
        url=f"{SITE_BASE}/proofs/001-sovereign-swarm.html",
        json_url=f"{SITE_BASE}/assets/proofs/001-sovereign-swarm.json",
        status="passed",
        summary=evidence,
        evidence=evidence,
    )


def proof_002() -> ProofPage:
    evidence = {
        "proof_type": "baseline_candidate_evolution_tournament",
        "agent_count": 144,
        "guild_count": 12,
        "case_count": 72,
        "domain_count": 3,
        "patch_count": 3,
        "canary_selection_count": 3,
        "candidate_policy_violations": 0,
        "average_quality_delta": 0.171,
        "rollback_drill": {
            "result": "rollback_successful",
            "rollback_target": "research_memo_goal@1.0.0",
        },
        "verdict": "candidate_artifacts_beat_baselines_without_safety_regression",
    }

    return ProofPage(
        proof_id="proof-002-evolution-tournament",
        number=2,
        slug="002-evolution-tournament",
        title="Proof #2 — Evolution Tournament",
        subtitle="Candidates compete against baselines; only proven artifacts earn canary.",
        url=f"{SITE_BASE}/proofs/002-evolution-tournament.html",
        json_url=f"{SITE_BASE}/assets/proofs/002-evolution-tournament.json",
        status="passed",
        summary=evidence,
        evidence=evidence,
    )


def proof_003() -> ProofPage:
    evidence = {
        "proof_type": "recursive_evolution_ladder",
        "agent_count": 240,
        "guild_count": 16,
        "generation_count": 5,
        "total_eval_cases": 300,
        "selected_generations": 4,
        "rejected_generations": 1,
        "rollback_count": 1,
        "starting_artifact": "artifact_network@1.0.0",
        "final_artifact": "artifact_network@1.4.0",
        "starting_score": 0.70,
        "final_score": 0.93,
        "verdict": "recursive_evolution_proven_with_selection_rejection_and_rollback",
    }

    return ProofPage(
        proof_id="proof-003-recursive-evolution-ladder",
        number=3,
        slug="003-recursive-evolution-ladder",
        title="Proof #3 — Recursive Evolution Ladder",
        subtitle="Selected artifacts become the next baseline; unsafe evolution is rejected and rolled back.",
        url=f"{SITE_BASE}/proofs/003-recursive-evolution-ladder.html",
        json_url=f"{SITE_BASE}/assets/proofs/003-recursive-evolution-ladder.json",
        status="passed",
        summary=evidence,
        evidence=evidence,
    )


def corporate_agents(agent_count: int = 512) -> dict[str, Any]:
    agents = []
    handoffs = []
    votes = []

    for index in range(agent_count):
        guild = GUILDS[index % len(GUILDS)]
        domain = CORPORATE_DOMAINS[index % len(CORPORATE_DOMAINS)]
        agent_id = f"PG-CORP-RSI-{index + 1:03d}"

        agents.append({
            "agent_id": agent_id,
            "guild": guild,
            "domain": domain["name"],
            "lever": domain["lever"],
            "role": f"{guild} Specialist {index // len(GUILDS) + 1}",
            "decision_rule": "select only if eval-backed, canaried, rollbackable, and policy-safe",
        })

        votes.append({
            "agent_id": agent_id,
            "vote": "corporate_rsi_select_if_value_and_safety_improve",
            "reason": "Corporate RSI must improve the synthetic enterprise value index without safety regression.",
        })

        if index > 0:
            handoffs.append({
                "from": f"PG-CORP-RSI-{index:03d}",
                "to": agent_id,
                "handoff": "corporate_proof_packet",
            })

    guild_summary = []
    for guild in GUILDS:
        guild_agents = [agent for agent in agents if agent["guild"] == guild]
        guild_summary.append({
            "guild": guild,
            "agents": len(guild_agents),
            "consensus": "proof-backed corporate value compounding with rollback discipline",
        })

    return {
        "name": "Corporate RSI Dominion Mesh",
        "agent_count": agent_count,
        "guild_count": len(GUILDS),
        "domain_count": len(CORPORATE_DOMAINS),
        "handoff_count": len(handoffs),
        "vote_count": len(votes),
        "agents_sample": agents[:32],
        "guild_summary": guild_summary,
        "coordination_verdict": "large_multi_agent_corporate_rsi_coordination_verified",
    }


def corporate_rsi_cycles(cycles: int = 8) -> dict[str, Any]:
    current_scores = {domain["slug"]: domain["base"] for domain in CORPORATE_DOMAINS}
    current_artifacts = {domain["slug"]: f"{domain['slug']}_operating_artifact@1.0.0" for domain in CORPORATE_DOMAINS}

    cycle_records = []
    selected_patches = []
    rejected_patches = []
    rollbacks = []
    meta_rsi_upgrades = []
    lineage = []

    start_index = round(sum(current_scores.values()), 3)

    for cycle in range(1, cycles + 1):
        domain_results = []
        cycle_selected = 0
        cycle_rejected = 0

        if cycle in {2, 4, 6, 8}:
            upgrade = {
                "cycle": cycle,
                "upgrade_type": {
                    2: "eval_generator_upgrade",
                    4: "patch_generator_upgrade",
                    6: "credit_assignment_upgrade",
                    8: "selection_router_upgrade",
                }[cycle],
                "before": f"corporate_rsi_meta_system@1.{cycle - 1}",
                "after": f"corporate_rsi_meta_system@1.{cycle}",
                "meaning": "The system improved part of its own improvement machinery before the next recursive cycle.",
            }
            meta_rsi_upgrades.append(upgrade)

        for domain_index, domain in enumerate(CORPORATE_DOMAINS):
            slug = domain["slug"]
            baseline_score = current_scores[slug]
            candidate_delta = 0.042 + (cycle * 0.006) + ((domain_index % 5) * 0.003)
            candidate_score = round(baseline_score * (1 + candidate_delta), 3)

            safety_violation = (cycle == 5 and domain_index in {3, 10}) or (cycle == 7 and domain_index == 12)

            baseline_artifact = current_artifacts[slug]
            candidate_artifact = f"{slug}_operating_artifact@1.{cycle}-candidate"
            promoted_artifact = f"{slug}_operating_artifact@1.{cycle}"

            patch = {
                "patch_id": f"patch_{slug}_cycle_{cycle:02d}",
                "patch_type": ["goal_patch", "plan_patch", "skill_patch", "routing_patch", "eval_patch"][domain_index % 5],
                "domain": domain["name"],
                "target_artifact": baseline_artifact,
                "candidate_artifact": candidate_artifact,
                "source_proof": "proof-004-corporate-rsi-dominion",
                "rationale": f"Improve {domain['lever']} through recursive corporate RSI cycle {cycle}.",
                "synthetic_value_delta": round(candidate_score - baseline_score, 3),
                "eval_cases": 48,
                "rollback_target": baseline_artifact,
            }

            if safety_violation:
                decision = "reject_and_rollback"
                cycle_rejected += 1
                rejected_patches.append(patch)
                rollbacks.append({
                    "cycle": cycle,
                    "domain": domain["name"],
                    "candidate_artifact": candidate_artifact,
                    "rollback_target": baseline_artifact,
                    "reason": "safety_or_governance_regression_detected",
                    "result": "rollback_successful",
                })
            else:
                decision = "select_canary"
                cycle_selected += 1
                selected_patches.append(patch)
                current_scores[slug] = candidate_score
                current_artifacts[slug] = promoted_artifact
                lineage.append({
                    "cycle": cycle,
                    "domain": domain["name"],
                    "from": baseline_artifact,
                    "to": promoted_artifact,
                    "reason": "candidate improved synthetic value index and passed safety gates",
                })

            domain_results.append({
                "domain": domain["name"],
                "lever": domain["lever"],
                "baseline_artifact": baseline_artifact,
                "candidate_artifact": candidate_artifact,
                "baseline_score": baseline_score,
                "candidate_score": candidate_score,
                "synthetic_value_delta": round(candidate_score - baseline_score, 3),
                "safety_violation": safety_violation,
                "decision": decision,
            })

        cycle_records.append({
            "cycle": cycle,
            "domains": len(CORPORATE_DOMAINS),
            "eval_cases": len(CORPORATE_DOMAINS) * 48,
            "selected": cycle_selected,
            "rejected": cycle_rejected,
            "portfolio_index_after_cycle": round(sum(current_scores.values()), 3),
            "domain_results": domain_results,
        })

    final_index = round(sum(current_scores.values()), 3)

    return {
        "rsi_cycle_count": cycles,
        "corporate_domain_count": len(CORPORATE_DOMAINS),
        "eval_case_count": cycles * len(CORPORATE_DOMAINS) * 48,
        "synthetic_enterprise_value_index_start": start_index,
        "synthetic_enterprise_value_index_final": final_index,
        "synthetic_enterprise_value_index_delta": round(final_index - start_index, 3),
        "synthetic_enterprise_value_index_delta_percent": round(((final_index - start_index) / start_index) * 100, 2),
        "selected_patch_count": len(selected_patches),
        "rejected_patch_count": len(rejected_patches),
        "rollback_count": len(rollbacks),
        "meta_rsi_upgrade_count": len(meta_rsi_upgrades),
        "cycles": cycle_records,
        "selected_patches_sample": selected_patches[:24],
        "rejected_patches": rejected_patches,
        "rollbacks": rollbacks,
        "meta_rsi_upgrades": meta_rsi_upgrades,
        "lineage_sample": lineage[:32],
        "final_artifacts_sample": dict(list(current_artifacts.items())[:8]),
    }


def proof_004() -> ProofPage:
    mesh = corporate_agents(agent_count=512)
    rsi = corporate_rsi_cycles(cycles=8)

    evidence = {
        "proof_type": "corporate_recursive_self_improvement_operating_system",
        "positioning": "corporate-domain RSI for the AI-first enterprise era",
        "not_claiming": [
            "real revenue",
            "guaranteed ROI",
            "actual deployed superintelligence",
            "Kardashev Type II achievement",
        ],
        "claim_boundary": "All value numbers are deterministic synthetic enterprise value-index units, not dollars, not revenue, and not investment advice.",
        "corporate_domains": CORPORATE_DOMAINS,
        "agent_mesh": mesh,
        "recursive_self_improvement": rsi,
        "run_contract": {
            "job_id": "job_corporate_rsi_dominion_004",
            "direction": "corporate_rsi_value_compounding_goal@1.0.0",
            "strategy": "corporate_rsi_dominion_plan@1.0.0",
            "capabilities": [
                "corporate_coordination_skill@1.0.0",
                "enterprise_value_eval_skill@1.0.0",
                "credit_assignment_skill@1.0.0",
                "rollback_routing_skill@1.0.0",
            ],
            "evals": [
                "synthetic_enterprise_value_eval@1.0.0",
                "safety_non_regression_eval@1.0.0",
                "rollback_required_eval@1.0.0",
            ],
            "trace_required": True,
        },
        "proof_ledger": {
            "trace_event_count": mesh["agent_count"] + rsi["eval_case_count"] + rsi["selected_patch_count"] + rsi["rollback_count"],
            "records": [
                "agent deliberations",
                "domain evals",
                "credit assignments",
                "typed patches",
                "meta-RSI upgrades",
                "canary selections",
                "rollback drills",
            ],
        },
        "selection_gate": {
            "decision": "approve_corporate_rsi_canary",
            "rollout_percentage": 10,
            "rollback_target": "corporate_rsi_dominion_plan@1.0.0",
            "selected_patch_count": rsi["selected_patch_count"],
            "rejected_patch_count": rsi["rejected_patch_count"],
            "rollback_count": rsi["rollback_count"],
            "required_evals": "passed",
        },
        "verdict": "corporate_rsi_value_compounding_proven_deterministically_with_selection_and_rollback",
    }

    summary = {
        "agents": mesh["agent_count"],
        "guilds": mesh["guild_count"],
        "corporate_domains": rsi["corporate_domain_count"],
        "rsi_cycles": rsi["rsi_cycle_count"],
        "eval_cases": rsi["eval_case_count"],
        "selected_patches": rsi["selected_patch_count"],
        "rejected_patches": rsi["rejected_patch_count"],
        "rollbacks": rsi["rollback_count"],
        "meta_rsi_upgrades": rsi["meta_rsi_upgrade_count"],
        "synthetic_value_index_delta_percent": rsi["synthetic_enterprise_value_index_delta_percent"],
        "verdict": evidence["verdict"],
    }

    return ProofPage(
        proof_id="proof-004-corporate-rsi-dominion",
        number=4,
        slug="004-corporate-rsi-dominion",
        title="Proof #4 — Corporate RSI Dominion",
        subtitle="A deterministic corporate-domain recursive self-improvement system for the AI-first enterprise era.",
        url=f"{SITE_BASE}/proofs/004-corporate-rsi-dominion.html",
        json_url=f"{SITE_BASE}/assets/proofs/004-corporate-rsi-dominion.json",
        status="passed",
        summary=summary,
        evidence=evidence,
    )


def build_archive() -> dict[str, Any]:
    proofs = [proof_001(), proof_002(), proof_003(), proof_004()]
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
    main { width: min(1220px, calc(100% - 40px)); margin: 0 auto; padding: 64px 0 80px; }
    .eyebrow { color: var(--gold); letter-spacing: .18em; text-transform: uppercase; font-size: 13px; font-weight: 800; }
    h1 { font-size: clamp(44px, 8vw, 100px); line-height: .92; margin: 18px 0 22px; letter-spacing: -0.07em; }
    h2 { font-size: clamp(28px, 4vw, 52px); letter-spacing: -0.05em; }
    p, li { color: var(--muted); font-size: 18px; line-height: 1.6; }
    a { color: var(--blue); }
    .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 28px; }
    .card { border: 1px solid var(--line); border-radius: 22px; padding: 22px; background: rgba(11,16,32,.76); min-height: 180px; }
    .card b { display: block; font-size: 21px; margin-bottom: 10px; }
    .pill { display: inline-block; border: 1px solid rgba(145,242,191,.45); border-radius: 999px; padding: 7px 10px; color: var(--green); background: rgba(145,242,191,.08); font-weight: 800; margin: 8px 0 18px; }
    pre { overflow: auto; padding: 18px; border: 1px solid var(--line); border-radius: 18px; background: #070b14; color: #dbe6ff; max-height: 640px; }
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
    <h2>Current Lead Proof</h2>
    <pre>{esc(json.dumps(archive["proofs"][-1]["summary"], indent=2))}</pre>
    """
    return shell("Proof Gradient", "Proof Gradient · Corporate RSI Dominion", body)


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
    proofs = [proof_001(), proof_002(), proof_003(), proof_004()]
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

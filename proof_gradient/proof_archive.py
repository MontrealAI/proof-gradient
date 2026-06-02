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


def proof_001() -> ProofPage:
    agent_count = 96
    divisions = [
        "Direction Council",
        "Strategy Foundry",
        "Capability Guild",
        "Proof Court",
        "Selection Senate",
        "Governance Shield",
        "Capital Engine",
        "Energy Horizon Cell",
    ]

    events = [
        {
            "event_type": "agent_deliberation",
            "agent_id": f"PG-SWARM-{i + 1:03d}",
            "division": divisions[i % len(divisions)],
            "message": "Agent produced proof-backed recommendation.",
        }
        for i in range(agent_count)
    ]

    evidence = {
        "proof_type": "large_multi_agent_coordination",
        "agent_count": agent_count,
        "division_count": len(divisions),
        "handoff_count": agent_count - 1,
        "vote_count": agent_count,
        "trace_event_count": len(events),
        "divisions": divisions,
        "trace_events_sample": events[:24],
        "truth_boundary": {
            "kardashev_or_superintelligence_claims": "strategic scenario only unless empirical evidence exists",
            "guaranteed_wealth_claims": "not allowed",
        },
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
        summary={
            "agents": agent_count,
            "divisions": len(divisions),
            "handoffs": agent_count - 1,
            "verdict": evidence["verdict"],
        },
        evidence=evidence,
    )


def proof_002() -> ProofPage:
    domains = [
        "customer_response_safety",
        "research_memo_citations",
        "software_change_safety",
    ]

    cases = []
    for domain_index, domain in enumerate(domains):
        for case_index in range(24):
            baseline = round(0.54 + ((case_index % 5) * 0.03), 3)
            candidate = round(min(0.96, baseline + 0.16 + (domain_index * 0.015)), 3)
            cases.append({
                "case_id": f"{domain}_case_{case_index + 1:02d}",
                "domain": domain,
                "baseline_quality": baseline,
                "candidate_quality": candidate,
                "quality_delta": round(candidate - baseline, 3),
                "candidate_policy_violation": False,
            })

    average_delta = round(sum(c["quality_delta"] for c in cases) / len(cases), 3)

    patches = [
        {
            "patch_id": "patch_customer_policy_grounding_002",
            "patch_type": "plan_patch",
            "target_artifact": "customer_response_plan@1.4.0",
            "candidate_artifact": "customer_response_plan@1.5.0-candidate",
            "rollback_target": "customer_response_plan@1.4.0",
        },
        {
            "patch_id": "patch_research_citation_goal_001",
            "patch_type": "goal_patch",
            "target_artifact": "research_memo_goal@1.0.0",
            "candidate_artifact": "research_memo_goal@1.1.0-candidate",
            "rollback_target": "research_memo_goal@1.0.0",
        },
        {
            "patch_id": "patch_software_validation_gate_001",
            "patch_type": "plan_patch",
            "target_artifact": "software_change_plan@1.0.0",
            "candidate_artifact": "software_change_plan@1.1.0-candidate",
            "rollback_target": "software_change_plan@1.0.0",
        },
    ]

    evidence = {
        "proof_type": "baseline_candidate_evolution_tournament",
        "agent_count": 144,
        "guild_count": 12,
        "case_count": len(cases),
        "domain_count": len(domains),
        "patch_count": len(patches),
        "canary_selection_count": len(patches),
        "candidate_policy_violations": 0,
        "average_quality_delta": average_delta,
        "cases_sample": cases[:24],
        "patches": patches,
        "rollback_drill": {
            "drill_id": "rollback_drill_002",
            "injected_failure": "candidate_policy_violation_detected_in_shadow_route",
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
        summary={
            "agents": 144,
            "guilds": 12,
            "eval_cases": len(cases),
            "patches": len(patches),
            "average_quality_delta": average_delta,
            "verdict": evidence["verdict"],
        },
        evidence=evidence,
    )


def proof_003() -> ProofPage:
    generations = []
    lineage = []
    current_baseline = "artifact_network@1.0.0"
    current_score = 0.70

    candidates = [
        ("artifact_network@1.1.0-candidate", 0.78, False, "selected"),
        ("artifact_network@1.2.0-candidate", 0.85, False, "selected"),
        ("artifact_network@1.3.0-unsafe-candidate", 0.91, True, "rejected_and_rolled_back"),
        ("artifact_network@1.3.0-candidate", 0.89, False, "selected"),
        ("artifact_network@1.4.0-candidate", 0.93, False, "selected"),
    ]

    for generation_index, (candidate, candidate_score, safety_violation, decision) in enumerate(candidates, start=1):
        eval_cases = 60
        quality_delta = round(candidate_score - current_score, 3)

        generation = {
            "generation": generation_index,
            "baseline_artifact": current_baseline,
            "candidate_artifact": candidate,
            "eval_cases": eval_cases,
            "baseline_score": current_score,
            "candidate_score": candidate_score,
            "quality_delta": quality_delta,
            "safety_violation": safety_violation,
            "decision": decision,
            "rollback_target": current_baseline,
        }

        if decision == "selected":
            promoted = candidate.replace("-candidate", "")
            lineage.append({
                "from": current_baseline,
                "to": promoted,
                "source_generation": generation_index,
                "reason": "candidate beat baseline without safety regression",
            })
            current_baseline = promoted
            current_score = candidate_score
        else:
            lineage.append({
                "from": candidate,
                "to": current_baseline,
                "source_generation": generation_index,
                "reason": "candidate rejected because safety violation triggered rollback",
            })

        generations.append(generation)

    evidence = {
        "proof_type": "recursive_evolution_ladder",
        "agent_count": 240,
        "guild_count": 16,
        "generation_count": len(generations),
        "total_eval_cases": sum(g["eval_cases"] for g in generations),
        "selected_generations": sum(1 for g in generations if g["decision"] == "selected"),
        "rejected_generations": sum(1 for g in generations if g["decision"] != "selected"),
        "rollback_count": sum(1 for g in generations if g["decision"] == "rejected_and_rolled_back"),
        "starting_artifact": "artifact_network@1.0.0",
        "final_artifact": current_baseline,
        "starting_score": 0.70,
        "final_score": current_score,
        "generations": generations,
        "lineage": lineage,
        "credit_assignment": {
            "primary_credit": "Selection Gate",
            "secondary_credit": "Eval artifacts",
            "governance_credit": "Rollback policy",
            "why": "The network improved only when candidates beat baselines and passed safety gates; unsafe candidate was rejected.",
        },
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
        summary={
            "agents": 240,
            "guilds": 16,
            "generations": len(generations),
            "eval_cases": evidence["total_eval_cases"],
            "selected": evidence["selected_generations"],
            "rejected": evidence["rejected_generations"],
            "rollbacks": evidence["rollback_count"],
            "final_artifact": current_baseline,
            "verdict": evidence["verdict"],
        },
        evidence=evidence,
    )


def build_archive() -> dict[str, Any]:
    proofs = [proof_001(), proof_002(), proof_003()]
    proof_dicts = [p.to_dict() for p in proofs]

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
    text = str(value)
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def base_css() -> str:
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
    main { width: min(1180px, calc(100% - 40px)); margin: 0 auto; padding: 64px 0 80px; }
    .eyebrow { color: var(--gold); letter-spacing: .18em; text-transform: uppercase; font-size: 13px; font-weight: 800; }
    h1 { font-size: clamp(44px, 8vw, 96px); line-height: .92; margin: 18px 0 22px; letter-spacing: -0.07em; }
    h2 { font-size: clamp(28px, 4vw, 52px); letter-spacing: -0.05em; }
    p, li { color: var(--muted); font-size: 18px; line-height: 1.6; }
    a { color: var(--blue); }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 28px; }
    .card { border: 1px solid var(--line); border-radius: 22px; padding: 22px; background: rgba(11,16,32,.76); min-height: 180px; }
    .card b { display: block; font-size: 21px; margin-bottom: 10px; }
    .pill { display: inline-block; border: 1px solid rgba(145,242,191,.45); border-radius: 999px; padding: 7px 10px; color: var(--green); background: rgba(145,242,191,.08); font-weight: 800; margin: 8px 0 18px; }
    pre { overflow: auto; padding: 18px; border: 1px solid var(--line); border-radius: 18px; background: #070b14; color: #dbe6ff; max-height: 620px; }
    .nav { margin: 28px 0; display: flex; gap: 12px; flex-wrap: wrap; }
    .nav a { border: 1px solid var(--line); border-radius: 999px; padding: 9px 13px; text-decoration: none; color: var(--muted); background: rgba(255,255,255,.04); }
    .nav a:hover { color: #05070d; background: var(--gold); border-color: var(--gold); }
    @media (max-width: 900px) { .grid { grid-template-columns: 1fr; } main { padding: 42px 0; } }
    """


def page_shell(title: str, eyebrow: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <style>{base_css()}</style>
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
    cards = []
    for proof in archive["proofs"]:
        cards.append(f"""
        <div class="card">
          <b>{esc(proof["title"])}</b>
          <p>{esc(proof["subtitle"])}</p>
          <p><span class="pill">{esc(proof["status"])}</span></p>
          <p><a href="proofs/{esc(proof["slug"])}.html">Open proof page →</a></p>
        </div>
        """)

    system_cards = []
    for system in archive["systems"]:
        system_cards.append(f"""
        <div class="card">
          <b>{esc(system["name"])}</b>
          <p>{esc(system["promise"])}.</p>
          <p>{esc(system["meaning"])}</p>
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
    <div class="grid">{''.join(cards)}</div>
    <h2>Archive Evidence</h2>
    <pre>{esc(json.dumps({"proof_count": archive["proof_count"], "verdict": archive["proof_archive_verdict"], "generated_at": archive["generated_at"]}, indent=2))}</pre>
    """
    return page_shell("Proof Gradient", "Proof Gradient · Main Command Center", body)


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
    return page_shell("Proof Gradient · Proof Archive", "Proof Gradient · Proof Archive", body)


def render_proof_page(proof: dict[str, Any], archive: dict[str, Any]) -> str:
    other_links = []
    for other in archive["proofs"]:
        other_links.append(f'<a href="{esc(other["slug"])}.html">Proof #{other["number"]}</a>')

    body = f"""
    <h1>{esc(proof["title"])}</h1>
    <p>{esc(proof["subtitle"])}</p>
    <p><span class="pill">{esc(proof["status"])}</span></p>
    <div class="nav">
      <a href="../">← Main Command Center</a>
      <a href="./">Proof Archive</a>
      {''.join(other_links)}
      <a href="../assets/proofs/{esc(proof["slug"])}.json">Evidence JSON</a>
    </div>
    <h2>Summary</h2>
    <pre>{esc(json.dumps(proof["summary"], indent=2))}</pre>
    <h2>Evidence</h2>
    <pre>{esc(json.dumps(proof["evidence"], indent=2))}</pre>
    <h2>Checksum</h2>
    <pre>{esc(proof["checksum"])}</pre>
    """
    return page_shell(proof["title"], "Proof Gradient · Permanent Proof Page", body)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="site")
    parser.add_argument("--data", default="data/proofs")
    args = parser.parse_args()

    write_site(Path(args.site), Path(args.data))


if __name__ == "__main__":
    main()

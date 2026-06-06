import {
  DEMO_CASES,
  createInitialState,
  executeWorkflow,
  evaluateRun,
  createProofRecord,
  runBenchmark,
  proposeImprovement,
  approveImprovement,
  rollback,
  buildProofGraph,
  createPublicSafeProofCard,
  findVersionById,
  audit
} from "./enterprise-core.mjs";

const KEY = "goalos_cloud_mvp_v0_2_state";
let state = load();

function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || createInitialState(); } catch { return createInitialState(); } }
function save(){ localStorage.setItem(KEY, JSON.stringify(state)); }
function log(action, detail, target=null){ state.auditLogs.unshift(audit("demo-user", action, detail, target)); state.auditLogs = state.auditLogs.slice(0,160); save(); }
function el(id){ return document.getElementById(id); }
function pretty(x){ return JSON.stringify(x, null, 2); }
function active(){ return findVersionById(state, state.activeWorkflowVersionId); }
function activeCase(){ return DEMO_CASES.find(c => c.id === el("caseSelect")?.value) || DEMO_CASES[0]; }

function tab(name){
  document.querySelectorAll("[data-tab]").forEach(b => b.classList.toggle("active", b.dataset.tab === name));
  document.querySelectorAll("[data-panel]").forEach(p => p.hidden = p.dataset.panel !== name);
}
function render(){
  renderMetrics(); renderGovernance(); renderStudio(); renderRun(); renderEval(); renderProof(); renderImprove(); renderVersions(); renderGraph(); renderAdmin();
}
function renderMetrics(){
  const latestBench = state.benchmarkRuns[0];
  const graph = buildProofGraph(state);
  el("metrics").innerHTML = [
    ["Versions", state.workflows[0].versions.length],
    ["Runs", state.runs.length],
    ["Proof", state.proofRecords.length],
    ["Proposals", state.improvementProposals.length],
    ["Graph nodes", graph.nodes.length],
    ["Latest pass", latestBench ? latestBench.passRate + "%" : "—"]
  ].map(([a,b]) => `<div class="metric"><strong>${b}</strong><span>${a}</span></div>`).join("");
}
function renderGovernance(){
  el("orgJson").textContent = pretty({ organization: state.organization, workspace: state.workspace, users: state.users });
  el("policyJson").textContent = pretty(state.policies[0]);
  el("memoryJson").textContent = pretty(state.memoryItems);
  el("modelJson").textContent = pretty(state.modelProviders);
}
function renderStudio(){
  const found = active();
  el("versionSelect").innerHTML = state.workflows[0].versions.map(v => `<option value="${v.id}" ${v.id === state.activeWorkflowVersionId ? "selected" : ""}>${v.version} — ${v.status}</option>`).join("");
  el("workflowSummary").innerHTML = `<h3>${state.workflows[0].name}</h3><p><b>Active:</b> ${found.version.version} · <b>Status:</b> ${found.version.status} · <b>Risk:</b> ${found.version.riskLevel}</p><p>${found.version.definition.goal}</p>`;
  el("workflowJson").value = pretty(found.version);
}
function renderRun(){
  el("caseSelect").innerHTML = DEMO_CASES.map(c => `<option value="${c.id}">${c.title} — ${c.type} — ${c.dataClass}</option>`).join("");
  const latest = state.runs[0];
  el("latestRun").textContent = latest ? pretty(latest) : "No run yet.";
}
function renderEval(){
  const latest = state.evaluations[0];
  el("latestEval").textContent = latest ? pretty(latest) : "No evaluation yet.";
}
function renderProof(){
  el("proofRows").innerHTML = state.proofRecords.map(p => `<tr><td>${p.createdAt.slice(0,19).replace("T"," ")}</td><td>${p.workflowVersion}</td><td>${p.inputSummary}</td><td>${p.approvalStatus}</td><td>${p.finalDecision}</td></tr>`).join("") || `<tr><td colspan="5">No proof records.</td></tr>`;
  el("latestProof").textContent = state.proofRecords[0] ? pretty(state.proofRecords[0]) : "No proof yet.";
}
function renderImprove(){
  el("latestBenchmark").textContent = state.benchmarkRuns[0] ? pretty(summaryBenchmark(state.benchmarkRuns[0])) : "No benchmark yet.";
  el("latestProposal").textContent = state.improvementProposals[0] ? pretty(state.improvementProposals[0]) : "No proposal yet.";
  const canApprove = state.improvementProposals[0]?.status === "pending-approval";
  el("approveBtn").disabled = !canApprove;
}
function renderVersions(){
  el("versionsRows").innerHTML = state.workflows[0].versions.map(v => `<tr><td>${v.version}</td><td>${v.status}</td><td>${v.approvalStatus}</td><td>${v.rollbackOption || "—"}</td><td>${v.changeSummary}</td></tr>`).join("");
  const b10 = state.benchmarkRuns.find(b => b.workflowVersion === "1.0.0");
  const b11 = state.benchmarkRuns.find(b => b.workflowVersion === "1.1.0");
  el("versionCompare").textContent = pretty({ v1_0: b10 ? summaryBenchmark(b10) : null, v1_1: b11 ? summaryBenchmark(b11) : null, rollbackTarget: "wfv_1_0_0" });
}
function renderGraph(){
  const graph = buildProofGraph(state);
  el("graphJson").textContent = pretty(graph);
  el("graphSummary").innerHTML = `<p><b>${graph.nodes.length}</b> nodes · <b>${graph.edges.length}</b> edges</p><p>workflow → version → run → evaluation → proof → proposal → approval</p>`;
}
function renderAdmin(){
  el("auditLog").innerHTML = state.auditLogs.map(a => `<li><b>${a.time.slice(0,19).replace("T"," ")}</b> — ${a.action}: ${a.detail}</li>`).join("");
  el("stateExport").value = pretty(state);
}
function summaryBenchmark(b){ return { version: b.workflowVersion, avgScore: b.avgScore, passRate: b.passRate, refundPolicyCompliance: b.refundPolicyCompliance, caseCount: b.caseCount, createdAt: b.createdAt }; }

function runCase(){
  const run = executeWorkflow(state, activeCase());
  const ev = evaluateRun(state, run);
  const proof = createProofRecord(state, run, ev);
  state.runs.unshift(run); state.evaluations.unshift(ev); state.proofRecords.unshift(proof);
  log("workflow_run", `${run.workflowVersion} ${run.input.caseId} score ${ev.overallScore}`, run.id);
  save(); render(); tab("run");
}
function benchmark(){
  const b = runBenchmark(state, state.activeWorkflowVersionId);
  state.benchmarkRuns.unshift(b);
  state.runs.unshift(...b.runs.reverse()); state.evaluations.unshift(...b.evaluations.reverse()); state.proofRecords.unshift(...b.proofRecords.reverse());
  log("benchmark_run", `${b.workflowVersion}: pass ${b.passRate}%, refund policy ${b.refundPolicyCompliance}%`, b.id);
  save(); render(); tab("improve");
}
function proposal(){
  let b = state.benchmarkRuns.find(x => x.workflowVersionId === state.activeWorkflowVersionId);
  if (!b){ b = runBenchmark(state, state.activeWorkflowVersionId); state.benchmarkRuns.unshift(b); }
  const p = proposeImprovement(state, b);
  state.improvementProposals.unshift(p);
  log("improvement_proposal", p.problemDetected, p.id);
  save(); render(); tab("improve");
}
function approve(){
  const p = state.improvementProposals[0];
  if (!p || p.status !== "pending-approval") return;
  const res = approveImprovement(state, p);
  state.approvals.unshift(res.approval); state.deployments.unshift(res.deployment);
  const b = runBenchmark(state, res.approvedVersion.id);
  state.benchmarkRuns.unshift(b);
  state.runs.unshift(...b.runs.reverse()); state.evaluations.unshift(...b.evaluations.reverse()); state.proofRecords.unshift(...b.proofRecords.reverse());
  log("proposal_approved", `Approved ${res.approvedVersion.version} with rollback target ${res.approval.rollbackTargetVersionId}`, res.approval.id);
  save(); render(); tab("versions");
}
function doRollback(){
  const ev = rollback(state);
  log("rollback", "Rollback target selected: wfv_1_0_0", ev.id);
  save(); render(); tab("versions");
}
function download(filename, text, type="application/json"){
  const blob = new Blob([text], { type });
  const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = filename; a.click(); URL.revokeObjectURL(a.href);
}
function exportGraph(){ download("goalos_proof_graph.json", pretty(buildProofGraph(state))); log("export_graph", "Proof Graph exported."); }
function proofCard(){ download("goalos_public_safe_proof_card_001.json", pretty(createPublicSafeProofCard(state))); log("export_public_safe_proof_card", "Public-safe proof card exported."); }
function report(){
  const b10 = state.benchmarkRuns.find(b => b.workflowVersion === "1.0.0");
  const b11 = state.benchmarkRuns.find(b => b.workflowVersion === "1.1.0");
  const txt = `GoalOS Cloud MVP 0.2 Executive Proof Room Report

Loop:
Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run

Workflow family:
Customer Support Reply Workflow

v1.0:
${b10 ? `${b10.passRate}% pass rate, ${b10.refundPolicyCompliance}% refund-policy compliance, average score ${b10.avgScore}` : "not run"}

v1.1:
${b11 ? `${b11.passRate}% pass rate, ${b11.refundPolicyCompliance}% refund-policy compliance, average score ${b11.avgScore}` : "not approved/run"}

Proof records:
${state.proofRecords.length}

Safe boundary:
GoalOS does not modify AI models. It improves workflows around AI through instructions, checks, scorecards, proof records, versions, approvals, monitoring, and rollback.

Claims avoided:
No ROI guarantee. No productivity guarantee. No compliance certification. No autonomous sending claim. No model self-modification claim.
`;
  download("goalos_cloud_mvp_executive_report.txt", txt, "text/plain"); log("export_report", "Executive report exported.");
}
function exportState(){ download("goalos_cloud_mvp_state.json", pretty(state)); }
function reset(){ if(!confirm("Reset demo state?")) return; state = createInitialState(); save(); render(); log("reset", "State reset."); }

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-tab]").forEach(btn => btn.addEventListener("click", () => tab(btn.dataset.tab)));
  el("versionSelect").addEventListener("change", e => { state.activeWorkflowVersionId = e.target.value; save(); render(); });
  el("runBtn").addEventListener("click", runCase);
  el("benchmarkBtn").addEventListener("click", benchmark);
  el("proposalBtn").addEventListener("click", proposal);
  el("approveBtn").addEventListener("click", approve);
  el("rollbackBtn").addEventListener("click", doRollback);
  el("proofCardBtn").addEventListener("click", proofCard);
  el("reportBtn").addEventListener("click", report);
  el("graphBtn").addEventListener("click", exportGraph);
  el("stateBtn").addEventListener("click", exportState);
  el("resetBtn").addEventListener("click", reset);
  tab("governance"); render();
});

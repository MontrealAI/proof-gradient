import {
  SAMPLE_CASES,
  initialWorkflow,
  runWorkflow,
  evaluateRun,
  createProofRecord,
  benchmarkWorkflow,
  detectFailurePattern,
  proposeImprovement,
  approveProposal,
  createPublicSafeProofCard,
  exportState
} from "./goalos-core.mjs";

const STORAGE_KEY = "goalos_cloud_mvp_0_1_state";

function defaultState() {
  const workflow = initialWorkflow();
  return {
    organization: {
      id: "org_demo",
      name: "GoalOS Demo Organization",
      workspace: "Proof Room Demo",
      role: "Owner / Reviewer"
    },
    workflows: [workflow],
    activeWorkflowVersion: workflow.version,
    activeCaseId: SAMPLE_CASES[0].id,
    runs: [],
    evaluations: [],
    proofRecords: [],
    benchmarks: [],
    proposals: [],
    approvals: [],
    auditLog: [{
      time: new Date().toISOString(),
      action: "mvp_initialized",
      actor: "system",
      detail: "GoalOS Cloud MVP initialized with Customer Support Reply Workflow v1.0."
    }]
  };
}

let state = loadState();

function loadState() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved ? JSON.parse(saved) : defaultState();
  } catch {
    return defaultState();
  }
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function log(action, detail) {
  state.auditLog.unshift({
    time: new Date().toISOString(),
    action,
    actor: "demo-user",
    detail
  });
  state.auditLog = state.auditLog.slice(0, 100);
  saveState();
}

function currentWorkflow() {
  return state.workflows.find(w => w.version === state.activeWorkflowVersion) || state.workflows[0];
}

function currentCase() {
  return SAMPLE_CASES.find(c => c.id === state.activeCaseId) || SAMPLE_CASES[0];
}

function el(id) { return document.getElementById(id); }
function pretty(obj) { return JSON.stringify(obj, null, 2); }

function setTab(name) {
  document.querySelectorAll("[data-tab]").forEach(btn => btn.classList.toggle("active", btn.dataset.tab === name));
  document.querySelectorAll("[data-panel]").forEach(panel => panel.hidden = panel.dataset.panel !== name);
}

function render() {
  renderStatus();
  renderStudio();
  renderRun();
  renderProofRoom();
  renderImprovement();
  renderVersions();
  renderAdmin();
}

function renderStatus() {
  const latestBenchmark = state.benchmarks[0];
  const approved = state.workflows.find(w => w.status.includes("approved"));
  el("statusCards").innerHTML = `
    <div class="metric"><strong>${state.workflows.length}</strong><span>Workflow versions</span></div>
    <div class="metric"><strong>${state.runs.length}</strong><span>Runs</span></div>
    <div class="metric"><strong>${state.proofRecords.length}</strong><span>Proof records</span></div>
    <div class="metric"><strong>${latestBenchmark ? latestBenchmark.passRate + "%" : "—"}</strong><span>Latest pass rate</span></div>
    <div class="metric"><strong>${approved ? approved.version : "—"}</strong><span>Approved version</span></div>
  `;
}

function renderStudio() {
  const workflow = currentWorkflow();
  el("workflowVersionSelect").innerHTML = state.workflows.map(w => `<option value="${w.version}" ${w.version === state.activeWorkflowVersion ? "selected" : ""}>${w.name} ${w.version} — ${w.status}</option>`).join("");
  el("workflowJson").value = pretty(workflow);
  el("workflowSummary").innerHTML = `
    <h3>${workflow.name}</h3>
    <p><b>Version:</b> ${workflow.version} · <b>Status:</b> ${workflow.status} · <b>Risk:</b> ${workflow.riskLevel}</p>
    <p>${workflow.goal}</p>
    <div class="pillrow">${workflow.checks.map(c => `<span>${c}</span>`).join("")}</div>
  `;
}

function renderRun() {
  el("caseSelect").innerHTML = SAMPLE_CASES.map(c => `<option value="${c.id}" ${c.id === state.activeCaseId ? "selected" : ""}>${c.title} — ${c.issueType}</option>`).join("");
  const input = currentCase();
  el("caseDetails").innerHTML = `<h3>${input.title}</h3><p><b>Issue:</b> ${input.issueType} · <b>Risk:</b> ${input.risk}</p><blockquote>${input.customerMessage}</blockquote><p><b>Expected qualities:</b> ${input.expectedQualities.join(", ")}</p>`;
  const latestRun = state.runs[0];
  const latestEval = state.evaluations[0];
  el("latestRun").textContent = latestRun ? pretty(latestRun) : "No run yet.";
  el("latestEvaluation").textContent = latestEval ? pretty(latestEval) : "No evaluation yet.";
}

function renderProofRoom() {
  el("proofTable").innerHTML = state.proofRecords.map(p => `
    <tr>
      <td>${p.createdAt.slice(0,19).replace("T", " ")}</td>
      <td>${p.workflowVersion}</td>
      <td>${p.inputSummary}</td>
      <td>${p.approvalStatus}</td>
      <td>${p.finalDecision}</td>
    </tr>
  `).join("") || `<tr><td colspan="5">No proof records yet.</td></tr>`;
  el("proofJson").textContent = state.proofRecords.length ? pretty(state.proofRecords[0]) : "Run a workflow to generate proof.";
}

function renderImprovement() {
  const latestBenchmark = state.benchmarks[0];
  const latestProposal = state.proposals[0];
  el("benchmarkJson").textContent = latestBenchmark ? pretty({
    workflowVersion: latestBenchmark.workflowVersion,
    avgScore: latestBenchmark.avgScore,
    passRate: latestBenchmark.passRate,
    refundPolicyCompliance: latestBenchmark.refundPolicyCompliance,
    runCount: latestBenchmark.runCount,
    createdAt: latestBenchmark.createdAt
  }) : "No benchmark yet.";
  el("proposalJson").textContent = latestProposal ? pretty(latestProposal) : "No improvement proposal yet.";
  el("approveProposalBtn").disabled = !latestProposal || latestProposal.status !== "pending-approval";
}

function renderVersions() {
  el("versionTable").innerHTML = state.workflows.map(w => `
    <tr>
      <td>${w.version}</td>
      <td>${w.status}</td>
      <td>${w.riskLevel}</td>
      <td>${w.versionNotes || ""}</td>
    </tr>
  `).join("");
  const v10 = state.benchmarks.find(b => b.workflowVersion === "1.0.0");
  const v11 = state.benchmarks.find(b => b.workflowVersion === "1.1.0");
  el("comparisonJson").textContent = pretty({
    v1_0: v10 ? { avgScore: v10.avgScore, passRate: v10.passRate, refundPolicyCompliance: v10.refundPolicyCompliance } : null,
    v1_1: v11 ? { avgScore: v11.avgScore, passRate: v11.passRate, refundPolicyCompliance: v11.refundPolicyCompliance } : null,
    rollbackTarget: "1.0.0"
  });
}

function renderAdmin() {
  el("auditLog").innerHTML = state.auditLog.map(a => `<li><b>${a.time.slice(0,19).replace("T", " ")}</b> — ${a.action}: ${a.detail}</li>`).join("");
  el("exportJson").value = exportState(state);
}

function runCurrentCase() {
  const workflow = currentWorkflow();
  const input = currentCase();
  const run = runWorkflow(workflow, input);
  const evaluation = evaluateRun(workflow, input, run);
  const proof = createProofRecord(workflow, input, run, evaluation);
  state.runs.unshift(run);
  state.evaluations.unshift(evaluation);
  state.proofRecords.unshift(proof);
  log("workflow_run_completed", `${workflow.name} ${workflow.version} ran on ${input.id}; score ${evaluation.overallScore}.`);
  render();
  setTab("run");
}

function runBenchmark() {
  const workflow = currentWorkflow();
  const result = benchmarkWorkflow(workflow);
  state.benchmarks.unshift(result);
  state.runs.unshift(...result.runs.reverse());
  state.evaluations.unshift(...result.evaluations.reverse());
  state.proofRecords.unshift(...result.proofRecords.reverse());
  log("benchmark_completed", `${workflow.version}: pass ${result.passRate}%, refund compliance ${result.refundPolicyCompliance}%.`);
  saveState();
  render();
  setTab("improve");
}

function generateProposal() {
  let benchmark = state.benchmarks.find(b => b.workflowVersion === currentWorkflow().version);
  if (!benchmark) {
    benchmark = benchmarkWorkflow(currentWorkflow());
    state.benchmarks.unshift(benchmark);
  }
  const pattern = detectFailurePattern(benchmark);
  const proposal = proposeImprovement(currentWorkflow(), pattern);

  const proposedBenchmark = benchmarkWorkflow(proposal.proposedWorkflow);
  proposal.testResults = {
    proposedAvgScore: proposedBenchmark.avgScore,
    proposedPassRate: proposedBenchmark.passRate,
    proposedRefundPolicyCompliance: proposedBenchmark.refundPolicyCompliance
  };
  proposal.benchmarkComparison = {
    current: {
      version: benchmark.workflowVersion,
      avgScore: benchmark.avgScore,
      passRate: benchmark.passRate,
      refundPolicyCompliance: benchmark.refundPolicyCompliance
    },
    proposed: {
      version: proposal.proposedVersion,
      avgScore: proposedBenchmark.avgScore,
      passRate: proposedBenchmark.passRate,
      refundPolicyCompliance: proposedBenchmark.refundPolicyCompliance
    }
  };
  state.proposals.unshift(proposal);
  state.benchmarks.unshift(proposedBenchmark);
  log("improvement_proposal_created", `${proposal.proposalId}: ${proposal.problemDetected}`);
  saveState();
  render();
}

function approveLatestProposal() {
  const proposal = state.proposals[0];
  if (!proposal || proposal.status !== "pending-approval") return;
  const approval = approveProposal(proposal);
  proposal.status = "approved";
  state.approvals.unshift(approval);
  state.workflows.unshift(approval.approvedWorkflow);
  state.activeWorkflowVersion = approval.approvedWorkflow.version;

  const benchmark = benchmarkWorkflow(approval.approvedWorkflow);
  state.benchmarks.unshift(benchmark);
  state.runs.unshift(...benchmark.runs.reverse());
  state.evaluations.unshift(...benchmark.evaluations.reverse());
  state.proofRecords.unshift(...benchmark.proofRecords.reverse());

  log("proposal_approved_and_deployed", `Approved ${approval.approvedWorkflow.version}; rollback target ${approval.rollbackTarget}.`);
  saveState();
  render();
  setTab("versions");
}

function rollbackToV10() {
  if (!state.workflows.find(w => w.version === "1.0.0")) return;
  state.activeWorkflowVersion = "1.0.0";
  log("rollback_selected", "Active workflow set back to v1.0.0. This demo preserves all versions.");
  saveState();
  render();
}

function generateProofCard() {
  const before = state.benchmarks.find(b => b.workflowVersion === "1.0.0");
  const after = state.benchmarks.find(b => b.workflowVersion === "1.1.0");
  const card = createPublicSafeProofCard(state.proofRecords, before, after);
  const blob = new Blob([pretty(card)], { type: "application/json" });
  downloadBlob(blob, "goalos_public_safe_proof_card_001.json");
  log("public_safe_proof_card_exported", "Exported public-safe proof card.");
}

function downloadReport() {
  const before = state.benchmarks.find(b => b.workflowVersion === "1.0.0");
  const after = state.benchmarks.find(b => b.workflowVersion === "1.1.0");
  const report = `GoalOS Cloud MVP 0.1 Proof Room Report

Loop:
Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run

Workflow:
Customer Support Reply Workflow

Versions:
${state.workflows.map(w => `- ${w.version}: ${w.status} — ${w.versionNotes}`).join("\n")}

Benchmark summary:
v1.0: ${before ? `${before.passRate}% pass rate, ${before.refundPolicyCompliance}% refund-policy compliance` : "not run"}
v1.1: ${after ? `${after.passRate}% pass rate, ${after.refundPolicyCompliance}% refund-policy compliance` : "not approved/run"}

Proof records:
${state.proofRecords.length}

Safe boundary:
GoalOS does not modify AI models. It improves workflows around AI through instructions, checks, scorecards, proof records, versions, approvals, monitoring, and rollback.

Claims avoided:
No ROI guarantee. No productivity guarantee. No compliance certification. No autonomous sending claim. No model self-modification claim.
`;
  downloadBlob(new Blob([report], { type: "text/plain" }), "goalos_proof_room_report.txt");
  log("proof_room_report_downloaded", "Downloaded text proof report.");
}

function downloadBlob(blob, filename) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = filename;
  a.click();
  URL.revokeObjectURL(a.href);
}

function downloadState() {
  downloadBlob(new Blob([exportState(state)], { type: "application/json" }), "goalos_cloud_mvp_state.json");
}

function resetDemo() {
  if (!confirm("Reset GoalOS Cloud MVP demo state?")) return;
  state = defaultState();
  saveState();
  render();
  log("demo_reset", "Demo state reset.");
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-tab]").forEach(btn => btn.addEventListener("click", () => setTab(btn.dataset.tab)));
  el("workflowVersionSelect").addEventListener("change", e => { state.activeWorkflowVersion = e.target.value; saveState(); render(); });
  el("caseSelect").addEventListener("change", e => { state.activeCaseId = e.target.value; saveState(); render(); });
  el("runCaseBtn").addEventListener("click", runCurrentCase);
  el("benchmarkBtn").addEventListener("click", runBenchmark);
  el("proposalBtn").addEventListener("click", generateProposal);
  el("approveProposalBtn").addEventListener("click", approveLatestProposal);
  el("rollbackBtn").addEventListener("click", rollbackToV10);
  el("downloadStateBtn").addEventListener("click", downloadState);
  el("downloadReportBtn").addEventListener("click", downloadReport);
  el("proofCardBtn").addEventListener("click", generateProofCard);
  el("resetBtn").addEventListener("click", resetDemo);
  setTab("studio");
  render();
});

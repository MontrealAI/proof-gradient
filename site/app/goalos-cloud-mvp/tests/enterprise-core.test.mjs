import assert from "node:assert/strict";
import {
  createInitialState,
  DEMO_CASES,
  executeWorkflow,
  evaluateRun,
  createProofRecord,
  runBenchmark,
  proposeImprovement,
  approveImprovement,
  rollback,
  buildProofGraph,
  createPublicSafeProofCard,
  policyDecision
} from "../assets/enterprise-core.mjs";

const state = createInitialState();
const b10 = runBenchmark(state);
assert.equal(b10.workflowVersion, "1.0.0");
assert.ok(b10.refundPolicyCompliance < 90, "v1.0 should reveal refund-policy weakness");

const proposal = proposeImprovement(state, b10);
assert.equal(proposal.status, "pending-approval");
assert.ok(proposal.proposedVersion.definition.rules.join(" ").toLowerCase().includes("refund"));

state.improvementProposals.unshift(proposal);
const result = approveImprovement(state, proposal);
state.approvals.unshift(result.approval);
state.deployments.unshift(result.deployment);
assert.equal(result.approvedVersion.version, "1.1.0");
assert.equal(result.approval.rollbackTargetVersionId, "wfv_1_0_0");

const b11 = runBenchmark(state, result.approvedVersion.id);
assert.ok(b11.refundPolicyCompliance > b10.refundPolicyCompliance, "v1.1 should improve refund policy compliance");
assert.ok(b11.passRate >= b10.passRate, "v1.1 should not regress pass rate in demo");

const confidential = DEMO_CASES.find(c => c.dataClass === "confidential");
const policy = policyDecision(state, confidential, result.approvedVersion);
assert.equal(policy.allowed, false, "external/local provider should be blocked for confidential data");

const run = executeWorkflow(state, DEMO_CASES[0]);
const ev = evaluateRun(state, run);
const proof = createProofRecord(state, run, ev);
state.runs.unshift(run); state.evaluations.unshift(ev); state.proofRecords.unshift(proof);
const graph = buildProofGraph(state);
assert.ok(graph.nodes.length > 0);
assert.ok(graph.edges.length > 0);

const rb = rollback(state);
assert.equal(rb.status, "complete");
assert.equal(state.activeWorkflowVersionId, "wfv_1_0_0");

const card = createPublicSafeProofCard(state);
assert.equal(card.publicSafe, true);
assert.ok(card.claimsAvoided.includes("No model self-modification claim"));

console.log("GoalOS Cloud MVP v0.2 tests passed", {
  v10RefundPolicyCompliance: b10.refundPolicyCompliance,
  v11RefundPolicyCompliance: b11.refundPolicyCompliance,
  graphNodes: graph.nodes.length,
  graphEdges: graph.edges.length
});

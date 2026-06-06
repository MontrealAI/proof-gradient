import assert from "node:assert/strict";
import {
  SAMPLE_CASES,
  initialWorkflow,
  benchmarkWorkflow,
  detectFailurePattern,
  proposeImprovement,
  approveProposal,
  createPublicSafeProofCard
} from "../assets/goalos-core.mjs";

const v10 = initialWorkflow();
const b10 = benchmarkWorkflow(v10, SAMPLE_CASES);
assert.equal(b10.workflowVersion, "1.0.0");
assert.ok(b10.refundPolicyCompliance < 90, "v1.0 should expose refund policy weakness");

const pattern = detectFailurePattern(b10);
assert.equal(pattern.pattern, "refund_policy_failure");

const proposal = proposeImprovement(v10, pattern);
assert.equal(proposal.status, "pending-approval");
assert.ok(proposal.proposedWorkflow.rules.join(" ").toLowerCase().includes("refund"));

const approval = approveProposal(proposal);
const v11 = approval.approvedWorkflow;
assert.equal(v11.version, "1.1.0");

const b11 = benchmarkWorkflow(v11, SAMPLE_CASES);
assert.ok(b11.refundPolicyCompliance > b10.refundPolicyCompliance, "v1.1 should improve refund policy compliance");
assert.ok(b11.passRate >= b10.passRate, "v1.1 should not regress pass rate in demo benchmark");

const card = createPublicSafeProofCard(b11.proofRecords, b10, b11);
assert.equal(card.publicSafe, true);
assert.ok(card.claimsAvoided.includes("No model self-modification claim"));

console.log("GoalOS Cloud MVP tests passed:", {
  v10RefundPolicyCompliance: b10.refundPolicyCompliance,
  v11RefundPolicyCompliance: b11.refundPolicyCompliance,
  v10PassRate: b10.passRate,
  v11PassRate: b11.passRate
});

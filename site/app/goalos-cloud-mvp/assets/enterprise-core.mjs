export const DATA_CLASSES = ["public", "internal", "confidential", "restricted"];

export const DEMO_CASES = [
  { id: "case_refund_001", dataClass: "internal", type: "refund", title: "Refund / access issue", input: "I bought the digital kit but cannot access the files. Can I get a refund?", expected: ["digital product terms", "technical access exception", "human review"] },
  { id: "case_refund_002", dataClass: "internal", type: "refund", title: "Changed mind after download", input: "I downloaded the product but changed my mind. Can you refund me?", expected: ["final sale boundary", "no legal advice", "human review"] },
  { id: "case_access_003", dataClass: "internal", type: "access", title: "Missing file", input: "The ZIP opens but one file seems missing.", expected: ["access support", "replacement path"] },
  { id: "case_claims_004", dataClass: "public", type: "claims", title: "ROI guarantee question", input: "Will this guarantee I save 10 hours per week or make more revenue?", expected: ["no ROI guarantee", "safe claim boundary"] },
  { id: "case_fr_005", dataClass: "internal", type: "onboarding", title: "French beginner", input: "Je suis débutant. Quelle est la première étape pour utiliser RSI Lite?", expected: ["French guidance", "first step"] },
  { id: "case_security_006", dataClass: "confidential", type: "security", title: "Confidential upload blocked", input: "Here is an internal customer file with private details. Can I paste it into a public model?", expected: ["block external provider", "escalation"] }
];

export function createInitialState() {
  const workflow = createWorkflowV1();
  return {
    organization: { id: "org_demo", name: "GoalOS Demo Enterprise", region: "CA", plan: "enterprise-pilot" },
    workspace: { id: "ws_demo", name: "Customer Support Proof Room", organizationId: "org_demo" },
    users: [
      { id: "user_owner", name: "Owner", role: "Owner" },
      { id: "user_reviewer", name: "Reviewer", role: "Reviewer" },
      { id: "user_runner", name: "Runner", role: "Runner" }
    ],
    policies: [defaultPolicy()],
    modelProviders: [
      { id: "provider_local", name: "GoalOS Local Demo Model", classesAllowed: ["public", "internal"], enabled: true },
      { id: "provider_restricted", name: "Restricted Internal Model Placeholder", classesAllowed: ["public", "internal", "confidential"], enabled: true }
    ],
    memoryItems: [
      { id: "mem_terms", type: "product_terms", status: "approved", scope: "workspace", title: "Digital product terms", content: "Digital product with instant access. Sales are final once delivered except where required by law or for duplicate charges / technical access failures.", approvedBy: "user_owner" },
      { id: "mem_boundary", type: "claim_boundary", status: "approved", scope: "workspace", title: "No guaranteed results", content: "No guaranteed income, ROI, productivity, compliance, safety, or business results. Human review required.", approvedBy: "user_owner" },
      { id: "mem_voice", type: "brand_voice", status: "approved", scope: "workspace", title: "Support voice", content: "Calm, clear, direct, practical, no hype.", approvedBy: "user_owner" }
    ],
    workflows: [workflow],
    activeWorkflowVersionId: workflow.versions[0].id,
    runs: [],
    evaluations: [],
    proofRecords: [],
    benchmarkRuns: [],
    improvementProposals: [],
    approvals: [],
    deployments: [],
    rollbackEvents: [],
    auditLogs: [audit("system", "state_initialized", "GoalOS Cloud MVP v0.2 initialized.")]
  };
}

export function defaultPolicy() {
  return {
    id: "policy_default",
    name: "Default enterprise-safe pilot policy",
    noModelSelfModification: true,
    humanApprovalRequiredFor: ["workflow_logic_change", "external_output", "confidential_data", "public_proof", "model_provider_change"],
    providerRestrictions: {
      public: ["provider_local", "provider_restricted"],
      internal: ["provider_local", "provider_restricted"],
      confidential: ["provider_restricted"],
      restricted: []
    },
    externalOutputRequiresReview: true,
    publicProofRequiresRedaction: true,
    noUnsupportedClaims: true,
    noHiddenMemoryUpdates: true,
    noUnapprovedToolCalls: true
  };
}

export function audit(actor, action, detail, target = null) {
  return { id: "audit_" + cryptoId(), time: now(), actor, action, target, detail };
}

export function createWorkflowV1() {
  return {
    id: "wf_support_reply",
    name: "Customer Support Reply Workflow",
    owner: "user_owner",
    riskLevel: "medium",
    productionVersionId: "wfv_1_0_0",
    versions: [{
      id: "wfv_1_0_0",
      version: "1.0.0",
      status: "production-demo",
      author: "GoalOS",
      timestamp: now(),
      changeSummary: "Initial support reply workflow.",
      reasonForChange: "Baseline workflow.",
      riskLevel: "medium",
      approvalStatus: "approved-demo",
      benchmarkScore: null,
      rollbackOption: null,
      definition: {
        goal: "Draft helpful customer support replies for digital product buyers.",
        context: [
          "Buyer may be non-technical.",
          "Products are digital educational products.",
          "Support is limited to access issues, duplicate charges, missing files, or corrupted files."
        ],
        rules: [
          "Be calm, clear, and helpful.",
          "Do not guarantee income, ROI, productivity, compliance, safety, or business results.",
          "Do not provide legal, financial, medical, employment, security, tax, or regulatory advice.",
          "If uncertain, mark the answer for human review."
        ],
        memoryRefs: ["mem_terms", "mem_boundary", "mem_voice"],
        inputs: [{ key: "customer_message", type: "text", required: true }],
        steps: [
          "Classify the buyer issue.",
          "Draft a short answer.",
          "Add one next step.",
          "Add support boundary when relevant."
        ],
        outputFormat: "support_reply",
        checks: [
          "No ROI or income guarantee.",
          "No legal/compliance claim.",
          "Tone is calm and useful.",
          "Uncertainty is marked."
        ],
        proofRequirements: ["claims_made", "claims_avoided", "checks_performed", "review_status", "next_improvement"],
        humanReview: { requiredWhen: ["refund", "billing", "legal", "privacy", "confidential_data"] },
        modelSettings: { providerId: "provider_local", model: "goalos-local-demo-model" },
        toolsAllowed: []
      }
    }]
  };
}

export function latestVersion(workflow) {
  return workflow.versions[0];
}

export function findActiveVersion(state) {
  for (const w of state.workflows) {
    const v = w.versions.find(x => x.id === state.activeWorkflowVersionId);
    if (v) return { workflow: w, version: v };
  }
  return { workflow: state.workflows[0], version: latestVersion(state.workflows[0]) };
}

export function policyDecision(state, caseData, version) {
  const policy = state.policies[0];
  const providerId = version.definition.modelSettings.providerId;
  const allowedProviders = policy.providerRestrictions[caseData.dataClass] || [];
  const allowed = allowedProviders.includes(providerId);
  const reasons = [];
  if (!allowed) reasons.push(`Provider ${providerId} is not allowed for ${caseData.dataClass} data.`);
  if (caseData.dataClass === "confidential" || caseData.dataClass === "restricted") reasons.push("Human review required for sensitive data.");
  if (["refund", "billing", "security"].includes(caseData.type)) reasons.push("Human review required by workflow policy.");
  return {
    allowed,
    blocked: !allowed,
    humanReviewRequired: reasons.length > 0,
    reasons
  };
}

function memoryText(state, version) {
  return version.definition.memoryRefs.map(id => state.memoryItems.find(m => m.id === id)).filter(Boolean).map(m => m.content).join("\n");
}

function hasRefundPolicyRule(version) {
  const def = version.definition;
  return [...def.rules, ...def.steps, ...def.checks].join(" ").toLowerCase().includes("refund") &&
         [...def.rules, ...def.steps, ...def.checks].join(" ").toLowerCase().includes("policy");
}

export function executeWorkflow(state, caseData, actor = "user_runner") {
  const { workflow, version } = findActiveVersion(state);
  const policy = policyDecision(state, caseData, version);
  const run = {
    id: "run_" + cryptoId(),
    organizationId: state.organization.id,
    workspaceId: state.workspace.id,
    workflowId: workflow.id,
    workflowName: workflow.name,
    workflowVersionId: version.id,
    workflowVersion: version.version,
    actor,
    providerId: version.definition.modelSettings.providerId,
    model: version.definition.modelSettings.model,
    input: { caseId: caseData.id, title: caseData.title, dataClass: caseData.dataClass, type: caseData.type, summary: caseData.input.slice(0, 160) },
    status: policy.blocked ? "blocked_by_policy" : "completed",
    policyDecision: policy,
    output: "",
    reasoningSummary: "",
    warnings: [],
    assumptions: ["Demo input is treated as sanitized unless marked confidential."],
    uncertainty: [],
    modelMetadata: { provider: version.definition.modelSettings.providerId, model: version.definition.modelSettings.model, latencyMs: 140, costUsd: 0 },
    createdAt: now()
  };

  if (policy.blocked) {
    run.output = "This input is blocked by policy for the selected model provider. Use an approved internal provider or sanitized data.";
    run.warnings.push("Policy blocked execution.");
    run.reasoningSummary = "Provider/data-class policy prevented execution.";
    return run;
  }

  const refundAware = hasRefundPolicyRule(version);
  const memory = memoryText(state, version);
  if (caseData.type === "refund" && refundAware) {
    run.output = `Thanks for reaching out. I can help check the access or refund-related issue.\n\nBecause this is a digital educational product with instant access, sales are generally final once delivered, except where required by law or for duplicate charges / technical access failures.\n\nNext step: please send the order email and a screenshot or description of the access problem so support can check whether this is a technical access issue.\n\nHuman review required: refund/access cases should be reviewed before a final decision is sent.`;
    run.reasoningSummary = "The issue was classified as refund/access. The workflow used approved digital product terms and added human review.";
    run.uncertainty.push("Final refund/access decision requires human review.");
  } else if (caseData.type === "refund") {
    run.output = "Thanks for reaching out. Please send your order email and we will review the situation. We will do our best to help.";
    run.reasoningSummary = "The workflow recognized a support request but did not apply a specific refund/access policy step.";
    run.warnings.push("Refund/access policy boundary missing.");
  } else if (caseData.type === "claims") {
    run.output = "GoalOS is an educational workflow product. It can help you structure repeated AI work, but it does not guarantee income, ROI, savings, productivity, compliance, safety, or business results. The best next step is to use it on one repeated task and review the result.";
    run.reasoningSummary = "The workflow avoided unsupported ROI and productivity claims.";
  } else if (caseData.type === "onboarding" && /je suis|étape|débutant/i.test(caseData.input)) {
    run.output = "Bonjour — commencez par une seule tâche IA répétée. Ouvrez le guide Start Here, créez le flux v1.0, exécutez-le, notez-le, puis améliorez-le. La revue humaine reste requise avant toute utilisation importante.";
    run.reasoningSummary = "The buyer asked in French, so the output used French beginner guidance.";
  } else if (caseData.type === "security") {
    run.output = "Do not paste private or confidential customer data into an unapproved public AI tool. Use sanitized examples or an approved internal model/provider. Escalate to the workspace owner before proceeding.";
    run.reasoningSummary = "The case was security-sensitive and received a data-boundary response.";
    run.uncertainty.push("Security-sensitive issue requires review.");
  } else {
    run.output = "Thanks for reaching out. Please describe the access issue and include your order email. If a file is missing or corrupted, support can help with access or replacement.";
    run.reasoningSummary = "The workflow created a simple access-support response.";
  }
  run.memoryUsed = version.definition.memoryRefs;
  run.memoryInfluenceSummary = memory.slice(0, 240);
  return run;
}

export function evaluateRun(state, run) {
  const caseData = DEMO_CASES.find(c => c.id === run.input.caseId);
  const { version } = state.workflows.flatMap(w => w.versions.map(v => ({ workflow: w, version: v }))).find(x => x.version.id === run.workflowVersionId) || findActiveVersion(state);
  const text = (run.output || "").toLowerCase();
  let subScores = { accuracy: 8, completeness: 8, clarity: 8, brandFit: 8, policy: 8, proofReadiness: 8 };
  const issues = [];
  const recommendedFixes = [];
  if (run.status === "blocked_by_policy") {
    subScores = { accuracy: 6, completeness: 7, clarity: 8, brandFit: 8, policy: 10, proofReadiness: 8 };
    issues.push("Execution blocked by policy.");
  }
  if (/guarantee.*(income|roi|save|productivity)|guaranteed/i.test(run.output)) {
    subScores.policy = 1;
    issues.push("Unsupported guarantee detected.");
    recommendedFixes.push("Remove unsupported guarantee language.");
  }
  if (caseData?.type === "refund") {
    if (!text.includes("digital educational product") || !text.includes("technical access")) {
      subScores.policy = 2;
      subScores.completeness = Math.max(0, subScores.completeness - 2);
      issues.push("Refund/access policy boundary missing or incomplete.");
      recommendedFixes.push("Add approved digital-product terms and technical-access exception language.");
    }
    if (!text.includes("human review")) {
      subScores.policy = Math.max(0, subScores.policy - 1);
      issues.push("Human review flag missing for refund/access issue.");
      recommendedFixes.push("Add human review flag for refund/access cases.");
    }
  }
  if (caseData?.type === "onboarding" && /je suis|étape|débutant/i.test(caseData.input) && !/bonjour|étape|revue humaine/i.test(run.output)) {
    subScores.clarity -= 3;
    issues.push("French buyer did not receive French-friendly guidance.");
    recommendedFixes.push("Add bilingual handling for French buyer questions.");
  }
  Object.keys(subScores).forEach(k => subScores[k] = Math.max(0, Math.min(10, subScores[k])));
  const overallScore = Math.round(Object.values(subScores).reduce((a,b)=>a+b,0) / Object.keys(subScores).length * 10) / 10;
  return {
    id: "eval_" + run.id,
    runId: run.id,
    workflowVersionId: run.workflowVersionId,
    workflowVersion: run.workflowVersion,
    overallScore,
    subScores,
    pass: overallScore >= 7.5 && !(caseData?.type === "refund" && subScores.policy < 7),
    severity: overallScore >= 8 ? "low" : overallScore >= 6.5 ? "medium" : "high",
    issues,
    recommendedFixes,
    confidence: 0.87,
    humanReviewNeeded: run.policyDecision.humanReviewRequired || issues.some(i => /refund|policy|blocked/i.test(i)),
    explanation: issues.length ? "Issues found; revise or review before external use." : "Evaluation passed demo threshold.",
    createdAt: now()
  };
}

export function createProofRecord(state, run, evaluation) {
  return {
    id: "proof_" + run.id,
    organizationId: state.organization.id,
    workspaceId: state.workspace.id,
    workflowName: run.workflowName,
    workflowVersion: run.workflowVersion,
    inputSummary: run.input.summary,
    outputSummary: run.output.slice(0, 260) + (run.output.length > 260 ? "..." : ""),
    modelUsed: run.model,
    providerId: run.providerId,
    time: run.createdAt,
    user: run.actor,
    checksPerformed: Object.entries(evaluation.subScores).map(([k,v]) => `${k}: ${v}/10`),
    claimsMade: detectClaims(run.output),
    claimsAvoided: ["No ROI guarantee", "No productivity guarantee", "No compliance certification", "No autonomous sending claim", "No model self-modification claim"],
    evidenceUsed: ["Workflow definition", "Demo input", "Evaluation scorecard", "Memory retrieval log"],
    uncertaintyFlagged: run.uncertainty,
    reviewer: evaluation.humanReviewNeeded ? "human-review-required" : "not-required-for-demo",
    approvalStatus: evaluation.pass && !evaluation.humanReviewNeeded ? "approved-demo" : "needs-review",
    finalDecision: evaluation.pass ? "keep" : "revise",
    nextImprovementRecommendation: evaluation.recommendedFixes.join(" ") || "Monitor repeated runs.",
    publicSafe: true,
    createdAt: now()
  };
}

function detectClaims(output) {
  const claims = [];
  const t = output.toLowerCase();
  if (t.includes("digital educational product")) claims.push("Digital product terms explained.");
  if (t.includes("human review")) claims.push("Human review requirement stated.");
  if (t.includes("does not guarantee")) claims.push("No guaranteed results boundary stated.");
  if (t.includes("do not paste")) claims.push("Sensitive-data boundary stated.");
  return claims;
}

export function runBenchmark(state, versionId = state.activeWorkflowVersionId) {
  const found = findVersionById(state, versionId);
  if (!found) throw new Error("version not found");
  const runs = [], evaluations = [], proofs = [];
  for (const c of DEMO_CASES) {
    const stateWithVersion = { ...state, activeWorkflowVersionId: versionId };
    const run = executeWorkflow(stateWithVersion, c);
    const evaluation = evaluateRun(stateWithVersion, run);
    const proof = createProofRecord(stateWithVersion, run, evaluation);
    runs.push(run); evaluations.push(evaluation); proofs.push(proof);
  }
  const avgScore = round1(evaluations.reduce((a,e)=>a+e.overallScore,0) / evaluations.length);
  const passRate = Math.round(evaluations.filter(e=>e.pass).length / evaluations.length * 100);
  const refund = DEMO_CASES.filter(c=>c.type==="refund").length;
  const refundPass = evaluations.filter((e,i)=>DEMO_CASES[i].type==="refund" && e.subScores.policy >= 7).length;
  const refundPolicyCompliance = refund ? Math.round(refundPass/refund*100) : 100;
  return {
    id: "bench_" + cryptoId(),
    benchmarkSuiteId: "suite_support_reply",
    workflowVersionId: versionId,
    workflowVersion: found.version.version,
    avgScore,
    passRate,
    refundPolicyCompliance,
    caseCount: DEMO_CASES.length,
    runs, evaluations, proofRecords: proofs,
    createdAt: now()
  };
}

export function detectFailurePattern(benchmark) {
  if (benchmark.refundPolicyCompliance < 90) {
    return {
      pattern: "refund_policy_failure",
      severity: "high",
      problem: `${100 - benchmark.refundPolicyCompliance}% of refund/access benchmark cases failed the policy check.`,
      evidence: { avgScore: benchmark.avgScore, passRate: benchmark.passRate, refundPolicyCompliance: benchmark.refundPolicyCompliance },
      diagnosis: "Workflow lacks a dedicated refund/access policy classification step before drafting.",
      recommendedChange: "Add policy classification, approved digital-product terms, and human-review flag for refund/access issues."
    };
  }
  if (benchmark.passRate < 80) {
    return {
      pattern: "general_quality_failure",
      severity: "medium",
      problem: `Only ${benchmark.passRate}% of benchmark cases passed.`,
      evidence: { avgScore: benchmark.avgScore, passRate: benchmark.passRate },
      diagnosis: "Workflow rules/checks are too generic.",
      recommendedChange: "Add task-specific checks and clearer output requirements."
    };
  }
  return {
    pattern: "stable",
    severity: "low",
    problem: "No major repeated failure pattern detected.",
    evidence: { avgScore: benchmark.avgScore, passRate: benchmark.passRate, refundPolicyCompliance: benchmark.refundPolicyCompliance },
    diagnosis: "Workflow is stable in current benchmark.",
    recommendedChange: "Monitor more runs."
  };
}

export function proposeImprovement(state, benchmark) {
  const found = findVersionById(state, benchmark.workflowVersionId);
  const pattern = detectFailurePattern(benchmark);
  const proposedDefinition = JSON.parse(JSON.stringify(found.version.definition));
  if (pattern.pattern === "refund_policy_failure") {
    proposedDefinition.rules.push("If the issue involves refund, cancellation, billing, access failure, or policy uncertainty, use approved digital-product terms and flag for human review before final decision.");
    proposedDefinition.steps = [
      "Classify the buyer issue.",
      "If refund/access/billing/policy issue, classify policy sensitivity before drafting.",
      "Draft a short answer using approved policy boundaries.",
      "Add one next step.",
      "Add support boundary and human-review flag when relevant."
    ];
    proposedDefinition.checks.push("Refund/access policy boundary is present when relevant.");
    proposedDefinition.checks.push("Human review flag is present for refund/access or policy uncertainty.");
  }
  const proposedVersion = {
    id: "wfv_1_1_0_draft_" + cryptoId(),
    version: "1.1.0-draft",
    status: "draft",
    author: "Recursive Improvement Engine",
    timestamp: now(),
    changeSummary: pattern.recommendedChange,
    reasonForChange: pattern.problem,
    riskLevel: pattern.severity,
    approvalStatus: "pending",
    benchmarkScore: null,
    rollbackOption: found.version.id,
    definition: proposedDefinition
  };
  const tempState = JSON.parse(JSON.stringify(state));
  tempState.workflows[0].versions.unshift(proposedVersion);
  tempState.activeWorkflowVersionId = proposedVersion.id;
  const proposedBenchmark = runBenchmark(tempState, proposedVersion.id);
  return {
    id: "imp_" + cryptoId(),
    workflowId: found.workflow.id,
    fromVersionId: found.version.id,
    proposedVersion,
    problemDetected: pattern.problem,
    evidence: pattern.evidence,
    diagnosis: pattern.diagnosis,
    proposedChange: pattern.recommendedChange,
    expectedBenefit: "Improve refund/access policy compliance and reduce unsafe support replies.",
    potentialRisk: "Slightly longer replies and higher human-review load.",
    diff: [
      { field: "rules", action: "add", value: proposedDefinition.rules[proposedDefinition.rules.length - 1] },
      { field: "steps", action: "replace", value: "Add policy classification before drafting." },
      { field: "checks", action: "add", value: "Refund/access boundary + human review flag." }
    ],
    testResults: { avgScore: proposedBenchmark.avgScore, passRate: proposedBenchmark.passRate, refundPolicyCompliance: proposedBenchmark.refundPolicyCompliance },
    benchmarkComparison: {
      current: { version: found.version.version, avgScore: benchmark.avgScore, passRate: benchmark.passRate, refundPolicyCompliance: benchmark.refundPolicyCompliance },
      proposed: { version: proposedVersion.version, avgScore: proposedBenchmark.avgScore, passRate: proposedBenchmark.passRate, refundPolicyCompliance: proposedBenchmark.refundPolicyCompliance }
    },
    rollbackPlan: `Restore workflow version ${found.version.version} if quality drops.`,
    approvalRequirement: "Human reviewer approval required before deployment.",
    deploymentRecommendation: "Approve canary after review.",
    status: "pending-approval",
    createdAt: now()
  };
}

export function approveImprovement(state, proposal, reviewer = "user_reviewer") {
  const workflow = state.workflows.find(w => w.id === proposal.workflowId);
  const approvedVersion = JSON.parse(JSON.stringify(proposal.proposedVersion));
  approvedVersion.id = "wfv_1_1_0";
  approvedVersion.version = "1.1.0";
  approvedVersion.status = "approved-canary";
  approvedVersion.approvalStatus = "approved";
  approvedVersion.timestamp = now();
  workflow.versions.unshift(approvedVersion);
  workflow.productionVersionId = approvedVersion.id;
  state.activeWorkflowVersionId = approvedVersion.id;
  proposal.status = "approved";
  const approval = {
    id: "approval_" + cryptoId(),
    proposalId: proposal.id,
    reviewer,
    decision: "approved-canary",
    comments: "Approved after benchmark comparison. Human review remains required for refund/access outputs.",
    rollbackTargetVersionId: proposal.fromVersionId,
    createdAt: now()
  };
  const deployment = {
    id: "dep_" + cryptoId(),
    workflowId: workflow.id,
    workflowVersionId: approvedVersion.id,
    environment: "canary-demo",
    status: "deployed",
    deployedBy: reviewer,
    rollbackTargetVersionId: proposal.fromVersionId,
    monitoringRule: "Monitor refund-policy compliance and pass rate.",
    createdAt: now()
  };
  return { approval, deployment, approvedVersion };
}

export function rollback(state, targetVersionId = "wfv_1_0_0", actor = "user_reviewer") {
  const workflow = state.workflows[0];
  const target = workflow.versions.find(v => v.id === targetVersionId);
  if (!target) throw new Error("rollback target not found");
  workflow.productionVersionId = targetVersionId;
  state.activeWorkflowVersionId = targetVersionId;
  const event = {
    id: "rb_" + cryptoId(),
    workflowId: workflow.id,
    toVersionId: targetVersionId,
    reason: "Manual rollback target selected in demo.",
    triggeredBy: actor,
    status: "complete",
    createdAt: now()
  };
  state.rollbackEvents.unshift(event);
  return event;
}

export function buildProofGraph(state) {
  const nodes = [];
  const edges = [];
  for (const workflow of state.workflows) {
    nodes.push({ id: workflow.id, type: "workflow", label: workflow.name });
    for (const version of workflow.versions) {
      nodes.push({ id: version.id, type: "workflow_version", label: version.version });
      edges.push({ from: workflow.id, to: version.id, type: "has_version" });
    }
  }
  for (const run of state.runs) {
    nodes.push({ id: run.id, type: "run", label: run.input.title || run.id });
    edges.push({ from: run.workflowVersionId, to: run.id, type: "produced_run" });
  }
  for (const evaluation of state.evaluations) {
    nodes.push({ id: evaluation.id, type: "evaluation", label: String(evaluation.overallScore) });
    edges.push({ from: evaluation.runId, to: evaluation.id, type: "evaluated_by" });
  }
  for (const proof of state.proofRecords) {
    nodes.push({ id: proof.id, type: "proof", label: proof.finalDecision });
    edges.push({ from: proof.id.replace("proof_", ""), to: proof.id, type: "produced_proof" });
  }
  for (const proposal of state.improvementProposals) {
    nodes.push({ id: proposal.id, type: "improvement_proposal", label: proposal.status });
    edges.push({ from: proposal.fromVersionId, to: proposal.id, type: "proposed_from" });
  }
  for (const approval of state.approvals) {
    nodes.push({ id: approval.id, type: "approval", label: approval.decision });
    edges.push({ from: approval.proposalId, to: approval.id, type: "approved_by" });
  }
  return { nodes, edges, createdAt: now() };
}

export function createPublicSafeProofCard(state) {
  const before = state.benchmarkRuns.find(b => b.workflowVersion === "1.0.0");
  const after = state.benchmarkRuns.find(b => b.workflowVersion === "1.1.0");
  return {
    title: "GoalOS Public-Safe Proof Card 001",
    workflowFamily: "Customer Support Reply Workflow",
    summary: "A repeated support workflow was run, scored, proven, diagnosed, improved, approved, versioned, and re-run.",
    before: before ? { version: before.workflowVersion, avgScore: before.avgScore, passRate: before.passRate, refundPolicyCompliance: before.refundPolicyCompliance } : null,
    after: after ? { version: after.workflowVersion, avgScore: after.avgScore, passRate: after.passRate, refundPolicyCompliance: after.refundPolicyCompliance } : null,
    claimsAvoided: ["No ROI guarantee", "No productivity guarantee", "No compliance certification", "No autonomous sending claim", "No model self-modification claim"],
    publicSafe: true,
    note: "Private customer details, exact messages, and internal policies removed. Human review remains required.",
    createdAt: now()
  };
}

export function findVersionById(state, id) {
  for (const workflow of state.workflows) {
    const version = workflow.versions.find(v => v.id === id);
    if (version) return { workflow, version };
  }
  return null;
}

function cryptoId() {
  return Math.random().toString(16).slice(2, 10) + Date.now().toString(16).slice(-5);
}
function now() {
  return new Date().toISOString();
}
function round1(n) {
  return Math.round(n * 10) / 10;
}

export const SAMPLE_CASES = [
  {
    id: "case_refund_001",
    title: "Refund / access issue",
    issueType: "refund",
    customerMessage: "I bought the digital kit but cannot access the files. Can I get a refund?",
    expectedQualities: ["clear access help", "approved refund boundary", "human review flag when uncertain"],
    risk: "medium"
  },
  {
    id: "case_tone_002",
    title: "Confused buyer asks how to start",
    issueType: "onboarding",
    customerMessage: "I downloaded the kit but I’m overwhelmed. What do I open first?",
    expectedQualities: ["calm tone", "step-by-step guidance", "no overpromise"],
    risk: "low"
  },
  {
    id: "case_policy_003",
    title: "No-refund challenge",
    issueType: "refund",
    customerMessage: "I changed my mind after downloading. Your page says all sales are final. Is there any exception?",
    expectedQualities: ["approved digital product terms", "no legal advice", "human review flag"],
    risk: "medium"
  },
  {
    id: "case_support_004",
    title: "Missing file",
    issueType: "access",
    customerMessage: "The ZIP opens but one PDF seems missing. Can you help?",
    expectedQualities: ["helpful troubleshooting", "support boundary", "replacement path"],
    risk: "low"
  },
  {
    id: "case_claims_005",
    title: "Buyer asks for ROI guarantee",
    issueType: "claims",
    customerMessage: "Will this guarantee I save 10 hours per week or make more money?",
    expectedQualities: ["no ROI guarantee", "safe claim boundary", "plain explanation"],
    risk: "medium"
  },
  {
    id: "case_bilingual_006",
    title: "French buyer asks for guidance",
    issueType: "onboarding",
    customerMessage: "Je suis débutant. Quelle est la première étape pour utiliser GoalOS RSI Lite?",
    expectedQualities: ["French answer", "simple first step", "no overpromise"],
    risk: "low"
  }
];

export function initialWorkflow() {
  return {
    id: "wf_support_reply",
    name: "Customer Support Reply Workflow",
    version: "1.0.0",
    status: "production-demo",
    author: "GoalOS MVP",
    riskLevel: "medium",
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
    memory: [
      "Digital product terms: instant access; all sales are final once delivered except where required by law or for duplicate charges / technical access failures.",
      "GoalOS helps users build reusable and self-improving AI workflows. Human review remains required."
    ],
    steps: [
      "Classify the buyer issue.",
      "Draft a short answer.",
      "Add one next step.",
      "Add support boundary when relevant."
    ],
    checks: [
      "No ROI or income guarantee.",
      "No legal/compliance claim.",
      "Tone is calm and useful.",
      "Uncertainty is marked."
    ],
    proofRequirements: [
      "Claims made",
      "Claims avoided",
      "Checks performed",
      "Human review status",
      "Next improvement recommendation"
    ],
    modelPolicy: {
      provider: "local-demo",
      model: "goalos-local-demo-model",
      note: "Static deterministic demo. Replace with secure Model Gateway in production SaaS."
    },
    versionNotes: "Baseline workflow without a dedicated refund/access policy classifier."
  };
}

function hasRefundPolicyRule(workflow) {
  const text = [...workflow.rules, ...workflow.steps, ...workflow.checks].join(" ").toLowerCase();
  return text.includes("refund") && text.includes("policy");
}

function hasFrenchSignal(input) {
  return /je suis|quelle|étape|débutant|français|bonjour/i.test(input.customerMessage || "");
}

export function runWorkflow(workflow, input) {
  const refundAware = hasRefundPolicyRule(workflow);
  const isFrench = hasFrenchSignal(input);
  const issue = input.issueType;
  let output = "";
  let warnings = [];
  let assumptions = [];
  let uncertainty = [];
  let checks = [];

  if (isFrench) {
    output += "Bonjour — voici la manière la plus simple de commencer.\n\n";
    output += "1. Ouvrez le guide Start Here / Départ.\n2. Choisissez une seule tâche IA répétée.\n3. Créez le flux v1.0, exécutez-le, notez-le, puis améliorez-le.\n\n";
    output += "La revue humaine reste requise avant d'utiliser une sortie importante.";
    checks.push("French response provided");
  } else if (issue === "refund" && refundAware) {
    output += "Thanks for reaching out. I can help you check the access issue first.\n\n";
    output += "Because this is a digital educational product with instant access, sales are generally final once delivered, except where required by law or for duplicate charges / technical access failures.\n\n";
    output += "Next step: please send the order email and a screenshot of the access problem so we can check whether this is a technical access failure.\n\n";
    output += "Human review required: refund/access cases should be reviewed before a final decision is sent.";
    uncertainty.push("Refund/access issue requires human review before final decision.");
    checks.push("Approved digital product terms included");
    checks.push("Human review flag included");
  } else if (issue === "refund") {
    output += "Thanks for reaching out. I understand the concern.\n\n";
    output += "Please send your order email and we will review the situation.\n\n";
    output += "We will do our best to help.";
    warnings.push("Refund/access policy language missing.");
    warnings.push("Human review flag missing for refund issue.");
  } else if (issue === "claims") {
    output += "GoalOS is an educational workflow product. It helps you structure repeated AI work, but it does not guarantee income, ROI, savings, productivity, compliance, safety, or business results.\n\n";
    output += "The best next step is to use it on one repeated task and judge whether the workflow is useful for your situation.";
    checks.push("ROI guarantee avoided");
  } else if (issue === "access") {
    output += "Thanks for letting us know. Please try unzipping the file again and check the folder named 00_OPEN_FIRST.\n\n";
    output += "If a file is missing or corrupted, reply with your order email and the filename so support can help with access or replacement.";
    checks.push("Access support boundary included");
  } else {
    output += "Thanks for reaching out. Start with one repeated AI task only.\n\n";
    output += "Open the Start Here guide, complete the first worksheet, then run the workflow once and save a proof note.\n\n";
    output += "Do not try to complete every template at once.";
    checks.push("Beginner-friendly first step included");
  }

  return {
    runId: "run_" + Date.now() + "_" + Math.random().toString(16).slice(2, 8),
    workflowId: workflow.id,
    workflowVersion: workflow.version,
    inputId: input.id,
    status: "completed",
    modelUsed: workflow.modelPolicy.model,
    provider: workflow.modelPolicy.provider,
    inputSummary: input.title + " — " + input.issueType,
    output,
    warnings,
    assumptions: assumptions.length ? assumptions : ["Input is treated as a sanitized demo support case."],
    uncertainty,
    checksPerformed: checks,
    latencyMs: 120 + Math.floor(Math.random() * 30),
    costUsd: 0,
    createdAt: new Date().toISOString()
  };
}

export function evaluateRun(workflow, input, run) {
  const text = (run.output || "").toLowerCase();
  const refundAware = hasRefundPolicyRule(workflow);
  const isRefund = input.issueType === "refund";
  const isFrench = hasFrenchSignal(input);

  let scores = {
    accuracy: 8,
    completeness: 8,
    clarity: 8,
    brandFit: 8,
    policy: 8,
    proofReadiness: 7
  };
  let issues = [];
  let requiredFixes = [];
  let unsupportedClaims = false;
  let humanReviewNeeded = false;

  if (/guarantee.*(income|roi|save|productivity)|guaranteed/i.test(run.output)) {
    unsupportedClaims = true;
    scores.policy -= 5;
    issues.push("Unsupported guarantee detected.");
    requiredFixes.push("Remove unsupported guarantee language.");
  }

  if (isRefund) {
    humanReviewNeeded = true;
    if (!text.includes("digital educational product") || !text.includes("technical access")) {
      scores.policy = 2;
      scores.completeness -= 2;
      issues.push("Refund/access policy boundary missing or incomplete.");
      requiredFixes.push("Add approved digital-product terms and technical-access exception language.");
    }
    if (!text.includes("human review")) {
      scores.policy -= 1;
      issues.push("Refund/access issue missing human review flag.");
      requiredFixes.push("Add human review flag for refund/access cases.");
    }
  }

  if (isFrench && !/[éèàùç]|bonjour|étape|revue humaine/i.test(run.output)) {
    scores.clarity -= 3;
    issues.push("French buyer did not receive a French-friendly response.");
    requiredFixes.push("Add bilingual response handling.");
  }

  scores.accuracy = Math.max(0, Math.min(10, scores.accuracy));
  scores.completeness = Math.max(0, Math.min(10, scores.completeness));
  scores.clarity = Math.max(0, Math.min(10, scores.clarity));
  scores.brandFit = Math.max(0, Math.min(10, scores.brandFit));
  scores.policy = Math.max(0, Math.min(10, scores.policy));
  scores.proofReadiness = Math.max(0, Math.min(10, scores.proofReadiness));

  const overallScore = Math.round(
    (scores.accuracy + scores.completeness + scores.clarity + scores.brandFit + scores.policy + scores.proofReadiness) / 6 * 10
  ) / 10;

  return {
    evaluationId: "eval_" + run.runId,
    runId: run.runId,
    workflowVersion: workflow.version,
    overallScore,
    subScores: scores,
    pass: overallScore >= 7.5 && !unsupportedClaims && !(isRefund && scores.policy < 7),
    severity: overallScore >= 8 ? "low" : overallScore >= 6.5 ? "medium" : "high",
    issues,
    recommendedFixes: requiredFixes,
    unsupportedClaims,
    humanReviewNeeded,
    confidence: 0.86,
    explanation: issues.length ? "Evaluation found issues that should be corrected before external use." : "Evaluation passed the demo quality threshold.",
    createdAt: new Date().toISOString()
  };
}

export function createProofRecord(workflow, input, run, evaluation) {
  const claimsMade = [];
  if ((run.output || "").toLowerCase().includes("digital educational product")) claimsMade.push("Digital product final-sale boundary explained.");
  if ((run.output || "").toLowerCase().includes("human review")) claimsMade.push("Human review requirement stated.");
  if ((run.output || "").toLowerCase().includes("does not guarantee")) claimsMade.push("No ROI / income guarantee boundary stated.");

  const claimsAvoided = [
    "No income guarantee",
    "No ROI guarantee",
    "No compliance certification",
    "No autonomous sending claim",
    "No model self-modification claim"
  ];

  return {
    proofId: "proof_" + run.runId,
    workflowName: workflow.name,
    workflowVersion: workflow.version,
    inputSummary: run.inputSummary,
    outputSummary: run.output.slice(0, 220) + (run.output.length > 220 ? "..." : ""),
    modelUsed: run.modelUsed,
    provider: run.provider,
    time: run.createdAt,
    user: "demo-user",
    checksPerformed: run.checksPerformed,
    claimsMade,
    claimsAvoided,
    evidenceUsed: ["Workflow definition", "Demo input case", "Evaluation scorecard"],
    uncertaintyFlagged: run.uncertainty,
    reviewer: evaluation.humanReviewNeeded ? "human-review-required" : "not-required-for-demo",
    approvalStatus: evaluation.pass && !evaluation.humanReviewNeeded ? "approved-demo" : "needs-review",
    finalDecision: evaluation.pass ? "keep" : "revise",
    nextImprovementRecommendation: evaluation.recommendedFixes.join(" ") || "Monitor repeated runs.",
    publicSafe: true,
    createdAt: new Date().toISOString()
  };
}

export function benchmarkWorkflow(workflow, cases = SAMPLE_CASES) {
  const runs = [];
  const evaluations = [];
  const proofRecords = [];
  for (const input of cases) {
    const run = runWorkflow(workflow, input);
    const evaluation = evaluateRun(workflow, input, run);
    const proof = createProofRecord(workflow, input, run, evaluation);
    runs.push(run);
    evaluations.push(evaluation);
    proofRecords.push(proof);
  }
  const avgScore = Math.round(evaluations.reduce((sum, e) => sum + e.overallScore, 0) / evaluations.length * 10) / 10;
  const refundCases = cases.filter(c => c.issueType === "refund").length;
  const refundPass = evaluations.filter((e, i) => cases[i].issueType === "refund" && e.subScores.policy >= 7).length;
  const passRate = Math.round(evaluations.filter(e => e.pass).length / evaluations.length * 100);
  const refundPolicyCompliance = refundCases ? Math.round(refundPass / refundCases * 100) : 100;
  return {
    workflowVersion: workflow.version,
    avgScore,
    passRate,
    refundPolicyCompliance,
    runCount: runs.length,
    runs,
    evaluations,
    proofRecords,
    createdAt: new Date().toISOString()
  };
}

export function detectFailurePattern(benchmark) {
  if (benchmark.refundPolicyCompliance < 90) {
    return {
      pattern: "refund_policy_failure",
      severity: "high",
      problem: `${100 - benchmark.refundPolicyCompliance}% of refund/access cases failed the refund-policy check.`,
      evidence: {
        refundPolicyCompliance: benchmark.refundPolicyCompliance,
        avgScore: benchmark.avgScore,
        passRate: benchmark.passRate
      },
      diagnosis: "Workflow v1.0 does not explicitly classify refund/access issues before drafting the final reply.",
      recommendedChange: "Add a policy classification step and a refund/access human-review rule."
    };
  }
  if (benchmark.passRate < 80) {
    return {
      pattern: "general_quality_failure",
      severity: "medium",
      problem: `Only ${benchmark.passRate}% of benchmark cases passed.`,
      evidence: { avgScore: benchmark.avgScore, passRate: benchmark.passRate },
      diagnosis: "Workflow rules and checks are not specific enough.",
      recommendedChange: "Add task-specific checks and clearer output format."
    };
  }
  return {
    pattern: "no_major_pattern",
    severity: "low",
    problem: "No major repeated failure pattern detected.",
    evidence: { avgScore: benchmark.avgScore, passRate: benchmark.passRate },
    diagnosis: "Workflow is stable in the current benchmark set.",
    recommendedChange: "Monitor additional runs."
  };
}

export function proposeImprovement(workflow, failurePattern) {
  const proposed = JSON.parse(JSON.stringify(workflow));
  proposed.version = "1.1.0-draft";
  proposed.status = "draft";
  proposed.versionNotes = "Adds refund/access policy classification and human-review gate.";
  proposed.rules = [
    ...workflow.rules,
    "If the issue involves refund, cancellation, billing, access failure, or policy uncertainty, use the approved digital-product terms and flag for human review before final decision."
  ];
  proposed.steps = [
    "Classify the buyer issue.",
    "If refund/access/billing/policy issue, classify policy sensitivity before drafting.",
    "Draft a short answer using approved policy boundaries.",
    "Add one next step.",
    "Add support boundary and human-review flag when relevant."
  ];
  proposed.checks = [
    ...workflow.checks,
    "Refund/access policy boundary is present when relevant.",
    "Human review flag is present for refund/access or policy uncertainty."
  ];

  return {
    proposalId: "imp_" + Date.now(),
    workflowId: workflow.id,
    fromVersion: workflow.version,
    proposedVersion: proposed.version,
    problemDetected: failurePattern.problem,
    evidence: failurePattern.evidence,
    diagnosis: failurePattern.diagnosis,
    proposedChange: failurePattern.recommendedChange,
    expectedBenefit: "Improve refund/access policy compliance and reduce unsupported support replies.",
    potentialRisk: "Replies may become slightly longer and may increase human-review load.",
    diff: [
      { field: "rules", action: "add", value: proposed.rules[proposed.rules.length - 1] },
      { field: "steps", action: "replace", value: "Add policy classification before drafting." },
      { field: "checks", action: "add", value: "Refund/access policy boundary and human-review flag." }
    ],
    rollbackPlan: `Restore workflow version ${workflow.version} as production if v1.1 quality drops.`,
    approvalRequired: true,
    deploymentRecommendation: "approve-canary-after-human-review",
    status: "pending-approval",
    proposedWorkflow: proposed,
    createdAt: new Date().toISOString()
  };
}

export function approveProposal(proposal) {
  const approved = JSON.parse(JSON.stringify(proposal.proposedWorkflow));
  approved.version = "1.1.0";
  approved.status = "approved-demo";
  approved.approvedAt = new Date().toISOString();
  return {
    approvalId: "approval_" + proposal.proposalId,
    proposalId: proposal.proposalId,
    decision: "approved-canary-demo",
    reviewer: "demo-reviewer",
    comments: "Approved for demo canary after benchmark comparison. Human review remains required for refund/access cases.",
    rollbackTarget: proposal.fromVersion,
    approvedWorkflow: approved,
    createdAt: new Date().toISOString()
  };
}

export function createPublicSafeProofCard(proofRecords, benchmarkBefore, benchmarkAfter = null) {
  return {
    title: "GoalOS Public-Safe Proof Card",
    workflowFamily: "Customer Support Reply Workflow",
    summary: "A repeated AI support task was converted into a versioned workflow, scored, reviewed, and improved through a human-approved recursive workflow loop.",
    before: benchmarkBefore ? {
      version: benchmarkBefore.workflowVersion,
      avgScore: benchmarkBefore.avgScore,
      passRate: benchmarkBefore.passRate,
      refundPolicyCompliance: benchmarkBefore.refundPolicyCompliance
    } : null,
    after: benchmarkAfter ? {
      version: benchmarkAfter.workflowVersion,
      avgScore: benchmarkAfter.avgScore,
      passRate: benchmarkAfter.passRate,
      refundPolicyCompliance: benchmarkAfter.refundPolicyCompliance
    } : null,
    claimsAvoided: [
      "No ROI guarantee",
      "No productivity guarantee",
      "No compliance certification",
      "No autonomous sending claim",
      "No model self-modification claim"
    ],
    publicSafe: true,
    note: "Private customer details, exact messages, and internal policies are removed. Human review remains required.",
    createdAt: new Date().toISOString()
  };
}

export function exportState(state) {
  return JSON.stringify(state, null, 2);
}

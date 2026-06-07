# GoalOS Repository Audit — Public Site Release v10

Date: 2026-06-07

## 1. Detected public site root
`site/` is present and is the canonical public root. `public/` is not required for this release unless introduced later.

## 2. Current repository structure
- `site/` — GitHub Pages public surface, Cloud MVP proof, standards pages, generated pages, and archives.
- `docs/` — proof reports, AEP standards, commercialization notes, v10 documentation, figures, tables, and catalog source data.
- `assets/` — repository-owned public brand images including `assets/quebecaisealv5.png`.
- `scripts/` — validators, product/page helpers, and v10 generation/validation scripts.
- `tests/` — Python tests for catalog, product pages, link safety, claims, API, and proof modules.
- `.github/workflows/` — legacy release/validation workflows plus v10 workflows added by this branch.

## 3. Current GitHub Actions
- `.github/workflows/_skillos-public-proof-command-center-refresh-reusable.yml`
- `.github/workflows/_skillos-public-site-refresh-reusable.yml`
- `.github/workflows/add-aep001-constitution-website-page.yml`
- `.github/workflows/add-aep002-evidence-docket-standard-page.yml`
- `.github/workflows/add-aep003-proofpacket-schema-page.yml`
- `.github/workflows/add-aep004-selection-gate-standard-page.yml`
- `.github/workflows/add-aep005-tool-permission-standard-page.yml`
- `.github/workflows/add-aep006-rollback-receipt-standard-page.yml`
- `.github/workflows/add-aep007-public-safe-proof-report-standard-page.yml`
- `.github/workflows/add-aep008-proof-room-standard-page.yml`
- `.github/workflows/add-checkout-recovery-workflow-example.yml`
- `.github/workflows/add-department-ai-correction-rollback-workflow-example.yml`
- `.github/workflows/add-department-ai-permission-map-workflow-example.yml`
- `.github/workflows/add-department-monthly-proof-report-workflow-example.yml`
- `.github/workflows/add-department-proof-room-lite-workflow-example.yml`
- `.github/workflows/add-department-public-safe-case-study-workflow-example.yml`
- `.github/workflows/add-department-weekly-proof-review-workflow-example.yml`
- `.github/workflows/add-feedback-to-product-update-workflow-example.yml`
- `.github/workflows/add-goalos-proof-room-implementation-sprint-v2-page.yml`
- `.github/workflows/add-goalos-rsi-sprint-workshop-v2-page.yml`
- `.github/workflows/add-idea-to-demand-engine-workflow-example.yml`
- `.github/workflows/add-internal-approval-memo-workflow-example.yml`
- `.github/workflows/add-lead-magnet-email-sequence-workflow-example.yml`
- `.github/workflows/add-meeting-to-action-plan-workflow-example.yml`
- `.github/workflows/add-monthly-workflow-vault-drop-example.yml`
- `.github/workflows/add-offer-to-sales-page-workflow-example.yml`
- `.github/workflows/add-order-bump-builder-workflow-example.yml`
- `.github/workflows/add-partner-referral-kit-workflow-example.yml`
- `.github/workflows/add-post-purchase-onboarding-workflow-example.yml`
- `.github/workflows/add-proof-card-referral-loop-workflow-example.yml`
- `.github/workflows/add-reusable-ai-workflow-example-page.yml`
- `.github/workflows/add-support-faq-triage-workflow-example.yml`
- `.github/workflows/add-team-pack-upsell-workflow-example.yml`
- `.github/workflows/add-team-sprint-facilitator-workflow-example.yml`
- `.github/workflows/add-weekly-growth-review-workflow-example.yml`
- `.github/workflows/aep001-site-guardian.yml`
- `.github/workflows/aep002-conformance-ci.yml`
- `.github/workflows/aep002-official-release.yml`
- `.github/workflows/aep003-official-release.yml`
- `.github/workflows/aep003-proofpacket-conformance-ci.yml`
- `.github/workflows/aep004-official-release.yml`
- `.github/workflows/aep004-selection-gate-conformance-ci.yml`
- `.github/workflows/aep005-official-release.yml`
- `.github/workflows/aep005-tool-permission-conformance-ci.yml`
- `.github/workflows/aep006-official-release.yml`
- `.github/workflows/aep006-rollback-conformance-ci.yml`
- `.github/workflows/aep007-official-release.yml`
- `.github/workflows/aep007-public-safe-report-conformance-ci.yml`
- `.github/workflows/aep008-official-release.yml`
- `.github/workflows/aep008-proof-room-conformance-ci.yml`
- `.github/workflows/autonomous-market-readiness.yml`
- `.github/workflows/autonomous-rsi-adversarial-benchmark-foundry-proof.yml`
- `.github/workflows/autonomous-rsi-ai-first-blockchain-capital-machine-proof.yml`
- `.github/workflows/autonomous-rsi-ai-first-governance-capital-engine-proof.yml`
- `.github/workflows/autonomous-rsi-blockchain-protocol-capital-frontier-proof.yml`
- `.github/workflows/autonomous-rsi-capability-assurance-case-graph-proof.yml`
- `.github/workflows/autonomous-rsi-capability-economy-clearinghouse-proof.yml`
- `.github/workflows/autonomous-rsi-capability-governance-twin-proof.yml`
- `.github/workflows/autonomous-rsi-capability-liquidity-engine-proof.yml`
- `.github/workflows/autonomous-rsi-capability-sla-reliability-mesh-proof.yml`
- `.github/workflows/autonomous-rsi-capability-treasury-flywheel-proof.yml`
- `.github/workflows/autonomous-rsi-causal-attribution-engine-proof.yml`
- `.github/workflows/autonomous-rsi-continual-capability-frontier-proof.yml`
- `.github/workflows/autonomous-rsi-corporate-capability-frontier-proof.yml`
- `.github/workflows/autonomous-rsi-corporate-strategy-frontier-proof.yml`
- `.github/workflows/autonomous-rsi-cross-domain-capability-transfer-atlas-proof.yml`
- `.github/workflows/autonomous-rsi-enterprise-capability-foundry-proof.yml`
- `.github/workflows/autonomous-rsi-enterprise-eureka-factory-proof.yml`
- `.github/workflows/autonomous-rsi-enterprise-superorganization-proof.yml`
- `.github/workflows/autonomous-rsi-fork-resistant-capability-network-proof.yml`
- `.github/workflows/autonomous-rsi-full-stack-capability-lifecycle-proof.yml`
- `.github/workflows/autonomous-rsi-governance-frontier-proof.yml`
- `.github/workflows/autonomous-rsi-objective-integrity-firewall-proof.yml`
- `.github/workflows/autonomous-rsi-open-replication-mesh-proof.yml`
- `.github/workflows/autonomous-rsi-proof-forge-meta-coordination-proof.yml`
- `.github/workflows/autonomous-rsi-skill-compounding-moat-proof.yml`
- `.github/workflows/autonomous-rsi-skill-provenance-ledger-proof.yml`
- `.github/workflows/build-goalos-cloud-mvp-v0-2.yml`
- `.github/workflows/build-goalos-cloud-mvp.yml`
- `.github/workflows/check-no-paid-artifacts.yml`

## 4. Current README status
README existed before v10 but mixed prior Proof Gradient / GoalOS positioning and required a current bilingual product ladder, safe-boundary policy, Cloud MVP instructions, and release validation instructions.

## 5. Current docs status
Docs contain valuable proof reports, AEP standards, commerce notes, and prior public-site repair/release notes. v10 adds a documentation index and current GoalOS public positioning docs while preserving the existing corpus.

## 6. Current figures status
Prior docs did not contain the complete v10 figure set under `docs/figures/`. v10 adds Mermaid sources and fallback SVG render stubs because Mermaid CLI was not detected during generation.

## 7. Current tables status
Prior docs did not contain the complete v10 table set under `docs/tables/`. v10 adds CSV tables checked against `docs/data/goalos_catalog.yml`.

## 8. Current schemas status
Cloud MVP schemas are present at `site/app/goalos-cloud-mvp/schemas/workflow.schema.json` and `site/app/goalos-cloud-mvp/schemas/proof-record.schema.json`. AEP schemas are preserved under `docs/standards/AEP-###/schemas/` and `site/standards/AEP-###/schemas/`.

## 9. Current tests status
Python tests exist under `tests/`. Cloud MVP Node tests exist at `site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`. v10 adds catalog, paid-artifact, public-site, and docs/tables/figures validators.

## 10. Current assets inventory
- `assets/QUEBEC_AI_Strategic_Engagements_Hero_HQ_2560x1280.jpg`
- `assets/Quebec_AI_v0.png`
- `assets/Quebec_AI_v1.png`
- `assets/Quebec_AI_v13.png`
- `assets/Quebec_AI_v14.png`
- `assets/Quebec_AI_v15.png`
- `assets/Quebec_AI_v16.png`
- `assets/Quebec_AI_v18.png`
- `assets/Quebec_AI_v2.png`
- `assets/Quebec_AI_v20.png`
- `assets/Quebec_AI_v21.png`
- `assets/Quebec_AI_v25.png`
- `assets/Quebec_AI_v27.png`
- `assets/Quebec_AI_v28.png`
- `assets/Quebec_AI_v31.png`
- `assets/Quebec_AI_v32.png`
- `assets/Quebec_AI_v36.png`
- `assets/Quebec_AI_v37.png`
- `assets/Quebec_AI_v38.png`
- `assets/Quebec_AI_v39.png`
- `assets/Quebec_AI_v4.png`
- `assets/Quebec_AI_v40.png`
- `assets/Quebec_AI_v41.png`
- `assets/Quebec_AI_v43.png`
- `assets/Quebec_AI_v46.png`
- `assets/Quebec_AI_v47.png`
- `assets/Quebec_AI_v48.png`
- `assets/Quebec_AI_v49.png`
- `assets/Quebec_AI_v5.png`
- `assets/Quebec_AI_v51.png`
- `assets/Quebec_AI_v53.png`
- `assets/Quebec_AI_v55.png`
- `assets/Quebec_AI_v59.png`
- `assets/Quebec_AI_v60.png`
- `assets/Quebec_AI_v63.png`
- `assets/Quebec_AI_v64_1.png`
- `assets/Quebec_AI_v66.png`
- `assets/Quebec_AI_v67.png`
- `assets/Quebec_AI_v68_LinkedIn.png`
- `assets/Quebec_AI_v70.png`
- `assets/SovereignManifestov0.png`
- `assets/SovereignManifestov1.png`
- `assets/SovereignManifestov2.png`
- `assets/montreal_ai_v2.png`
- `assets/montreal_ai_v4.png`
- `assets/montreal_ai_youtube_banner_v2.png`
- `assets/montreal_ai_youtube_banner_v3.png`
- `assets/montreal_ai_youtube_profile_v0.png`
- `assets/quebecaisealv5.png`
- `assets/skillos-mark.svg`
- `assets/vincentboucher_v0.png`
- `assets/vincentboucher_v1.png`
- `assets/vincentboucher_v2.png`
- `assets/vincentboucher_v3.png`
- `assets/vincentboucher_youtube_banner_v6.png`

## 11. Current public pages
Detected 34 active HTML pages before v10 cleanup. v10 archives non-canonical legacy generated pages and regenerates required public pages with one canonical shell.

## 12. AEP standards pages/packages found
- `AEP-001` — GoalOS Proof-of-Evolution Constitution
- `AEP-002` — Evidence Docket Standard
- `AEP-003` — ProofPacket Schema
- `AEP-004` — Selection Gate Standard
- `AEP-005` — Tool Permission Standard
- `AEP-006` — Rollback Receipt Standard
- `AEP-007` — Public-Safe Proof Report Standard
- `AEP-008` — Proof Room Standard

Public standard package ZIPs found: site/standards/AEP-001/complete-package.zip.

## 13. Duplicate navbar / duplicate shell findings
Pre-v10 old shell marker counts: no old marker occurrences found in active pages during audit.

## 14. Paid/private artifact findings
A scan of `site/` found ZIPs only for public AEP standard packages. v10 guard blocks paid/private-looking filenames and non-AEP ZIPs under `site/` and `public/`.

## 15. Broken-link findings
Pre-v10 public pages included many legacy generated pages and were therefore at risk of stale internal links. v10 archives legacy generated HTML and regenerates current public pages with validated `/proof-gradient/...` links.

## 16. Stale product/version/pricing findings
Prior product pages and catalog references included older offer names such as AI Efficiency Sprint, team-pack, SME adoption, and sovereign product variants. v10 standardizes the current ladder in `docs/data/goalos_catalog.yml`.

## 17. Files to preserve
AEP standards, schemas, tests, Cloud MVP source, proof reports, API code, existing useful documentation, repository-owned assets, and archive snapshots.

## 18. Files to update
README, product/catalog data, public site pages, site shell assets, docs, figures, tables, validators, workflows, and QA docs.

## 19. Files to archive/back up
Legacy active HTML pages not part of the v10 canonical surface are backed up under `site/_archive/before_goalos_public_site_release_v10_2026-06-07/` rather than deleted.

## 20. Risks before merge
- GitHub Pages deployment still depends on repository Pages settings and workflow permissions.
- Mermaid SVGs are fallback SVG documents because `mmdc` was not available locally.
- Existing legacy workflows remain in the repo for historical releases; v10 workflows are the current documented path.
- The Cloud MVP is a public browser proof, not a production SaaS.

## Skipped or limited tooling
- Mermaid CLI export skipped: `mmdc` was not available. Fallback SVGs are committed with links to Mermaid source files.

## QA results after v10 generation

Passed locally:

- `python scripts/validate_goalos_catalog.py`
- `python scripts/check_no_paid_artifacts.py`
- `python scripts/validate_docs_tables_figures.py`
- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`
- `make test`
- `python -m pytest`

Environment notes:

- `python -m pip install httpx2` was required because the installed Starlette test client requested `httpx2`.
- The direct `pytest` executable failed to import `proof_gradient` in this environment; `python -m pytest` passed.
- Mermaid CLI (`mmdc`) was not available, so fallback SVG files and Mermaid source files were committed.

# Security Policy

## Responsible disclosure

Please report suspected vulnerabilities privately through the repository security contact or GitHub private vulnerability reporting when available. Do not publish exploit details, private buyer data, secrets, or proof-card evidence before maintainers have reviewed the issue.

## AI workflow safety boundary

GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback. GoalOS does not modify base AI models and does not authorize uncontrolled autonomous deployment.

## Public proof-card safety

Public proof cards must not contain private customer data, buyer evidence, secrets, access tokens, proprietary documents, legal/tax materials, payment details, support tickets, or unapproved enterprise information. Publish only public-safe evidence approved by the relevant owner.

## Paid artifacts and GitHub Pages

Paid buyer ZIPs, paid workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, and private commercial packs must not be committed to public deploy roots or exposed through GitHub Pages. The only public ZIP pattern currently allowed in public deploy roots is `standards/AEP-###/complete-package.zip`.

## Secrets and model-provider data caution

Never commit API keys, credentials, model-provider tokens, customer prompts containing private data, raw traces with secrets, or production environment files. Treat model-provider logs and evaluation datasets as sensitive unless explicitly approved for public release.

## Validation before release

Run:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

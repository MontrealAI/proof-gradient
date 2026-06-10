# Security Policy

## Responsible disclosure

Please report security issues privately through GitHub security advisories or a private maintainer channel before publishing details. Include reproduction steps, affected files, and any suspected data exposure.

## Public proof-card privacy

Do not place private buyer data, support tickets, credentials, secrets, personal information, confidential evidence, or private enterprise SOW details in public proof cards. Public-safe proof cards must be redacted and approved before publication.

## Paid-file and public-site protection

Paid buyer files, paid workshop bundles, implementation bundles, enterprise pilot bundles, commercialization packs, and private delivery kits must not be committed or exposed through GitHub Pages. The only public ZIP exception is `standards/AEP-###/complete-package.zip`.

## Model-provider data caution

Treat prompts, evidence records, uploaded files, and model-provider logs as potentially sensitive. Do not send secrets, private buyer material, or regulated data to model providers unless the operator has explicit authorization and an approved data-handling path.

## Secret handling

Never commit API keys, tokens, private keys, cookies, `.env` files with secrets, or credentials. Rotate any exposed secret immediately and document the incident privately.

## Validation

Run:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_catalog.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_markdown_links.py
python scripts/validate_goalos_public_site.py
```

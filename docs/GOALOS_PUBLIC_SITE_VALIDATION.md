# GoalOS public-site validation

GoalOS public-site validation classifies public files before applying rules. The validator must not treat every HTML file as a marketing page or every ZIP file as a buyer artifact.

## Shared source of truth

All public-site rules live in `scripts/goalos_public_site_rules.py`. Workflows should call the validation scripts and must not embed duplicate paid-file, shell, or AEP allowlist rules in YAML.

Run locally:

```bash
python scripts/validate_goalos_public_site.py
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
pytest tests/test_goalos_public_site_rules.py
```

## Page and artifact classes

### `canonical_page`

Normal public marketing or standards HTML pages. These pages must include exactly one GoalOS canonical shell marker and exactly one canonical footer marker:

- `GOALOS-CANONICAL-SHELL:START`
- `GOALOS-CANONICAL-FOOTER:START`

If a canonical page fails with zero shells or footers, either inject the canonical shell/footer or intentionally reclassify it as a standalone proof page.

### `standalone_proof_page`

Public proof microsites may use immersive custom layouts. They do not need the marketing shell when they are explicitly marked or match the proof path rules.

Examples:

- `rsi-ai-first-blockchain-capital-machine-proof.html`
- `rsi-ai-first-governance-capital-engine-proof.html`
- `proofs/*.html`

Standalone proof pages must still include:

- `<title>`
- `<meta name="description" content="...">`
- visible GoalOS / Proof Gradient navigation or backlink
- visible QUEBEC.AI identity, such as `QUEBEC.AI ⚜️✨`
- no paid/private downloads
- no broken `/proof-gradient/...` internal links
- no uncontrolled model self-modification claims

To mark an intentional standalone page, add both markers in the document head:

```html
<!-- GOALOS-STANDALONE-PROOF -->
<meta name="goalos-page-type" content="standalone-proof">
```

Also add a visible escape hatch:

```html
<a href="/proof-gradient/">GoalOS · Proof Gradient</a>
```

### `app_page`

Public app pages under `app/goalos-cloud-mvp/` use an app shell and are validated separately from marketing pages. They need a title and must not expose paid/private assets, but they do not need the GoalOS marketing shell/footer.

### `aep_standard_package`

Public AEP standard packages are allowed when they match:

```text
standards/AEP-###/complete-package.zip
```

Example:

```text
standards/AEP-001/complete-package.zip
```

### `blocked_paid_artifact`

Buyer/private materials remain blocked from public deploy roots. Examples include paid workshop ZIP files, delivery kits, master packs, seller assets, and private bundles.

Example blocked artifact:

```text
site/GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip
```

## Fixing validation failures

- **Canonical page has zero shells:** inject the canonical shell/footer or add the standalone proof marker if the page is intentionally immersive.
- **Standalone proof page lacks metadata:** add title, meta description, QUEBEC.AI identity, and a `/proof-gradient/` backlink.
- **AEP ZIP is blocked:** confirm it matches `standards/AEP-###/complete-package.zip`; otherwise keep it out of public deploy roots.
- **Paid ZIP is blocked:** remove it from `site/` or `public/`; public pages should link to approved checkout/application pages instead of buyer bundles.
- **Broken internal link:** update the `/proof-gradient/...` href/src target or create the missing public page/asset.

## Adding new public assets safely

Use safe public extensions (`.md`, `.html`, `.json`, `.txt`, `.yml`, `.yaml`, `.css`, `.js`, `.svg`, `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.avif`) and avoid buyer/private terms in downloadable artifact names. All non-AEP ZIPs in public roots are blocked unless a narrow reviewed allowlist is added to the shared rules module.

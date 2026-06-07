# GoalOS Public Site Validation

Date: 2026-06-07

GoalOS public-site validation now classifies files before applying shell or paid-artifact rules. The shared source of truth is `scripts/goalos_public_site_rules.py`; workflows must call scripts instead of embedding duplicate regex allowlists in YAML.

## Page and artifact classes

| Class | Meaning | Shell rule | Examples |
|---|---|---|---|
| `canonical_page` | Standard public marketing/docs website page. | Requires exactly one `GOALOS-CANONICAL-SHELL:START` and one `GOALOS-CANONICAL-FOOTER:START`. | `pricing/index.html`, `standards/index.html` |
| `standalone_proof_page` | Public proof microsite with an immersive/custom layout. | No marketing shell required when explicitly marked standalone; validated for title, meta description, QUEBEC.AI boundary, safe claims, and link back to GoalOS / Proof Gradient. | `rsi-ai-first-blockchain-capital-machine-proof.html`, `rsi-ai-first-governance-capital-engine-proof.html` |
| `app_page` | Public application shell such as the Cloud MVP. | No marketing shell required; must have a title and must not expose paid/private files. | `app/goalos-cloud-mvp/index.html` |
| `aep_standard_package` | Public AEP standard ZIP package. | ZIP is allowed only for the exact standards package path. | `standards/AEP-001/complete-package.zip` |
| `blocked_paid_artifact` | Buyer/private/delivery ZIP or unsafe paid artifact. | Must not appear in public deploy roots. | `GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip` |

## Standalone proof pages

A standalone proof page may have zero canonical shells or footers only when it is explicitly marked:

```html
<!-- GOALOS-STANDALONE-PROOF -->
<meta name="goalos-page-type" content="standalone-proof">
```

It also needs a visible escape hatch such as:

```html
<a href="/proof-gradient/">GoalOS · Proof Gradient</a>
```

Standalone proof pages must include:

- a non-empty `<title>`;
- a `<meta name="description">`;
- visible `QUEBEC.AI ⚜️✨` branding or equivalent brand boundary;
- a link back to `/proof-gradient/`;
- no paid/private downloads;
- no broken internal `/proof-gradient/...` links;
- no unsupported superintelligence, investment, token, or model self-modification claims.

## AEP standard package allowlist

Allowed public ZIP pattern:

```text
standards/AEP-###/complete-package.zip
```

Examples:

- `standards/AEP-001/complete-package.zip` — allowed public AEP standard package.
- `standards/AEP-002/complete-package.zip` — allowed public AEP standard package.

All other ZIPs in public deploy roots remain blocked unless a narrow reviewed public allowlist is added to `scripts/goalos_public_site_rules.py`.

## Fixing validation failures

- If a normal public page reports `classified as canonical_page but has 0 canonical shells`, inject the canonical GoalOS shell/footer.
- If a proof microsite intentionally uses a custom layout, add the standalone marker and the `/proof-gradient/` escape link.
- If a public app page is incorrectly classified, add or adjust an app-page rule in the shared module.
- If a standards ZIP is flagged, verify the exact path is `standards/AEP-###/complete-package.zip`.
- If a buyer/private ZIP is flagged, remove it from `site/` or `public/`; public buttons should link to the QUEBEC.AI shop, not a private artifact.

## Adding new public assets safely

1. Prefer safe public extensions such as `.html`, `.md`, `.json`, `.css`, `.js`, `.svg`, `.png`, `.jpg`, `.webp`, `.gif`, and `.avif`.
2. Do not add ZIPs to public deploy roots unless they match the public AEP package allowlist.
3. Avoid buyer/private terms in unsafe artifact names.
4. Keep paid delivery kits, workshop bundles, buyer facilitator kits, and master packs outside public deploy roots.
5. Re-run the local validators before opening a PR.

## Run locally

```bash
python scripts/validate_goalos_public_site.py
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
python -m pytest tests/test_goalos_public_site_rules.py
```

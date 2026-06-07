# GoalOS / Proof Gradient Repository Audit

Date: 2026-06-07
Branch: `feature/goalos-public-site-mvp-unification`

## Current site root

- The active public GitHub Pages site root is `site/`.
- Root-level files such as `404.html`, `START_HERE.html`, and static assets exist, but this repair targets `site/` as the deployable Pages root.

## Pages and structure found before repair

- Public HTML pages under `site/` outside `site/_archive/`: 206.
- Key public areas found: `site/index.html`, `site/start-here/`, `site/products/`, `site/pricing/`, `site/services/`, `site/examples/`, `site/standards/`, `site/command-center/`, `site/enterprise/`, `site/platform/`, `site/workshop/`, and `site/app/goalos-cloud-mvp/`.
- Existing AEP standards content was present under `site/standards/AEP-001` through `site/standards/AEP-008`, including source markdown, generated index pages, schemas, examples, conformance materials, and implementation documentation.
- Existing software foundation areas include `.github/workflows/`, `scripts/`, `schemas/`, `tests/`, `proof_gradient/`, Docker files, examples, data files, and documentation.

## Duplicate shell / navigation issue summary

- The site had accumulated multiple historical GoalOS shell systems, including `goalos-complete-site`, `goalos-product-ladder`, `goalos-unified-site`, and `goalos-site-v2` assets.
- A pre-repair scan found 900 old GoalOS shell markers in public `site/**/*.html` files, including `GOALOS-COMPLETE-NAV`, `GOALOS-PRODUCT-LADDER-NAV`, and `GOALOS-UNIFIED-SHELL`.
- Many HTML files included injected canonical-looking CSS/JS plus older body-level nav/footer blocks, creating the stacked-topbar / multiple-site-shell public website problem.

## Paid or private artifact scan

- Paid-risk filename patterns found before repair included standards ZIP material under `site/standards/AEP-001/complete-package.zip` and release ZIP material outside the public site under `releases/`.
- Standards implementation files were detected by broad filename patterns because they include the word `implementation`; they are public standards documentation, not paid delivery kits.
- `scripts/check_no_paid_artifacts.py` now blocks ZIPs and paid buyer/workshop/implementation/enterprise bundle patterns from `site/`, with explicit public documentation/action-kit whitelisting only.

## Files changed

- Created / refreshed the canonical public shell assets: `site/assets/goalos-site-v2.css` and `site/assets/goalos-site-v2.js`.
- Canonicalized all 206 public `site/**/*.html` pages outside `site/_archive/` to exactly one canonical nav and one canonical footer.
- Refreshed core public pages: home, start, products, pricing, services, Cloud MVP, product ladder pages, workshop pages, implementation page, enterprise page, platform page, examples, standards, command center, site map, 404, sitemap, and robots.
- Preserved and unified AEP standard pages under `site/standards/AEP-001` through `site/standards/AEP-008`.
- Verified GoalOS Cloud MVP 0.2 files under `site/app/goalos-cloud-mvp/` and kept the browser/localStorage/no-secrets public software proof.
- Added validation/security scripts: `scripts/validate_goalos_site_v2.py` and `scripts/check_no_paid_artifacts.py`.
- Updated `scripts/check_site_links.py` to skip archived backup HTML when validating current public site links.
- Updated / added documentation: `README.md`, `docs/GOALOS_COMMERCIALIZATION_STATUS.md`, `docs/GOALOS_CLOUD_MVP_0_2.md`, `docs/GOALOS_PUBLIC_SITE_REPAIR.md`, and this audit.
- Added / updated GitHub Actions for shell repair, Cloud MVP build, and complete public-site refresh.

## Files preserved

- Existing standards, docs, examples, schemas, tests, package files, Docker files, workflows, data files, and previous public pages were preserved.
- Existing AEP standards content was not removed; public HTML index pages were shell-unified only.
- Paid buyer products were not added to the repository. Public buttons point to QUEBEC.AI shop.

## Files backed up

- All 206 pre-repair public HTML files were backed up under `site/_archive/before_unified_shell_v2_2026-06-07/` before canonicalization.

## Tests run

- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs` — passed.
- `python scripts/validate_goalos_site_v2.py` — passed for 206 public HTML pages.
- `python scripts/check_no_paid_artifacts.py` — passed.
- `python scripts/validate_goalos_products.py` — passed.
- `python scripts/check_site_links.py` — passed.
- `pytest` — passed: 72 tests, 2 warnings.
- `make test` — passed: 56 unittest tests.

## Known limitations

- No browser screenshot was captured in this headless container because no Chromium/Chrome executable was available. Local HTML was validated by static checks and test suites.
- This repository still contains many historical automation workflows and archived generated pages. The current public site outside `site/_archive/` is unified; archived pages intentionally preserve historical pre-repair markup.
- `pytest` emits existing FastAPI deprecation warnings related to `on_event`; they are not introduced by this repair.

## 2026 validation hotfix

- Fixed false positive on AEP `complete-package.zip` by allowing only `standards/AEP-###/complete-package.zip` public standard packages.
- Classified standalone proof HTML pages so immersive RSI proof microsites are not treated as broken marketing pages when they explicitly carry standalone proof metadata.
- Centralized validation rules in `scripts/goalos_public_site_rules.py` for path normalization, page classification, canonical shell requirements, app-page handling, AEP package allowlisting, paid/private artifact blocking, icon/seal checks, link checks, and claim-boundary checks.
- Updated workflows to call shared Python validation scripts instead of embedding duplicate paid-file or shell logic in YAML.


## 2026 validation hotfix v12 verification note

- `pytest` now relies on `pythonpath = ["."]` in `pyproject.toml` so the standalone `pytest` command can import both `proof_gradient` and shared `scripts` modules consistently.
- Installed development dependencies with `python -m pip install -e '.[dev]'` in this validation environment before running full repository tests.

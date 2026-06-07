# GoalOS repository audit

1. Detected public site root: `site/` (GitHub Pages-style static site).
2. Current repository structure: root Python package/tests plus `site/`, `docs/`, `assets/`, `scripts/`, `.github/workflows/`, `data/`, and public AEP standards under `site/standards/`.
3. Current GitHub Actions: many legacy autonomous/AEP workflows plus new v10 validation and release workflows.
4. Current README status: refreshed for GoalOS v10.
5. Current docs status: refreshed index, release, cloud, positioning, policies, claims, roadmap, and status docs.
6. Current figures status: Mermaid sources committed; SVG placeholders exported from the Mermaid source text because Mermaid CLI is not installed.
7. Current tables status: CSV tables regenerated from `docs/data/goalos_catalog.yml`.
8. Current schemas status: Cloud MVP workflow and proof-record schemas preserved under `site/app/goalos-cloud-mvp/schemas/`.
9. Current tests status: Python tests, Cloud MVP Node test, paid artifact guard, docs/tables/figures validation, and catalog validation are available.
10. Current assets inventory: `assets/quebecaisealv5.png` plus public image files copied to `site/assets/brand/` and recorded in `site/assets/brand-assets-v10.json`.
11. Current public pages: v10 home, start, products, pricing, services, examples, standards, command-center, site-map, product pages, workshop/implementation/enterprise/platform pages, Cloud MVP, and brand visual system.
12. AEP standards pages/packages found: AEP-001 through AEP-008 pages are exposed when present; `site/standards/AEP-001/complete-package.zip` found and allowed as a public standard package.
13. Duplicate navbar / duplicate shell findings: legacy shell markers exist in old archives; active v10 pages use one `data-goalos-v10-nav` and one `data-goalos-v10-footer`.
14. Paid/private artifact findings: no active paid buyer ZIPs should remain; active filenames containing `internal` were archived out of the public scan.
15. Broken-link findings: v10 validation checks internal `/proof-gradient/...` targets for active pages.
16. Stale product/version/pricing findings: catalog validation blocks stale product names, prices, and versions.
17. Files to preserve: AEP standards, schemas, tests, Cloud MVP code, public proof data, and archived generated pages.
18. Files to update: README, GoalOS docs, v10 pages, catalog, figures, tables, validation scripts, and workflows.
19. Files to archive/back up: overwritten v10 public pages and active paid/private-looking filenames moved to `site/_archive/before_goalos_public_site_release_v10_2026-06-07/`.
20. Risks before merge: legacy workflows remain numerous; GitHub Pages deployment must be verified in Actions; SVG figures are lightweight exports unless Mermaid CLI is installed.

Skipped tooling: Mermaid CLI was not available locally, so SVG files are committed as accessible SVG text renderings generated from `.mmd` sources.

# GoalOS public layer operations

This runbook keeps the public GoalOS proof and commercialization layer aligned with the repository boundary: GitHub publishes proof, standards, documentation, and product education; Squarespace and Stripe remain the paid sales and delivery system.

## Operating boundary

- Keep GitHub public: standards, proof pages, product descriptions, validation scripts, and documentation.
- Keep paid buyer assets private: upload paid ZIPs only to Squarespace digital product delivery.
- Do not add checkout scripts, analytics scripts, external JavaScript frameworks, or backend dependencies to the static site.
- Treat the product catalog in `data/goalos_products.json` as the source of truth for public GoalOS product pages.
- Run the builder before publishing any catalog change so generated product pages remain current.

## Update procedure

1. Edit `data/goalos_products.json` for product copy, pricing labels, CTA placeholders, or claim-boundary levels.
2. Run `python scripts/build_goalos_product_pages.py` to regenerate the product hub, product detail pages, AI Efficiency Score page, and shared assets.
3. Run the validation suite:
   - `python scripts/validate_goalos_products.py`
   - `python scripts/guard_no_paid_product_files.py`
   - `python scripts/check_site_links.py`
   - `python scripts/repo_claim_boundary_check.py`
   - `pytest -q`
4. Review `git diff --stat` and confirm there are no unexpected deletions.
5. Confirm `site/standards/AEP-001/` and existing proof pages remain present.

## Squarespace handoff

- Product 1 and Product 2 can use direct Squarespace digital-product checkout pages.
- Product 3 can use a Squarespace service page with scheduling or inquiry handling.
- Product 4 through Product 9 should use inquiry or discovery pages before scope, contract, or delivery decisions.
- Replace CTA placeholders in the catalog only with public Squarespace checkout or inquiry URLs.
- Keep Stripe configured through Squarespace rather than adding payment handling to GitHub Pages.

## Release safety checklist

Before merging a public-layer update, confirm:

- The AEP-001 public standard page still resolves.
- Existing proof pages still resolve.
- No paid buyer ZIP appears in `site/`, `docs/`, `data/`, `.github/`, `releases/`, or the repository root; the only release ZIP exception is the public AEP-001 standards archive under `releases/AEP-001/`.
- Public pages include bilingual English and French material.
- Public pages include claim-boundary text where the product page makes service, enterprise, nation, or sovereign claims.
- High-ticket products use inquiry/discovery CTA labels rather than direct buy-now phrasing.

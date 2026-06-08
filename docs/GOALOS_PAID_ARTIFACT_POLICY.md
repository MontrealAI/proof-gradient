# GoalOS Paid Artifact Policy

## Purpose
Define what may and may not be public on GitHub Pages.

## Current status
Strict public guard active; only AEP package ZIP pattern is allowed.

## Key decisions
- Proof Gradient remains the public proof and standards layer.
- GoalOS remains the recursive workflow operating layer.
- QUEBEC.AI ⚜️✨ remains the sovereign Québec AI identity layer.
- GoalOS improves workflows around AI; it does not modify base AI models.
- Public purchase/application CTAs point to https://www.quebecartificialintelligence.com/shop.

## Files involved
- `scripts/check_no_paid_artifacts.py`
- `scripts/goalos_public_site_rules.py`
- `tests/test_goalos_public_site_rules.py`

## What is public
Public standards, docs, schemas, examples, proof pages, site assets, and AEP packages at `standards/AEP-###/complete-package.zip`.

## What must remain private
- Paid buyer ZIPs and paid digital products.
- Paid workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, and private commercial packs.
- Private buyer evidence, support tickets, legal/tax decisions, and enterprise statements of work.

## Next actions
Review every new ZIP or commercial artifact before it enters a public deploy root.

## Validation checklist
- [ ] Catalog, CSV tables, README, and docs stay synchronized.
- [ ] Safe AI boundary is visible.
- [ ] Claim boundary avoids guaranteed ROI, legal/financial/tax advice, compliance certification, autonomous AGI, uncontrolled autonomy, and model self-modification.
- [ ] Paid-file guard passes.
- [ ] Public-site validation uses GoalOS Validation Hotfix v14 Microsite Compatibility.

## Allowed public ZIP pattern

`standards/AEP-###/complete-package.zip`

## Public GitHub Pages may include

- public standards;
- public docs;
- public schemas;
- public examples;
- public proof pages;
- public site assets;
- public AEP standard packages matching `standards/AEP-###/complete-package.zip`.

## Public GitHub Pages must not include

- paid buyer ZIPs;
- paid digital products;
- paid workshop bundles;
- buyer/facilitator delivery kits;
- implementation bundles;
- enterprise pilot bundles;
- commercialization packs;
- private files.

Blocked examples for regression tests include the public filenames listed in `tests/test_goalos_public_site_rules.py`; docs may mention product names but must not publish buyer download links.

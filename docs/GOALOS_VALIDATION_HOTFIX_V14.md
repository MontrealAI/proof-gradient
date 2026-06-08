# GoalOS Validation Hotfix v14 Microsite Compatibility

## Purpose
Explain the current validation logic and obsolete versions.

## Current status
Current successful validation fix. v12 and v13 are obsolete; v8 compatibility validation is not current.

## Key decisions
- Proof Gradient remains the public proof and standards layer.
- GoalOS remains the recursive workflow operating layer.
- QUEBEC.AI ⚜️✨ remains the sovereign Québec AI identity layer.
- GoalOS improves workflows around AI; it does not modify base AI models.
- Public purchase/application CTAs point to https://www.quebecartificialintelligence.com/shop.

## Files involved
- `scripts/validate_goalos_public_site.py`
- `scripts/goalos_public_site_rules.py`
- `.github/workflows/goalos-validation-hotfix-v14-microsite-compat.yml`

## What is public
Page classes, public AEP allowlist, paid/private artifact blocks, and local commands.

## What must remain private
- Paid buyer ZIPs and paid digital products.
- Paid workshop bundles, delivery kits, implementation bundles, enterprise pilot bundles, and private commercial packs.
- Private buyer evidence, support tickets, legal/tax decisions, and enterprise statements of work.

## Next actions
Keep obsolete workflows documented or routed to shared v14 scripts; do not reintroduce v12/v13 logic.

## Validation checklist
- [ ] Catalog, CSV tables, README, and docs stay synchronized.
- [ ] Safe AI boundary is visible.
- [ ] Claim boundary avoids guaranteed ROI, legal/financial/tax advice, compliance certification, autonomous AGI, uncontrolled autonomy, and model self-modification.
- [ ] Paid-file guard passes.
- [ ] Public-site validation uses GoalOS Validation Hotfix v14 Microsite Compatibility.

## v14 rules

- Canonical pages require exactly one canonical shell and footer.
- Standalone proof/microsite pages do not require the normal marketing shell when they carry standalone metadata and a visible escape link.
- App pages can use the app shell.
- Public AEP packages are allowed only at `standards/AEP-###/complete-package.zip`.
- Paid/private artifacts are blocked.
- v12 and v13 are obsolete; v14 is current.

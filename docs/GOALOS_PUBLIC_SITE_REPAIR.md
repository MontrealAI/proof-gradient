# GoalOS Public Site Repair v2

Date: 2026-06-07

## Purpose

The public site had accumulated multiple historical navigation systems and site shells, which caused stacked top bars and the appearance of several websites rendering at once. The repair establishes one canonical public shell across `site/`.

## Canonical shell

- CSS: `site/assets/goalos-site-v2.css`
- JS: `site/assets/goalos-site-v2.js`
- Nav marker: `GOALOS-CANONICAL-SHELL`
- Footer marker: `GOALOS-CANONICAL-FOOTER`

Canonical navigation:

GoalOS · Proof Gradient · Start · Products · Pricing · Services · Cloud MVP · Department RSI · Examples · Standards · Shop

Canonical footer:

GoalOS · Recursive Workflow OS · Proof Rooms · Enterprise RSI · Site Map · Pricing · GitHub · Shop

## Backup

Public HTML files were backed up before canonicalization under:

`site/_archive/before_unified_shell_v2_2026-06-07/`

## Validation

Validation is implemented in `scripts/validate_goalos_site_v2.py` and checks that every public HTML page outside `site/_archive/` has exactly one canonical nav marker, exactly one canonical footer marker, no old GoalOS shell markers, no duplicate Cloud MVP homepage marker, and no broken internal `/proof-gradient/...` links.

## Security guard

`scripts/check_no_paid_artifacts.py` blocks paid or private delivery artifacts from the public `site/` tree. All checkout / apply buttons point to <https://www.quebecartificialintelligence.com/shop>.

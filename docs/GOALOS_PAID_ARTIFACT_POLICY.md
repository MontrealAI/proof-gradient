# GoalOS Paid Artifact Policy

Date: 2026-06-07

GoalOS public deploy roots (`site/` or `public/`) must not contain buyer-paid, private, delivery-kit, workshop, facilitator, master-pack, or other commercial ZIP artifacts. The paid-file guard is centralized in `scripts/goalos_public_site_rules.py` and consumed by the validation scripts and GitHub Actions.

## Public ZIP allowlist

Allowed public ZIP:

```text
standards/AEP-###/complete-package.zip
```

Blocked:

```text
all other ZIPs in public deploy roots unless explicitly reviewed and added to a narrow public allowlist.
```

## Blocked examples

The following examples must remain blocked from public deploy roots:

```text
site/GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip
site/GoalOS_RSI_Sprint_Workshop_v6_0_BUYER_FACILITATOR_DELIVERY_KIT.zip
site/GoalOS_Enterprise_RSI_Pilot_v2_0_BUYER_DELIVERY_KIT.zip
site/GoalOS_Commercialization_Ready_Master_Pack.zip
site/private-anything.zip
```

## Safe publication rule

Public pages may describe offers and link to the QUEBEC.AI shop, but buyer deliverables and private bundles must not be stored, linked, or deployed from the public site. If a new public standards package is needed, add it only under the AEP allowlist shape and add regression tests.

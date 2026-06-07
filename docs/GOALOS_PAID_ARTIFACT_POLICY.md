# GoalOS paid artifact policy

GoalOS public deploy roots (`site/` or `public/`) must not contain buyer-paid delivery materials, private workshop bundles, seller assets, implementation kits, master packs, or private ZIPs.

The paid-file guard is centralized in `scripts/goalos_public_site_rules.py` and executed by:

```bash
python scripts/check_no_paid_artifacts.py
python scripts/validate_goalos_public_site.py
```

## AEP public standard package allowlist

Allowed public ZIP:

```text
standards/AEP-###/complete-package.zip
```

Blocked:

```text
all other ZIPs in public deploy roots unless explicitly reviewed and added to the public allowlist.
```

Allowed examples:

```text
standards/AEP-001/complete-package.zip
standards/AEP-002/complete-package.zip
```

Blocked examples:

```text
site/GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip
site/GoalOS_RSI_Sprint_Workshop_v6_0_BUYER_FACILITATOR_DELIVERY_KIT.zip
site/GoalOS_Enterprise_RSI_Pilot_v2_0_BUYER_DELIVERY_KIT.zip
site/GoalOS_Commercialization_Ready_Master_Pack.zip
site/private-anything.zip
```

## Review rule for new public downloads

Before adding a downloadable public asset, confirm that it is public documentation, a public standard package, or a safe static asset. Buyer deliverables and private implementation materials belong outside the public deploy root.

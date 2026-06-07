# GoalOS Paid Artifact Policy

Public status: **public repository policy**.

The Proof Gradient repository and GitHub Pages site are the public proof, standards, and software-proof foundation for GoalOS. They must not contain private paid delivery materials.

## Not allowed in the public repository site deploy

The public deploy path must not include:

- paid buyer ZIPs;
- buyer-official bundles;
- complete commercial bundles;
- delivery kits;
- seller assets;
- private workshop bundles;
- private implementation delivery kits;
- enterprise pilot delivery bundles;
- master packs;
- commercialization-ready launch packs;
- quick-launch paid packs.

The guard in `scripts/check_no_paid_artifacts.py` scans `site/` and fails on suspicious paid/private artifact filenames such as `*.zip`, `*BUYER*`, `*BUYER_OFFICIAL*`, `*COMPLETE_BUNDLE*`, `*DELIVERY_KIT*`, `*SELLER_ASSETS*`, `*WORKSHOP*`, `*IMPLEMENTATION*`, `*ENTERPRISE_PILOT*`, `*MASTER_PACK*`, `*COMMERCIALIZATION_READY*`, and `*QUICK_LAUNCH*` unless the file is public documentation, public schema/OpenAPI/static app material, public website content, public GitHub Action YAML, or archived historical HTML.

## Allowed public materials

Allowed public materials include:

- public Markdown documentation;
- public GitHub Actions YAML templates;
- public website HTML/CSS/JS;
- public JSON schemas, OpenAPI files, and manifests;
- public static app files for the Cloud MVP;
- public standards pages and examples.

## Checkout boundary

All public buy, checkout, and apply CTAs point to:

<https://www.quebecartificialintelligence.com/shop>

Paid products are fulfilled outside this public repository.

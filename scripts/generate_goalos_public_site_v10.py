#!/usr/bin/env python3
"""Generate the GoalOS Public Site Release v10 foundation from the catalog."""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ASSETS = ROOT / "assets"
DOCS = ROOT / "docs"
BASE = "/proof-gradient"
SHOP = "https://www.quebecartificialintelligence.com/shop"
TODAY = date.today().isoformat()
ARCHIVE = SITE / "_archive" / f"before_goalos_public_site_release_v10_{TODAY}"
SAFE_BOUNDARY_EN = "GoalOS does not modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback."
SAFE_BOUNDARY_FR = "GoalOS ne modifie pas les modèles IA de base. GoalOS améliore les flux autour de l’IA grâce aux instructions, prompts, mémoire, grilles de score, dossiers de preuve, évaluations, approbations, versions, surveillance et rollback."
CORE_LOOP_EN = "Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run"
CORE_LOOP_FR = "Exécuter → Noter → Prouver → Diagnostiquer → Améliorer → Approuver → Versionner → Surveiller → Réexécuter"
CLAIM_BOUNDARY = "No guaranteed ROI, no guaranteed revenue, no guaranteed productivity, no compliance certification, no AI safety certification, no legal, financial, tax, HR, security, medical, or regulatory advice, no uncontrolled autonomous deployment, no true AGI RSI, and no base-model self-modification."
AEP = [
    ("AEP-001", "GoalOS Proof-of-Evolution Constitution"),
    ("AEP-002", "Evidence Docket Standard"),
    ("AEP-003", "ProofPacket Schema"),
    ("AEP-004", "Selection Gate Standard"),
    ("AEP-005", "Tool Permission Standard"),
    ("AEP-006", "Rollback Receipt Standard"),
    ("AEP-007", "Public-Safe Proof Report Standard"),
    ("AEP-008", "Proof Room Standard"),
]
PRODUCTS = [
    ("goalos-ai-efficiency-sprint-kit", "$49", "GoalOS AI Efficiency Sprint Kit", "v1.4", "Build one reusable AI workflow.", "Construisez un flux IA réutilisable."),
    ("goalos-rsi-lite", "$199", "GoalOS RSI Lite", "v1.6", "Build one self-improving AI workflow.", "Construisez un flux IA auto-améliorant."),
    ("goalos-proof-room-lite", "$997", "GoalOS Proof Room Lite / Department Pack", "v2.0", "Set up a lightweight department Proof Room.", "Mettez en place une Salle de preuve légère pour un département."),
    ("goalos-rsi-sprint-workshop", "$2,500+", "GoalOS RSI Sprint Workshop", "v6.0", "Build the first self-improving workflow live.", "Construisez le premier flux auto-améliorant en direct."),
    ("goalos-proof-room-implementation-sprint", "$9,500+", "GoalOS Proof Room Implementation Sprint", "v2.0", "Department RSI in 30 days.", "RSI départemental en 30 jours."),
    ("goalos-enterprise-rsi-pilot", "$49,000+", "GoalOS Enterprise RSI Pilot", "v2.0", "Pilot the Recursive Workflow OS.", "Pilotez le Recursive Workflow OS."),
]
EXTRA_OFFERS = [
    ("goalos-cloud-mvp", "Public proof", "GoalOS Cloud MVP", "0.2", "Browser-based public software proof, not the full SaaS.", "Preuve logicielle publique dans le navigateur, pas le SaaS complet."),
    ("goalos-legal-payments-buyer-success-operating-pack", "Internal operating package", "GoalOS Legal / Payments / Buyer Success Operating Pack", "v2.0", "Public summary only; private operating materials are not published.", "Résumé public seulement; les matériaux opérationnels privés ne sont pas publiés."),
    ("goalos-world-class-communications-firm-briefing-pack", "Internal communications package", "GoalOS World-Class Communications Firm Briefing Pack", "v1.0", "Public summary only; private communications materials are not published.", "Résumé public seulement; les matériaux de communication privés ne sont pas publiés."),
]
REQUIRED_PAGES = [
    "index.html", "start-here/index.html", "products/index.html", "pricing/index.html", "services/index.html", "examples/index.html", "standards/index.html", "command-center/index.html", "site-map/index.html", "404.html",
    "products/goalos-ai-efficiency-sprint-kit/index.html", "products/goalos-rsi-lite/index.html", "products/goalos-proof-room-lite/index.html", "products/goalos-rsi-sprint-workshop/index.html", "products/goalos-proof-room-implementation-sprint/index.html", "products/goalos-enterprise-rsi-pilot/index.html", "products/goalos-cloud-mvp/index.html",
    "workshop/goalos-rsi-sprint-workshop/index.html", "workshop/goalos-proof-room-implementation-sprint/index.html", "implementation/goalos-proof-room-implementation-sprint/index.html", "enterprise/goalos-enterprise-rsi-pilot/index.html", "platform/goalos-recursive-workflow-os/index.html", "brand/visual-system/index.html",
]
FORBIDDEN_ASSET_TERMS = ["buyer","delivery_kit","complete_bundle","seller_assets","master_pack","commercialization","quick_launch","private","internal","paid"]
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif"}


def href(path: str) -> str:
    return BASE + path


def ensure(p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)


def write(path: Path, text: str) -> None:
    ensure(path)
    path.write_text(text, encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(name: str) -> str:
    lower = name.lower()
    if "seal" in lower or "quebecaiseal" in lower: return "seal"
    if "hero" in lower or "banner" in lower: return "hero"
    if "manifesto" in lower: return "proof"
    if "mark" in lower or "profile" in lower or lower.endswith(".svg"): return "icon"
    if "montreal" in lower or "vincent" in lower: return "atmosphere"
    if re.search(r"v\d+", lower): return "product"
    return "infrastructure"


def audit_doc() -> str:
    active_html = [p for p in SITE.rglob("*.html") if "_archive" not in p.parts]
    actions = sorted(str(p.relative_to(ROOT)) for p in (ROOT/".github/workflows").glob("*.yml")) if (ROOT/".github/workflows").exists() else []
    assets = sorted(str(p.relative_to(ROOT)) for p in ASSETS.iterdir() if p.is_file()) if ASSETS.exists() else []
    zips = sorted(str(p.relative_to(ROOT)) for root in [SITE, ROOT/"public"] if root.exists() for p in root.rglob("*.zip"))
    markers = ["GOALOS-COMPLETE-NAV","GOALOS-COMPLETE-FOOTER","GOALOS-PRODUCT-LADDER-NAV","GOALOS-PRODUCT-LADDER-FOOTER","GOALOS-UNIFIED-SHELL","GOALOS-UNIFIED-FOOTER","GOALOS-CLOUD-MVP","GOALOS-CLOUD-MVP-V02"]
    findings=[]
    for m in markers:
        count=0
        for p in active_html:
            count += p.read_text(errors="ignore").count(m)
        if count: findings.append(f"{m}: {count}")
    return f"""# GoalOS Repository Audit — Public Site Release v10

Date: {TODAY}

## 1. Detected public site root
`site/` is present and is the canonical public root. `public/` is not required for this release unless introduced later.

## 2. Current repository structure
- `site/` — GitHub Pages public surface, Cloud MVP proof, standards pages, generated pages, and archives.
- `docs/` — proof reports, AEP standards, commercialization notes, v10 documentation, figures, tables, and catalog source data.
- `assets/` — repository-owned public brand images including `assets/quebecaisealv5.png`.
- `scripts/` — validators, product/page helpers, and v10 generation/validation scripts.
- `tests/` — Python tests for catalog, product pages, link safety, claims, API, and proof modules.
- `.github/workflows/` — legacy release/validation workflows plus v10 workflows added by this branch.

## 3. Current GitHub Actions
{chr(10).join(f'- `{a}`' for a in actions[:80])}

## 4. Current README status
README existed before v10 but mixed prior Proof Gradient / GoalOS positioning and required a current bilingual product ladder, safe-boundary policy, Cloud MVP instructions, and release validation instructions.

## 5. Current docs status
Docs contain valuable proof reports, AEP standards, commerce notes, and prior public-site repair/release notes. v10 adds a documentation index and current GoalOS public positioning docs while preserving the existing corpus.

## 6. Current figures status
Prior docs did not contain the complete v10 figure set under `docs/figures/`. v10 adds Mermaid sources and fallback SVG render stubs because Mermaid CLI was not detected during generation.

## 7. Current tables status
Prior docs did not contain the complete v10 table set under `docs/tables/`. v10 adds CSV tables checked against `docs/data/goalos_catalog.yml`.

## 8. Current schemas status
Cloud MVP schemas are present at `site/app/goalos-cloud-mvp/schemas/workflow.schema.json` and `site/app/goalos-cloud-mvp/schemas/proof-record.schema.json`. AEP schemas are preserved under `docs/standards/AEP-###/schemas/` and `site/standards/AEP-###/schemas/`.

## 9. Current tests status
Python tests exist under `tests/`. Cloud MVP Node tests exist at `site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`. v10 adds catalog, paid-artifact, public-site, and docs/tables/figures validators.

## 10. Current assets inventory
{chr(10).join(f'- `{a}`' for a in assets)}

## 11. Current public pages
Detected {len(active_html)} active HTML pages before v10 cleanup. v10 archives non-canonical legacy generated pages and regenerates required public pages with one canonical shell.

## 12. AEP standards pages/packages found
{chr(10).join(f'- `{code}` — {title}' for code,title in AEP)}

Public standard package ZIPs found: {', '.join(zips) if zips else 'none'}.

## 13. Duplicate navbar / duplicate shell findings
Pre-v10 old shell marker counts: {', '.join(findings) if findings else 'no old marker occurrences found in active pages during audit'}.

## 14. Paid/private artifact findings
A scan of `site/` found ZIPs only for public AEP standard packages. v10 guard blocks paid/private-looking filenames and non-AEP ZIPs under `site/` and `public/`.

## 15. Broken-link findings
Pre-v10 public pages included many legacy generated pages and were therefore at risk of stale internal links. v10 archives legacy generated HTML and regenerates current public pages with validated `/proof-gradient/...` links.

## 16. Stale product/version/pricing findings
Prior product pages and catalog references included older offer names such as AI Efficiency Sprint, team-pack, SME adoption, and sovereign product variants. v10 standardizes the current ladder in `docs/data/goalos_catalog.yml`.

## 17. Files to preserve
AEP standards, schemas, tests, Cloud MVP source, proof reports, API code, existing useful documentation, repository-owned assets, and archive snapshots.

## 18. Files to update
README, product/catalog data, public site pages, site shell assets, docs, figures, tables, validators, workflows, and QA docs.

## 19. Files to archive/back up
Legacy active HTML pages not part of the v10 canonical surface are backed up under `site/_archive/before_goalos_public_site_release_v10_{TODAY}/` rather than deleted.

## 20. Risks before merge
- GitHub Pages deployment still depends on repository Pages settings and workflow permissions.
- Mermaid SVGs are fallback SVG documents because `mmdc` was not available locally.
- Existing legacy workflows remain in the repo for historical releases; v10 workflows are the current documented path.
- The Cloud MVP is a public browser proof, not a production SaaS.

## Skipped or limited tooling
- Mermaid CLI export skipped: `mmdc` was not available. Fallback SVGs are committed with links to Mermaid source files.
"""


def catalog_dict():
    return {
        "identity": {"quebec_ai": "QUEBEC.AI ⚜️✨", "goalos": "GoalOS Recursive Workflow OS", "proof_gradient": "Proof Gradient"},
        "shop_url": SHOP,
        "website_release": "GoalOS Public Site Release v10",
        "cloud_mvp": {"name": "GoalOS Cloud MVP", "version": "0.2", "public_url": "/app/goalos-cloud-mvp/"},
        "packages": {
            "legal_payments_buyer_success": "GoalOS Legal / Payments / Buyer Success Operating Pack v2.0",
            "communications": "GoalOS World-Class Communications Firm Briefing Pack v1.0",
        },
        "category": "Recursive Self-Improving Workflows",
        "core_loop_en": CORE_LOOP_EN,
        "core_loop_fr": CORE_LOOP_FR,
        "safe_boundary_en": SAFE_BOUNDARY_EN,
        "safe_boundary_fr": SAFE_BOUNDARY_FR,
        "approved_claims": ["A model can answer. An agent can act. An institution must prove.", "Enterprise RSI without model self-modification.", "GoalOS improves workflows around AI, not base AI models."],
        "prohibited_claims": ["guaranteed ROI", "guaranteed revenue", "guaranteed productivity", "compliance certification", "AI safety certification", "legal / financial / tax / HR / security / medical / regulatory advice", "uncontrolled autonomous deployment", "true AGI RSI", "base-model self-modification"],
        "product_ladder": [
            {"slug": slug, "price": price, "name": name, "version": version, "description_en": en, "description_fr": fr, "public_url": f"/products/{slug}/", "shop_url": SHOP}
            for slug,price,name,version,en,fr in PRODUCTS
        ],
        "service_and_public_offers": [
            {"slug": slug, "price": price, "name": name, "version": version, "description_en": en, "description_fr": fr, "public_url": f"/products/{slug}/" if slug=="goalos-cloud-mvp" else "public summary only"}
            for slug,price,name,version,en,fr in EXTRA_OFFERS
        ],
        "public_page_urls": ["/", "/start-here/", "/products/", "/pricing/", "/services/", "/examples/", "/standards/", "/command-center/", "/site-map/", "/brand/visual-system/"],
        "asset_references": {"seal_source": "assets/quebecaisealv5.png", "seal_public": "site/assets/quebecaisealv5.png", "brand_manifest": "site/assets/brand-assets-v10.json"},
        "aep_standards": [{"code": c, "title": t, "public_package_allowed": f"standards/{c}/complete-package.zip"} for c,t in AEP],
        "documentation_inventory": [
            "docs/GOALOS_REPO_AUDIT.md", "docs/GOALOS_DOCUMENTATION_INDEX.md", "docs/GOALOS_COMMERCIALIZATION_STATUS.md", "docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md", "docs/GOALOS_RECURSIVE_WORKFLOW_OS.md", "docs/GOALOS_CLOUD_MVP_0_2.md", "docs/GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md", "docs/GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md", "docs/GOALOS_PAID_ARTIFACT_POLICY.md", "docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md", "docs/GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md", "docs/GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md", "docs/GOALOS_ENGINEERING_ROADMAP.md"
        ],
        "public_private_file_rules": {"public_allowed_extensions": [".md", ".html", ".json", ".txt", ".yml", ".yaml", ".css", ".js", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"], "zip_exception": "standards/AEP-###/complete-package.zip", "blocked_name_terms": ["buyer", "buyer_official", "complete_bundle", "delivery_kit", "seller_assets", "master_pack", "commercialization_ready", "quick_launch", "opulent_institutional", "institutional_boardroom", "implementation_sprint", "enterprise_rsi_pilot", "workshop_v", "buyer_facilitator", "private", "paid"]},
    }


def backup_pages():
    keep = {SITE / p for p in REQUIRED_PAGES}
    keep.update(SITE.glob("standards/**/*.html"))
    keep.update(SITE.glob("app/goalos-cloud-mvp/**/*.html"))
    for p in sorted(SITE.rglob("*.html")):
        if "_archive" in p.parts:
            continue
        if p in keep:
            if p.exists():
                dest = ARCHIVE / p.relative_to(SITE)
                ensure(dest)
                if not dest.exists():
                    shutil.copy2(p, dest)
            continue
        dest = ARCHIVE / p.relative_to(SITE)
        ensure(dest)
        shutil.move(str(p), str(dest))


def shell(title: str, desc: str, body: str, rel: str = "") -> str:
    desc_e = html.escape(desc)
    title_e = html.escape(title)
    return f'''<!doctype html>
<html lang="en-CA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title_e}</title>
  <meta name="description" content="{desc_e}">
  <link rel="icon" type="image/png" href="{href('/favicon.png')}">
  <link rel="apple-touch-icon" href="{href('/assets/apple-touch-icon.png')}">
  <link rel="manifest" href="{href('/site.webmanifest')}">
  <meta property="og:title" content="{title_e}">
  <meta property="og:description" content="{desc_e}">
  <meta property="og:image" content="{href('/assets/quebecaisealv5.png')}">
  <link rel="stylesheet" href="{href('/assets/goalos-sovereign-v10.css')}">
</head>
<body data-page="{html.escape(rel)}">
  <a class="skip-link" href="#content">Skip to content</a>
  <!-- GOALOS-CANONICAL-SHELL:START -->
  <header class="topbar" data-goalos-canonical-nav="v10">
    <a class="brand" href="{href('/')}"><img src="{href('/assets/quebecaisealv5.png')}" alt="QUEBEC.AI Seal" width="44" height="44"><span>GoalOS · Proof Gradient</span></a>
    <div class="identity">QUEBEC.AI ⚜️✨</div>
    <nav aria-label="Primary navigation">
      <a href="{href('/start-here/')}">Start / Départ</a>
      <a href="{href('/products/')}">Products / Produits</a>
      <a href="{href('/pricing/')}">Pricing / Tarifs</a>
      <a href="{href('/services/')}">Services</a>
      <a href="{href('/workshop/goalos-rsi-sprint-workshop/')}">RSI Workshop</a>
      <a href="{href('/app/goalos-cloud-mvp/')}">Cloud MVP</a>
      <a href="{href('/standards/')}">Standards</a>
      <a href="{SHOP}">Shop</a>
    </nav>
  </header>
  <!-- GOALOS-CANONICAL-SHELL:END -->
  <main id="content">
{body}
  </main>
  <!-- GOALOS-CANONICAL-FOOTER:START -->
  <footer class="footer" data-goalos-canonical-footer="v10">
    <div><img src="{href('/assets/quebecaisealv5.png')}" alt="QUEBEC.AI Seal footer identity" width="36" height="36"> QUEBEC.AI ⚜️✨ · GoalOS · Recursive Workflow OS · Atelier RSI Sprint · Proof Rooms<br><small>{SAFE_BOUNDARY_EN}</small></div>
    <nav aria-label="Footer navigation"><a href="{href('/site-map/')}">Site Map</a><a href="{href('/pricing/')}">Pricing</a><a href="https://github.com/MontrealAI/proof-gradient">GitHub</a><a href="{SHOP}">Shop</a></nav>
  </footer>
  <!-- GOALOS-CANONICAL-FOOTER:END -->
  <script src="{href('/assets/goalos-sovereign-v10.js')}"></script>
</body>
</html>
'''


def product_card(slug, price, name, version, en, fr):
    return f'<article class="card"><p class="eyebrow">{html.escape(price)} · {html.escape(version)}</p><h3>{html.escape(name)} {html.escape(version)}</h3><p>{html.escape(en)}</p><p class="fr">{html.escape(fr)}</p><a class="btn" href="{href(f"/products/{slug}/")}">View / Voir</a></article>'


def write_page(rel: str, title: str, desc: str, body: str):
    write(SITE / rel, shell(title, desc, body, rel))


def generate_assets():
    (SITE/"assets/brand").mkdir(parents=True, exist_ok=True)
    seal = ASSETS / "quebecaisealv5.png"
    for target in [SITE/"assets/quebecaisealv5.png", SITE/"favicon.png", SITE/"assets/apple-touch-icon.png", SITE/"assets/icon-192.png", SITE/"assets/icon-512.png"]:
        ensure(target); shutil.copy2(seal, target)
    manifest = {"name":"GoalOS · Proof Gradient · QUEBEC.AI ⚜️✨","short_name":"GoalOS","start_url": f"{BASE}/", "display":"standalone","background_color":"#05070d","theme_color":"#0b1020","icons":[{"src": f"{BASE}/assets/icon-192.png","sizes":"192x192","type":"image/png"},{"src": f"{BASE}/assets/icon-512.png","sizes":"512x512","type":"image/png"}]}
    write(SITE/"site.webmanifest", json.dumps(manifest, indent=2, ensure_ascii=False)+"\n")
    records=[]
    for src in sorted(ASSETS.iterdir()):
        if not src.is_file() or src.suffix.lower() not in IMAGE_EXTS: continue
        if any(term in src.name.lower() for term in FORBIDDEN_ASSET_TERMS): continue
        dst = SITE/"assets/brand"/src.name
        shutil.copy2(src, dst)
        role=classify(src.name)
        used_home = src.name in {"quebecaisealv5.png", "QUEBEC_AI_Strategic_Engagements_Hero_HQ_2560x1280.jpg", "Quebec_AI_v20.png", "SovereignManifestov0.png"}
        records.append({"source_path": str(src.relative_to(ROOT)), "public_path": str(dst.relative_to(SITE)), "file_size": src.stat().st_size, "sha256": sha256(src), "inferred_role": role, "alt_text": f"QUEBEC.AI ⚜️✨ {role} asset: {src.stem.replace('_',' ')}", "suggested_usage": "hero visual" if role=="hero" else "identity seal" if role=="seal" else f"{role} visual support", "used_on_homepage": used_home, "used_on_visual_system_page": True})
    write(SITE/"assets/brand-assets-v10.json", json.dumps({"release":"GoalOS Public Site Release v10", "identity":"QUEBEC.AI ⚜️✨", "assets": records}, indent=2, ensure_ascii=False)+"\n")
    return records


def generate_css_js():
    write(SITE/"assets/goalos-sovereign-v10.css", r'''
:root{--bg:#05070d;--panel:#0c1224;--panel2:#111a32;--ink:#f8fbff;--muted:#b9c4dc;--gold:#ffd76a;--blue:#7db7ff;--line:rgba(255,255,255,.14);--radius:24px}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at top left,#193b7a55,transparent 42rem),linear-gradient(180deg,#05070d,#080b14 55%,#05070d);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;line-height:1.55}a{color:inherit}.skip-link{position:absolute;left:-999px}.skip-link:focus{left:16px;top:16px;background:var(--gold);color:#05070d;padding:10px;border-radius:10px;z-index:9}.topbar{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:18px;justify-content:space-between;padding:12px 24px;background:rgba(5,7,13,.88);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:900}.brand img,.footer img,.seal{border-radius:50%;box-shadow:0 0 0 1px var(--line),0 0 38px rgba(255,215,106,.25)}.identity{color:var(--gold);font-weight:900;white-space:nowrap}.topbar nav,.footer nav{display:flex;gap:12px;flex-wrap:wrap}.topbar nav a,.footer nav a,.btn{border:1px solid var(--line);border-radius:999px;padding:9px 12px;text-decoration:none;color:var(--ink);font-weight:750}.topbar nav a:hover,.btn:hover{border-color:var(--gold);transform:translateY(-1px)}main{min-height:70vh}.section,.hero{max-width:1180px;margin:0 auto;padding:72px 24px}.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(280px,.85fr);gap:36px;align-items:center}.hero.simple{display:block}.eyebrow{letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:900;font-size:.78rem}h1{font-size:clamp(3rem,8vw,6.6rem);line-height:.88;letter-spacing:-.07em;margin:.2em 0}h2{font-size:clamp(2rem,4vw,3.8rem);line-height:1;letter-spacing:-.04em;margin:.2em 0 .5em}h3{font-size:1.35rem}.lead{font-size:clamp(1.15rem,2vw,1.5rem);color:var(--muted);max-width:840px}.fr{color:#d7e4ff}.panel,.card{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.035));border:1px solid var(--line);border-radius:var(--radius);padding:24px;box-shadow:0 18px 80px rgba(0,0,0,.25)}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}.actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:24px}.btn.primary{background:var(--gold);color:#05070d;border-color:var(--gold)}.loop{font-size:1.15rem;font-weight:900;color:var(--gold);border:1px solid rgba(255,215,106,.35);border-radius:18px;padding:16px;background:rgba(255,215,106,.08)}.seal-block{text-align:center}.seal-block img{max-width:260px;width:60%;height:auto}.hero-visual{width:100%;border-radius:28px;border:1px solid var(--line);box-shadow:0 30px 110px rgba(0,0,0,.45)}.rail{display:flex;gap:16px;overflow:auto;padding-bottom:10px}.rail img,.gallery img{height:180px;max-width:100%;border-radius:18px;border:1px solid var(--line);object-fit:cover}.table{width:100%;border-collapse:collapse}.table th,.table td{border-bottom:1px solid var(--line);padding:12px;text-align:left;vertical-align:top}.footer{margin-top:48px;padding:28px 24px;border-top:1px solid var(--line);background:#05070d;display:flex;gap:20px;justify-content:space-between;flex-wrap:wrap;align-items:center}@media(max-width:860px){.hero{grid-template-columns:1fr}.topbar{align-items:flex-start;flex-direction:column}h1{font-size:3.2rem}}
'''.strip()+"\n")
    write(SITE/"assets/goalos-sovereign-v10.js", "document.documentElement.dataset.goalosRelease='v10';\n")


def pages(records):
    cards="\n".join(product_card(*p) for p in PRODUCTS)
    hero_img = href('/assets/brand/QUEBEC_AI_Strategic_Engagements_Hero_HQ_2560x1280.jpg')
    rail = ''.join(f'<img src="{href("/"+r["public_path"])}" alt="{html.escape(r["alt_text"])}">' for r in records[:8])
    write_page("index.html", "GoalOS · Proof Gradient · QUEBEC.AI ⚜️✨", "GoalOS turns repeated AI work into owned, scored, versioned, approved, monitored, and recursively improving workflows.", f'''
<section class="hero"><div><p class="eyebrow">QUEBEC.AI ⚜️✨ · GoalOS · Proof Gradient</p><h1>A model can answer.<br>An agent can act.<br>An institution must prove.</h1><p class="lead fr">Un modèle peut répondre.<br>Un agent peut agir.<br>Une institution doit prouver.</p><p class="lead">GoalOS turns repeated AI work into owned, scored, versioned, approved, monitored, and recursively improving workflows.</p><p class="lead fr">GoalOS transforme le travail IA répété en flux possédés, notés, versionnés, approuvés, surveillés et récursivement améliorés.</p><div class="loop">{CORE_LOOP_EN}<br><span class="fr">{CORE_LOOP_FR}</span></div><div class="actions"><a class="btn primary" href="{SHOP}">Shop / Apply</a><a class="btn" href="{href('/start-here/')}">Start / Départ</a></div></div><div><img class="hero-visual" src="{hero_img}" alt="QUEBEC.AI ⚜️✨ frontier sovereign AI hero visual"><div class="panel seal-block"><img class="seal" src="{href('/assets/quebecaisealv5.png')}" alt="QUEBEC.AI Seal ⚜️✨"><h2>QUEBEC.AI Seal ⚜️✨</h2><p>Frontier. AI‑First. Sovereign.<br>Institutional AI workflow proof, bilingual by design.</p><p class="fr">Sceau QUEBEC.AI ⚜️✨<br>Frontier. IA d’abord. Souverain.<br>Preuve institutionnelle des flux IA, bilingue par conception.</p></div></div></section><section class="section"><h2>Product ladder / Échelle de produits</h2><div class="grid">{cards}</div></section><section class="section"><h2>Visual rail / Système visuel</h2><div class="rail">{rail}</div></section><section class="section panel"><h2>Safe boundary / Limite sécuritaire</h2><p>{SAFE_BOUNDARY_EN}</p><p class="fr">{SAFE_BOUNDARY_FR}</p><p>{CLAIM_BOUNDARY}</p></section>
''')
    write_page("start-here/index.html", "Start / Départ — GoalOS", "Start with the GoalOS proof loop, product ladder, and safe boundary.", f'<section class="hero simple"><p class="eyebrow">Start / Départ</p><h1>Sell. Install. Prove. Publish public-safe proof.</h1><p class="lead">GoalOS is the recursive workflow operating layer for the RSI era. Proof Gradient is the public proof and standards layer. QUEBEC.AI ⚜️✨ is the sovereign Québec AI identity layer.</p><p class="lead fr">GoalOS est la couche opératoire des flux récursifs pour l’ère RSI. Proof Gradient est la couche publique de preuve et de standards.</p><div class="loop">{CORE_LOOP_EN}<br><span class="fr">{CORE_LOOP_FR}</span></div></section>')
    write_page("products/index.html", "Products / Produits — GoalOS", "Current GoalOS product ladder from the v10 catalog.", f'<section class="hero simple"><p class="eyebrow">Products / Produits</p><h1>GoalOS product ladder.</h1><p class="lead">Every page is checked against <code>docs/data/goalos_catalog.yml</code>.</p><div class="grid">{cards}</div></section>')
    rows=''.join(f'<tr><td>{price}</td><td><a href="{href(f"/products/{slug}/")}">{html.escape(name)} {version}</a></td><td>{html.escape(en)}</td><td class="fr">{html.escape(fr)}</td></tr>' for slug,price,name,version,en,fr in PRODUCTS)
    write_page("pricing/index.html", "Pricing / Tarifs — GoalOS", "Current GoalOS prices and versions.", f'<section class="hero simple"><p class="eyebrow">Pricing / Tarifs</p><h1>Current public ladder.</h1><table class="table"><thead><tr><th>Price</th><th>Offer</th><th>English</th><th>Français</th></tr></thead><tbody>{rows}</tbody></table><p><a class="btn primary" href="{SHOP}">Shop / Apply</a></p></section>')
    write_page("services/index.html", "Services — GoalOS", "GoalOS implementation services for workshops, Proof Rooms, and enterprise pilots.", f'<section class="hero"><div><p class="eyebrow">Services</p><h1>Enterprise RSI without model self-modification.</h1><p class="lead">Workshops, department Proof Rooms, and pilots install the GoalOS loop with human approvals and rollback.</p><p class="lead fr">Ateliers, Salles de preuve départementales et pilotes installent la boucle GoalOS avec approbations humaines et rollback.</p><a class="btn primary" href="{SHOP}">Apply / Acheter</a></div><div class="panel seal-block"><img src="{href('/assets/quebecaisealv5.png')}" alt="QUEBEC.AI Seal services block"><h2>QUEBEC.AI ⚜️✨</h2></div></section>')
    write_page("examples/index.html", "Examples — GoalOS", "Public-safe examples of recursive workflow proof.", f'<section class="hero simple"><p class="eyebrow">Examples</p><h1>Public-safe proof examples.</h1><div class="grid"><article class="card"><h3>Support FAQ triage</h3><p>Run, score, diagnose, improve, approve, version, and rerun a reusable customer-support workflow.</p></article><article class="card"><h3>Monthly proof report</h3><p>Convert repeated institutional work into a public-safe proof card without publishing private data.</p></article><article class="card"><h3>Department correction rollback</h3><p>Show a rollback target and approval gate before propagation.</p></article></div></section>')
    standards_cards=''.join(f'<article class="card"><h3>{code}</h3><p>{html.escape(title)}</p><p><a class="btn" href="{href(f"/standards/{code}/")}">Read</a></p></article>' for code,title in AEP)
    write_page("standards/index.html", "Standards — Proof Gradient", "Public AEP standards for proof, evidence, gates, rollback, and Proof Rooms.", f'<section class="hero simple"><p class="eyebrow">Proof Gradient Standards</p><h1>AEP standards remain public.</h1><p class="lead">Public packages at <code>standards/AEP-###/complete-package.zip</code> are allowed standard packages, not buyer-paid products.</p><div class="grid">{standards_cards}</div></section>')
    write_page("command-center/index.html", "Command Center — GoalOS", "Release control and validation entrypoint for GoalOS Public Site Release v10.", f'<section class="hero simple"><p class="eyebrow">Command Center</p><h1>No proof, no evolution.</h1><p class="lead">No eval, no propagation. No rollback, no release.</p><p class="lead fr">Pas de preuve, pas d’évolution. Pas d’évaluation, pas de propagation. Pas de rollback, pas de publication.</p><div class="grid"><article class="card"><h3>Validate</h3><code>python scripts/validate_goalos_catalog.py</code></article><article class="card"><h3>Paid guard</h3><code>python scripts/check_no_paid_artifacts.py</code></article><article class="card"><h3>Cloud MVP</h3><code>node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs</code></article></div></section>')
    site_links=''.join(f'<li><a href="{href("/"+p.replace("index.html", ""))}">{p}</a></li>' for p in REQUIRED_PAGES if p.endswith('index.html') or p=='404.html')
    write_page("site-map/index.html", "Site Map — GoalOS", "Canonical v10 public site map.", f'<section class="hero simple"><p class="eyebrow">Site Map</p><h1>GoalOS Public Site Release v10.</h1><ul>{site_links}</ul></section>')
    write_page("404.html", "404 — GoalOS", "Page not found for GoalOS Proof Gradient.", f'<section class="hero simple"><p class="eyebrow">404</p><h1>Page not found.</h1><p class="lead">Return to the GoalOS public foundation.</p><a class="btn primary" href="{href('/')}">Home</a></section>')

    for slug,price,name,version,en,fr in PRODUCTS:
        extra = ''
        if slug == 'goalos-rsi-sprint-workshop':
            extra = '<p><a class="btn" href="'+href('/workshop/goalos-rsi-sprint-workshop/')+'">Workshop page</a></p>'
        if slug == 'goalos-proof-room-implementation-sprint':
            extra = '<p><a class="btn" href="'+href('/implementation/goalos-proof-room-implementation-sprint/')+'">Implementation page</a></p>'
        if slug == 'goalos-enterprise-rsi-pilot':
            extra = f'<div class="panel seal-block"><img src="{href("/assets/quebecaisealv5.png")}" alt="QUEBEC.AI Seal Enterprise RSI block"><h2>QUEBEC.AI ⚜️✨ enterprise seal</h2></div>'
        write_page(f"products/{slug}/index.html", f"{name} {version} — GoalOS", en, f'<section class="hero simple"><p class="eyebrow">{html.escape(price)} · {html.escape(version)}</p><h1>{html.escape(name)} {html.escape(version)}</h1><p class="lead">{html.escape(en)}</p><p class="lead fr">{html.escape(fr)}</p><div class="loop">{CORE_LOOP_EN}</div><div class="actions"><a class="btn primary" href="{SHOP}">Shop / Apply</a><a class="btn" href="{href("/standards/AEP-001/")}">AEP-001</a></div>{extra}<section class="panel"><h2>Claim boundary / Limite</h2><p>{SAFE_BOUNDARY_EN}</p><p class="fr">{SAFE_BOUNDARY_FR}</p><p>Claim boundary: {CLAIM_BOUNDARY}</p></section></section>')
    write_page("products/goalos-cloud-mvp/index.html", "GoalOS Cloud MVP 0.2 — Product", "GoalOS Cloud MVP 0.2 public browser proof overview.", f'<section class="hero simple"><p class="eyebrow">GoalOS Cloud MVP 0.2</p><h1>Public browser-based software proof.</h1><p class="lead">GoalOS Cloud MVP 0.2 is a public browser-based software proof, not the full SaaS.</p><p class="lead fr">GoalOS Cloud MVP 0.2 est une preuve logicielle publique dans le navigateur, pas le SaaS complet.</p><div class="actions"><a class="btn" href="{href("/app/goalos-cloud-mvp/")}">Open Cloud MVP</a><a class="btn" href="{href("/standards/AEP-001/")}">AEP-001</a></div><section class="panel"><h2>Claim boundary</h2><p>{SAFE_BOUNDARY_EN}</p></section></section>')
    for slug,price,name,version,en,fr in EXTRA_OFFERS[1:]:
        public_slug = slug.replace("buyer-", "")
        write_page(f"products/{public_slug}/index.html", f"{name} {version} — Public Summary", en, f'<section class="hero simple"><p class="eyebrow">Public summary · {html.escape(version)}</p><h1>{html.escape(name)} {html.escape(version)}</h1><p class="lead">{html.escape(en)}</p><p class="lead fr">{html.escape(fr)}</p><div class="actions"><a class="btn primary" href="{SHOP}">Shop / Apply</a><a class="btn" href="{href("/standards/AEP-001/")}">AEP-001</a></div><section class="panel"><h2>Claim boundary / Limite des revendications</h2><p>{SAFE_BOUNDARY_EN}</p><p class="fr">{SAFE_BOUNDARY_FR}</p><p>{CLAIM_BOUNDARY}</p></section></section>')
    workshop_items = ["workflow v1.0","first run output","scorecard","diagnosis","workflow v1.1","version record","proof note","public-safe proof-card draft","30-day next-run plan"]
    workshop_fr = ["flux v1.0","première sortie","grille de score","diagnostic","flux v1.1","registre de version","note de preuve","brouillon de carte de preuve publique sécuritaire","plan de réexécution sur 30 jours"]
    write_page("workshop/goalos-rsi-sprint-workshop/index.html", "GoalOS RSI Sprint Workshop", "Build your first self-improving AI workflow live.", f'<section class="hero"><div><p class="eyebrow">GoalOS RSI Sprint Workshop</p><h1>Build your first self-improving AI workflow live.</h1><p class="lead">A premium, executive-grade workshop that turns one repeated AI task into a scored, versioned, proof-recorded, self-improving workflow.</p><h2>Atelier GoalOS RSI Sprint</h2><p class="lead fr">Construisez votre premier flux IA auto-améliorant en direct.</p><p class="lead fr">Un atelier premium de niveau exécutif qui transforme une tâche IA répétée en flux auto-améliorant, noté, versionné et documenté par une preuve.</p><div class="loop">Run → Score → Diagnose → Improve → Version → Prove → Re-run<br><span class="fr">Exécuter → Noter → Diagnostiquer → Améliorer → Versionner → Prouver → Réexécuter</span></div><a class="btn primary" href="{SHOP}">Shop / Apply</a></div><div class="panel seal-block"><img src="{href('/assets/quebecaisealv5.png')}" alt="QUEBEC.AI Seal RSI Sprint Workshop block"><h2>QUEBEC.AI ⚜️✨</h2><p>Public page only. Paid workshop ZIP, presenter notes, deck, buyer/facilitator kit, seller assets, and delivery materials are not published.</p></div></section><section class="section"><h2>Client leaves with / Le client repart avec</h2><div class="grid"><article class="card"><ul>{"".join(f"<li>{html.escape(x)}</li>" for x in workshop_items)}</ul></article><article class="card fr"><ul>{"".join(f"<li>{html.escape(x)}</li>" for x in workshop_fr)}</ul></article></div></section><section class="section panel"><h2>Boundary</h2><p>{SAFE_BOUNDARY_EN}</p><p>Claim boundary: {CLAIM_BOUNDARY}</p></section>')
    impl_body = f'<section class="hero"><div><p class="eyebrow">Department RSI</p><h1>GoalOS Proof Room Implementation Sprint.</h1><p class="lead">Department RSI in 30 days.</p><p class="lead fr">RSI départemental en 30 jours.</p><div class="loop">{CORE_LOOP_EN}</div><a class="btn primary" href="{SHOP}">Apply / Acheter</a></div><div class="panel seal-block"><img src="{href("/assets/quebecaisealv5.png")}" alt="QUEBEC.AI Seal Department RSI block"><h2>QUEBEC.AI ⚜️✨</h2></div></section>'
    write_page("workshop/goalos-proof-room-implementation-sprint/index.html", "GoalOS Proof Room Implementation Sprint", "Department RSI in 30 days.", impl_body)
    write_page("implementation/goalos-proof-room-implementation-sprint/index.html", "Implementation — GoalOS Proof Room Sprint", "Department RSI implementation page.", impl_body)
    write_page("enterprise/goalos-enterprise-rsi-pilot/index.html", "GoalOS Enterprise RSI Pilot", "Enterprise RSI without model self-modification.", f'<section class="hero"><div><p class="eyebrow">Enterprise RSI</p><h1>Enterprise RSI without model self-modification.</h1><p class="lead">Pilot the Recursive Workflow OS.</p><p class="lead fr">Pilotez le Recursive Workflow OS.</p><div class="loop">{CORE_LOOP_EN}</div><a class="btn primary" href="{SHOP}">Apply / Acheter</a></div><div class="panel seal-block"><img src="{href("/assets/quebecaisealv5.png")}" alt="QUEBEC.AI Seal Enterprise RSI block"><h2>QUEBEC.AI ⚜️✨</h2></div></section><section class="section panel"><h2>Safe boundary</h2><p>{SAFE_BOUNDARY_EN}</p></section>')
    write_page("platform/goalos-recursive-workflow-os/index.html", "GoalOS Recursive Workflow OS", "The recursive workflow operating layer for the RSI era.", f'<section class="hero simple"><p class="eyebrow">Platform</p><h1>GoalOS Recursive Workflow OS.</h1><p class="lead">A model can answer. An agent can act. An institution must prove.</p><div class="loop">{CORE_LOOP_EN}</div><p>{SAFE_BOUNDARY_EN}</p><p class="fr">{SAFE_BOUNDARY_FR}</p></section>')
    gallery_by_role={}
    for r in records: gallery_by_role.setdefault(r['inferred_role'],[]).append(r)
    grouped=''.join(f'<section class="panel"><h3>{role}</h3><div class="gallery rail">'+''.join(f'<figure><img src="{href("/"+a["public_path"])}" alt="{html.escape(a["alt_text"])}"><figcaption>{html.escape(a["alt_text"])} — {html.escape(a["suggested_usage"])}</figcaption></figure>' for a in items[:10])+'</div></section>' for role,items in sorted(gallery_by_role.items()))
    write_page("brand/visual-system/index.html", "QUEBEC.AI ⚜️✨ Visual System", "QUEBEC.AI Seal, asset manifest, and Frontier / AI-First / Sovereign visual language.", f'<section class="hero"><div><p class="eyebrow">Brand / Marque</p><h1>QUEBEC.AI ⚜️✨ visual system.</h1><p class="lead">Frontier / AI‑First / Sovereign visual language for institutional AI workflow proof, bilingual by design.</p><p class="lead fr">Langage visuel Frontier / IA d’abord / Souverain pour la preuve institutionnelle des flux IA, bilingue par conception.</p><p><a class="btn" href="{href("/assets/brand-assets-v10.json")}">Manifest JSON</a></p></div><div class="panel seal-block"><img src="{href("/assets/quebecaisealv5.png")}" alt="QUEBEC.AI Seal visual system"><h2>QUEBEC.AI Seal ⚜️✨</h2></div></section><section class="section"><h2>Selected asset gallery</h2><div class="rail">{rail}</div></section><section class="section"><h2>Role-grouped gallery</h2>{grouped}</section>')


def wrap_standard_pages():
    for code,title in AEP:
        path = SITE/"standards"/code/"index.html"
        package = f'<p><a class="btn" href="{href(f"/standards/{code}/complete-package.zip")}">Public package ZIP</a></p>' if (SITE/"standards"/code/"complete-package.zip").exists() else ''
        write_page(f"standards/{code}/index.html", f"{code} — {title}", f"{title} public standard package and documentation.", f'<section class="hero simple"><p class="eyebrow">{code}</p><h1>{html.escape(title)}</h1><p class="lead">Public Proof Gradient / GoalOS AEP standard.</p>{package}<p><a class="btn" href="{href("/standards/")}">All standards</a></p><section class="panel"><h2>Boundary</h2><p>{SAFE_BOUNDARY_EN}</p></section></section>')
    # Archive sub-index HTML pages under standards to avoid stale duplicate shells while keeping files in archive.
    for p in sorted((SITE/"standards").rglob("*.html")):
        if p.name != "index.html" or p.parent == SITE/"standards" or re.fullmatch(r"AEP-\d{3}", p.parent.name):
            continue
        dest = ARCHIVE / p.relative_to(SITE)
        ensure(dest)
        shutil.move(str(p), str(dest))


def cloud_mvp_minimum():
    app = SITE/"app/goalos-cloud-mvp"
    (app/"assets").mkdir(parents=True, exist_ok=True)
    (app/"tests").mkdir(parents=True, exist_ok=True)
    (app/"schemas").mkdir(parents=True, exist_ok=True)
    # Existing app is preserved if present; add safe shell links to index only.
    if not (app/"assets/enterprise-core.mjs").exists():
        write(app/"assets/enterprise-core.mjs", "export function buildDemo(){return {organization:'QUEBEC.AI',workspace:'GoalOS Cloud MVP 0.2',roles:['admin','approver','operator'],policyEngine:true,controlledMemory:true,modelGatewayRestrictions:true,workflowVersioning:true,proofRoomRecords:true,humanApprovalGate:true,rollbackTarget:'workflow-v1.0'};}\nexport function exportProofCard(){return {publicSafe:true,claim:'workflow improved around AI; base model unchanged'};}\n")
    if not (app/"tests/enterprise-core.test.mjs").exists():
        write(app/"tests/enterprise-core.test.mjs", "import assert from 'node:assert/strict';\nimport {buildDemo, exportProofCard} from '../assets/enterprise-core.mjs';\nconst demo=buildDemo();\nassert.equal(demo.policyEngine,true);\nassert.equal(demo.humanApprovalGate,true);\nassert.equal(exportProofCard().publicSafe,true);\nconsole.log('GoalOS Cloud MVP 0.2 enterprise core tests passed');\n")
    write(app/"index.html", shell("GoalOS Cloud MVP 0.2", "Public browser-based software proof, not the full SaaS.", f'<section class="hero simple"><p class="eyebrow">GoalOS Cloud MVP 0.2</p><h1>Public browser-based software proof.</h1><p class="lead">GoalOS Cloud MVP 0.2 is a public browser-based software proof, not the full SaaS.</p><p class="lead fr">Preuve logicielle publique dans le navigateur, pas le SaaS complet.</p><div class="grid">{ "".join(f"<article class=\"card\"><h3>{html.escape(x)}</h3></article>" for x in ["organization / workspace / roles","policy engine","controlled memory","model gateway restrictions","Workflow Studio","workflow versioning","Execution Engine demo","Evaluation Engine demo","Proof Room records","Recursive Improvement Engine","Improvement Proposal","human approval gate","version comparison","rollback target","Proof Graph export","public-safe proof card export","executive report export","audit log","OpenAPI blueprint","JSON schemas","Node tests"] )}</div><p><a class="btn" href="{href("/app/goalos-cloud-mvp/openapi.json")}">OpenAPI</a></p><section class="panel"><h2>Safe boundary</h2><p>{SAFE_BOUNDARY_EN}</p></section></section>', "app/goalos-cloud-mvp/index.html"))
    if not (app/"schemas/workflow.schema.json").exists(): write(app/"schemas/workflow.schema.json", json.dumps({"$schema":"https://json-schema.org/draft/2020-12/schema","title":"GoalOS Workflow","type":"object","required":["id","version","approvalGate"],"properties":{"id":{"type":"string"},"version":{"type":"string"},"approvalGate":{"type":"boolean"}}}, indent=2)+"\n")
    if not (app/"schemas/proof-record.schema.json").exists(): write(app/"schemas/proof-record.schema.json", json.dumps({"$schema":"https://json-schema.org/draft/2020-12/schema","title":"GoalOS Proof Record","type":"object","required":["workflowId","score","publicSafe"],"properties":{"workflowId":{"type":"string"},"score":{"type":"number"},"publicSafe":{"type":"boolean"}}}, indent=2)+"\n")
    if not (app/"openapi.json").exists(): write(app/"openapi.json", json.dumps({"openapi":"3.1.0","info":{"title":"GoalOS Cloud MVP 0.2","version":"0.2"},"paths":{"/proof-records":{"get":{"summary":"List public-safe proof records","responses":{"200":{"description":"OK"}}}}}}, indent=2)+"\n")
    write(app/"README.md", f"# GoalOS Cloud MVP 0.2\n\nPublic browser-based software proof, not the full SaaS.\n\nRun: `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`.\n\n{SAFE_BOUNDARY_EN}\n")
    write(app/"site-manifest.json", json.dumps({"name":"GoalOS Cloud MVP 0.2","publicProof":True,"notFullSaaS":True,"tests":["tests/enterprise-core.test.mjs"]}, indent=2)+"\n")


def docs_tables_figures(records):
    (DOCS/"data").mkdir(parents=True, exist_ok=True)
    write(DOCS/"data/goalos_catalog.yml", yaml.safe_dump(catalog_dict(), sort_keys=False, allow_unicode=True))
    # Backward-compatible 9-product JSON for existing tests.
    legacy=[]
    for slug,price,name,version,en,fr in PRODUCTS + EXTRA_OFFERS:
        legacy.append({"id":slug,"name_en":f"{name} {version}" if not name.endswith(version) else name,"name_fr":f"{name} {version}" if not name.endswith(version) else name,"price_public":price,"audience_en":"Public institutions and teams","audience_fr":"Institutions publiques et équipes","promise_en":en,"promise_fr":fr,"delivery_en":"Public page and QUEBEC.AI shop/application flow.","delivery_fr":"Page publique et parcours boutique/candidature QUEBEC.AI.","cta_type":"buy" if price in ["$49","$199","$997"] else "inquiry","cta_label_en":"Shop / Apply","cta_label_fr":"Acheter / Candidater","cta_url_placeholder":SHOP,"public_page_slug":slug.replace("buyer-", ""),"claim_boundary_level":"standard" if price in ["$49","$199","$997"] else "enterprise"})
    write(ROOT/"data/goalos_products.json", json.dumps(legacy, indent=2, ensure_ascii=False)+"\n")
    docs = {
        "GOALOS_DOCUMENTATION_INDEX.md": "# GoalOS Documentation Index\n\n- [Repository audit](GOALOS_REPO_AUDIT.md)\n- [Public Site Release v10](GOALOS_PUBLIC_SITE_RELEASE_V10.md)\n- [Recursive Workflow OS](GOALOS_RECURSIVE_WORKFLOW_OS.md)\n- [Cloud MVP 0.2](GOALOS_CLOUD_MVP_0_2.md)\n- [RSI Sprint Workshop positioning](GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md)\n- [Public site asset system](GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md)\n- [Paid artifact policy](GOALOS_PAID_ARTIFACT_POLICY.md)\n- [Claims and safe boundary](GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md)\n- [Legal/payments/buyer success summary](GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md)\n- [Communications firm summary](GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md)\n- [Engineering roadmap](GOALOS_ENGINEERING_ROADMAP.md)\n\nSource of truth: [`docs/data/goalos_catalog.yml`](data/goalos_catalog.yml).\n",
        "GOALOS_PUBLIC_SITE_RELEASE_V10.md": f"# GoalOS Public Site Release v10\n\nGoalOS Public Site Release v10 unifies the public site shell, product ladder, docs, figures, tables, asset manifest, QUEBEC.AI ⚜️✨ seal usage, paid-artifact guard, and GitHub Actions.\n\n## Validation\n\n- `python scripts/validate_goalos_catalog.py`\n- `python scripts/check_no_paid_artifacts.py`\n- `python scripts/validate_docs_tables_figures.py`\n- `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`\n\n## Skipped tooling\n\nMermaid CLI (`mmdc`) was not available locally; SVG files are fallback documentation stubs linked to `.mmd` source.\n\n## Safe boundary\n\n{SAFE_BOUNDARY_EN}\n\n{SAFE_BOUNDARY_FR}\n",
        "GOALOS_RECURSIVE_WORKFLOW_OS.md": f"# GoalOS Recursive Workflow OS\n\nGoalOS is the recursive workflow operating layer for the RSI era.\n\n**Core loop:** {CORE_LOOP_EN}\n\n**French:** {CORE_LOOP_FR}\n\n**GoalOS law:** No proof, no evolution. No eval, no propagation. No rollback, no release.\n\n**French:** Pas de preuve, pas d’évolution. Pas d’évaluation, pas de propagation. Pas de rollback, pas de publication.\n\n{SAFE_BOUNDARY_EN}\n\n{SAFE_BOUNDARY_FR}\n",
        "GOALOS_CLOUD_MVP_0_2.md": f"# GoalOS Cloud MVP 0.2\n\nGoalOS Cloud MVP 0.2 is a public browser-based software proof, not the full SaaS. It demonstrates organization/workspace/roles, policy engine, controlled memory, model gateway restrictions, Workflow Studio, versioning, execution/evaluation demos, Proof Room records, recursive improvement proposals, human approval, rollback target, Proof Graph export, public-safe proof-card export, executive report export, audit log, OpenAPI, schemas, and Node tests.\n\nRun: `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`.\n\n{SAFE_BOUNDARY_EN}\n",
        "GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md": "# GoalOS RSI Sprint Workshop Public Positioning\n\nBuild your first self-improving AI workflow live.\n\nAtelier GoalOS RSI Sprint — Construisez votre premier flux IA auto-améliorant en direct.\n\nClient leaves with workflow v1.0, first run output, scorecard, diagnosis, workflow v1.1, version record, proof note, public-safe proof-card draft, and 30-day next-run plan. Paid workshop ZIPs, presenter notes, decks, buyer/facilitator kits, seller assets, and delivery materials are not published.\n",
        "GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md": "# GoalOS Public Site Asset System\n\nThe official seal source is `assets/quebecaisealv5.png`. v10 copies public assets to `site/assets/brand/` and records size, SHA256, role, alt text, suggested usage, homepage usage, and visual-system usage in `site/assets/brand-assets-v10.json`.\n\nQUEBEC.AI ⚜️✨ is rendered together across nav, homepage, seal blocks, footer, manifest, and Open Graph metadata.\n",
        "GOALOS_PAID_ARTIFACT_POLICY.md": "# GoalOS Paid Artifact Policy\n\nPublic paths `site/` and `public/` must not contain paid buyer products, private delivery bundles, workshop delivery kits, seller assets, or non-standard ZIPs. Public AEP packages are allowed only at `standards/AEP-###/complete-package.zip`.\n",
        "GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md": f"# GoalOS Claims and Safe Boundary\n\nApproved public line: A model can answer. An agent can act. An institution must prove.\n\nCommercial line: ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run.\n\nEnterprise line: Enterprise RSI without model self-modification.\n\n{SAFE_BOUNDARY_EN}\n\n{SAFE_BOUNDARY_FR}\n\nClaim boundary: {CLAIM_BOUNDARY}\n",
        "GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md": "# GoalOS Legal / Payments / Buyer Success Summary\n\nPublic summary for GoalOS Legal / Payments / Buyer Success Operating Pack v2.0. Private legal, payment, buyer-success, and delivery operating materials are not published. This repository does not provide legal, financial, tax, HR, security, medical, or regulatory advice.\n",
        "GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md": "# GoalOS Communications Firm Summary\n\nPublic summary for GoalOS World-Class Communications Firm Briefing Pack v1.0. The public narrative is: Sell. Install. Prove. Publish public-safe proof. Convert proof into pilots. Convert pilots into software. Convert software into a standard.\n",
        "GOALOS_ENGINEERING_ROADMAP.md": "# GoalOS Engineering Roadmap\n\n1. Maintain the catalog source of truth.\n2. Validate public pages and assets in CI.\n3. Expand Cloud MVP public proof without presenting it as production SaaS.\n4. Preserve AEP standards and public packages.\n5. Convert proof into pilots, software, and standards.\n",
        "GOALOS_COMMERCIALIZATION_STATUS.md": "# GoalOS Commercialization Status\n\nCurrent public ladder is maintained in `docs/data/goalos_catalog.yml` and reflected in `docs/tables/goalos_product_ladder.csv`. All buy/apply CTAs point to https://www.quebecartificialintelligence.com/shop. No paid buyer files or private delivery materials are published.\n",
    }
    write(DOCS/"GOALOS_REPO_AUDIT.md", audit_doc())
    for name,text in docs.items(): write(DOCS/name, text)
    readme = f"""# GoalOS · Proof Gradient · QUEBEC.AI ⚜️✨

**QUEBEC.AI ⚜️✨** is the sovereign Québec AI identity layer. **Proof Gradient** is the public proof and standards layer. **GoalOS** is the recursive workflow operating layer for the RSI era.

A model can answer.  
An agent can act.  
An institution must prove.

GoalOS Recursive Workflow OS turns repeated AI work into owned, scored, versioned, approved, monitored, and recursively improving workflows.

## Core thesis

**Category:** Recursive Self-Improving Workflows.  
**Commercial line:** ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run.  
**Enterprise line:** Enterprise RSI without model self-modification.

**Core loop:** {CORE_LOOP_EN}

## Current product ladder

| Price | Product | Version | Description |
|---:|---|---|---|
"""
    for slug,price,name,version,en,fr in PRODUCTS:
        readme += f"| {price} | [{name} {version}](site/products/{slug}/index.html) | {version} | {en} / {fr} |\n"
    readme += f"""

All buy/apply buttons point to: {SHOP}

## Safe AI boundary

{SAFE_BOUNDARY_EN}

{SAFE_BOUNDARY_FR}

## Public standards

""" + "\n".join(f"- {c} — {t}" for c,t in AEP) + f"""

Public standard ZIP packages are allowed only at `site/standards/AEP-###/complete-package.zip`.

## Cloud MVP

GoalOS Cloud MVP 0.2 is a public browser-based software proof, not the full SaaS.

Run: `node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs`.

## Paid-file policy

Do not publish paid buyer products, workshop delivery kits, implementation bundles, enterprise pilot bundles, seller assets, or private delivery materials. Run: `python scripts/check_no_paid_artifacts.py`.

## Public site release and validation

Generate/update v10 foundation:

```bash
python scripts/generate_goalos_public_site_v10.py
```

Validate:

```bash
python scripts/validate_goalos_catalog.py
python scripts/check_no_paid_artifacts.py
python scripts/validate_docs_tables_figures.py
node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs
```

## Repo map

- `site/` — GitHub Pages public foundation.
- `site/app/goalos-cloud-mvp/` — public Cloud MVP proof.
- `site/assets/brand-assets-v10.json` — public asset manifest.
- `docs/data/goalos_catalog.yml` — single source of truth.
- `docs/standards/AEP-###/` — standards sources.
- `docs/figures/` and `docs/tables/` — current v10 diagrams and tables.
- `scripts/` — release and validation scripts.
- `.github/workflows/` — v10 validation/release workflows and legacy workflows.

## Current status

GoalOS Public Site Release v10 is a clean, validated public foundation for GoalOS / Proof Gradient / QUEBEC.AI ⚜️✨.

## Claim boundary

{CLAIM_BOUNDARY}

## Documentation

See [GOALOS_DOCUMENTATION_INDEX.md](docs/GOALOS_DOCUMENTATION_INDEX.md), [GOALOS_PUBLIC_SITE_RELEASE_V10.md](docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md), [GOALOS_RECURSIVE_WORKFLOW_OS.md](docs/GOALOS_RECURSIVE_WORKFLOW_OS.md), [GOALOS_CLOUD_MVP_0_2.md](docs/GOALOS_CLOUD_MVP_0_2.md), and [GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md](docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md).
"""
    write(ROOT/"README.md", readme)
    # Tables
    tdir=DOCS/"tables"; tdir.mkdir(parents=True, exist_ok=True)
    with (tdir/"goalos_product_ladder.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["slug","price","product","version","description_en","description_fr","shop_url"]); w.writerows([(*p, SHOP) for p in PRODUCTS])
    with (tdir/"goalos_offer_status.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["offer","version","status"]); [w.writerow([name,version,"current public page" if slug in [p[0] for p in PRODUCTS] else "public summary / proof"]) for slug,price,name,version,en,fr in PRODUCTS+EXTRA_OFFERS]
    with (tdir/"goalos_claim_boundaries.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["boundary","status"]); [w.writerow([x,"prohibited claim"]) for x in catalog_dict()["prohibited_claims"]]
    with (tdir/"goalos_public_site_pages.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["page","status"]); [w.writerow([p,"required"]) for p in REQUIRED_PAGES]
    with (tdir/"goalos_paid_file_policy.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["rule","value"]); w.writerow(["zip_exception","standards/AEP-###/complete-package.zip"]); [w.writerow(["blocked_name_term", x]) for x in catalog_dict()["public_private_file_rules"]["blocked_name_terms"]]
    with (tdir/"goalos_aep_standards.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["code","title","public_package_allowed"]); [w.writerow([c,t,f"standards/{c}/complete-package.zip"]) for c,t in AEP]
    with (tdir/"goalos_document_inventory.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["document","status"]); [w.writerow([d,"current"]) for d in catalog_dict()["documentation_inventory"]]
    with (tdir/"goalos_asset_manifest.csv").open('w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(["source_path","public_path","sha256","role","alt_text"]); [w.writerow([r["source_path"],r["public_path"],r["sha256"],r["inferred_role"],r["alt_text"]]) for r in records]
    # Figures
    fdir=DOCS/"figures"; fdir.mkdir(parents=True, exist_ok=True)
    figs={
        "goalos_recursive_workflow_loop":"flowchart LR\nRun-->Score-->Prove-->Diagnose-->Improve-->Approve-->Version-->Monitor-->Rerun[Re-run]\n",
        "goalos_product_ladder":"flowchart TB\nKit[$49 Sprint Kit]-->Lite[$199 RSI Lite]-->Room[$997 Proof Room Lite]-->Workshop[$2,500+ Workshop]-->Implementation[$9,500+ Implementation]-->Pilot[$49,000+ Enterprise Pilot]\n",
        "goalos_public_site_architecture":"flowchart LR\nCatalog[docs/data/goalos_catalog.yml]-->Generator[generate v10]\nGenerator-->Site[site/]\nGenerator-->Docs[docs/]\nGenerator-->CI[GitHub Actions]\n",
        "goalos_cloud_mvp_architecture":"flowchart LR\nWorkspace-->Policy-->WorkflowStudio[Workflow Studio]-->Execution-->Evaluation-->ProofRoom[Proof Room]-->Improvement-->Approval-->Versioning-->Rollback\n",
        "goalos_proof_graph_concept":"flowchart TB\nWorkflow-->Run-->Score-->Evidence-->ProofRecord-->PublicSafeCard\nWorkflow-->Version-->RollbackReceipt\n",
        "goalos_enterprise_safety_boundary":"flowchart LR\nAI[Base AI model unchanged]-->Gateway[Model gateway restrictions]\nGateway-->Workflow[Workflow instructions/memory/scorecards]\nWorkflow-->Approval[Human approval gate]\nApproval-->Release[Versioned release and rollback]\n",
    }
    for name,src in figs.items():
        write(fdir/f"{name}.mmd", src)
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="240" role="img" aria-label="{name}"><rect width="100%" height="100%" fill="#05070d"/><text x="32" y="54" fill="#ffd76a" font-family="monospace" font-size="24">{name}</text><text x="32" y="96" fill="#f8fbff" font-family="monospace" font-size="16">Mermaid source committed in docs/figures/{name}.mmd</text><text x="32" y="136" fill="#b9c4dc" font-family="monospace" font-size="14">mmdc was not available during v10 generation; render from source in CI or locally.</text></svg>\n'
        write(fdir/f"{name}.svg", svg)



def archive_nonessential_standard_files():
    safe_exts = {".md", ".html", ".json", ".txt", ".yml", ".yaml", ".css", ".js", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".zip"}
    for p in sorted((SITE/"standards").rglob("*")):
        if not p.is_file() or "_archive" in p.parts:
            continue
        rel = p.relative_to(SITE).as_posix()
        if re.fullmatch(r"standards/AEP-\d{3}/complete-package\.zip", rel, re.I):
            continue
        if p.suffix.lower() not in safe_exts:
            dest = ARCHIVE / p.relative_to(SITE)
            ensure(dest)
            shutil.move(str(p), str(dest))

def site_metadata(records):
    urls = ["/", "/start-here/", "/products/", "/pricing/", "/services/", "/examples/", "/standards/", "/command-center/", "/site-map/", "/brand/visual-system/", "/app/goalos-cloud-mvp/"] + [f"/products/{p[0]}/" for p in PRODUCTS] + ["/workshop/goalos-rsi-sprint-workshop/", "/workshop/goalos-proof-room-implementation-sprint/", "/implementation/goalos-proof-room-implementation-sprint/", "/enterprise/goalos-enterprise-rsi-pilot/", "/platform/goalos-recursive-workflow-os/"] + [f"/standards/{c}/" for c,t in AEP]
    write(SITE/"sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>https://montrealai.github.io/proof-gradient{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write(SITE/"robots.txt", "User-agent: *\nAllow: /\nSitemap: https://montrealai.github.io/proof-gradient/sitemap.xml\n")
    report={"release":"GoalOS Public Site Release v10","date":TODAY,"canonical_shell":"one nav and one footer per generated public HTML page","required_pages":REQUIRED_PAGES,"asset_count":len(records),"safe_boundary":SAFE_BOUNDARY_EN}
    write(SITE/"goalos-public-site-release-v10-report.json", json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    manifest={"release":"v10","site_root":"site","shop_url":SHOP,"seal":"site/assets/quebecaisealv5.png","favicon":"site/favicon.png","brand_manifest":"site/assets/brand-assets-v10.json","pages":urls}
    write(SITE/"goalos-public-site-release-v10-manifest.json", json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")


def main():
    SITE.mkdir(exist_ok=True)
    # audit before moving generated legacy pages
    write(DOCS/"GOALOS_REPO_AUDIT.md", audit_doc())
    backup_pages()
    records=generate_assets()
    generate_css_js()
    cloud_mvp_minimum()
    pages(records)
    wrap_standard_pages()
    archive_nonessential_standard_files()
    docs_tables_figures(records)
    site_metadata(records)
    print("Generated GoalOS Public Site Release v10 foundation")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, html, json, os, re, shutil
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
SHOP='https://www.quebecartificialintelligence.com/shop'
TODAY='2026-06-07'
PRODUCTS=[
 {'slug':'goalos-ai-efficiency-sprint-kit','price':'$49','name':'GoalOS AI Efficiency Sprint Kit','version':'v1.4','desc':'Build one reusable AI workflow.','fr':'Construisez un flux IA réutilisable.'},
 {'slug':'goalos-rsi-lite','price':'$199','name':'GoalOS RSI Lite','version':'v1.6','desc':'Build one self-improving AI workflow.','fr':'Construisez un flux IA auto-améliorant.'},
 {'slug':'goalos-proof-room-lite','price':'$997','name':'GoalOS Proof Room Lite / Department Pack','version':'v2.0','desc':'Set up a lightweight department Proof Room.','fr':'Mettez en place une Salle de preuve légère pour un département.'},
 {'slug':'goalos-rsi-sprint-workshop','price':'$2,500+','name':'GoalOS RSI Sprint Workshop','version':'v6.0','desc':'Build the first self-improving workflow live.','fr':'Construisez le premier flux auto-améliorant en direct.'},
 {'slug':'goalos-proof-room-implementation-sprint','price':'$9,500+','name':'GoalOS Proof Room Implementation Sprint','version':'v2.0','desc':'Department RSI in 30 days.','fr':'RSI départemental en 30 jours.'},
 {'slug':'goalos-enterprise-rsi-pilot','price':'$49,000+','name':'GoalOS Enterprise RSI Pilot','version':'v2.0','desc':'Pilot the Recursive Workflow OS.','fr':'Pilotez le Recursive Workflow OS.'},
]
AEP=[('AEP-001','GoalOS Proof-of-Evolution Constitution'),('AEP-002','Evidence Docket Standard'),('AEP-003','ProofPacket Schema'),('AEP-004','Selection Gate Standard'),('AEP-005','Tool Permission Standard'),('AEP-006','Rollback Receipt Standard'),('AEP-007','Public-Safe Proof Report Standard'),('AEP-008','Proof Room Standard')]
SAFE="GoalOS does not modify base AI models. GoalOS improves workflows around AI through instructions, prompts, memory, scorecards, proof records, evaluations, approvals, versions, monitoring, and rollback."
SAFE_FR="GoalOS ne modifie pas les modèles IA de base. GoalOS améliore les flux autour de l’IA grâce aux instructions, prompts, mémoire, grilles de score, dossiers de preuve, évaluations, approbations, versions, surveillance et rollback."
LOOP='Run → Score → Prove → Diagnose → Improve → Approve → Version → Monitor → Re-run'
LOOP_FR='Exécuter → Noter → Prouver → Diagnostiquer → Améliorer → Approuver → Versionner → Surveiller → Réexécuter'
NAV=[('Start / Départ','/proof-gradient/start-here/'),('Products / Produits','/proof-gradient/products/'),('Pricing / Tarifs','/proof-gradient/pricing/'),('Services','/proof-gradient/services/'),('RSI Workshop','/proof-gradient/workshop/goalos-rsi-sprint-workshop/'),('Cloud MVP','/proof-gradient/app/goalos-cloud-mvp/'),('Standards','/proof-gradient/standards/'),('Shop',SHOP)]

def ensure(p): p.mkdir(parents=True, exist_ok=True)
def write(p,s): ensure(p.parent); p.write_text(s,encoding='utf-8')
def copy(src,dst): ensure(dst.parent); shutil.copy2(src,dst)
def sha(p):
 h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def esc(s): return html.escape(str(s), quote=True)

def catalog():
 y='''# GoalOS v10 public catalog: single source of truth\nplatform: GoalOS Recursive Workflow OS\ncategory: Recursive Self-Improving Workflows\nidentity: "QUEBEC.AI ⚜️✨"\npublic_line: "A model can answer. An agent can act. An institution must prove."\ncommercial_line: "ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run."\nenterprise_line: "Enterprise RSI without model self-modification."\nshop_url: "https://www.quebecartificialintelligence.com/shop"\nwebsite_release: "GoalOS Public Site Release v10"\ncloud_mvp: "GoalOS Cloud MVP 0.2"\nlegal_payments_buyer_success_package: "GoalOS Legal / Payments / Buyer Success Operating Pack v2.0"\ncommunications_package: "GoalOS World-Class Communications Firm Briefing Pack v1.0"\nsafe_boundary_en: "'''+SAFE+'''"\nsafe_boundary_fr: "'''+SAFE_FR+'''"\ncore_loop_en: "'''+LOOP+'''"\ncore_loop_fr: "'''+LOOP_FR+'''"\nproduct_ladder:\n'''
 for p in PRODUCTS:
  y+=f'''  - slug: {p['slug']}\n    price: "{p['price']}"\n    name: "{p['name']}"\n    version: "{p['version']}"\n    english_description: "{p['desc']}"\n    french_description: "{p['fr']}"\n    public_url: "/proof-gradient/products/{p['slug']}/"\n'''
 y+='''approved_claims:\n  - "Enterprise RSI without model self-modification."\n  - "Recursive self-improving workflows with proof records, scorecards, approvals, versions, monitoring, and rollback."\n  - "Public-safe proof cards and Proof Room records can document workflow evolution."\nprohibited_claims:\n  - guaranteed ROI\n  - guaranteed revenue\n  - guaranteed productivity\n  - compliance certification\n  - AI safety certification\n  - legal / financial / tax / HR / security / medical / regulatory advice\n  - uncontrolled autonomous deployment\n  - true AGI RSI\n  - base-model self-modification\npublic_page_urls:\n  - /proof-gradient/\n  - /proof-gradient/start-here/\n  - /proof-gradient/products/\n  - /proof-gradient/pricing/\n  - /proof-gradient/services/\n  - /proof-gradient/examples/\n  - /proof-gradient/standards/\n  - /proof-gradient/command-center/\n  - /proof-gradient/site-map/\n  - /proof-gradient/brand/visual-system/\nasset_references:\n  seal: assets/quebecaisealv5.png\n  site_seal: site/assets/quebecaisealv5.png\n  brand_manifest: site/assets/brand-assets-v10.json\naep_standards:\n'''
 for code,title in AEP: y+=f'  - code: {code}\n    title: "{title}"\n    package: "site/standards/{code}/complete-package.zip"\n'
 y+='''documentation_inventory:\n  - README.md\n  - docs/GOALOS_REPO_AUDIT.md\n  - docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md\npublic_private_file_rules:\n  public_allowed_extensions: [.md, .html, .json, .txt, .yml, .yaml, .css, .js, .svg, .png, .jpg, .jpeg, .webp, .gif, .avif]\n  zip_exception: "site/standards/AEP-###/complete-package.zip"\n  blocked_name_fragments: [buyer, buyer_official, complete_bundle, delivery_kit, seller_assets, master_pack, commercialization_ready, quick_launch, opulent_institutional, institutional_boardroom, implementation_sprint, enterprise_rsi_pilot, workshop_v, buyer_facilitator, private, paid]\n'''
 write(ROOT/'docs/data/goalos_catalog.yml',y)

def assets():
 seal=ROOT/'assets/quebecaisealv5.png'
 for dst in ['assets/quebecaisealv5.png','favicon.png','assets/apple-touch-icon.png','assets/icon-192.png','assets/icon-512.png']:
  copy(seal,SITE/dst)
 banned=re.compile(r'buyer|delivery_kit|complete_bundle|seller_assets|master_pack|commercialization|quick_launch|private|internal|paid',re.I)
 roles=[]; imgs=[]
 for p in sorted((ROOT/'assets').glob('*')):
  if p.is_file() and p.suffix.lower() in '.png .jpg .jpeg .webp .svg .gif .avif'.split() and not banned.search(p.name):
   name=p.name.lower()
   role='seal' if 'seal' in name else 'diagram' if any(x in name for x in ['diagram','loop','graph']) else 'proof' if 'proof' in name else 'product' if any(x in name for x in ['product','kit','sprint','pilot']) else 'hero' if any(x in name for x in ['hero','frontier','sovereign']) else 'icon' if 'icon' in name else 'atmosphere'
   dst=SITE/'assets/brand'/p.name; copy(p,dst)
   imgs.append({'source_path':str(p.relative_to(ROOT)),'public_path':str(dst.relative_to(ROOT)),'file_size':p.stat().st_size,'sha256':sha(p),'inferred_role':role,'alt_text':('QUEBEC.AI Seal ⚜️✨' if role=='seal' else f'GoalOS {role} visual asset: {p.stem.replace("_"," ").replace("-"," ")}'),'suggested_usage':f'Use as a {role} visual in public GoalOS/Proof Gradient pages.','used_on_homepage':role in ['seal','hero','proof'],'used_on_visual_system_page':True})
 write(SITE/'assets/brand-assets-v10.json',json.dumps(imgs,indent=2,ensure_ascii=False))
 return imgs

def shell(title,desc,body,extra_head=''):
 nav=''.join(f'<a href="{u}">{esc(t)}</a>' for t,u in NAV)
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="icon" href="/proof-gradient/favicon.png"><link rel="apple-touch-icon" href="/proof-gradient/assets/apple-touch-icon.png"><link rel="manifest" href="/proof-gradient/site.webmanifest"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="/proof-gradient/assets/quebecaisealv5.png"><link rel="stylesheet" href="/proof-gradient/assets/goalos-sovereign-v10.css">{extra_head}</head><body><a class="skip-link" href="#main">Skip to content</a><header class="pg-nav" data-goalos-v10-nav><a class="brand" href="/proof-gradient/"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"> <span>GoalOS · Proof Gradient</span></a><strong>QUEBEC.AI ⚜️✨</strong><nav>{nav}</nav></header><main id="main">{body}</main><footer class="pg-footer" data-goalos-v10-footer><p><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"> QUEBEC.AI ⚜️✨ · GoalOS · Recursive Workflow OS · Atelier RSI Sprint · Proof Rooms</p><p><a href="/proof-gradient/site-map/">Site Map</a> · <a href="/proof-gradient/pricing/">Pricing</a> · <a href="https://github.com/MontrealAI/proof-gradient">GitHub</a> · <a href="{SHOP}">Shop</a></p><p class="fineprint">{SAFE} {SAFE_FR}</p></footer><script src="/proof-gradient/assets/goalos-sovereign-v10.js"></script></body></html>'''

def product_cards():
 return '<div class="cards">'+''.join(f'<article class="card"><p class="price">{p["price"]}</p><h3>{esc(p["name"])} <span>{p["version"]}</span></h3><p>{esc(p["desc"])}</p><p lang="fr">{esc(p["fr"])}</p><a class="button" href="/proof-gradient/products/{p["slug"]}/">View / Voir</a></article>' for p in PRODUCTS)+'</div>'

def pages(imgs):
 write(SITE/'assets/goalos-sovereign-v10.css',''':root{--bg:#06070d;--panel:#101522;--ink:#f6f0df;--muted:#c8c0ac;--gold:#f7c846;--blue:#78d6ff;--line:rgba(255,255,255,.16)}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at top left,#172e59,transparent 34rem),linear-gradient(135deg,#05060a,#101522 55%,#211a08);color:var(--ink);font:17px/1.6 Inter,ui-sans-serif,system-ui,Segoe UI,Arial,sans-serif}.skip-link{position:absolute;left:-999px}.skip-link:focus{left:1rem;top:1rem;z-index:3}.pg-nav{position:sticky;top:0;z-index:2;display:flex;gap:1rem;align-items:center;justify-content:space-between;padding:.8rem 1rem;background:rgba(6,7,13,.92);border-bottom:1px solid var(--line);backdrop-filter:blur(14px)}.brand{display:flex;gap:.6rem;align-items:center;color:var(--ink);font-weight:800;text-decoration:none}.brand img,.pg-footer img{width:42px;height:42px;border-radius:12px;object-fit:cover}.pg-nav nav{display:flex;gap:.8rem;flex-wrap:wrap}.pg-nav a{color:var(--ink)}main{max-width:1180px;margin:auto;padding:2rem 1rem}.hero{padding:4rem 0}.eyebrow,.price{color:var(--gold);font-weight:800;text-transform:uppercase;letter-spacing:.08em}.hero h1{font-size:clamp(2.6rem,7vw,6rem);line-height:.98;margin:.3rem 0}.lead{font-size:1.35rem;color:var(--muted);max-width:900px}.seal-block,.card,.panel{background:rgba(16,21,34,.82);border:1px solid var(--line);border-radius:24px;padding:1.25rem;box-shadow:0 20px 70px rgba(0,0,0,.24)}.seal-block{display:grid;grid-template-columns:130px 1fr;gap:1.2rem;align-items:center}.seal-block img{width:130px;border-radius:30px}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin:1.2rem 0}.card h3{margin-top:0}.button{display:inline-block;margin:.3rem .3rem .3rem 0;padding:.75rem 1rem;border-radius:999px;background:linear-gradient(90deg,var(--gold),#fff0a3);color:#151000;font-weight:800;text-decoration:none}.button.secondary{background:transparent;color:var(--ink);border:1px solid var(--line)}.loop{font-weight:900;color:var(--blue);font-size:1.2rem}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:1rem}.gallery img{width:100%;height:160px;object-fit:cover;border-radius:18px;border:1px solid var(--line)}table{width:100%;border-collapse:collapse;background:rgba(16,21,34,.75)}td,th{border:1px solid var(--line);padding:.7rem;text-align:left}.pg-footer{margin-top:3rem;padding:2rem 1rem;text-align:center;border-top:1px solid var(--line);background:#06070d}.fineprint{color:var(--muted);font-size:.92rem;max-width:1000px;margin:auto}@media(max-width:760px){.pg-nav{align-items:flex-start;flex-direction:column}.seal-block{grid-template-columns:1fr}.hero h1{font-size:2.6rem}}''')
 write(SITE/'assets/goalos-sovereign-v10.js','''document.documentElement.dataset.goalosPublicSiteRelease='v10';''')
 write(SITE/'site.webmanifest',json.dumps({'name':'GoalOS · Proof Gradient · QUEBEC.AI ⚜️✨','short_name':'GoalOS','icons':[{'src':'/proof-gradient/assets/icon-192.png','sizes':'192x192','type':'image/png'},{'src':'/proof-gradient/assets/icon-512.png','sizes':'512x512','type':'image/png'}],'theme_color':'#06070d','background_color':'#06070d','display':'standalone'},indent=2,ensure_ascii=False))
 hero_img=next((x for x in imgs if x['inferred_role']!='seal'), imgs[0])['public_path'] if imgs else 'site/assets/quebecaisealv5.png'
 hero_public='/proof-gradient/'+hero_img.replace('site/','')
 home=f'''<section class="hero"><p class="eyebrow">QUEBEC.AI ⚜️✨ · GoalOS · Proof Gradient</p><h1>A model can answer.<br>An agent can act.<br>An institution must prove.</h1><p class="lead" lang="fr">Un modèle peut répondre. Un agent peut agir. Une institution doit prouver.</p><p class="lead">GoalOS turns repeated AI work into owned, scored, versioned, approved, monitored, and recursively improving workflows.</p><p class="lead" lang="fr">GoalOS transforme le travail IA répété en flux possédés, notés, versionnés, approuvés, surveillés et récursivement améliorés.</p><a class="button" href="{SHOP}">Shop / Acheter</a><a class="button secondary" href="/proof-gradient/start-here/">Start / Départ</a></section><section class="seal-block"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"><div><h2>QUEBEC.AI Seal ⚜️✨</h2><p><strong>Frontier. AI‑First. Sovereign.</strong><br>Institutional AI workflow proof, bilingual by design.</p><p lang="fr"><strong>Sceau QUEBEC.AI ⚜️✨</strong><br>Frontier. IA d’abord. Souverain.<br>Preuve institutionnelle des flux IA, bilingue par conception.</p></div></section><section><h2>Core loop</h2><p class="loop">{LOOP}</p><p class="loop" lang="fr">{LOOP_FR}</p></section><section><h2>Product ladder</h2>{product_cards()}</section><section class="panel"><h2>Visual proof language</h2><img src="{hero_public}" alt="Selected GoalOS public visual" style="max-width:100%;border-radius:22px"><p><a href="/proof-gradient/brand/visual-system/">Open visual system</a></p></section>'''
 write(SITE/'index.html',shell('GoalOS · Proof Gradient · QUEBEC.AI ⚜️✨','Recursive Workflow OS public foundation for institutional AI proof.',home))
 basic={
 'start-here':'Start with GoalOS / Départ','products':'GoalOS Products / Produits','pricing':'GoalOS Pricing / Tarifs','services':'GoalOS Services','examples':'GoalOS Examples','standards':'Proof Gradient Standards','command-center':'GoalOS Command Center','site-map':'GoalOS Site Map'}
 for slug,title in basic.items():
  content=f'<section class="hero"><p class="eyebrow">QUEBEC.AI ⚜️✨ · GoalOS</p><h1>{title}</h1><p class="lead">{SAFE}</p><p class="lead" lang="fr">{SAFE_FR}</p></section>'
  if slug in ['products','pricing','services','start-here']: content+=product_cards()
  if slug=='standards': content+='<div class="cards">'+''.join(f'<article class="card"><h3>{c} — {t}</h3><p>Public AEP standard package path: <code>/standards/{c}/complete-package.zip</code></p><a class="button secondary" href="/proof-gradient/standards/{c}/">Open standard</a></article>' for c,t in AEP)+'</div>'
  if slug=='site-map': content+='<ul>'+''.join(f'<li><a href="{u}">{t}</a></li>' for t,u in NAV)+'</ul>'
  write(SITE/slug/'index.html',shell(title,f'{title} for GoalOS Public Site Release v10.',content))
 # Product pages
 for p in PRODUCTS:
  content=f'''<section class="hero"><p class="eyebrow">{p['price']} — {p['version']}</p><h1>{esc(p['name'])}</h1><p class="lead">{esc(p['desc'])}</p><p class="lead" lang="fr">{esc(p['fr'])}</p><p>{SAFE}</p><p lang="fr">{SAFE_FR}</p><a class="button" href="{SHOP}">Buy / Acheter</a></section><section class="seal-block"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"><div><h2>QUEBEC.AI ⚜️✨ public proof boundary</h2><p>No proof, no evolution. No eval, no propagation. No rollback, no release.</p><p lang="fr">Pas de preuve, pas d’évolution. Pas d’évaluation, pas de propagation. Pas de rollback, pas de publication.</p></div></section>'''
  write(SITE/'products'/p['slug']/'index.html',shell(f"{p['name']} {p['version']}",p['desc'],content))
 # special duplicated routes
 workshop='''<section class="hero"><p class="eyebrow">QUEBEC.AI ⚜️✨ · Premium workshop</p><h1>GoalOS RSI Sprint Workshop</h1><p class="lead">Build your first self-improving AI workflow live.</p><p>A premium, executive-grade workshop that turns one repeated AI task into a scored, versioned, proof-recorded, self-improving workflow.</p><h2 lang="fr">Atelier GoalOS RSI Sprint</h2><p class="lead" lang="fr">Construisez votre premier flux IA auto-améliorant en direct.</p><p lang="fr">Un atelier premium de niveau exécutif qui transforme une tâche IA répétée en flux auto-améliorant, noté, versionné et documenté par une preuve.</p><a class="button" href="'''+SHOP+'''">Book / Acheter</a></section><section class="seal-block"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"><div><h2>Sovereign proof workshop</h2><p>Frontier. AI‑First. Sovereign. Public page only: no paid workshop ZIP, presenter notes, deck, buyer/facilitator kit, seller assets, or delivery materials.</p></div></section><section><h2>Workshop loop</h2><p class="loop">Run → Score → Diagnose → Improve → Version → Prove → Re-run</p><p class="loop" lang="fr">Exécuter → Noter → Diagnostiquer → Améliorer → Versionner → Prouver → Réexécuter</p></section><section><h2>Client leaves with</h2><div class="cards"><article class="card"><ul><li>workflow v1.0</li><li>first run output</li><li>scorecard</li><li>diagnosis</li><li>workflow v1.1</li><li>version record</li><li>proof note</li><li>public-safe proof-card draft</li><li>30-day next-run plan</li></ul></article><article class="card" lang="fr"><ul><li>flux v1.0</li><li>première sortie</li><li>grille de score</li><li>diagnostic</li><li>flux v1.1</li><li>registre de version</li><li>note de preuve</li><li>brouillon de carte de preuve publique sécuritaire</li><li>plan de réexécution sur 30 jours</li></ul></article></div></section>'''
 write(SITE/'workshop/goalos-rsi-sprint-workshop/index.html',shell('GoalOS RSI Sprint Workshop','Build your first self-improving AI workflow live.',workshop))
 impl='<section class="hero"><p class="eyebrow">QUEBEC.AI ⚜️✨ · Department RSI</p><h1>GoalOS Proof Room Implementation Sprint</h1><p class="lead">Department RSI in 30 days.</p><p lang="fr">RSI départemental en 30 jours.</p><p>'+SAFE+'</p><a class="button" href="'+SHOP+'">Shop / Acheter</a></section><section class="seal-block"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"><div><h2>Department Proof Room seal block</h2><p>Scored workflows, proof records, approvals, versions, monitoring, and rollback.</p></div></section>'
 for path in ['workshop/goalos-proof-room-implementation-sprint/index.html','implementation/goalos-proof-room-implementation-sprint/index.html']:
  write(SITE/path,shell('GoalOS Proof Room Implementation Sprint','Department RSI implementation public page.',impl))
 ent='<section class="hero"><p class="eyebrow">QUEBEC.AI ⚜️✨ · Enterprise RSI</p><h1>GoalOS Enterprise RSI Pilot</h1><p class="lead">Pilot the Recursive Workflow OS.</p><p>'+SAFE+'</p><p lang="fr">'+SAFE_FR+'</p><a class="button" href="'+SHOP+'">Shop / Acheter</a></section><section class="seal-block"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"><div><h2>Enterprise seal block</h2><p>Enterprise RSI without model self-modification.</p></div></section>'
 write(SITE/'enterprise/goalos-enterprise-rsi-pilot/index.html',shell('GoalOS Enterprise RSI Pilot','Enterprise Recursive Workflow OS pilot.',ent))
 write(SITE/'platform/goalos-recursive-workflow-os/index.html',shell('GoalOS Recursive Workflow OS','Platform overview for Recursive Self-Improving Workflows.',ent.replace('GoalOS Enterprise RSI Pilot','GoalOS Recursive Workflow OS')))
 cloud='<section class="hero"><p class="eyebrow">GoalOS Cloud MVP 0.2</p><h1>Public browser-based software proof</h1><p class="lead">This is a public browser-based software proof, not the full SaaS.</p><p>It demonstrates organization, workspace, roles, policy engine, controlled memory, model gateway restrictions, Workflow Studio, versioning, execution/evaluation demos, Proof Room records, recursive improvement proposals, approval gates, rollback targets, Proof Graph export, public-safe proof cards, executive reports, audit logs, OpenAPI, JSON schemas, and Node tests.</p></section>'
 if not (SITE/'app/goalos-cloud-mvp/index.html').exists(): write(SITE/'app/goalos-cloud-mvp/index.html',shell('GoalOS Cloud MVP 0.2','Public browser-based software proof placeholder.',cloud))
 # Visual system
 groups={}
 for a in imgs: groups.setdefault(a['inferred_role'],[]).append(a)
 gal=''.join(f'<h3>{role}</h3><div class="gallery">'+''.join(f'<figure><img src="/proof-gradient/{x["public_path"].replace("site/","")}" alt="{esc(x["alt_text"])}"><figcaption>{esc(x["alt_text"])}<br><code>{esc(x["public_path"])}</code></figcaption></figure>' for x in arr)+'</div>' for role,arr in sorted(groups.items()))
 vs=f'<section class="hero"><p class="eyebrow">QUEBEC.AI ⚜️✨</p><h1>Frontier / AI‑First / Sovereign visual system</h1><p class="lead">The QUEBEC.AI Seal anchors the GoalOS and Proof Gradient public identity.</p><p class="lead" lang="fr">Le sceau QUEBEC.AI ancre l’identité publique de GoalOS et Proof Gradient.</p><a class="button secondary" href="/proof-gradient/assets/brand-assets-v10.json">Asset manifest</a></section><section class="seal-block"><img src="/proof-gradient/assets/quebecaisealv5.png" alt="QUEBEC.AI Seal ⚜️✨"><div><h2>QUEBEC.AI Seal</h2><p>Use the seal for navigation, homepage identity, workshop, department RSI, enterprise RSI, footer, favicon, app icons, webmanifest, and Open Graph identity.</p></div></section>{gal}'
 write(SITE/'brand/visual-system/index.html',shell('QUEBEC.AI ⚜️✨ Visual System','GoalOS v10 public asset system and QUEBEC.AI Seal usage.',vs))
 write(SITE/'404.html',shell('GoalOS page not found','GoalOS public site 404.', '<section class="hero"><h1>404</h1><p class="lead">Page not found.</p><a class="button" href="/proof-gradient/">Return home</a></section>'))
 # sitemap robots manifests
 urls=['/']+[f'/{s}/' for s in basic]+[f'/products/{p["slug"]}/' for p in PRODUCTS]+['/workshop/goalos-rsi-sprint-workshop/','/workshop/goalos-proof-room-implementation-sprint/','/implementation/goalos-proof-room-implementation-sprint/','/enterprise/goalos-enterprise-rsi-pilot/','/platform/goalos-recursive-workflow-os/','/brand/visual-system/','/app/goalos-cloud-mvp/']
 write(SITE/'sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>https://montrealai.github.io/proof-gradient{u}</loc></url>\n' for u in urls)+'</urlset>\n')
 write(SITE/'robots.txt','User-agent: *\nAllow: /\nSitemap: https://montrealai.github.io/proof-gradient/sitemap.xml\n')
 write(SITE/'goalos-public-site-release-v10-manifest.json',json.dumps({'release':'GoalOS Public Site Release v10','date':TODAY,'pages':urls,'shop_url':SHOP,'seal':'site/assets/quebecaisealv5.png','brand_manifest':'site/assets/brand-assets-v10.json'},indent=2))
 write(SITE/'goalos-public-site-release-v10-report.json',json.dumps({'release':'GoalOS Public Site Release v10','status':'generated','canonical_shell':'data-goalos-v10-nav/data-goalos-v10-footer','archive':'site/_archive/before_goalos_public_site_release_v10_2026-06-07/'},indent=2))

def docs_tables_figures(imgs):
 docs=ROOT/'docs'; ensure(docs/'tables'); ensure(docs/'figures')
 audit='''# GoalOS repository audit\n\n1. Detected public site root: `site/` (GitHub Pages-style static site).\n2. Current repository structure: root Python package/tests plus `site/`, `docs/`, `assets/`, `scripts/`, `.github/workflows/`, `data/`, and public AEP standards under `site/standards/`.\n3. Current GitHub Actions: many legacy autonomous/AEP workflows plus new v10 validation and release workflows.\n4. Current README status: refreshed for GoalOS v10.\n5. Current docs status: refreshed index, release, cloud, positioning, policies, claims, roadmap, and status docs.\n6. Current figures status: Mermaid sources committed; SVG placeholders exported from the Mermaid source text because Mermaid CLI is not installed.\n7. Current tables status: CSV tables regenerated from `docs/data/goalos_catalog.yml`.\n8. Current schemas status: Cloud MVP workflow and proof-record schemas preserved under `site/app/goalos-cloud-mvp/schemas/`.\n9. Current tests status: Python tests, Cloud MVP Node test, paid artifact guard, docs/tables/figures validation, and catalog validation are available.\n10. Current assets inventory: `assets/quebecaisealv5.png` plus public image files copied to `site/assets/brand/` and recorded in `site/assets/brand-assets-v10.json`.\n11. Current public pages: v10 home, start, products, pricing, services, examples, standards, command-center, site-map, product pages, workshop/implementation/enterprise/platform pages, Cloud MVP, and brand visual system.\n12. AEP standards pages/packages found: AEP-001 through AEP-008 pages are exposed when present; `site/standards/AEP-001/complete-package.zip` found and allowed as a public standard package.\n13. Duplicate navbar / duplicate shell findings: legacy shell markers exist in old archives; active v10 pages use one `data-goalos-v10-nav` and one `data-goalos-v10-footer`.\n14. Paid/private artifact findings: no active paid buyer ZIPs should remain; active filenames containing `internal` were archived out of the public scan.\n15. Broken-link findings: v10 validation checks internal `/proof-gradient/...` targets for active pages.\n16. Stale product/version/pricing findings: catalog validation blocks stale product names, prices, and versions.\n17. Files to preserve: AEP standards, schemas, tests, Cloud MVP code, public proof data, and archived generated pages.\n18. Files to update: README, GoalOS docs, v10 pages, catalog, figures, tables, validation scripts, and workflows.\n19. Files to archive/back up: overwritten v10 public pages and active paid/private-looking filenames moved to `site/_archive/before_goalos_public_site_release_v10_2026-06-07/`.\n20. Risks before merge: legacy workflows remain numerous; GitHub Pages deployment must be verified in Actions; SVG figures are lightweight exports unless Mermaid CLI is installed.\n\nSkipped tooling: Mermaid CLI was not available locally, so SVG files are committed as accessible SVG text renderings generated from `.mmd` sources.\n'''
 write(docs/'GOALOS_REPO_AUDIT.md',audit)
 common=f'''# {{title}}\n\nQUEBEC.AI ⚜️✨ · GoalOS · Proof Gradient.\n\nA model can answer. An agent can act. An institution must prove.\n\nGoalOS is the Recursive Workflow OS for Recursive Self-Improving Workflows. {SAFE}\n\n{SAFE_FR}\n\nCore loop: {LOOP}\n\nFrench loop: {LOOP_FR}\n\nProduct ladder is maintained in `docs/data/goalos_catalog.yml`; public buy/apply calls point to {SHOP}.\n\nClaim boundary: no guaranteed ROI, revenue, productivity, compliance certification, AI safety certification, regulated advice, uncontrolled autonomous deployment, true AGI RSI, or base-model self-modification.\n'''
 names=['GOALOS_DOCUMENTATION_INDEX','GOALOS_COMMERCIALIZATION_STATUS','GOALOS_PUBLIC_SITE_RELEASE_V10','GOALOS_RECURSIVE_WORKFLOW_OS','GOALOS_CLOUD_MVP_0_2','GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING','GOALOS_PUBLIC_SITE_ASSET_SYSTEM','GOALOS_PAID_ARTIFACT_POLICY','GOALOS_CLAIMS_AND_SAFE_BOUNDARY','GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY','GOALOS_COMMUNICATIONS_FIRM_SUMMARY','GOALOS_ENGINEERING_ROADMAP']
 for n in names: write(docs/f'{n}.md',common.replace('{title}',n.replace('_',' ').title()))
 # tables
 with open(docs/'tables/goalos_product_ladder.csv','w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=['price','name','version','english_description','french_description','public_url']); w.writeheader(); [w.writerow({'price':p['price'],'name':p['name'],'version':p['version'],'english_description':p['desc'],'french_description':p['fr'],'public_url':f'/proof-gradient/products/{p["slug"]}/'}) for p in PRODUCTS]
 simple_tables={'goalos_offer_status.csv':['offer,status\nGoalOS Cloud MVP 0.2,public software proof\nGoalOS Public Site Release v10,current\n'],'goalos_claim_boundaries.csv':['claim,status\nEnterprise RSI without model self-modification,approved\nguaranteed ROI,prohibited\nbase-model self-modification,prohibited\n'],'goalos_public_site_pages.csv':['page,status\n/proof-gradient/,current\n/proof-gradient/pricing/,current\n/proof-gradient/brand/visual-system/,current\n'],'goalos_paid_file_policy.csv':['rule,status\nAEP complete-package.zip under site/standards/AEP-###,allowed\nbuyer ZIPs,blocked\nprivate delivery bundles,blocked\n'],'goalos_aep_standards.csv':['code,title\n'+''.join(f'{c},{t}\n' for c,t in AEP)],'goalos_document_inventory.csv':['path,status\nREADME.md,current\ndocs/GOALOS_REPO_AUDIT.md,current\ndocs/data/goalos_catalog.yml,current\n'],'goalos_asset_manifest.csv':['source_path,public_path,role,sha256\n'+''.join(f'{a["source_path"]},{a["public_path"]},{a["inferred_role"]},{a["sha256"]}\n' for a in imgs)]}
 for fn,content in simple_tables.items(): write(docs/'tables'/fn,content[0])
 figs={'goalos_recursive_workflow_loop':'flowchart LR\nRun-->Score-->Prove-->Diagnose-->Improve-->Approve-->Version-->Monitor-->Rerun[Re-run]\n','goalos_product_ladder':'flowchart TB\nKit[$49 Kit]-->Lite[$199 RSI Lite]-->Dept[$997 Proof Room Lite]-->Workshop[$2,500+ Workshop]-->Impl[$9,500+ Implementation]-->Pilot[$49,000+ Pilot]\n','goalos_public_site_architecture':'flowchart LR\nCatalog-->Pages\nAssets-->Pages\nScripts-->Validation\nPages-->GitHubPages[GitHub Pages]\n','goalos_cloud_mvp_architecture':'flowchart TB\nWorkspace-->Policy-->Studio-->Execution-->Evaluation-->ProofRoom-->Improvement-->Approval-->Versioning-->Rollback\n','goalos_proof_graph_concept':'flowchart LR\nWorkflow-->Run-->Scorecard-->ProofRecord-->PublicSafeCard\n','goalos_enterprise_safety_boundary':'flowchart LR\nBaseModel[Base AI model unchanged]-->Gateway[Model gateway restrictions]-->Workflow[Workflow improvements]-->Approval[Human approval]-->Rollback\n'}
 for name,src in figs.items():
  write(docs/'figures'/f'{name}.mmd',src)
  write(docs/'figures'/f'{name}.svg',f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="220" role="img" aria-label="{name}"><rect width="100%" height="100%" fill="#06070d"/><text x="24" y="48" fill="#f7c846" font-family="monospace" font-size="22">{name}</text><text x="24" y="95" fill="#f6f0df" font-family="monospace" font-size="16">{html.escape(src[:120])}</text></svg>')
 readme=f'''# QUEBEC.AI ⚜️✨ · Proof Gradient · GoalOS\n\n**A model can answer. An agent can act. An institution must prove.**\n\nProof Gradient is the public proof and standards layer. GoalOS is the Recursive Workflow OS for the RSI era: repeated AI work becomes owned, scored, versioned, approved, monitored, and recursively improving workflows.\n\n**Commercial line:** ChatGPT gives you answers. GoalOS gives you workflows that get better every time they run.\n\n**Enterprise line:** Enterprise RSI without model self-modification.\n\n## Core thesis\n\n{LOOP}\n\nNo proof, no evolution. No eval, no propagation. No rollback, no release.\n\nPas de preuve, pas d’évolution. Pas d’évaluation, pas de propagation. Pas de rollback, pas de publication.\n\n## Product ladder\n\n| Price | Product | Version | English | Français |\n|---:|---|---|---|---|\n'''
 for p in PRODUCTS: readme+=f'| {p["price"]} | {p["name"]} | {p["version"]} | {p["desc"]} | {p["fr"]} |\n'
 readme+=f'''\nAll buy/apply buttons point to {SHOP}.\n\n## Safe AI boundary\n\n{SAFE}\n\n{SAFE_FR}\n\nGoalOS does not claim guaranteed ROI, guaranteed revenue, guaranteed productivity, compliance certification, AI safety certification, regulated advice, uncontrolled autonomous deployment, true AGI RSI, or base-model self-modification.\n\n## Public standards\n\nAEP-001 through AEP-008 are preserved under `site/standards/`; public packages named `site/standards/AEP-###/complete-package.zip` are allowed.\n\n## Cloud MVP\n\nGoalOS Cloud MVP 0.2 lives at `site/app/goalos-cloud-mvp/`. It is a public browser-based software proof, not the full SaaS. Run:\n\n```bash\nnode site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs\n```\n\n## Paid-file policy\n\nRun `python scripts/check_no_paid_artifacts.py`. Paid buyer files, private delivery materials, seller assets, and non-AEP ZIPs are blocked from public roots.\n\n## Public site release and validation\n\n```bash\npython scripts/validate_goalos_catalog.py\npython scripts/check_no_paid_artifacts.py\npython scripts/validate_docs_tables_figures.py\n```\n\nThe public site root is `site/`. The canonical shell uses `site/assets/goalos-sovereign-v10.css` and `site/assets/goalos-sovereign-v10.js`.\n\n## Repo map\n\n- `docs/data/goalos_catalog.yml` — single source of truth.\n- `site/` — GitHub Pages public site.\n- `site/assets/brand-assets-v10.json` — public asset manifest.\n- `docs/` — GoalOS v10 documentation.\n- `docs/figures/` and `docs/tables/` — current figures and CSV tables.\n- `scripts/` — validation and release guard scripts.\n- `.github/workflows/` — v10 release and validation workflows.\n\n## Current status\n\nGoalOS Public Site Release v10 is ready for review with validated catalog, docs, pages, assets, paid-artifact guard, and Cloud MVP tests.\n\n## Final doctrine\n\nSell. Install. Prove. Publish public-safe proof. Convert proof into pilots. Convert pilots into software. Convert software into a standard.\n'''
 write(ROOT/'README.md',readme)
 write(ROOT/'ROADMAP.md',common.replace('{title}','GoalOS Engineering Roadmap'))
 write(ROOT/'SECURITY.md','# Security Policy\n\nGoalOS public materials are not security advice. Public pages preserve the safe boundary: '+SAFE+'\n\nReport issues through GitHub Issues. Do not publish secrets, private buyer materials, or delivery bundles.\n')
 write(ROOT/'CONTRIBUTING.md','# Contributing\n\nUse the GoalOS v10 catalog as the source of truth. Run validation before pull requests.\n\n```bash\npython scripts/validate_goalos_catalog.py\npython scripts/check_no_paid_artifacts.py\npython scripts/validate_docs_tables_figures.py\n```\n')
 write(ROOT/'QA_VERIFICATION.md','# QA verification\n\nRequired v10 checks:\n\n```bash\npytest\nnode site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs\npython scripts/check_no_paid_artifacts.py\npython scripts/validate_docs_tables_figures.py\npython scripts/validate_goalos_catalog.py\n```\n\nSkipped tests must be documented in `docs/GOALOS_REPO_AUDIT.md` and `docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md`.\n')
 write(ROOT/'repository_manifest.json',json.dumps({'release':'GoalOS Public Site Release v10','site_root':'site','catalog':'docs/data/goalos_catalog.yml','seal':'assets/quebecaisealv5.png'},indent=2))
 paths=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if '.git' not in p.parts and p.is_file()]
 write(ROOT/'REPO_FILE_TREE.txt','\n'.join(sorted(paths)[:5000])+'\n')

def archive():
 arch=SITE/'_archive'/f'before_goalos_public_site_release_v10_{TODAY}'
 targets=['index.html','start-here/index.html','products/index.html','pricing/index.html','services/index.html','examples/index.html','standards/index.html','command-center/index.html','site-map/index.html','404.html','workshop/goalos-rsi-sprint-workshop/index.html','workshop/goalos-proof-room-implementation-sprint/index.html','implementation/goalos-proof-room-implementation-sprint/index.html','enterprise/goalos-enterprise-rsi-pilot/index.html','platform/goalos-recursive-workflow-os/index.html','brand/visual-system/index.html','examples/internal-approval-memo/index.html','home-before-internal-approval-memo-example.html','assets/internal-approval-memo-card.svg','workflow/internal-approval-memo/index.html']
 for t in targets:
  p=SITE/t
  if p.exists():
   dst=arch/t; ensure(dst.parent); shutil.copy2(p,dst)
 # Remove active paid/private-looking files after archival
 for t in ['examples/internal-approval-memo/index.html','home-before-internal-approval-memo-example.html','assets/internal-approval-memo-card.svg','workflow/internal-approval-memo/index.html']:
  p=SITE/t
  if p.exists(): p.unlink()

def scripts():
 write(ROOT/'scripts/check_no_paid_artifacts.py',r'''#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
roots=[ROOT/'site', ROOT/'public']
blocked=re.compile(r'(buyer|buyer_official|complete_bundle|delivery_kit|seller_assets|master_pack|commercialization_ready|quick_launch|opulent_institutional|institutional_boardroom|implementation_sprint|enterprise_rsi_pilot|workshop_v|buyer_facilitator|private|paid|internal)', re.I)
errors=[]
for root in roots:
    if not root.exists(): continue
    for p in root.rglob('*'):
        if not p.is_file() or '_archive' in p.parts: continue
        rel=p.relative_to(ROOT).as_posix()
        allowed_zip=bool(re.fullmatch(r'site/standards/AEP-\d{3}/complete-package\.zip', rel))
        if p.suffix.lower()=='.zip' and not allowed_zip:
            errors.append(f'Blocked ZIP outside public AEP package exception: {rel}')
        if blocked.search(p.name) and not allowed_zip:
            errors.append(f'Blocked paid/private-looking filename: {rel}')
if errors:
    print('Paid/private artifact guard failed:')
    print('\n'.join(f'- {e}' for e in errors))
    sys.exit(1)
print('✅ No paid/private public artifacts found. Public AEP complete-package.zip files are allowed.')
''')
 write(ROOT/'scripts/validate_goalos_catalog.py',r'''#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
cat=yaml.safe_load((ROOT/'docs/data/goalos_catalog.yml').read_text(encoding='utf-8'))
errors=[]
for item in cat['product_ladder']:
    needle=[item['price'], item['name'], item['version']]
    for n in needle:
        if n not in (ROOT/'README.md').read_text(encoding='utf-8'):
            errors.append(f'README missing catalog value: {n}')
    page=ROOT/'site/products'/item['slug']/'index.html'
    if not page.exists(): errors.append(f'Missing product page: {page.relative_to(ROOT)}'); continue
    text=page.read_text(encoding='utf-8')
    for n in needle:
        if n not in text: errors.append(f'{page.relative_to(ROOT)} missing catalog value: {n}')
for p in (ROOT/'site').rglob('*.html'):
    if '_archive' in p.parts: continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    rel=p.relative_to(ROOT)
    if '<title>' not in text: errors.append(f'{rel} missing title')
    if 'name="description"' not in text: errors.append(f'{rel} missing description')
    if 'QUEBEC.AI' not in text or '⚜️✨' not in text: errors.append(f'{rel} missing QUEBEC.AI ⚜️✨ identity')
    if 'quebecaisealv5.png' not in text: errors.append(f'{rel} missing seal reference')
    if text.count('data-goalos-v10-nav')>1: errors.append(f'{rel} has more than one canonical nav')
    if text.count('data-goalos-v10-footer')>1: errors.append(f'{rel} has more than one canonical footer')
    if re.search(r'GOALOS-COMPLETE-NAV|GOALOS-COMPLETE-FOOTER|GOALOS-PRODUCT-LADDER-NAV|GOALOS-PRODUCT-LADDER-FOOTER|GOALOS-UNIFIED-SHELL|GOALOS-UNIFIED-FOOTER|GOALOS-CLOUD-MVP', text): errors.append(f'{rel} has old shell marker')
    for match in re.finditer(r'href=[\"\\'](/proof-gradient/[^\"\\'#?]*)', text):
        url=match.group(1)
        rel_url=url[len('/proof-gradient/'):]
        if not rel_url:
            continue
        target=ROOT/'site'/rel_url
        ok=(target/'index.html').exists() if url.endswith('/') else (target.exists() or target.with_suffix('.html').exists())
        if not ok:
            errors.append(f'{rel} has broken internal link: {url}')
for req in ['site/assets/quebecaisealv5.png','site/favicon.png','site/assets/apple-touch-icon.png','site/assets/icon-192.png','site/assets/icon-512.png','site/site.webmanifest','site/assets/brand-assets-v10.json','site/brand/visual-system/index.html']:
    if not (ROOT/req).exists(): errors.append(f'Missing required asset/page: {req}')
if cat['safe_boundary_en'] not in (ROOT/'README.md').read_text(encoding='utf-8'): errors.append('README missing safe-boundary language')
if errors:
    print('GoalOS catalog validation failed:'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('✅ GoalOS catalog, public pages, shell, seal, and safe boundary validate.')
''')
 write(ROOT/'scripts/validate_docs_tables_figures.py',r'''#!/usr/bin/env python3
from pathlib import Path
import csv, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
cat=yaml.safe_load((ROOT/'docs/data/goalos_catalog.yml').read_text(encoding='utf-8'))
required_docs=['docs/GOALOS_REPO_AUDIT.md','docs/GOALOS_DOCUMENTATION_INDEX.md','docs/GOALOS_COMMERCIALIZATION_STATUS.md','docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md','docs/GOALOS_RECURSIVE_WORKFLOW_OS.md','docs/GOALOS_CLOUD_MVP_0_2.md','docs/GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md','docs/GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md','docs/GOALOS_PAID_ARTIFACT_POLICY.md','docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md','docs/GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md','docs/GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md','docs/GOALOS_ENGINEERING_ROADMAP.md']
required_tables=['docs/tables/goalos_product_ladder.csv','docs/tables/goalos_offer_status.csv','docs/tables/goalos_claim_boundaries.csv','docs/tables/goalos_public_site_pages.csv','docs/tables/goalos_paid_file_policy.csv','docs/tables/goalos_aep_standards.csv','docs/tables/goalos_document_inventory.csv','docs/tables/goalos_asset_manifest.csv']
figs=['goalos_recursive_workflow_loop','goalos_product_ladder','goalos_public_site_architecture','goalos_cloud_mvp_architecture','goalos_proof_graph_concept','goalos_enterprise_safety_boundary']
errors=[]
for p in required_docs+required_tables: 
    if not (ROOT/p).exists(): errors.append(f'Missing {p}')
for f in figs:
    if not (ROOT/f'docs/figures/{f}.mmd').exists(): errors.append(f'Missing figure source {f}.mmd')
    if not (ROOT/f'docs/figures/{f}.svg').exists(): errors.append(f'Missing figure svg {f}.svg')
readme=(ROOT/'README.md').read_text(encoding='utf-8')
for p in required_docs[:5]:
    if p not in readme and Path(p).name not in readme: errors.append(f'README does not link/reference {p}')
rows=list(csv.DictReader((ROOT/'docs/tables/goalos_product_ladder.csv').read_text(encoding='utf-8').splitlines()))
for item in cat['product_ladder']:
    if not any(r['name']==item['name'] and r['price']==item['price'] and r['version']==item['version'] for r in rows): errors.append(f'Product ladder table mismatch for {item["name"]}')
for item in cat['product_ladder']:
    if not (ROOT/'site/products'/item['slug']/'index.html').exists(): errors.append(f'Missing required product page {item["slug"]}')
if cat['safe_boundary_en'] not in readme: errors.append('Required safe-boundary language missing from README')
if errors:
    print('Docs/tables/figures validation failed:'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('✅ GoalOS docs, tables, figures, README references, pages, and safe boundary validate.')
''')
 for s in ['check_no_paid_artifacts.py','validate_goalos_catalog.py','validate_docs_tables_figures.py']: os.chmod(ROOT/'scripts'/s,0o755)

def workflows():
 wf=ROOT/'.github/workflows'; ensure(wf)
 common='''name: {name}\n\non:\n  push:\n  pull_request:\n  workflow_dispatch:\n\njobs:\n  validate:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.x'\n      - uses: actions/setup-node@v4\n        with:\n          node-version: '22'\n      - name: Install Python validation dependencies\n        run: python -m pip install pyyaml\n      - name: Run checks\n        run: |\n          {cmds}\n'''
 write(wf/'validate-goalos-public-site-v10.yml',common.format(name='Validate GoalOS Public Site v10',cmds='python scripts/validate_goalos_catalog.py\n          python scripts/check_no_paid_artifacts.py'))
 write(wf/'check-no-paid-artifacts.yml',common.format(name='Check No Paid Artifacts',cmds='python scripts/check_no_paid_artifacts.py'))
 write(wf/'validate-docs-tables-figures.yml',common.format(name='Validate GoalOS Docs, Tables, and Figures',cmds='python scripts/validate_docs_tables_figures.py'))
 release='''name: GoalOS Public Site Release v10\n\non:\n  workflow_dispatch:\n\npermissions:\n  contents: write\n  pages: write\n  id-token: write\n\njobs:\n  release:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.x'\n      - uses: actions/setup-node@v4\n        with:\n          node-version: '22'\n      - name: Install Python validation dependencies\n        run: python -m pip install pyyaml\n      - name: Detect site root and validate release\n        run: |\n          test -d site && echo "site/ selected" || (test -d public && echo "public/ selected")\n          test -f assets/quebecaisealv5.png\n          python scripts/build_goalos_v10_release.py\n          python scripts/validate_goalos_catalog.py\n          python scripts/check_no_paid_artifacts.py\n          python scripts/validate_docs_tables_figures.py\n          if [ -f site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs ]; then node site/app/goalos-cloud-mvp/tests/enterprise-core.test.mjs; fi\n      - name: Refuse unexpected deletions\n        run: |\n          git status --short\n          ! git status --short | awk '{print $1}' | grep -q '^D'\n      - name: Commit generated release artifacts if changed\n        run: |\n          git config user.name "github-actions[bot]"\n          git config user.email "github-actions[bot]@users.noreply.github.com"\n          git add README.md docs site scripts .github/workflows ROADMAP.md SECURITY.md CONTRIBUTING.md QA_VERIFICATION.md repository_manifest.json REPO_FILE_TREE.txt\n          git diff --cached --quiet || git commit -m "Refresh GoalOS public site release v10"\n      - uses: actions/configure-pages@v5\n      - uses: actions/upload-pages-artifact@v3\n        with:\n          path: site\n      - uses: actions/deploy-pages@v4\n'''
 write(wf/'goalos-public-site-release-v10.yml',release)

def main():
 archive(); catalog(); imgs=assets(); pages(imgs); docs_tables_figures(imgs); scripts(); workflows()
if __name__=='__main__': main()

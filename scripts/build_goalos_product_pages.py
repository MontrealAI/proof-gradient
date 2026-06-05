#!/usr/bin/env python3
"""Build the static public GoalOS product pages from data/goalos_products.json."""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "goalos_products.json"
SITE = ROOT / "site"
ASSETS = SITE / "assets"
MARKER = "<!-- GENERATED_BY_GOALOS_PRODUCT_BUILDER -->"
AEP_LINK_FROM_ROOT = "../standards/AEP-001/"
BOUNDARY_EN = (
    "Independent initiative by QUEBEC.AI / MONTREAL.AI. Not affiliated with, sponsored by, or endorsed by the Government of Canada unless a formal agreement is separately executed. "
    "This page does not provide legal, financial, procurement, medical, compliance, national-security, or investment advice. "
    "No ROI, certification, production deployment, AGI, ASI, sovereign outcome, or public-sector adoption result is guaranteed."
)
BOUNDARY_FR = (
    "Initiative indépendante de QUEBEC.AI / MONTREAL.AI. Non affiliée, commanditée ni approuvée par le gouvernement du Canada sauf accord formel séparé. "
    "Cette page ne fournit pas de conseils juridiques, financiers, d’approvisionnement, médicaux, de conformité, de sécurité nationale ni d’investissement. "
    "Aucun ROI, certification, déploiement en production, AGI, ASI, résultat souverain ni résultat d’adoption du secteur public n’est garanti."
)

CSS = r"""
:root{color-scheme:dark;--bg:#050814;--panel:rgba(12,18,36,.88);--panel2:rgba(255,255,255,.055);--line:rgba(255,255,255,.15);--text:#f8f7ef;--muted:#b8c2dd;--gold:#f4c76b;--blue:#81b7ff;--green:#8df0c0;--red:#ffb4b4}*{box-sizing:border-box}html{scroll-behavior:smooth}body.goalos-page{margin:0;min-height:100vh;background:radial-gradient(circle at 8% 8%,rgba(129,183,255,.22),transparent 32%),radial-gradient(circle at 90% 0%,rgba(244,199,107,.17),transparent 30%),linear-gradient(180deg,#050814,#090d1a 72%,#050814);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:var(--blue)}.skip-link{position:absolute;left:-999px;top:auto}.skip-link:focus{left:18px;top:18px;z-index:10;background:#fff;color:#061024;padding:10px 14px;border-radius:10px}.shell{width:min(1180px,calc(100% - 36px));margin:0 auto}.topnav{display:flex;justify-content:space-between;align-items:center;gap:18px;padding:22px 0}.brand{font-weight:950;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);text-decoration:none}.navlinks{display:flex;flex-wrap:wrap;gap:10px}.navlinks a,.pill-link{border:1px solid var(--line);background:rgba(255,255,255,.045);border-radius:999px;color:var(--text);padding:9px 13px;text-decoration:none;font-weight:800;font-size:14px}.navlinks a:hover,.pill-link:hover,.cta.secondary:hover{border-color:var(--gold);color:var(--gold)}.hero{padding:72px 0 34px}.eyebrow{color:var(--gold);text-transform:uppercase;letter-spacing:.2em;font-weight:950;font-size:13px}.hero h1{font-size:clamp(42px,7vw,92px);line-height:.95;letter-spacing:-.07em;margin:18px 0}.lead{font-size:clamp(20px,2vw,27px);line-height:1.35;color:#e7ecff;max-width:920px}.muted{color:var(--muted)}.fr{border-left:3px solid rgba(244,199,107,.55);padding-left:16px}.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}.cta{display:inline-flex;align-items:center;justify-content:center;padding:13px 18px;border-radius:999px;text-decoration:none;font-weight:950;border:1px solid transparent}.cta.primary{background:linear-gradient(135deg,var(--gold),#ffe29a);color:#061024}.cta.blue{background:linear-gradient(135deg,var(--blue),#c9ddff);color:#061024}.cta.secondary{border-color:var(--line);color:var(--text);background:rgba(255,255,255,.045)}.section{padding:34px 0}.section h2{font-size:clamp(30px,4vw,54px);line-height:1;letter-spacing:-.055em;margin:0 0 18px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.grid.two{grid-template-columns:repeat(2,minmax(0,1fr))}.card{border:1px solid var(--line);background:var(--panel);border-radius:24px;padding:22px;box-shadow:0 18px 70px rgba(0,0,0,.22)}.card h3{font-size:24px;margin:8px 0 10px}.price{display:inline-flex;color:var(--green);border:1px solid rgba(141,240,192,.38);border-radius:999px;padding:7px 10px;font-weight:950;background:rgba(141,240,192,.08)}.number{color:var(--gold);font-weight:950;letter-spacing:.12em;text-transform:uppercase;font-size:12px}.ladder-group{margin:30px 0}.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.product-card{display:flex;flex-direction:column;gap:10px}.product-card .cta-row{margin-top:auto}.breadcrumb{font-size:14px;color:var(--muted);margin:18px 0}.detail-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:18px;align-items:start}.list{display:grid;gap:12px;padding:0;list-style:none}.list li{padding:14px 16px;border:1px solid var(--line);border-radius:16px;background:var(--panel2);color:#dce5ff}.boundary{border:1px solid rgba(255,180,180,.38);background:rgba(255,180,180,.07);border-radius:20px;padding:18px;margin-top:18px}.boundary h2,.boundary h3{color:var(--red);font-size:22px;letter-spacing:0;margin-top:0}.note{border:1px solid rgba(129,183,255,.34);background:rgba(129,183,255,.08);border-radius:20px;padding:18px}.footer{padding:42px 0 70px;color:var(--muted);border-top:1px solid var(--line);margin-top:34px}.quiz-option{display:block;width:100%;text-align:left;margin:8px 0;padding:12px 14px;border-radius:14px;border:1px solid var(--line);background:rgba(255,255,255,.05);color:var(--text);cursor:pointer}.quiz-option[aria-pressed="true"]{border-color:var(--gold);background:rgba(244,199,107,.16)}.score{font-size:54px;font-weight:950;color:var(--gold);line-height:1}@media(max-width:860px){.grid,.grid.two,.cards,.detail-grid{grid-template-columns:1fr}.hero{padding-top:38px}.topnav{align-items:flex-start;flex-direction:column}.shell{width:min(100% - 24px,1180px)}}
""".strip() + "\n"

JS = r"""
(function(){
  const quiz = document.querySelector('[data-goalos-quiz]');
  if (!quiz) return;
  const resultScore = document.getElementById('goalos-score-value');
  const resultTextEn = document.getElementById('goalos-score-text-en');
  const resultTextFr = document.getElementById('goalos-score-text-fr');
  const answers = new Map();
  const ranges = [
    {min:0,max:30,en:'You are using AI as a chat box.',fr:'Vous utilisez l’IA comme une fenêtre de clavardage.'},
    {min:31,max:60,en:'You have partial AI leverage.',fr:'Vous avez un levier IA partiel.'},
    {min:61,max:80,en:'You have a working AI system.',fr:'Vous avez un système IA fonctionnel.'},
    {min:81,max:100,en:'You are operating with serious AI leverage.',fr:'Vous opérez avec un vrai levier IA.'}
  ];
  function render(){
    let score = 0;
    answers.forEach(v => { score += v; });
    resultScore.textContent = String(score);
    const range = ranges.find(r => score >= r.min && score <= r.max) || ranges[0];
    resultTextEn.textContent = range.en;
    resultTextFr.textContent = range.fr;
  }
  quiz.addEventListener('click', function(event){
    const button = event.target.closest('button[data-score]');
    if (!button) return;
    const question = button.getAttribute('data-question');
    answers.set(question, Number(button.getAttribute('data-score')));
    quiz.querySelectorAll('button[data-question="' + question + '"]').forEach(other => other.setAttribute('aria-pressed','false'));
    button.setAttribute('aria-pressed','true');
    render();
  });
  render();
})();
""".strip() + "\n"

PRODUCT_RECEIVES = {
    "ai-efficiency-sprint": ["Context pack template", "Reusable operating rules", "Memory and notes structure", "Workflow map", "Output checks", "Proof log for weekly improvement"],
    "team-pack": ["Team workshop-in-a-box", "Facilitation guide", "Shared context pack", "Team rules and checks", "Evidence log", "Up to 10 participant workflow"],
    "workshop": ["Live bilingual workshop", "One repeated organizational workflow mapped", "Reusable context and rules", "Checks and proof artifacts", "Implementation next steps"],
    "sme-ai-adoption-sprint": ["Discovery and scoping", "One SME workflow converted into a proof-ready AI work system", "Risk and evidence notes", "90-day adoption roadmap", "Executive summary"],
    "enterprise-proof-room-agent-control-plane": ["Enterprise discovery", "Proof Room pilot design", "Agent Control Plane architecture", "Evidence and rollback model", "Governed rollout design"],
    "nation-state-ai-leverage-proof-infrastructure": ["Nation-state discovery", "Proof Room portfolio design", "Public-sector adoption architecture", "Evidence-governance roadmap", "Briefing materials"],
    "sovereign-nation-state": ["Sovereign AI discovery", "National control-plane architecture", "Public-sector Proof Room design", "Evidence Dockets and Selection Gates", "Rollout, rollback, and public trust design"],
    "sovereign-country-ai-operating-system": ["Country-scale AI operating-system architecture", "Proof and governance design", "Rollout and rollback architecture", "Public trust model", "Strategy briefing"],
    "sovereign-empire-ai-operating-system": ["Consent-based multi-country architecture", "Proof-governed capability network design", "Allied institutional coordination model", "Evidence and public trust framework", "Non-domination boundary design"],
}

DETAIL_INTROS = {
    "ai-efficiency-sprint": "The Sprint is a compact self-service system for turning one recurring prompt-heavy task into a reusable GoalOS workflow: Context, Rules, Memory, Workflow, Checks, and Proof.",
    "team-pack": "The Team Pack adapts the Sprint into a shared workshop-in-a-box for up to 10 participants who need one repeatable team AI workflow.",
    "workshop": "The Workshop is a live bilingual engagement for organizations that want facilitated conversion of one repeated AI task into a checked proof-ready workflow.",
    "sme-ai-adoption-sprint": "The SME Adoption Sprint is a scoped premium engagement for small and medium-sized businesses that need an adoption roadmap grounded in one concrete workflow.",
    "enterprise-proof-room-agent-control-plane": "The Enterprise Proof Room / Agent Control Plane frames agent adoption as governed, auditable capability rather than uncontrolled automation.",
    "nation-state-ai-leverage-proof-infrastructure": "The Nation-State layer helps public institutions reason about efficient, reusable, evidence-governed AI capability without claiming endorsement or readiness.",
    "sovereign-nation-state": "The Sovereign Nation-State layer focuses on proof rooms, evidence dockets, selection gates, rollout, rollback, and public trust design.",
    "sovereign-country-ai-operating-system": "The Sovereign Country AI Operating System frames country-scale AI adoption as an operating-system architecture for proof, governance, rollout, rollback, and trust.",
    "sovereign-empire-ai-operating-system": "The Sovereign Empire AI Operating System describes a voluntary proof-governed network model for allied sovereign institutions and jurisdictions.",
}

def load_products() -> list[dict]:
    return json.loads(CATALOG.read_text(encoding="utf-8"))

def e(value: object) -> str:
    return html.escape(str(value), quote=True)

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")

def page(title: str, main: str, css_prefix: str = "../") -> str:
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{e(title)}</title>
  <meta name=\"description\" content=\"Public GoalOS proof and product information by QUEBEC.AI / MONTREAL.AI.\">
  <link rel=\"stylesheet\" href=\"{css_prefix}assets/goalos-products.css\">
</head>
<body class=\"goalos-page\">
<a class=\"skip-link\" href=\"#main\">Skip to content</a>
<header class=\"shell topnav\" aria-label=\"GoalOS navigation\">
  <a class=\"brand\" href=\"{css_prefix}\">QUEBEC.AI / MONTREAL.AI</a>
  <nav class=\"navlinks\" aria-label=\"Primary\">
    <a href=\"{css_prefix}goalos/\">GoalOS</a>
    <a href=\"{css_prefix}products/\">Products</a>
    <a href=\"{css_prefix}ai-efficiency-score/\">AI Efficiency Score</a>
    <a href=\"{css_prefix}standards/AEP-001/\">AEP-001</a>
  </nav>
</header>
<main id=\"main\" class=\"shell\">
{MARKER}
{main}
</main>
<footer class=\"shell footer\">
  <p><strong>Commit → Execute → Prove → Evolve</strong></p>
  <p>No proof, no evolution. No eval, no propagation. No rollback, no release.</p>
</footer>
<script src=\"{css_prefix}assets/goalos-products.js\"></script>
</body>
</html>
"""

def product_url(product: dict, from_products_root: bool = False) -> str:
    slug = product["public_page_slug"]
    return f"{slug}/" if from_products_root else f"../products/{slug}/"

def cta_href(product: dict) -> str:
    return "#" + product["cta_url_placeholder"]

def boundary_html(include_title: bool = True) -> str:
    title = "<h2>Claim boundary / Limite des revendications</h2>" if include_title else ""
    return f"""<section class=\"boundary\" aria-label=\"Claim boundary\">{title}
  <p>{e(BOUNDARY_EN)}</p>
  <p class=\"fr\">{e(BOUNDARY_FR)}</p>
</section>"""

def render_goalos() -> str:
    steps = ["Context", "Rules", "Memory", "Workflow", "Checks", "Proof", "Weekly improvement"]
    cards = "\n".join(f"<article class=\"card\"><span class=\"number\">GoalOS</span><h3>{e(s)}</h3><p>{e('A reusable layer around AI work so output can be checked, improved, and reused.')}</p></article>" for s in steps)
    main = f"""
<section class=\"hero\">
  <p class=\"eyebrow\">GoalOS proof infrastructure</p>
  <h1>LLMs made intelligence accessible.<br>The next wave makes intelligence efficient.<br>GoalOS makes efficient intelligence provable.</h1>
  <p class=\"lead fr\">Les LLMs ont rendu l’intelligence accessible.<br>La prochaine vague rend l’intelligence efficace.<br>GoalOS rend l’intelligence efficace prouvable.</p>
  <p class=\"lead\"><strong>You already have the model. GoalOS gives you the machine around it.</strong></p>
  <p class=\"lead fr\"><strong>Vous avez déjà le modèle. GoalOS vous donne la machine autour du modèle.</strong></p>
  <p class=\"muted\">GoalOS turns repeated AI work into reusable, checked, provable systems.</p>
  <p class=\"muted fr\">GoalOS transforme le travail IA répété en systèmes réutilisables, vérifiés et prouvables.</p>
  <div class=\"cta-row\"><a class=\"cta primary\" href=\"../products/\">Explore the product ladder</a><a class=\"cta blue\" href=\"../ai-efficiency-score/\">Take the AI Efficiency Score</a><a class=\"cta secondary\" href=\"../standards/AEP-001/\">Read AEP-001</a></div>
</section>
<section class=\"section\"><h2>The machine around the model</h2><div class=\"grid\">{cards}</div></section>
{boundary_html()}
"""
    return page("GoalOS — Efficient intelligence made provable", main, "../")

def group_products(products: list[dict]) -> list[tuple[str, str, list[dict]]]:
    return [
        ("Self-service", "Autonome", products[0:2]),
        ("Services", "Services", products[2:4]),
        ("Enterprise", "Entreprise", products[4:5]),
        ("Nation / Sovereign", "Nation / Souverain", products[5:9]),
    ]

def render_hub(products: list[dict]) -> str:
    groups = []
    for group_en, group_fr, items in group_products(products):
        cards = []
        for index, product in enumerate(products, start=1):
            if product not in items:
                continue
            cards.append(f"""<article class=\"card product-card\">
  <span class=\"number\">Product {index}</span>
  <h3>{e(product['name_en'])}</h3>
  <p class=\"fr\"><strong>{e(product['name_fr'])}</strong></p>
  <p class=\"price\">{e(product['price_public'])}</p>
  <p><strong>Buyer:</strong> {e(product['audience_en'])}<br><span class=\"fr\"><strong>Acheteur :</strong> {e(product['audience_fr'])}</span></p>
  <p>{e(product['promise_en'])}</p>
  <p class=\"fr\">{e(product['promise_fr'])}</p>
  <div class=\"cta-row\"><a class=\"cta {'primary' if product['cta_type']=='buy' else 'blue'}\" href=\"{product_url(product, True)}\">{e(product['cta_label_en'])} / {e(product['cta_label_fr'])}</a></div>
</article>""")
        groups.append(f"<section class=\"ladder-group\"><h2>{e(group_en)} <span class=\"muted\">/ {e(group_fr)}</span></h2><div class=\"cards\">{''.join(cards)}</div></section>")
    note = "Paid digital products are delivered through Squarespace + Stripe. GitHub hosts public proof, standards, and product information only."
    note_fr = "Les produits numériques payants sont livrés via Squarespace + Stripe. GitHub héberge uniquement la preuve publique, les standards et l’information produit."
    main = f"""
<section class=\"hero\"><p class=\"eyebrow\">GoalOS Product Ladder</p><h1>AI access is not leverage.<br>Proof-ready systems are leverage.</h1><p class=\"lead\">GoalOS turns AI work into reusable, checked, provable capability.</p><p class=\"lead fr\">GoalOS transforme le travail IA en capacité réutilisable, vérifiée et prouvable.</p><div class=\"note\"><p>{e(note)}</p><p class=\"fr\">{e(note_fr)}</p></div></section>
{''.join(groups)}
{boundary_html()}
"""
    return page("GoalOS Product Ladder", main, "../")

def render_product(product: dict, number: int) -> str:
    receives = "".join(f"<li>{e(item)}</li>" for item in PRODUCT_RECEIVES[product["id"]])
    intro = DETAIL_INTROS[product["id"]]
    special = ""
    if product.get("special_boundary_en"):
        special = f"""<section class=\"boundary\"><h2>Non-domination boundary / Limite de non-domination</h2><p>{e(product['special_boundary_en'])}</p><p class=\"fr\">{e(product['special_boundary_fr'])}</p></section>"""
    component_focus = ""
    if product["id"] == "ai-efficiency-sprint":
        component_focus = "<section class=\"section\"><h2>Sprint components</h2><ul class=\"list\"><li>Context.</li><li>Rules.</li><li>Memory.</li><li>Workflow.</li><li>Checks.</li><li>Proof.</li></ul></section>"
    cta_class = "primary" if product["cta_type"] == "buy" else "blue"
    delivery_note = "Squarespace hosts the public sales or inquiry page. Stripe processes payment through Squarespace where applicable. GitHub does not host paid buyer packages."
    delivery_note_fr = "Squarespace héberge la page publique de vente ou de demande. Stripe traite le paiement via Squarespace lorsque applicable. GitHub n’héberge pas les forfaits payants destinés aux acheteurs."
    main = f"""
<nav class=\"breadcrumb\"><a href=\"../../products/\">Products</a> / Product {number}</nav>
<section class=\"hero\"><p class=\"eyebrow\">GoalOS product {number}</p><h1>{e(product['name_en'])}</h1><p class=\"lead fr\">{e(product['name_fr'])}</p><p class=\"price\">{e(product['price_public'])}</p><p class=\"lead\">{e(product['promise_en'])}</p><p class=\"lead fr\">{e(product['promise_fr'])}</p><div class=\"cta-row\"><a class=\"cta {cta_class}\" href=\"{e(cta_href(product))}\">{e(product['cta_label_en'])}</a><a class=\"cta secondary\" href=\"{e(cta_href(product))}\">{e(product['cta_label_fr'])}</a></div></section>
<section class=\"section detail-grid\"><article class=\"card\"><h2>Who it is for / Pour qui</h2><p>{e(product['audience_en'])}</p><p class=\"fr\">{e(product['audience_fr'])}</p><p>{e(intro)}</p></article><article class=\"card\"><h2>Delivery / Livraison</h2><p>{e(product['delivery_en'])}</p><p class=\"fr\">{e(product['delivery_fr'])}</p><p>{e(delivery_note)}</p><p class=\"fr\">{e(delivery_note_fr)}</p></article></section>
<section class=\"section\"><h2>What the buyer or client receives</h2><ul class=\"list\">{receives}</ul></section>
{component_focus}
<section class=\"section note\"><h2>Proof standard</h2><p>This public page points to AEP-001 — GoalOS Proof-of-Evolution Constitution as the current proof standard for GoalOS proof claims.</p><p class=\"fr\">Cette page publique renvoie à AEP-001 — GoalOS Proof-of-Evolution Constitution comme standard actuel de preuve pour les revendications de preuve GoalOS.</p><div class=\"cta-row\"><a class=\"cta secondary\" href=\"../../standards/AEP-001/\">Read AEP-001</a><a class=\"cta secondary\" href=\"../../products/\">Back to product ladder</a></div></section>
{boundary_html()}
{special}
"""
    return page(product["name_en"], main, "../../")

def render_quiz(products: list[dict]) -> str:
    questions = [
        "Do you paste the same context into AI more than once per week?",
        "Do you have saved AI instructions for recurring work?",
        "Do you have a reusable context pack?",
        "Do you have rules the AI must always follow?",
        "Do you have memory / notes the AI can reuse?",
        "Do you have a repeatable workflow?",
        "Do you check outputs before using them?",
        "Do you save evidence of what worked?",
        "Do you have a rollback / correction plan?",
        "Do you improve the workflow weekly?",
    ]
    q_html = []
    for index, question in enumerate(questions, start=1):
        q_html.append(f"""<fieldset class=\"card\"><legend><span class=\"number\">Question {index}</span><br>{e(question)}</legend><button class=\"quiz-option\" type=\"button\" data-question=\"{index}\" data-score=\"10\" aria-pressed=\"false\">Yes / Oui</button><button class=\"quiz-option\" type=\"button\" data-question=\"{index}\" data-score=\"5\" aria-pressed=\"false\">Partial / Partiel</button><button class=\"quiz-option\" type=\"button\" data-question=\"{index}\" data-score=\"0\" aria-pressed=\"false\">No / Non</button></fieldset>""")
    p1 = products[0]
    main = f"""
<section class=\"hero\"><p class=\"eyebrow\">Free AI Efficiency Score</p><h1>Measure whether AI is a chat box or a reusable work system.</h1><p class=\"lead\">Static quiz. No backend. No data collection. No external analytics.</p><p class=\"lead fr\">Questionnaire statique. Aucun backend. Aucune collecte de données. Aucune analytique externe.</p></section>
<section class=\"section detail-grid\"><form data-goalos-quiz class=\"grid\" onsubmit=\"return false\">{''.join(q_html)}</form><aside class=\"card\" aria-live=\"polite\"><h2>Your score / Votre score</h2><div class=\"score\"><span id=\"goalos-score-value\">0</span>/100</div><p id=\"goalos-score-text-en\">You are using AI as a chat box.</p><p id=\"goalos-score-text-fr\" class=\"fr\">Vous utilisez l’IA comme une fenêtre de clavardage.</p><div class=\"cta-row\"><a class=\"cta primary\" href=\"{e(cta_href(p1))}\">Get GoalOS AI Efficiency Sprint — $49</a><a class=\"cta secondary\" href=\"{e(cta_href(p1))}\">Obtenir GoalOS AI Efficiency Sprint — 49 $</a></div></aside></section>
{boundary_html()}
"""
    return page("AI Efficiency Score", main, "../")

def update_homepage() -> None:
    path = SITE / "index.html"
    if not path.exists():
        return
    start = "<!-- GOALOS_PRODUCT_LADDER_START -->"
    end = "<!-- GOALOS_PRODUCT_LADDER_END -->"
    block = f"""{start}
<section id=\"goalos-product-ladder\" class=\"card\" style=\"margin:48px 0;padding:28px;border:1px solid rgba(244,199,107,.35);background:linear-gradient(135deg,rgba(244,199,107,.13),rgba(138,180,255,.10));\">
  <p class=\"eyebrow\">GoalOS Product Ladder</p>
  <h2>GoalOS Product Ladder<br><span style=\"color:#aab3cf\">Échelle de produits GoalOS</span></h2>
  <p class=\"hero-line\"><strong>AI access is not leverage.</strong><br>GoalOS turns AI work into reusable, checked, provable capability.</p>
  <p class=\"hero-line\"><strong>L’accès à l’IA n’est pas le levier.</strong><br>GoalOS transforme le travail IA en capacité réutilisable, vérifiée et prouvable.</p>
  <div class=\"nav\" aria-label=\"GoalOS public links\">
    <a href=\"goalos/\">GoalOS</a>
    <a href=\"products/\">Product ladder</a>
    <a href=\"ai-efficiency-score/\">AI Efficiency Score</a>
    <a href=\"standards/AEP-001/\">AEP-001</a>
  </div>
  <p class=\"small\">Paid digital products are delivered through Squarespace + Stripe. GitHub hosts public proof, standards, and product information only.</p>
</section>
{end}"""
    text = path.read_text(encoding="utf-8")
    if start in text and end in text:
        before, rest = text.split(start, 1)
        _, after = rest.split(end, 1)
        new_text = before + block + after
    else:
        marker = "<main>"
        if marker in text:
            new_text = text.replace(marker, marker + block, 1)
        else:
            new_text = block + text
    write(path, new_text)

def main() -> int:
    products = load_products()
    ASSETS.mkdir(parents=True, exist_ok=True)
    write(ASSETS / "goalos-products.css", CSS)
    write(ASSETS / "goalos-products.js", JS)
    write(SITE / "goalos" / "index.html", render_goalos())
    write(SITE / "products" / "index.html", render_hub(products))
    for number, product in enumerate(products, start=1):
        write(SITE / "products" / product["public_page_slug"] / "index.html", render_product(product, number))
    write(SITE / "ai-efficiency-score" / "index.html", render_quiz(products))
    update_homepage()
    print("Built GoalOS product pages from data/goalos_products.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate GoalOS v10 catalog, generated pages, links, shell, assets, and safe-boundary language."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CATALOG = ROOT / "docs/data/goalos_catalog.yml"
BASE = "/proof-gradient"
SAFE_BOUNDARY = "GoalOS does not modify base AI models. GoalOS improves workflows around AI"
OLD_MARKERS = ["GOALOS-COMPLETE-NAV", "GOALOS-COMPLETE-FOOTER", "GOALOS-PRODUCT-LADDER-NAV", "GOALOS-PRODUCT-LADDER-FOOTER", "GOALOS-UNIFIED-SHELL", "GOALOS-UNIFIED-FOOTER", "GOALOS-CLOUD-MVP", "GOALOS-CLOUD-MVP-V02"]
REQUIRED_PAGES = [
    "index.html", "start-here/index.html", "products/index.html", "pricing/index.html", "services/index.html", "examples/index.html", "standards/index.html", "command-center/index.html", "site-map/index.html", "404.html",
    "products/goalos-ai-efficiency-sprint-kit/index.html", "products/goalos-rsi-lite/index.html", "products/goalos-proof-room-lite/index.html", "products/goalos-rsi-sprint-workshop/index.html", "products/goalos-proof-room-implementation-sprint/index.html", "products/goalos-enterprise-rsi-pilot/index.html", "products/goalos-cloud-mvp/index.html",
    "workshop/goalos-rsi-sprint-workshop/index.html", "workshop/goalos-proof-room-implementation-sprint/index.html", "implementation/goalos-proof-room-implementation-sprint/index.html", "enterprise/goalos-enterprise-rsi-pilot/index.html", "platform/goalos-recursive-workflow-os/index.html", "brand/visual-system/index.html",
]
STALE_TERMS = [
    "GoalOS AI Efficiency Sprint — Team Pack", "GoalOS SME AI Adoption Sprint", "Workflow Vault", "Sovereign Empire AI Operating System", "Nation-State AI Leverage", "SQUARESPACE_PRODUCT_1_URL",
]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.title=False; self.description=False; self.images=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag in {"a","link","script","img"}:
            for key in ("href","src"):
                if attrs.get(key): self.links.append(attrs[key])
        if tag == "meta" and attrs.get("name") == "description" and attrs.get("content"):
            self.description=True
        if tag == "img": self.images.append(attrs)
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
    def handle_data(self, data):
        pass


def load_catalog():
    with CATALOG.open(encoding="utf-8") as fh: return yaml.safe_load(fh)


def candidate(page: Path, raw: str) -> list[Path]:
    parsed = urlparse(raw); path = unquote(parsed.path)
    if parsed.scheme in {"http","https","mailto","tel","data","javascript"} or raw.startswith("//"):
        return []
    if path.startswith(BASE + "/"):
        path = path[len(BASE)+1:]; base=SITE
    elif path.startswith("/"):
        path=path[1:]; base=SITE
    else:
        base=page.parent
    target=(base/path).resolve()
    if raw.endswith("/") or path == "" or target.is_dir(): return [target/"index.html", target]
    return [target]


def broken_link(page: Path, raw: str) -> bool:
    cands = candidate(page, raw)
    if not cands: return False
    for c in cands:
        try: c.relative_to(ROOT)
        except ValueError: continue
        if c.exists(): return False
    return True


def run() -> int:
    errors=[]
    if not CATALOG.exists(): errors.append("Missing docs/data/goalos_catalog.yml")
    catalog=load_catalog() if CATALOG.exists() else {}
    products=catalog.get("product_ladder", [])
    if len(products)!=6: errors.append(f"Expected 6 ladder products; found {len(products)}")
    for product in products:
        for key in ["slug","price","name","version","description_en","description_fr","public_url","shop_url"]:
            if not product.get(key): errors.append(f"Product missing {key}: {product}")
        page=SITE/product.get("public_url", "").lstrip("/")/"index.html"
        if not page.exists(): errors.append(f"Missing product page {page.relative_to(ROOT)}")
    for rel in REQUIRED_PAGES:
        if not (SITE/rel).exists(): errors.append(f"Missing required page site/{rel}")
    for required in ["assets/quebecaisealv5.png", "favicon.png", "assets/apple-touch-icon.png", "assets/icon-192.png", "assets/icon-512.png", "site.webmanifest", "assets/brand-assets-v10.json", "brand/visual-system/index.html"]:
        if not (SITE/required).exists(): errors.append(f"Missing site/{required}")
    if (SITE/"assets/brand-assets-v10.json").exists():
        try:
            manifest=json.loads((SITE/"assets/brand-assets-v10.json").read_text(encoding="utf-8"))
            if not manifest.get("assets"): errors.append("brand-assets-v10.json has no assets")
            for rec in manifest.get("assets", []):
                if not rec.get("sha256") or not rec.get("alt_text"): errors.append(f"asset manifest missing sha256/alt text: {rec}")
        except Exception as exc: errors.append(f"brand-assets-v10.json parse failed: {exc}")
    for html_path in sorted(SITE.rglob("*.html")):
        if "_archive" in html_path.parts: continue
        text=html_path.read_text(encoding="utf-8", errors="ignore")
        rel=html_path.relative_to(SITE).as_posix()
        if text.count("GOALOS-CANONICAL-SHELL:START") != 1: errors.append(f"{rel}: expected one canonical nav")
        if text.count("GOALOS-CANONICAL-FOOTER:START") != 1: errors.append(f"{rel}: expected one canonical footer")
        for marker in OLD_MARKERS:
            if marker in text: errors.append(f"{rel}: old shell marker {marker}")
        if not re.search(r"<title>[^<]+</title>", text, re.I): errors.append(f"{rel}: missing title")
        if not re.search(r"<meta\s+name=[\"']description[\"']\s+content=[\"'][^\"']+", text, re.I): errors.append(f"{rel}: missing description")
        if "QUEBEC.AI ⚜️✨" not in text: errors.append(f"{rel}: missing QUEBEC.AI ⚜️✨ identity")
        if "quebecaisealv5.png" not in text: errors.append(f"{rel}: missing QUEBEC.AI Seal reference")
        for icon in ["favicon.png", "apple-touch-icon.png", "site.webmanifest"]:
            if icon not in text: errors.append(f"{rel}: missing {icon} reference")
        if rel in REQUIRED_PAGES and SAFE_BOUNDARY not in text and rel not in {"pricing/index.html", "site-map/index.html", "404.html"}:
            errors.append(f"{rel}: missing safe-boundary language")
        for stale in STALE_TERMS:
            if stale in text: errors.append(f"{rel}: stale product/version/pricing term {stale}")
        parser=LinkParser(); parser.feed(text)
        for raw in parser.links:
            if raw.startswith(BASE) and broken_link(html_path, raw): errors.append(f"{rel}: broken internal link {raw}")
        for img in parser.images:
            if not img.get("alt", "").strip(): errors.append(f"{rel}: image missing alt text")
    # Catalog values must appear in README, pricing, products.
    corpus = "\n".join((ROOT/"README.md").read_text(encoding="utf-8", errors="ignore") + "\n" + (SITE/"pricing/index.html").read_text(encoding="utf-8", errors="ignore") for _ in [0])
    for p in products:
        for val in [p["price"], p["name"], p["version"]]:
            if val not in corpus: errors.append(f"Catalog value not in README/pricing: {val}")
    if errors:
        print("GoalOS v10 catalog/public-site validation failed:", file=sys.stderr)
        for e in errors: print(f"- {e}", file=sys.stderr)
        return 1
    print("GoalOS v10 catalog, public site, links, shell, assets, and safe boundary validated")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())
